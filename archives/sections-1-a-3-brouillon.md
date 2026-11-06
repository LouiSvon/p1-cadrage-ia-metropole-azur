---
titre: Brouillon des sections 1 à 3 du dossier P1
date_maj: 2026-10-29
---

Brouillon à relire et corriger par Louis. Statut : non validé. Tous les chiffres renvoient à `registre.md` (identifiant H..). Les chiffrages (coûts, gains en euros) arrivent en section 6, pas ici.

# Avertissement (première page du dossier)

Métropole Azur est un client fictif. Ce dossier est un exercice de conseil : aucune donnée réelle de collectivité ni de personne. Les chiffres du client sont des hypothèses déclarées dans le registre ; les chiffres externes citent leur source et leur date.

# 1. Contexte et enjeux (1 page)

Métropole Azur compte environ 500 000 habitants (H01) et emploie environ 4 000 agents (H02). Ses services juridiques, de commande publique et administratifs manipulent chaque jour des délibérations, des règlements et des pièces de marchés publics, soit un corpus estimé à 200 000 documents (H07), répartis entre plusieurs outils.

Enjeu : environ 600 agents (H03) consacrent en moyenne 3 h par semaine à la recherche documentaire (H04). Ce temps est une hypothèse de départ, à valider par une mesure sur échantillon avant tout investissement. Il pèse sur la réactivité des services et sur la sécurité juridique (un règlement ou une délibération manqué).

Pourquoi maintenant : l'IA générative permet de poser une question en langage courant et d'obtenir un résumé sourcé, mais elle introduit des risques propres (réponses fausses, fuite de données, dépendance à un fournisseur). Le cadre réglementaire européen est en cours de précision (voir section 4 ; dates non vérifiées sur EUR-Lex à ce jour).

Question posée au comité : faut-il lancer un pilote, sous quelles conditions, et avec quels critères d'arrêt ?

# 2. Besoin, parties prenantes, périmètre (1,5 page)

## Besoin
Retrouver rapidement le bon texte (délibération, article de règlement, clause d'un marché) et en obtenir un résumé citant précisément la source et le passage, afin que l'agent vérifie avant d'agir.

## Périmètre
- Dans le périmètre : recherche et résumé sur un corpus de documents textuels, utilisateurs internes uniquement, réponses avec citation de la source.
- Hors périmètre : service aux citoyens, décision ou notation de personnes, rédaction d'actes signés, données de santé, sociales ou RH.
- Pilote : 3 mois et 50 utilisateurs (H08).

## Parties prenantes
Direction juridique et commande publique (porteur), DSI (hébergement, sécurité), DPO (RGPD, registre des traitements), direction générale et élus (budget, image), agents utilisateurs, représentants du personnel (consultation à confirmer). Détail dans `perimetre.md`.

## Contraintes et hypothèses de cadrage
Une part des documents contient des données personnelles, estimée à 30 % (H13). Les réponses doivent rester vérifiables par l'agent, qui garde la décision. Cible de qualité du pilote : 90 % de réponses correctes et sourcées (H14).

# 3. Options étudiées et critères de choix (2 pages)

## Options
| Option | Description |
|---|---|
| O0 Ne rien faire | Conserver les outils actuels. Sert de référence. |
| O1 Améliorer la recherche existante | Indexation plein texte, métadonnées, nettoyage du corpus, sans IA générative. |
| O2 Assistant IA sur service cloud d'un fournisseur | Assistant qui interroge les documents (recherche puis génération) via une offre externe. |
| O3 Assistant IA hébergé en environnement maîtrisé | Même principe avec un modèle ouvert hébergé par la métropole ou un cloud de confiance. |

## Critères (H16)
Valeur (gain de temps et de fiabilité), risque (réponses fausses, fuite de données), coût, souveraineté et dépendance au fournisseur, délai de mise en œuvre, maturité de l'organisation (données, compétences).

## Comparaison qualitative (hypothèses de travail, à affiner en sections 5 et 6)
| Critère | O0 | O1 | O2 | O3 |
|---|---|---|---|---|
| Valeur | nulle | moyenne (retrouver, pas résumer) | forte | forte |
| Risque | aucun nouveau | faible | élevé (confabulation, données hors maîtrise) | moyen (confabulation ; sécurité à charge de la métropole) |
| Coût | nul | faible | à chiffrer | à chiffrer, probablement plus élevé au départ |
| Souveraineté | totale | totale | faible | forte |
| Délai | immédiat | court | court | plus long |
| Maturité requise | aucune | faible | moyenne | élevée |

## Recommandation provisoire (hypothèse de travail, à confirmer en section 6)
O1 comme socle obligatoire (un assistant n'est utile que si le corpus est propre et indexé), puis pilote d'O3 sur un périmètre restreint. O2 écartée pour le pilote à cause de la maîtrise des données (30 % de documents avec données personnelles, H13). O0 reste la référence pour mesurer le gain.

## Meilleur contre-argument
O1 seule peut suffire : si l'essentiel du temps perdu vient de l'indexation, une meilleure recherche règle le problème à moindre risque. Le dossier doit donc mesurer d'abord la part du temps perdu à retrouver (H04) par rapport à lire et résumer. Cette mesure est la première condition du pilote.
