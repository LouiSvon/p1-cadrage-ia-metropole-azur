#!/bin/bash
# Reconstruit les PDF et lance les contrôles. Usage : outils/tout_construire.sh [chemin_python]
set -euo pipefail
cd "$(dirname "$0")/.."
PY="${1:-python3}"
mkdir -p livrables
"$PY" calcul/business_case.py > calcul/resultats.json
"$PY" outils/maj_registre.py
"$PY" outils/construire.py "Cadrage d'un assistant IA documentaire pour Métropole Azur (cas fictif)" livrables/dossier-cadrage-metropole-azur.pdf dossier/00-page-de-garde.md dossier/01-contexte.md dossier/02-besoin.md dossier/03-options.md dossier/04-ai-act.md dossier/05-risques.md dossier/06-business-case.md dossier/07-gouvernance.md dossier/08-plan-et-decision.md
"$PY" outils/construire.py "Synthèse : assistant IA documentaire pour Métropole Azur (cas fictif)" livrables/synthese-2-pages.pdf dossier/synthese.md
"$PY" verification/verifier_chiffres.py --autotest
"$PY" verification/verifier_chiffres.py
echo "pages dossier : $(pdfinfo livrables/dossier-cadrage-metropole-azur.pdf | awk '/Pages/{print $2}')"
echo "pages synthese : $(pdfinfo livrables/synthese-2-pages.pdf | awk '/Pages/{print $2}')"
echo "mots pitch : $(awk 'f>=2{print} /^---$/{f++}' dossier/pitch-5-minutes.md | wc -w)"
