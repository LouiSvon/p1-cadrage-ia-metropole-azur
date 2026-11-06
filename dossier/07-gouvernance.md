## 7. Gouvernance, conduite du changement, indicateurs

**Gouvernance.** Principes tirés de l'annexe A du NIST AI 600-1 (E04) : inventaire des systèmes, politique d'usage acceptable, surveillance, journalisation des incidents, retrait documenté.

| Instance ou rôle | Mission |
|---|---|
| Comité de pilotage (direction juridique, DSI, DPO, direction générale) | décide les passages de phase, reçoit les indicateurs chaque mois (H28) |
| Propriétaire métier (direction juridique et commande publique) | définit le périmètre, valide le corpus, arbitre les cas litigieux |
| DSI | hébergement, sécurité, quotas, journaux |
| DPO | registre des traitements, AIPD, droits des personnes, avis sur toute extension |
| Référents d'utilisateurs | remontée des erreurs, animation de la formation |

**Règles de fonctionnement.**
- **Politique d'usage acceptable** signée à l'ouverture des accès : l'assistant aide à chercher et résumer ; l'agent reste responsable de l'acte ; aucun usage pour évaluer des personnes ; aucune donnée hors périmètre saisie dans l'interface.
- **Inventaire** : l'assistant est inscrit à l'inventaire des systèmes d'IA de la métropole, avec son périmètre et sa note de classification (section 4) (action NIST GV-1.6-001).
- **Réévaluation obligatoire** à chaque changement de périmètre, de modèle ou de fournisseur : nouvelle note de classification, mise à jour de l'analyse de risques et de l'AIPD.
- **Désactivation** : le propriétaire métier, la DSI ou le DPO peuvent suspendre l'accès sans attendre le comité ; la réouverture exige l'accord du comité (action NIST MG-2.4).
- **Journalisation** des questions et des réponses pendant une durée limitée fixée avec le DPO, pour l'audit et l'analyse d'incidents sans exposer les agents.

**Conduite du changement.**
- Formation courte avant l'accès (limites de l'IA, vérification, cas d'erreur), qui répond aussi à l'obligation de maîtrise de l'IA (article 4).
- Information des représentants du personnel : l'assistant ne sert pas à évaluer les agents ; ce point est écrit dans la politique d'usage. La consultation formelle éventuelle est à confirmer avec les ressources humaines.
- Communication honnête sur les erreurs possibles, pour éviter la surconfiance (R03) comme le rejet.

**Indicateurs de suivi.** Mesurés sur le pilote de 3 mois et 50 utilisateurs (H08), présentés tous les mois (H28).

| Indicateur | Seuil ou cible | Pourquoi |
|---|---|---|
| Réponses correctes et sourcées sur le jeu de 200 questions (H26) | au moins 90 % (H14) | cible de qualité ; condition d'extension |
| Questions pièges refusées par l'assistant | 100 % (H29) | un refus vaut mieux qu'une invention |
| Gain de temps mesuré sur la recherche | au moins 10 % à la fin du mois 2 (H25) ; sinon arrêt | le gain doit apparaître vite |
| Taux d'adoption parmi les 50 pilotes | à comparer à la fourchette de H19 | second facteur le plus influent |
| Incidents de confidentialité | aucun toléré ; tout incident déclenche la procédure de désactivation | R04, R05 |
| Satisfaction et retours des agents | enquête mensuelle brève | usage réel, surconfiance |

Une fuite de données personnelles ou un accès à un document non autorisé suspend le pilote jusqu'à analyse, quel que soit le reste des indicateurs.
