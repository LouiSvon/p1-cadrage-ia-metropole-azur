## 6. Business case et sensibilité

### 6.1 Ce que le calcul mesure

Le gain est du temps d'agent libéré, valorisé au coût horaire chargé. Ce n'est pas une économie budgétaire : le temps libéré ne devient un euro épargné que s'il est réaffecté. Le calcul compare ce temps valorisé aux coûts de l'option retenue (socle O1, pilote, construction et exploitation d'O3) sur un horizon de 3 ans, avec des gains à 50 % la première année (H24). Tout est recalculable avec `calcul/business_case.py`, et les figures de cette section sont générées par `outils/figures.py` à partir de ses résultats.

**Formule du gain annuel en régime.** utilisateurs (H03) x heures de recherche par semaine (H04) x semaines (H17) x part économisée (H05) x taux d'adoption (H19) x coût horaire (H06).

### 6.2 Les hypothèses et leur solidité

| Hypothèse | Pessimiste | Central | Optimiste | Solidité |
|---|---|---|---|---|
| Part économisée (H05) | 20 % | 30 % | 40 % | basse : aucune mesure sur le terrain ; repère auto-déclaré (E01) |
| Adoption (H19) | 40 % | 60 % | 80 % | basse : dépend de la qualité perçue et de la formation |
| Coût horaire (H06) | 28 € | 35 € | 45 € | moyenne : ancré sur 2 640 € bruts par mois en fonction publique territoriale en 2022 (E02), puis majoré par des hypothèses |
| Socle (H20) | 150 k€ | 80 k€ | 40 k€ | basse : hypothèse sans devis |
| Pilote (H23) | 180 k€ | 100 k€ | 60 k€ | basse : hypothèse sans devis |
| Construction (H21) | 450 k€ | 250 k€ | 120 k€ | basse : hypothèse sans devis |
| Exploitation annuelle (H22) | 280 k€ | 150 k€ | 80 k€ | basse : hypothèse sans devis |

Les trois derniers coûts sont dits « élevé, central, bas » : dans le scénario pessimiste, on prend le coût élevé.

**Coûts non chiffrés.** Le calcul n'inclut ni la formation des agents, ni le temps des juristes pour la revue d'un échantillon de réponses (H32), ni la conduite du changement, ni l'effort du DPO et de la DSI. Le net réel est donc inférieur au net calculé. Ils sont à estimer en phase 0, avec les devis.

### 6.3 Trois scénarios

Le scénario pessimiste combine les gains bas et les coûts élevés, l'optimiste l'inverse : ce sont des bornes, pas des prévisions.

| Poste (3 ans) | Pessimiste | Central | Optimiste |
|---|---|---|---|
| Gain annuel en régime | 177 k€ | 499 k€ | 1 140 k€ |
| Gains sur 3 ans | 444 k€ | 1 247 k€ | 2 851 k€ |
| Coûts sur 3 ans | 1 620 k€ | 880 k€ | 460 k€ |
| **Net sur 3 ans** | **-1 176 k€** | **367 k€** | **2 391 k€** |

<div><!-- SVG:dossier/figures/scenarios.svg --></div>

Les coûts regroupent le socle (H20), le pilote (H23), la construction (H21) et trois ans d'exploitation (H22).

**Lecture.** Le scénario central est positif, mais le résultat va de -1 176 k€ à 2 391 k€ : l'incertitude dépasse le net central. La décision ne peut donc pas reposer sur le central. Elle doit reposer sur ce que le pilote permet de mesurer.

**Repère externe pour juger la part économisée.** Un test britannique dans l'administration a mesuré, par déclaration des agents, 26 minutes économisées par jour sur l'ensemble des tâches (E01, communiqué du 2 juin 2025). Notre scénario central suppose environ 11 minutes par jour sur la seule recherche documentaire (H05). Le repère britannique est auto-déclaré, porte sur d'autres usages et ne vaut pas validation ; il indique seulement que notre central n'est pas déraisonnable.

### 6.4 Analyse de sensibilité

On fait varier chaque paramètre seul, du pessimiste à l'optimiste, les autres restant au central. Les deux hypothèses les plus influentes sont la part de temps économisée (H05) et le taux d'adoption (H19) : chacune fait varier le net de 832 k€. Elles arrivent ex aequo parce que leurs deux fourchettes doublent le gain ; elles forment en pratique un seul facteur, le temps réellement libéré par agent. Viennent ensuite le coût horaire (606 k€) et le coût annuel d'exploitation (600 k€). La construction (330 k€), le pilote (120 k€) et le socle (110 k€) pèsent peu.

<div><!-- SVG:dossier/figures/tornade.svg --></div>

Net sur 3 ans, en k€, selon les deux facteurs (autres paramètres au central) :

| Part économisée \ Adoption | 40 % | 60 % | 80 % |
|---|---|---|---|
| 20 % | -326 | -48 | 229 |
| 30 % | -48 | 367 | 783 |
| 40 % | 229 | 783 | 1 338 |

### 6.5 Seuil de rentabilité et croisement des risques

**Seuil de rentabilité.** Avec les autres paramètres au central, l'assistant couvre ses coûts si la part de temps économisée atteint 21,2 % (D04), soit à peine au-dessus du bas de la fourchette (H05). Autrement dit, le central est rentable mais fragile : un gain réel un peu inférieur aux attentes suffit à le rendre déficitaire.

**Coûts pessimistes avec gains centraux.** Si le marché répond dans la zone des coûts élevés mais que l'usage est celui du scénario central, le net est de -373 k€ (D08). Cela signifie que la consultation du marché peut à elle seule faire échouer le projet : elle est donc l'un des livrables de la phase 0, avant tout engagement.

### 6.6 Conséquence pour la décision

Les deux facteurs qui décident du résultat sont précisément ceux qu'un pilote peut mesurer : le temps réellement économisé et l'adoption. Il faut donc piloter pour apprendre ces deux valeurs avant d'engager les coûts de construction et d'exploitation. La section 8 organise cet ordre.
