# Synthèse : assistant IA documentaire pour Métropole Azur

> **Cas fictif.** Métropole Azur est un client inventé. Les chiffres du client sont des hypothèses déclarées dans le registre (H). Relecture externe à fournir.

**La question.** Faut-il lancer un pilote d'assistant IA qui aide environ 600 agents (H03) à retrouver et résumer délibérations, règlements et pièces de marchés publics ?

**La recommandation en une phrase.** Mesurer d'abord, piloter ensuite, ne généraliser qu'après : une mesure préalable de 4 semaines (H27), puis un pilote de 3 mois et 50 utilisateurs (H08) plafonné, et aucun déploiement général avant les résultats.

## Le problème
Les agents passent en moyenne 3 h par semaine à chercher des documents (H04), sur un corpus estimé à 200 000 pièces (H07). C'est une hypothèse : le dossier prévoit de la mesurer avant d'investir.

## Les options
| Option | Verdict |
|---|---|
| O0 Ne rien faire | référence de mesure |
| O1 Améliorer la recherche existante | socle obligatoire ; peut suffire si le temps perdu vient de l'indexation |
| O2 Assistant sur service externe | écartée pour le pilote : environ 30 % des documents contiendraient des données personnelles (hypothèse H13) |
| O3 Assistant hébergé en environnement maîtrisé | retenue pour le pilote, après O1 |

## Le cadre réglementaire
L'assistant n'entre pas dans les catégories à haut risque du règlement sur l'IA tant que son périmètre exclut toute évaluation de personnes et tout usage par une autorité judiciaire. Les obligations de l'annexe III s'appliquent à partir du 2 décembre 2027 (H11, vérifié sur EUR-Lex). Restent la maîtrise de l'IA du personnel et l'information des utilisateurs. Le RGPD s'applique en parallèle : AIPD recommandée avant le pilote. Une erreur de classement coûterait cher : d'où un périmètre écrit et une réévaluation à chaque changement d'usage.

## Les risques qui comptent
Quatorze risques sont analysés avec mesure et responsable. Quatre concentrent l'enjeu : la réponse fausse sur le droit (R01), la fuite de données personnelles (R04), l'accès à un document non autorisé (R05) et l'injection d'instructions cachées dans les documents (R06). Mesures clés : réponse toujours citée et refusée sans source, droits d'accès au niveau du document, assistant en lecture seule, jeu de 200 questions dont des pièges (H26).

## Le business case
| Net sur 3 ans | Pessimiste | Central | Optimiste |
|---|---|---|---|
| Gains | 444 k€ | 1 247 k€ | 2 851 k€ |
| Coûts | 1 620 k€ | 880 k€ | 460 k€ |
| **Net** | **-1 176 k€** | **367 k€** | **2 391 k€** |

Le central est positif mais fragile : il couvre ses coûts à partir de 21.2 % de temps économisé (D04), contre 30 % supposé. Les deux facteurs décisifs sont la part de temps économisée (H05) et le taux d'adoption (H19) ; ce sont aussi ceux qu'un pilote mesure. Les coûts sont des hypothèses à confirmer par le marché.

## La décision demandée
1. Autoriser la phase de mesure préalable, l'AIPD et la consultation du marché.
2. Autoriser le pilote sous conditions, avec un budget plafonné à la borne haute de H23.
3. Refuser tout déploiement général avant la décision d'extension.

**Arrêt du pilote** si le gain mesuré reste sous 10 % à la fin du mois 2 (H25), si les réponses correctes et sourcées passent sous 90 % (H14), ou en cas d'incident de confidentialité non maîtrisé.

**Ce qui rendrait la recommandation fausse.** La mesure préalable montre que le temps est perdu à retrouver plutôt qu'à lire : O1 seule suffit. Ou les devis réels tombent dans la zone pessimiste des coûts.
