---
titre: P1, dossier de cadrage d'un assistant IA documentaire (client fictif)
date_maj: 2026-11-06
---

# P1 : cadrage d'un assistant IA documentaire pour une collectivité

> **Exercice fictif.** "Métropole Azur" est un client inventé. Aucune donnée réelle de collectivité ni de personne. Tous les chiffres du client sont des hypothèses déclarées dans `registre.md`.

Dossier de conseil qui cadre un cas d'usage IA : un assistant interne qui aide des agents à retrouver et résumer délibérations, règlements et pièces de marchés publics. Il compare quatre options, classe le système au regard du règlement européen sur l'IA, analyse 14 risques (OWASP LLM Top 10 2025, NIST AI 600-1, AI Act), chiffre un business case en fourchettes avec sensibilité, et demande au comité une décision conditionnelle : mesurer, piloter, puis étendre.

## Livrables

| Fichier | Contenu |
|---|---|
| `livrables/dossier-cadrage-metropole-azur.pdf` | dossier de 9 pages |
| `livrables/synthese-2-pages.pdf` | synthèse de 2 pages |
| `dossier/pitch-5-minutes.md` | script de pitch de 5 minutes |
| `dossier/*.md` | sources du dossier, une section par fichier |
| `registre.md` | registre des hypothèses, sources externes et valeurs calculées |
| `sources.md` | sources lues, dates de lecture, état de vérification |
| `calcul/business_case.py` | calcul du business case et de la sensibilité |
| `verification/verifier_chiffres.py` | contrôle : aucun chiffre du dossier absent du registre |
| `notes/` | notes de travail (résumé du NIST AI 600-1, fiche client, périmètre) |
| `archives/` | versions précédentes datées |

## Reconstruire et contrôler

Prérequis : Python 3, Google Chrome, `pdfinfo` (poppler). Installer la dépendance puis lancer le script.

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt && outils/tout_construire.sh .venv/bin/python
```

Le script recalcule le business case, réécrit les lignes D du registre, régénère les deux PDF, lance le contrôle des chiffres (avec un autotest sur un cas positif et un cas négatif) et affiche le nombre de pages et de mots.

## Limites

- Relecture externe : à fournir (critère 9 du cahier, `cahier.md`).
- Textes juridiques : règlement (UE) 2024/1689 lu dans sa version initiale, règlement (UE) 2026/1744 lu sur EUR-Lex ; version consolidée à vérifier avant tout usage réel. Ce n'est pas un avis juridique.
- Gravités, probabilités et coûts sont des jugements de l'auteur.
- Le contrôle des chiffres ne vérifie pas les nombres écrits en lettres.

## Licences

- Code (`calcul/`, `outils/`, `verification/`) : MIT, voir `LICENSE`.
- Documents (`dossier/`, `livrables/`, `registre.md`, `sources.md`, `notes/`, `cahier.md`, `archives/`) : Creative Commons Attribution 4.0 (CC BY 4.0), voir `LICENSE-DOCS.md`.
