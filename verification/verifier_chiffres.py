"""Critère 4 du cahier : aucun chiffre du dossier absent du registre.
Usage : python verification/verifier_chiffres.py            (vérifie le dossier)
        python verification/verifier_chiffres.py --autotest  (cas positif et négatif du détecteur)
Limite : les nombres écrits en lettres (quatre, quatorze) ne sont pas contrôlés."""
import re, sys, pathlib

RACINE = pathlib.Path(__file__).resolve().parent.parent
FICHIERS = sorted((RACINE / "dossier").glob("*.md")) + sorted((RACINE / "annexes").glob("*.md")) + sorted((RACINE / "dossier" / "figures").glob("*.svg"))
MOIS = "janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre"

# Constructions qui contiennent des chiffres sans être des chiffres du dossier : identifiants, références, dates, numérotation.
IGNORES = [
    r"^---\n.*?\n---\n",                              # frontmatter
    r"`[^`]*`",                                       # code en ligne (chemins, noms de fichiers)
    r"\b[HDER]\d{2}\b(?:\s*(?:à|et)\s*[HDER]\d{2}\b)?",   # identifiants du registre, plages comprises
    r"\bO\d\b", r"\bLLM\d{2}\b", r"\b[A-Z]{2}-\d\.\d+-\d{3}\b", r"\b(?:GV|MP|MS|MG)-\d\.\d+\b",
    r"NIST AI 600-1", r"AI 600-1", r"\b(?:20\d\d)/\d{3,4}\b",           # titres et références de textes
    r"\b(?:articles?|Articles?|sections?|Sections?|points?|annexes?|chapitres?|paragraphes?|phases?|Phase|critères?|critère)\s+\d+(?:\s*\(\w\))?(?:\s*(?:à|et|,)\s*\d+)*",
    r"\b\d+\(\w\)",                                    # 8(a)
    rf"\b\d{{1,2}}(?:er)?\s+(?:{MOIS})\s+20\d\d\b", rf"\b(?:{MOIS})\s+20\d\d\b", r"\b20\d\d-\d\d-\d\d\b", r"\b20[23]\d\b",
    r"^\s*#+\s*\d+\.", r"^\s*\d+\.\s", r"^\s*\|\s*\d+\.\s", r"\[\d:\d\d\]",                # titres numérotés, listes numérotées
    r"\bMétropole Azur\b", r"\bR\d{2}\b", r"\bUn\s*:", r"\b1 comité\b",
]
NOMBRE = re.compile(r"\d+(?:[  .,]\d{3})*(?:[.,]\d+)?")

def norm(tok):
    return tok.replace(" ", "").replace(" ", "").replace(" ", "").replace(",", ".")

def sans_balises(texte):
    return re.sub(r"<[^>]+>", " ", re.sub(r"<style.*?</style>", " ", texte, flags=re.S))

def jetons(texte):
    return {norm(t) for t in NOMBRE.findall(texte)}

def nettoyer(texte):
    for motif in IGNORES:
        texte = re.sub(motif, " ", texte, flags=re.M | re.S if motif.startswith("^---") else re.M)
    return texte

def manquants(texte, registre_jetons):
    return sorted(j for j in jetons(nettoyer(texte)) if j not in registre_jetons)

def charger_registre():
    return jetons((RACINE / "registre.md").read_text(encoding="utf-8"))

def autotest():
    reg = {"30", "21.2", "1247", "10"}
    assert manquants("Part de 30 % et 21,2 % et 1 247 k€.", reg) == [], "cas positif : tout est au registre"
    assert manquants("Part de 37 % et 30 %.", reg) == ["37"], "cas négatif : 37 doit être signalé"
    assert manquants("Voir article 50(2), R01, H05 et le 2 août 2026, O3, LLM09.", reg) == [], "références ignorées"
    print("autotest OK : cas positif, cas négatif et références ignorées")

if __name__ == "__main__":
    if "--autotest" in sys.argv:
        autotest(); sys.exit(0)
    reg = charger_registre(); code = 0
    for f in FICHIERS:
        t = f.read_text(encoding="utf-8")
        m = manquants(sans_balises(t) if f.suffix == ".svg" else t, reg)
        print(f"{f.name}: {'OK' if not m else 'ABSENTS DU REGISTRE ' + ', '.join(m)}")
        code |= bool(m)
    sys.exit(code)
