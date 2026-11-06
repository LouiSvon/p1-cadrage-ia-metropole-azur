## Annexe F. Les 12 risques du NIST AI 600-1 et leur traitement

Source : NIST AI 600-1, juillet 2024 (E04), texte lu le 2026-10-29. Douze risques (H10). La colonne « retenu » indique s'il est traité comme risque propre dans la section 5.

| Risque NIST | Résumé | Retenu | Raison |
|---|---|---|---|
| CBRN Information or Capabilities | accès facilité à des informations sur armes chimiques, biologiques, radiologiques, nucléaires | non | sans lien avec un outil documentaire interne |
| Confabulation | contenu faux énoncé avec assurance, y compris fausses citations | oui (R01, R02) | cœur du risque d'un assistant juridique |
| Dangerous, Violent, or Hateful Content | contenus dangereux ou haineux | non | usage interne, périmètre documentaire |
| Data Privacy | fuite, mémorisation, inférence de données personnelles | oui (R04) | données personnelles dans les pièces |
| Environmental Impacts | consommation de calcul | non, suivi seulement | impact limité à un pilote ; suivi d'exploitation |
| Harmful Bias and Homogenization | biais, écarts selon langues ou groupes | non | aucune décision sur des personnes |
| Human-AI Configuration | surconfiance, mauvaise interaction | oui (R03) | agents pressés qui ne vérifient plus |
| Information Integrity | désinformation à grande échelle | non | pas de diffusion publique |
| Information Security | attaques facilitées, surface d'attaque élargie, injection de prompt | oui (R06 et voisins) | injection indirecte par des documents |
| Intellectual Property | reproduction de contenus protégés | oui (R13) | à contrôler par les clauses d'achat |
| Obscene, Degrading, and/or Abusive Content | contenus abusifs | non | sans lien avec le cas d'usage |
| Value Chain and Component Integration | composants tiers mal vérifiés | oui (R08) | modèle et bibliothèques ouverts |

**Actions NIST mobilisées** (identifiants lus dans les tableaux d'actions) : GV-1.6-001 (inventaire), GV-6.1-001 (tiers et droits de tiers), MS-2.5-001 (ne pas extrapoler à partir de tests anecdotiques), MG-2.3 (réponse aux incidents), MG-2.4 (désactivation). Les tableaux d'actions ont été lus par sondage, non intégralement.
