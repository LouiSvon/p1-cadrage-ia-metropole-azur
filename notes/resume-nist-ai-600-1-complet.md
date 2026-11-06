---
titre: Résumé complet du NIST AI 600-1 (profil IA générative)
date_maj: 2026-10-29
---

Source : NIST AI 600-1, juillet 2024, 64 pages, https://doi.org/10.6028/NIST.AI.600-1. Lu en texte intégral le 2026-10-29 pour les parties 1, 2 et l'annexe A ; la partie 3 (tableaux d'actions) a été lue par sondage (une dizaine de sous-catégories), pas intégralement. Les passages "Pour P1" sont mes déductions.

# 1. Nature et usage
- Profil de l'AI RMF 1.0 (janvier 2023) pour l'IA générative, rédigé en application d'un décret présidentiel américain (EO 14110), avec un groupe de travail public.
- Volontaire, transversal (tous secteurs). Un profil sert à décider comment gérer les risques selon ses exigences, sa tolérance au risque et ses moyens.
- Il ne couvre que des risques avec preuves empiriques ; les risques spéculatifs d'IA futures sont exclus. Les risques inconnus ou difficiles à estimer sont reconnus, la science de la mesure étant jeune.
- Les actions visent surtout 4 thèmes issus du groupe de travail : gouvernance, provenance des contenus, tests avant déploiement, signalement d'incidents.

