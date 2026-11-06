---
titre: Cahier P1 (copie du CAHIER.md de la session Plan carrière)
date_maj: 2026-10-29
---

# P1 : Dossier de cadrage d'un cas d'usage IA

Statut : démarrage le 2026-10-19. Fin prévue le 2026-12-06 (7 semaines, 7 h par semaine, environ 48 h).

## But
Produire un dossier de conseil crédible sur un cas d'usage IA : cadrer, évaluer le risque, chiffrer, gouverner.
Il doit prouver une posture de conseil (décider avec des hypothèses assumées), pas une compétence de code.

## Cadre fictif (à dire en tête du dossier)
- Client : "Métropole Azur" (nom inventé, collectivité fictive de plusieurs centaines de milliers d'habitants).
- Cas d'usage : assistant IA interne qui aide les agents à retrouver et résumer délibérations, règlements et pièces de marchés publics.
- Tout chiffre du client est une hypothèse déclarée. Les chiffres externes ont une source publique et une date.

## Critères de réussite (vérifiables)
1. Dossier PDF de 15 pages maximum, plus une synthèse de 2 pages et un script de pitch de 5 minutes.
2. Le caractère fictif du client est écrit en première page.
3. Registre des hypothèses (`registre.md`) : au moins 15 lignes, chacune avec valeur, source ou "hypothèse", date, niveau de confiance.
4. Aucun chiffre du dossier absent du registre.
5. Matrice de risques : au moins 10 risques, chacun relié à une catégorie OWASP LLM Top 10 (2025), au NIST AI 600-1 ou à l'AI Act, avec gravité, probabilité, mesure et responsable.
6. Classification AI Act argumentée, avec la date de la source juridique consultée et la mention de ce qui reste incertain.
7. Business case en fourchettes (bas, central, haut) et une analyse de sensibilité sur les 2 hypothèses les plus influentes.
8. Au moins une option "ne pas faire" ou "faire autrement" comparée à la solution retenue.
9. Relu par au moins une personne extérieure (enseignant, professionnel, ami en conseil) ; retours notés.
10. Dépôt public avec README, PDF, registre, licence. Aucune donnée personnelle.

## Plan des sections du dossier
1. Contexte et enjeux du client (1 p.)
2. Besoin, parties prenantes, périmètre (1,5 p.)
3. Options étudiées et critères de choix (2 p.)
4. Classification AI Act et exigences associées (2 p.)
5. Analyse de risques et mesures (3 p.)
6. Business case et sensibilité (2,5 p.)
7. Gouvernance, conduite du changement, indicateurs (2 p.)
8. Plan de déploiement par phases et décision demandée (1 p.)

## Jalons
| Sem. | Dates | Livrable | Heures |
|---|---|---|---|
| 1 | 19 au 25 oct. | Fiche client fictif, périmètre. Lecture des sources primaires : AI Act (EUR-Lex), NIST AI 600-1, OWASP LLM Top 10 2025. Premières lignes du registre. | 7 |
| 2 | 26 oct. au 1er nov. | Sections 1 à 3 : besoin, parties prenantes, options. | 7 |
| 3 | 2 au 8 nov. | Sections 4 et 5 : classification AI Act, matrice de risques. | 7 |
| 4 | 9 au 15 nov. | Section 6 : business case et sensibilité. | 7 |
| 5 | 16 au 22 nov. | Sections 7 et 8 : gouvernance, plan, décision demandée. | 7 |
| 6 | 23 au 29 nov. | Synthèse 2 pages, script du pitch, relecture externe. | 7 |
| 7 | 30 nov. au 6 déc. | Corrections, mise en page PDF, publication du dépôt, brouillons de posts LinkedIn. | 6 |

## Règles de qualité
- Une hypothèse sans source reste étiquetée "hypothèse". Pas de chiffre inventé présenté comme un fait.
- Les dates d'application de l'AI Act ont changé avec l'Omnibus numérique et les sources divergent sur son état d'adoption : vérifier sur EUR-Lex le jour de la rédaction de la section 4 et noter la date de consultation.
- Pas de conseil financier personnalisé, pas de données réelles de personnes.
- Point d'arrêt à la fin de la semaine 3 : si le dossier dépasse 20 h au total, réduire le périmètre (retirer l'option la moins utile, pas la rigueur du registre).

## Ce que vous apprenez en le faisant
Structure et logique de l'AI Act (rôles, catégories de risque), NIST AI 600-1, OWASP LLM Top 10, construction d'un business case en fourchettes, rédaction d'une synthèse décisionnelle.
