## 7. Gouvernance, conduite du changement, indicateurs

### 7.1 Instances et responsabilités

Principes tirés de l'annexe A du NIST AI 600-1 (E04) : inventaire des systèmes, politique d'usage acceptable, surveillance, journalisation des incidents, retrait documenté.

| Instance ou rôle | Mission |
|---|---|
| Comité de pilotage (direction juridique, DSI, DPO, direction générale) | décide les passages de phase, reçoit les indicateurs chaque mois (H28) |
| Propriétaire métier (direction juridique et commande publique) | définit le périmètre, valide le corpus, arbitre les cas litigieux |
| DSI | hébergement, sécurité, quotas, journaux |
| DPO | registre des traitements, AIPD, droits des personnes, avis sur toute extension |
| Référents d'utilisateurs | remontée des erreurs, animation de la formation |

**Qui décide quoi (R = responsable, A = approuve, C = consulté, I = informé).**

| Décision | Propriétaire métier | DSI | DPO | Direction générale | Comité de pilotage |
|---|---|---|---|---|---|
| Périmètre et corpus | R | C | C | I | A |
| Choix du fournisseur et de l'hébergement | C | R | C | I | A |
| Note de classification AI Act | C | I | R | I | A |
| AIPD | C | C | R | I | A |
| Suspension du service | R ou DSI ou DPO | R | R | I | informé immédiatement |
| Réouverture après suspension | C | C | C | I | A |
| Extension du périmètre | R | C | C | C | A |

### 7.2 Règles de fonctionnement

- **Politique d'usage acceptable** signée à l'ouverture des accès : l'assistant aide à chercher et résumer ; l'agent reste responsable de l'acte ; aucun usage pour évaluer des personnes ; aucune donnée hors périmètre saisie dans l'interface.
- **Inventaire** : l'assistant est inscrit à l'inventaire des systèmes d'IA de la métropole, avec son périmètre et sa note de classification (section 4) (action NIST GV-1.6-001).
- **Réévaluation obligatoire** à chaque changement de périmètre, de modèle ou de fournisseur : nouvelle note de classification, mise à jour de l'analyse de risques et de l'AIPD.
- **Désactivation** : le propriétaire métier, la DSI ou le DPO peuvent suspendre l'accès sans attendre le comité ; la réouverture exige l'accord du comité (action NIST MG-2.4).
- **Journalisation** des questions et des réponses pendant une durée limitée fixée avec le DPO, pour l'audit et l'analyse d'incidents sans exposer les agents.

### 7.3 Conduite du changement

- Formation courte avant l'accès (limites de l'IA, vérification, cas d'erreur), qui répond aussi à l'obligation de maîtrise de l'IA (article 4, E09).
- Information et consultation des représentants du personnel : l'assistant ne sert pas à évaluer les agents ; ce point est écrit dans la politique d'usage. Le comité social territorial est compétent sur l'organisation et le fonctionnement des services (E14) : sa saisine est à confirmer avec les ressources humaines, ce texte n'ayant pas pu être lu.
- Communication honnête sur les erreurs possibles, pour éviter la surconfiance (R03) comme le rejet.
- Boucle de retour : un bouton « signaler une erreur » dans l'interface, traité chaque mois en comité.

### 7.4 Plan d'évaluation du pilote

Le jeu de 200 questions (H26) est construit avant l'ouverture, par les juristes, à partir de questions réelles anonymisées. Sa répartition (H30) : 80 questions factuelles simples, 60 questions multi-documents, 30 questions sur textes abrogés ou modifiés, 30 questions pièges sans réponse dans le corpus. Il est rejoué à chaque changement de modèle, de corpus ou de réglage. Chaque réponse est notée sur trois critères : l'information est exacte, la citation existe, la citation soutient bien l'information. Cette distinction reprend les deux types d'erreur de l'étude Stanford (E10). Le délai de réponse visé est de 10 secondes pour la majorité des requêtes (H33).

### 7.5 Indicateurs de suivi

Mesurés sur le pilote de 3 mois et 50 utilisateurs (H08), présentés tous les mois (H28).

| Indicateur | Seuil ou cible | Pourquoi |
|---|---|---|
| Réponses correctes et sourcées sur les 170 questions hors pièges (H34) du jeu de 200 questions (H26) | au moins 90 % (H14) | cible de qualité ; condition d'extension |
| Questions pièges refusées par l'assistant | 100 % (H29) | un refus vaut mieux qu'une invention |
| Réponses revues par un juriste (échantillon de 10 %, H32) | écart suivi chaque mois | détecte la dérive en exploitation |
| Gain de temps mesuré sur la recherche | au moins 10 % à la fin du mois 2 (H25) ; sinon arrêt | le gain doit apparaître vite |
| Taux d'adoption parmi les 50 pilotes | à comparer à la fourchette de H19 | second facteur le plus influent |
| Incidents de confidentialité | aucun toléré ; tout incident déclenche la procédure de désactivation | R04, R05 |
| Satisfaction et retours des agents | enquête mensuelle brève | usage réel, surconfiance |

Une fuite de données personnelles ou un accès à un document non autorisé suspend le pilote jusqu'à analyse, quel que soit le reste des indicateurs.
