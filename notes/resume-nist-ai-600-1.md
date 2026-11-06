---
titre: Résumé du NIST AI 600-1 (profil IA générative)
date_maj: 2026-10-29
---

Source : NIST AI 600-1, juillet 2024, 64 pages, https://doi.org/10.6028/NIST.AI.600-1 (PDF lu le 2026-10-29). Les passages "Pour P1" sont mes déductions, pas le texte du NIST.

# Nature du document
Profil de l'AI RMF 1.0 (janvier 2023) pour l'IA générative. Usage volontaire, transversal à tous les secteurs. Ce n'est pas une loi : c'est un catalogue de risques et d'actions suggérées.

# Structure (64 pages)
| Partie | Pages | Contenu |
|---|---|---|
| 1. Introduction | 1 | cadre, groupe de travail public du NIST |
| 2. Risques | 2 à 11 | 12 risques propres à l'IA générative ou aggravés par elle |
| 3. Actions suggérées | 12 à 46 | tableaux d'actions par fonction : GOVERN, MAP, MEASURE, MANAGE |
| Annexe A | 47 à 53 | 4 thèmes : gouvernance, provenance des contenus, tests avant déploiement, signalement d'incidents |
| Annexe B | 54 à 64 | références |

# Idée centrale
Un risque = probabilité x ampleur des conséquences. Ils varient selon l'étape du cycle de vie, la portée (modèle, application, écosystème), la source (modèle, entrées, sorties, comportement humain) et la durée. Certains risques sont inconnus ou mal mesurables : la science de la mesure est jeune. Le document ne traite que les risques avec preuves empiriques.

# Les 12 risques en une ligne
1. CBRN : accès facilité à des informations sur armes chimiques, biologiques, radiologiques, nucléaires (les études citées montrent une aide minime par rapport à une recherche web).
2. Confabulation : contenu faux énoncé avec assurance ("hallucination"), y compris fausses citations et faux raisonnements qui renforcent la confiance.
3. Contenu dangereux, violent ou haineux.
4. Vie privée : fuite ou mémorisation de données personnelles, inférence d'informations sensibles.
5. Impact environnemental : consommation de calcul.
6. Biais et homogénéisation : amplification de biais, écarts de performance selon groupes ou langues, résultats uniformisés.
7. Configuration humain-IA : excès de confiance (biais d'automatisation), méfiance injustifiée, attachement émotionnel.
8. Intégrité de l'information : désinformation à grande échelle, confusion fait/opinion.
9. Sécurité de l'information : attaques facilitées, et surface d'attaque élargie (injection de prompt directe et indirecte, empoisonnement de données).
10. Propriété intellectuelle : reproduction non autorisée de contenus protégés, exposition de secrets d'affaires.
11. Contenu obscène ou abusif (dont images sexuelles non consenties, contenus pédocriminels synthétiques).
12. Chaîne de valeur : composants tiers (modèles, données, bibliothèques) mal vérifiés, responsabilité diluée.

# Actions suggérées (partie 3)
Chaque action a un identifiant (GV, MP, MS, MG + numéro de sous-catégorie), les risques visés et les acteurs concernés. Toutes ne s'appliquent pas à tous : un déployeur n'est pas un développeur de modèle.
- GOVERN : cadre légal documenté, rôles et responsabilités, inventaire des systèmes IA, politiques, gestion des tiers et plans de secours.
- MAP : usages prévus, limites connues du système, probabilité et ampleur des impacts.
- MEASURE : métriques, évaluateurs indépendants, tests de fiabilité, vie privée, retours des utilisateurs.
- MANAGE : réponse aux risques, désactivation du système si besoin, surveillance après déploiement, communication des incidents, amélioration continue.

# Annexe A, les 4 thèmes prioritaires
Gouvernance, tests avant déploiement, provenance des contenus, signalement d'incidents. Les actions du document portent surtout sur eux.

# Pour P1 (déduction, à confirmer)
Risques les plus pertinents pour un assistant documentaire de collectivité : 2 Confabulation, 4 Vie privée, 7 Configuration humain-IA, 9 Sécurité (injection indirecte via les documents), 12 Chaîne de valeur, 10 Propriété intellectuelle. Les risques 1, 3, 5, 6, 8, 11 sont à traiter brièvement ou à écarter avec justification. Côté actions : GOVERN 1.1 (cadre légal), GOVERN 1.6 (inventaire), GOVERN 6.1 (tiers), MAP 2.2 (limites du système), MEASURE 2.5 (fiabilité), MANAGE 4.1 (surveillance), MANAGE 2.4 (arrêt du système) alimentent la matrice de risques et la gouvernance.