# 2. Cadre de lecture du risque (partie 2)
Risque = probabilité x ampleur des conséquences. Quatre dimensions :
- étape du cycle de vie (conception, développement, déploiement, exploitation, retrait) ;
- portée (modèle ou système, application ou cas d'usage, écosystème) ;
- source (le modèle, les entrées, les sorties, le comportement humain : abus, mauvais usage, interactions humain-IA) ;
- durée (immédiat ou sur le long terme).
Classement possible des 12 risques (note de bas de page) : techniques ou modèle, mauvais usage humain, systémiques.

# 3. Les 12 risques en détail
1. **CBRN** : l'IA pourrait faciliter l'accès à l'information sur armes chimiques, biologiques, radiologiques, nucléaires. Les études citées montrent une aide minime par rapport à une recherche classique ; à surveiller avec les outils de conception biologique spécialisés.
2. **Confabulation** : contenu faux énoncé avec assurance, conséquence normale du fonctionnement statistique (prédire le mot suivant). Plus fréquent sur les réponses longues et les domaines d'expertise. Inclut de fausses citations et de faux raisonnements qui trompent sur la fiabilité. Les confabulations juridiques sont citées comme répandues.
3. **Contenu dangereux, violent ou haineux** : recommandations dangereuses, jailbreaking (contourner les garde-fous par des prompts détournés), contenus haineux ou stéréotypés.
4. **Vie privée** : fuite ou mémorisation de données d'entraînement, inférence d'informations sensibles en recoupant des sources, même fausses (une inférence erronée peut nuire).
5. **Impact environnemental** : entraînement et inférence consomment beaucoup ; la génération (résumé) consomme plus que la classification ; pas de méthode d'estimation reconnue.
6. **Biais et homogénéisation** : amplification de biais, performances inégales selon groupes ou langues (moins bon hors anglais), sorties uniformisées, "effondrement de modèle" si l'entraînement repose trop sur des données synthétiques ; les modèles de fondation sont des points de défaillance uniques.
7. **Configuration humain-IA** : surconfiance (biais d'automatisation) qui aggrave confabulation et biais ; à l'inverse aversion injustifiée ; attachement émotionnel.
8. **Intégrité de l'information** : désinformation et mésinformation à grande échelle, hypertrucages, impersonation.
9. **Sécurité de l'information** : deux volets. Attaques facilitées (piratage, hameçonnage, découverte de failles). Surface d'attaque élargie : injection de prompt directe, injection indirecte (instructions cachées dans des données récupérées par l'application), empoisonnement des données. Inclut la disponibilité et l'intégrité du code, des données et des poids.
10. **Propriété intellectuelle** : reproduction de contenus protégés, mémorisation, usage de l'identité ou de la voix sans accord ; le cadre juridique est en débat.
11. **Contenu obscène ou abusif** : images intimes non consenties, contenus pédocriminels synthétiques.
12. **Chaîne de valeur et composants** : modèles, données et bibliothèques tiers mal vérifiés ; difficulté à attribuer un défaut à un composant ; erreurs dans les jeux de test de référence.
Chaque risque est relié aux caractéristiques d'une IA digne de confiance de l'AI RMF (sûre, sécurisée, fiable, explicable, respectueuse de la vie privée, équitable, responsable).

# 4. Actions suggérées (partie 3, pages 12 à 46)
- Organisées par sous-catégorie de l'AI RMF : GOVERN (GV), MAP (MP), MEASURE (MS), MANAGE (MG). Seules certaines sous-catégories sont couvertes.
- Chaque ligne : identifiant (ex. GV-1.1-001), action suggérée, risques visés, tâches des acteurs. J'ai compté environ 196 identifiants par script ; chiffre à confirmer.
- Toutes ne s'appliquent pas à tous : un déployeur (cas de P1) n'a pas les mêmes actions qu'un développeur de modèle.
Exemples lus :
- GV-1.1-001 : aligner le développement et l'usage avec les lois (vie privée, droit d'auteur).
- GV-1.3 : adapter le niveau de gestion du risque selon des facteurs dont la sécurité, la fiabilité, l'usage malveillant, la configuration humain-IA.
- GV-1.6-001 : recenser les systèmes IA générative dans l'inventaire.
- GV-6.1-001 : catégoriser les contenus selon les droits de tiers (copyright, vie privée).
- MP-2.2-001 : documenter les sources de données amont dont dépend le système.
- MS-2.5-001 : ne pas extrapoler les performances à partir de tests anecdotiques.
- MG-2.3 : plans de réponse et de reprise sur incident, incluant la chaîne de valeur.
- MG-2.4 : procédures de désactivation, d'escalade et d'alternative quand le système doit être retiré.
- MG-4.1 : surveillance après déploiement et veille avec des experts externes.

# 5. Annexe A (pages 47 à 53)
- **Gouvernance** : adapter les outils existants (inventaire, analyses d'impact, contrôle des changements, surveillance, retrait, politique d'usage acceptable, formation, rétention des données). L'IA générative peut demander plus de revue humaine et de supervision. Les tiers (modèles, API, données) exigent diligence d'achat, SLA, nomenclatures logicielles (SBOM) et rapports d'attestation.
- **Tests avant déploiement** : les méthodes actuelles sont souvent inadaptées ; réussir un examen humain ou un jeu vidéo ne prouve pas la fiabilité ; l'écart entre benchmarks et usage réel est important (sensibilité au prompt).
- **Retours externes structurés** : consultations (groupes, enquêtes), tests de terrain, red-teaming (grand public, experts, combiné, humain+IA).
- **Provenance des contenus** : suivi de l'origine (métadonnées, filigranes, empreintes) pour authentifier et tracer.
- **Signalement d'incidents** : pas de canal formel ; bases publiques ad hoc ; recommandation de journaliser, documenter et partager, y compris pour les plugins et entrées tierces.
- Annexe B (pages 54 à 64) : références.

# 6. Limites du document (à écrire dans le dossier si on le cite)
- Origine américaine, non contraignant, daté de juillet 2024.
- Ne traite pas tous les sujets de l'AI RMF et reste générique : il ne dit ni quelle gravité attribuer ni quelles mesures retenir pour un cas précis.
- N'est pas l'AI Act ; la correspondance entre les deux reste à construire.

# 7. Pour P1 (déduction à valider)
- À retenir dans la matrice (section 5 du dossier) : confabulation (réponses fausses sur le droit des marchés), vie privée (noms dans les pièces), configuration humain-IA (surconfiance des agents), sécurité (injection indirecte via les documents), chaîne de valeur (fournisseur de modèle), propriété intellectuelle.
- À écarter en une ligne justifiée : CBRN, contenu dangereux, environnement (à mentionner si hébergement lourd), biais, intégrité de l'information, contenu obscène.
- Gouvernance (section 7) : s'appuyer sur l'annexe A (inventaire, politique d'usage acceptable, surveillance, désactivation, journalisation des incidents).
- Citation : à chaque fois, référencer l'identifiant (ex. "NIST AI 600-1, risque Confabulation ; action MG-2.4").
