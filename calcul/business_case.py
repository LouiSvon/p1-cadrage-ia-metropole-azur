"""Business case de P1 : fourchettes et sensibilité. Toutes les entrées viennent de registre.md (H..)."""
import json, itertools

# (bas, central, haut) ; pour les coûts, "bas" = scénario prudent donc coût élevé : on stocke (prudent, central, optimiste)
G = dict(  # paramètres de gain : (pessimiste, central, optimiste)
    users=(600, 600, 600),             # H03
    h_semaine=(3, 3, 3),               # H04
    semaines=(44, 44, 44),             # H17
    part_eco=(0.20, 0.30, 0.40),       # H05
    adoption=(0.40, 0.60, 0.80),       # H19
    cout_h=(28, 35, 45),               # H06
)
C = dict(  # coûts en euros : (pessimiste = élevé, central, optimiste = bas)
    socle=(150_000, 80_000, 40_000),         # H20
    build=(450_000, 250_000, 120_000),       # H21
    run_an=(280_000, 150_000, 80_000),       # H22
    pilote=(180_000, 100_000, 60_000),       # H23
)
ANNEES = 3             # H24
RAMPE_A1 = 0.5         # H24 : gains de l'année 1 à 50 %

def benefice_an(p):
    return p["users"] * p["h_semaine"] * p["semaines"] * p["part_eco"] * p["adoption"] * p["cout_h"]

def net(p, c):
    gains = benefice_an(p) * (RAMPE_A1 + (ANNEES - 1))
    couts = c["pilote"] + c["socle"] + c["build"] + c["run_an"] * ANNEES
    return gains, couts, gains - couts

def pick(d, i):
    return {k: v[i] for k, v in d.items()}

res = {}
for nom, i in (("pessimiste", 0), ("central", 1), ("optimiste", 2)):
    g, c, n = net(pick(G, i), pick(C, i))
    res[nom] = dict(gains=round(g), couts=round(c), net=round(n), benefice_an=round(benefice_an(pick(G, i))))

# Sensibilité à un facteur : on fait varier un paramètre de pessimiste à optimiste, les autres au central.
sens = []
for d in (G, C):
    for k in d:
        if d[k][0] == d[k][2]:
            continue
        lo = dict(pick(G, 1)); lo2 = dict(pick(C, 1))
        hi = dict(pick(G, 1)); hi2 = dict(pick(C, 1))
        (lo if d is G else lo2)[k] = d[k][0]
        (hi if d is G else hi2)[k] = d[k][2]
        n_lo = net(lo, lo2)[2]; n_hi = net(hi, hi2)[2]
        sens.append((k, round(n_lo), round(n_hi), round(abs(n_hi - n_lo))))
sens.sort(key=lambda x: -x[3])

# Seuil de rentabilité : part économisée qui annule le net, autres paramètres au central
pc, cc = pick(G, 1), pick(C, 1)
couts = net(pc, cc)[1]
base = benefice_an({**pc, "part_eco": 1.0}) * (RAMPE_A1 + ANNEES - 1)
seuil_part = couts / base

# Grille à deux entrées sur les deux facteurs les plus influents (autres paramètres au central)
grille = {}
for pe in G["part_eco"]:
    for ad in G["adoption"]:
        grille[f"{int(pe*100)}%/{int(ad*100)}%"] = round(net({**pc, "part_eco": pe, "adoption": ad}, cc)[2])

# Coûts pessimistes avec gains centraux (croisement cité en section 8)
croise = round(net(pick(G, 1), pick(C, 0))[2])

out = dict(croise_gains_centraux_couts_pessimistes=croise, scenarios=res, sensibilite=sens, seuil_part_eco=round(seuil_part, 3), grille_part_eco_x_adoption=grille)
def net_seuil_go():
    """Net sur 3 ans avec les gains centraux et chaque coût au central majoré de 20 % (H35)."""
    c = {nom: v[1] * 1.2 for nom, v in C.items()}
    return round(net(pick(G, 1), c)[2])

def k(x):
    v = round(x / 1000)
    return ("-" if v < 0 else "") + f"{abs(v):,}".replace(",", " ")

def e(x):
    return f"{x:,}".replace(",", " ")

def lignes_registre():
    """Lignes D du registre, générées : aucune saisie manuelle."""
    L = []
    for i, nom in enumerate(("pessimiste", "central", "optimiste"), 1):
        r = res[nom]
        L.append((f"D0{i}", f"Scénario {nom} : gains sur 3 ans / coûts sur 3 ans / net",
                  f"{k(r['gains'])} k€ ({e(r['gains'])} €) / {k(r['couts'])} k€ ({e(r['couts'])} €) / {k(r['net'])} k€ ({e(r['net'])} €) ; gain annuel en régime {k(r['benefice_an'])} k€",
                  "calcul/business_case.py, entrées H03 à H06, H17 à H24"))
    L.append(("D04", "Seuil de rentabilité : part du temps économisée qui annule le net (autres paramètres au central)",
              f"{seuil_part*100:.1f} % ({str(round(seuil_part*100,1)).replace('.', ',')} % à l'écrit)", "calcul/business_case.py"))
    L.append(("D05", "Net sur 3 ans selon part économisée / adoption (autres au central), en k€",
              "; ".join(f"{a} : {k(v)}" for a, v in grille.items()), "calcul/business_case.py"))
    L.append(("D06", "Écart de net (pessimiste à optimiste) par facteur, en k€",
              "; ".join(f"{s_[0]} : {k(s_[3])}" for s_ in sens), "calcul/business_case.py"))
    L.append(("D07", "Valeurs arrondies à l'euro utilisées à l'oral dans le pitch (net sur 3 ans pessimiste / central / optimiste)",
              " / ".join(f"{e(round(res[n]['net'], -3))} €" for n in ("pessimiste", "central", "optimiste")), "arrondis de D01 à D03"))
    L.append(("D08", "Croisement : gains du scénario central avec les coûts pessimistes, net sur 3 ans",
              f"{k(croise)} k€ ({e(croise)} €)", "calcul/business_case.py, clé croise_gains_centraux_couts_pessimistes"))
    L.append(("D09", "Net sur 3 ans quand un paramètre varie seul de pessimiste à optimiste (autres au central), en k€",
              "; ".join(f"{s_[0]} : {k(s_[1])} à {k(s_[2])}" for s_ in sens), "calcul/business_case.py ; valeurs affichées dans la figure de sensibilité"))
    L.append(("D10", "Net du scénario central, repère de la figure de sensibilité, en k€", f"{k(res['central']['net'])}", "calcul/business_case.py"))
    L.append(("D11", "Net sur 3 ans avec les gains centraux et chaque coût au central majoré de 20 % (seuil de go, H35), en k€", f"{k(net_seuil_go())} k€ ({e(net_seuil_go())} €)", "calcul/business_case.py"))
    return "\n".join(f"| {a} | {b} | {c} | {d_} | 2026-11-06 | B |" for a, b, c, d_ in L)

if __name__ == "__main__":
    if "--registre" in __import__("sys").argv:
        print(lignes_registre()); raise SystemExit
    print(json.dumps(out, indent=1, ensure_ascii=False))
