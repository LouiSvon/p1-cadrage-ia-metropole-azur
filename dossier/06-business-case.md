## 6. Business case et sensibilité

**Ce que le calcul mesure.** Le gain est du temps d'agent libéré, valorisé au coût horaire chargé. Ce n'est pas une économie budgétaire : le temps libéré ne devient un euro épargné que s'il est réaffecté. Le calcul compare ce temps valorisé aux coûts de l'option retenue (socle O1, pilote, construction et exploitation d'O3) sur un horizon de 3 ans, avec des gains à 50 % la première année (H24). Tout est recalculable avec `calcul/business_case.py`.

**Formule du gain annuel en régime.** utilisateurs (H03) x heures de recherche par semaine (H04) x semaines (H17) x part économisée (H05) x taux d'adoption (H19) x coût horaire (H06).

**Trois scénarios.** Le scénario pessimiste combine les gains bas et les coûts élevés, l'optimiste l'inverse : ce sont des bornes, pas des prévisions.

| Poste (3 ans) | Pessimiste | Central | Optimiste |
|---|---|---|---|
| Part économisée (H05) | 20 % | 30 % | 40 % |
| Adoption (H19) | 40 % | 60 % | 80 % |
| Coût horaire (H06) | 28 € | 35 € | 45 € |
| Gain annuel en régime | 177 k€ | 499 k€ | 1 140 k€ |
| Gains sur 3 ans | 444 k€ | 1 247 k€ | 2 851 k€ |
| Coûts sur 3 ans | 1 620 k€ | 880 k€ | 460 k€ |
| **Net sur 3 ans** | **-1 176 k€** | **367 k€** | **2 391 k€** |

Les coûts regroupent le socle (H20), le pilote (H23), la construction (H21) et trois ans d'exploitation (H22). Ce sont des hypothèses larges à confirmer par une consultation du marché, non des devis.

**Lecture.** Le scénario central est positif, mais le résultat va de -1 176 k€ à 2 391 k€ : l'incertitude dépasse le net central. La décision ne peut donc pas reposer sur le central. Elle doit reposer sur ce que le pilote permet de mesurer.

**Repère externe pour juger la part économisée.** Un test britannique dans l'administration a mesuré, par déclaration des agents, 26 minutes économisées par jour sur l'ensemble des tâches (E01, communiqué du 2 juin 2025). Notre scénario central suppose environ 11 minutes par jour sur la seule recherche documentaire (H05). Le repère britannique est auto-déclaré, porte sur d'autres usages et ne vaut pas validation ; il indique seulement que notre central n'est pas déraisonnable.

**Analyse de sensibilité.** On fait varier chaque paramètre seul, du pessimiste à l'optimiste, les autres restant au central. Les deux hypothèses les plus influentes sont la part de temps économisée (H05) et le taux d'adoption (H19) : chacune fait varier le net de 832 k€. Elles arrivent ex aequo parce que leurs deux fourchettes doublent le gain ; elles forment en pratique un seul facteur, le temps réellement libéré par agent. Viennent ensuite le coût horaire (606 k€) et le coût annuel d'exploitation (600 k€). La construction (330 k€), le pilote (120 k€) et le socle (110 k€) pèsent peu.

Net sur 3 ans, en k€, selon les deux facteurs (autres paramètres au central) :

| Part économisée \ Adoption | 40 % | 60 % | 80 % |
|---|---|---|---|
| 20 % | -326 | -48 | 229 |
| 30 % | -48 | 367 | 783 |
| 40 % | 229 | 783 | 1 338 |

**Seuil de rentabilité.** Avec les autres paramètres au central, l'assistant couvre ses coûts si la part de temps économisée atteint 21.2 % (D04), soit à peine au-dessus du bas de la fourchette (H05). Autrement dit, le central est rentable mais fragile : un gain réel un peu inférieur aux attentes suffit à le rendre déficitaire.

**Conséquence pour la décision.** Les deux facteurs qui décident du résultat sont précisément ceux qu'un pilote peut mesurer : le temps réellement économisé et l'adoption. Il faut donc piloter pour apprendre ces deux valeurs avant d'engager les coûts de construction et d'exploitation. La section 8 organise cet ordre.
