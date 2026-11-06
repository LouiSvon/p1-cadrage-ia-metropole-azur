## 3. Options étudiées et critères de choix

### 3.1 Quatre options

| Option | Description |
|---|---|
| O0 Ne rien faire | Conserver les outils actuels. Sert de référence pour mesurer le gain. |
| O1 Améliorer la recherche existante | Indexation plein texte, métadonnées (date de validité, statut abrogé ou en vigueur), nettoyage du corpus, sans IA générative. |
| O2 Assistant IA sur service d'un fournisseur externe | L'assistant interroge les documents puis génère une réponse, via une offre hébergée par un tiers. |
| O3 Assistant IA hébergé en environnement maîtrisé | Même principe avec un modèle ouvert, hébergé par la métropole ou chez un hébergeur de confiance. |

### 3.2 Critères

Six critères (H16) : valeur (gain de temps et de fiabilité), risque (réponses fausses, fuite de données), coût, souveraineté et dépendance au fournisseur, délai, maturité de l'organisation. Ils ne sont pas pondérés numériquement : un score chiffré donnerait une précision que les données ne permettent pas. Le dossier classe les options qualitativement, puis teste ce qui ferait basculer le classement (dernière sous-section).

### 3.3 Comparaison qualitative

Jugement de l'auteur, à confronter aux devis réels.

| Critère | O0 | O1 | O2 | O3 |
|---|---|---|---|---|
| Valeur | nulle | moyenne : retrouver, sans résumer | forte | forte |
| Risque | aucun nouveau | faible | élevé : réponses fausses ; données hors maîtrise | moyen : réponses fausses ; sécurité à la charge de la métropole |
| Coût | nul | faible | à chiffrer | élevé au départ |
| Souveraineté | totale | totale | faible | forte |
| Délai | immédiat | court | court | long |
| Maturité requise | aucune | faible | moyenne | élevée |

### 3.4 À quoi ressemble O3

Ce schéma technique est nécessaire pour que le comité sache ce qu'il achète, et parce que chaque composant porte un risque de la section 5. Il reste volontairement simple.

| Composant | Rôle | Risques associés (section 5) |
|---|---|---|
| Ingestion | récupère les documents, les convertit en texte, applique la pseudonymisation et les métadonnées de validité | R04, R09, R02 |
| Index et base vectorielle | permet de retrouver les passages pertinents, avec les droits d'accès de chaque document | R05 |
| Recherche (retrieval) | sélectionne les passages à fournir au modèle | R05, R06 |
| Modèle de langage | rédige la réponse à partir des seuls passages fournis | R01, R08, R12 |
| Contrôle des citations | vérifie que chaque affirmation renvoie à un passage et refuse sinon | R01 |
| Interface | affiche réponse, sources, statut des textes, avertissement permanent | R03 |
| Journaux | consignent les questions et les réponses pour l'audit | R04 |

Principe retenu : le modèle ne répond qu'à partir des passages retrouvés et l'assistant n'a aucun droit d'action en dehors de l'affichage. Ce principe est l'une des mesures recommandées contre l'injection de prompt (moindre privilège, E15) et contre les fuites entre contextes (accès par document, E16). Le guide de l'ANSSI (E11) porte sur la sécurité de l'architecture d'un système d'IA générative ; il sert de référence à la DSI pour cette partie, sans que le dossier le détaille (PDF non lu, voir `sources.md`).

### 3.5 Recommandation et tests de bascule

**Recommandation.** O1 comme socle obligatoire, car un assistant n'est utile que sur un corpus propre, daté et correctement indexé, puis pilote d'O3 sur un périmètre restreint. O2 est écartée pour le pilote : selon l'hypothèse H13, près d'un tiers des documents contiendrait des données personnelles et le comité doit pouvoir garantir où elles sont traitées. O0 reste la référence de mesure.

**Ce qui ferait changer le classement.**
- Si la phase 0 montre que l'essentiel du temps est perdu à retrouver, non à lire : O1 seule devient la recommandation.
- Si un fournisseur externe propose un hébergement et des garanties contractuelles qui permettent de traiter les données personnelles dans le cadre voulu par le DPO, O2 redevient comparable à O3 sur le risque et meilleure sur le délai.
- Si la consultation du marché place le coût d'O3 dans la zone pessimiste (H21, H22), O2 ou O1 seule deviennent plus défendables.
- Si le comité refuse tout changement de rôle réglementaire (section 4 : devenir fournisseur d'un système d'IA), O2 est préférable à O3.

### 3.6 Le meilleur contre-argument

O1 seule pourrait suffire. Si l'essentiel du temps perdu vient de l'indexation, une meilleure recherche règle le problème à moindre risque et l'assistant n'apporte rien de plus. Cette objection est traitée par la mesure préalable de la section 8 : savoir la part du temps de H04 passée à retrouver, par rapport à lire et résumer, est la première condition du pilote. Le dossier ne prétend donc pas que l'IA générative est nécessaire ; il prétend qu'on ne peut pas le savoir sans mesurer.
