"""Génère les figures SVG du dossier à partir de calcul/resultats.json (aucune valeur saisie à la main)."""
import json, pathlib
racine = pathlib.Path(__file__).resolve().parent.parent
d = json.loads((racine / "calcul" / "resultats.json").read_text(encoding="utf-8"))
NOMS = {"part_eco": "Part de temps économisée", "adoption": "Taux d'adoption", "cout_h": "Coût horaire",
        "run_an": "Exploitation annuelle", "build": "Construction", "pilote": "Pilote", "socle": "Socle (O1)"}

def k(x): return f"{round(x/1000):,}".replace(",", " ")

def tornade():
    L = sorted(d["sensibilite"], key=lambda s: -s[3])
    W, H, m, ligne = 640, 40 + 30 * len(L), 190, 30
    lo = min(min(s[1], s[2]) for s in L); hi = max(max(s[1], s[2]) for s in L)
    x = lambda v: m + (v - lo) / (hi - lo) * (W - m - 30)
    net0 = d["scenarios"]["central"]["net"]
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Sensibilité du net sur 3 ans">',
           f'<style>text{{font:11px sans-serif;fill:#222}} .t{{font-weight:bold}}</style>',
           f'<text x="4" y="16" class="t">Net sur 3 ans (k€) quand un paramètre varie seul, les autres au central</text>']
    for i, (nom, a, b, _) in enumerate(L):
        y = 32 + i * ligne
        xa, xb = x(min(a, b)), x(max(a, b))
        out.append(f'<text x="4" y="{y+14}">{NOMS.get(nom, nom)}</text>')
        out.append(f'<rect x="{xa:.1f}" y="{y}" width="{max(xb-xa,1):.1f}" height="20" fill="#5b8bd6"/>')
        out.append(f'<text x="{xa-4:.1f}" y="{y+14}" text-anchor="end">{k(min(a,b))}</text>')
        out.append(f'<text x="{xb+4:.1f}" y="{y+14}">{k(max(a,b))}</text>')
    out.append(f'<line x1="{x(net0):.1f}" x2="{x(net0):.1f}" y1="24" y2="{H-4}" stroke="#b33" stroke-dasharray="4 3"/>')
    out.append(f'<line x1="{x(0):.1f}" x2="{x(0):.1f}" y1="24" y2="{H-4}" stroke="#555"/>')
    out.append(f'<text x="{x(net0)+3:.1f}" y="{H-8}" fill="#b33">central {k(net0)}</text></svg>')
    return "\n".join(out)

def scenarios():
    S = d["scenarios"]; noms = [("pessimiste", "Pessimiste"), ("central", "Central"), ("optimiste", "Optimiste")]
    W, H = 640, 190; base = 150; maxv = max(S[n]["gains"] for n, _ in noms)
    h = lambda v: v / maxv * 110
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Gains et coûts sur 3 ans par scénario">',
           '<style>text{font:11px sans-serif;fill:#222} .t{font-weight:bold}</style>',
           '<text x="4" y="16" class="t">Gains et coûts sur 3 ans par scénario (k€)</text>']
    for i, (n, lab) in enumerate(noms):
        x0 = 60 + i * 190
        g, c = S[n]["gains"], S[n]["couts"]
        out.append(f'<rect x="{x0}" y="{base-h(g):.1f}" width="60" height="{h(g):.1f}" fill="#4a9a6a"/><text x="{x0+30}" y="{base-h(g)-4:.1f}" text-anchor="middle">{k(g)}</text>')
        out.append(f'<rect x="{x0+70}" y="{base-h(c):.1f}" width="60" height="{h(c):.1f}" fill="#c4704f"/><text x="{x0+100}" y="{base-h(c)-4:.1f}" text-anchor="middle">{k(c)}</text>')
        out.append(f'<text x="{x0+65}" y="{base+16}" text-anchor="middle" class="t">{lab}</text><text x="{x0+65}" y="{base+30}" text-anchor="middle">net {k(S[n]["net"])}</text>')
    out.append(f'<text x="470" y="30"><tspan fill="#4a9a6a">■</tspan> gains  <tspan fill="#c4704f">■</tspan> coûts</text></svg>')
    return "\n".join(out)

(racine / "dossier" / "figures" / "tornade.svg").write_text(tornade(), encoding="utf-8")
(racine / "dossier" / "figures" / "scenarios.svg").write_text(scenarios(), encoding="utf-8")
print("figures écrites")
