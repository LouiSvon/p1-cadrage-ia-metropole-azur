---
titre: Registre des hypothèses de P1
date_maj: 2026-11-06
---

Règle : une valeur sans source reste "hypothèse". Aucun chiffre du dossier ne doit être absent de ce registre. Confiance : H haute, M moyenne, B basse. Les valeurs chiffrées du client sont des hypothèses de départ, pas des faits. Les valeurs D sont calculées par `calcul/business_case.py` (aucune saisie manuelle : `outils/maj_registre.py` réécrit le bloc entre les marqueurs). Version précédente : `archives/registre-2026-11-06-v2.md`.

| ID | Élément | Valeur | Source | Date | Confiance |
|---|---|---|---|---|---|
| H01 | Population de Métropole Azur | 500 000 habitants | hypothèse | 2026-11-06 | B |
| H02 | Effectif de la métropole | 4 000 agents | hypothèse | 2026-11-06 | B |
| H03 | Utilisateurs potentiels de l'assistant | 600 agents (juridique, achats, services administratifs) | hypothèse | 2026-11-06 | B |
| H04 | Temps de recherche documentaire par utilisateur et par semaine | 3 h | hypothèse, à mesurer avant tout investissement | 2026-11-06 | B |
| H05 | Part du temps de recherche économisable avec l'assistant (pessimiste / central / optimiste) | 20 % / 30 % / 40 % | hypothèse ; repère : 26 minutes par jour économisées, auto-déclarées, dans un test britannique (E01). Le central équivaut à 0,9 h par semaine, soit environ 11 minutes par jour, donc sous ce repère | 2026-11-06 | B |
| H06 | Coût horaire chargé d'un agent (pessimiste / central / optimiste) | 28 € / 35 € / 45 € | hypothèse ancrée sur E02 : 2 640 € bruts par mois en moyenne en fonction publique territoriale, x 1,4 de charges employeur (hypothèse), sur 1 607 h par an (hypothèse) = environ 27,6 € ; central et optimiste plus élevés car les utilisateurs visés sont plus qualifiés que la moyenne | 2026-11-06 | B |
| H07 | Volume du corpus | 200 000 documents | hypothèse | 2026-11-06 | B |
| H08 | Durée et taille du pilote | 3 mois, 50 utilisateurs | hypothèse de cadrage | 2026-11-06 | M |
| H09 | Catégories OWASP LLM Top 10 2025 | 10 (LLM01 à LLM10) | genai.owasp.org/llm-top-10/ (E03) | 2026-11-06 | H |
| H10 | Risques du NIST AI 600-1 | 12 catégories, publication juillet 2024 | NIST AI 600-1, PDF (E04) | 2026-11-06 | H |
| H11 | Dates AI Act (règlement 2026/1744) | publié au JO le 24 juillet 2026, en vigueur le 27 juillet 2026 ; systèmes à haut risque de l'annexe III : 2 décembre 2027 ; annexe I : 2 août 2028 ; marquage Article 50(2) pour les systèmes déjà sur le marché avant le 2 août 2026 : 2 décembre 2026 | EUR-Lex, texte du règlement (E05) et page de la Commission (E06) | 2026-11-06 | H |
| H12 | Classification AI Act de l'assistant | hors haut risque sous réserve du périmètre ; obligations restantes : maîtrise de l'IA (article 4, reformulée en mesures de soutien, E09) et information des utilisateurs (article 50(1)) | analyse de l'auteur, section 4 | 2026-11-06 | M |
| H13 | Part des documents contenant des données personnelles | 30 % | hypothèse | 2026-11-06 | B |
| H14 | Taux de réponses correctes et sourcées, cible du pilote | 90 % | hypothèse de cadrage | 2026-11-06 | B |
| H15 | Durée d'un déploiement complet après le pilote | 12 mois | hypothèse | 2026-11-06 | B |
| H16 | Critères de choix des options | 6 critères : valeur, risque, coût, souveraineté, délai, maturité | choix de l'auteur | 2026-11-06 | M |
| H17 | Semaines travaillées par agent et par an | 44 semaines | hypothèse | 2026-11-06 | B |
| H18 | Gravité et probabilité des risques | échelle qualitative faible, moyenne, élevée, notée par l'auteur | jugement de l'auteur, à relire par un tiers | 2026-11-06 | B |
| H19 | Taux d'adoption (part des utilisateurs potentiels qui l'utilisent réellement ; pessimiste / central / optimiste) | 40 % / 60 % / 80 % | hypothèse | 2026-11-06 | B |
| H20 | Coût unique du socle (indexation et nettoyage du corpus ; élevé / central / bas) | 150 k€ / 80 k€ / 40 k€ | hypothèse, à confirmer par consultation du marché | 2026-11-06 | B |
| H21 | Coût unique de construction de l'assistant hébergé en environnement maîtrisé (élevé / central / bas) | 450 k€ / 250 k€ / 120 k€ | hypothèse, à confirmer par consultation du marché | 2026-11-06 | B |
| H22 | Coût annuel d'exploitation de cet assistant (élevé / central / bas) | 280 k€ / 150 k€ / 80 k€ par an | hypothèse, à confirmer par consultation du marché | 2026-11-06 | B |
| H23 | Coût du pilote de 3 mois (élevé / central / bas) | 180 k€ / 100 k€ / 60 k€ | hypothèse, à confirmer par consultation du marché | 2026-11-06 | B |
| H24 | Horizon d'analyse et montée en charge | 3 ans ; gains de l'année 1 à 50 % | hypothèse | 2026-11-06 | B |
| H25 | Seuil d'arrêt du pilote sur le gain mesuré | moins de 10 % du temps de recherche économisé à la fin du mois 2 | hypothèse de cadrage | 2026-11-06 | B |
| H26 | Taille du jeu de questions d'évaluation | 200 questions, dont une part de questions pièges | hypothèse de cadrage | 2026-11-06 | B |
| H27 | Durée de la mesure préalable du temps de recherche | 4 semaines, auprès de 30 agents | hypothèse de cadrage | 2026-11-06 | B |
| H28 | Fréquence du comité de suivi du pilote | tous les mois | hypothèse de cadrage | 2026-11-06 | B |
| H29 | Part des questions sans réponse dans le corpus devant être refusées par l'assistant | 100 % des questions pièges du jeu de test (H26) | hypothèse de cadrage | 2026-11-06 | B |
| H30 | Répartition du jeu de 200 questions (H26) | 80 questions factuelles simples, 60 questions multi-documents, 30 questions sur textes abrogés ou modifiés, 30 questions pièges sans réponse dans le corpus | hypothèse de cadrage | 2026-11-06 | B |
| H31 | Durée du journal de recherche pendant la phase 0 | 2 semaines sur les 4 de la phase 0, auprès des 30 agents de H27 | hypothèse de cadrage | 2026-11-06 | B |
| H32 | Part des réponses du pilote revues chaque mois par un juriste | 10 % des réponses, tirées au hasard | hypothèse de cadrage | 2026-11-06 | B |
| H33 | Délai de réponse acceptable pour la majorité des requêtes | 10 secondes | hypothèse de cadrage | 2026-11-06 | B |

Sources externes vérifiées (E) :

| ID | Contenu | Source et date de lecture | Confiance |
|---|---|---|---|
| E01 | Test britannique de Microsoft 365 Copilot dans l'administration : 26 minutes économisées par jour en moyenne, plus de 20 000 agents, 3 mois, temps auto-déclaré (extrapolation à près de 2 semaines par an) | gov.uk, communiqué du 2 juin 2025, lu le 2026-11-06 | M |
| E02 | Salaire brut mensuel moyen en équivalent temps plein, fonction publique territoriale : 2 640 € (année 2022) | DGAFP, Faits et chiffres, édition 2024, fiche rémunérations (PDF lu le 2026-11-06) | H |
| E03 | OWASP LLM Top 10 2025 : LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Supply Chain, LLM04 Data and Model Poisoning, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage, LLM08 Vector and Embedding Weaknesses, LLM09 Misinformation, LLM10 Unbounded Consumption | genai.owasp.org/llm-top-10/, lu le 2026-10-29 | H |
| E04 | NIST AI 600-1, 12 risques dont Confabulation, Data Privacy, Human-AI Configuration, Information Security, Intellectual Property, Value Chain and Component Integration ; publié en juillet 2024 | PDF du NIST, lu le 2026-10-29 | H |
| E05 | Règlement (UE) 2026/1744 du 8 juillet 2026 (Digital Omnibus on AI), JO L 2026/1744 du 24 juillet 2026 | EUR-Lex, texte lu le 2026-11-06 | H |
| E06 | La Commission indique une entrée en vigueur le 27 juillet 2026, annexe III au 2 décembre 2027, annexe I au 2 août 2028 | digital-strategy.ec.europa.eu, lu le 2026-11-06 | H |
| E07 | Règlement (UE) 2024/1689 : annexe III point 8(a) (autorité judiciaire), article 3 (fournisseur, déployeur), article 4, article 6(3) et 6(4), article 25, article 26, article 27, article 50(1) | EUR-Lex, texte initial de 2024 lu le 2026-11-06 ; texte non consolidé avec le règlement 2026/1744 | M |
| E08 | CNIL : une analyse d'impact (AIPD) est obligatoire en cas de risque élevé (article 35 du RGPD) ou de profilage ; page mise à jour le 8 avril 2024 | cnil.fr, lu le 2026-11-06 | M |
| E09 | Considérant 8 du règlement 2026/1744 : l'article 4 est modifié pour que fournisseurs et déployeurs prennent des mesures de soutien à la maîtrise de l'IA de leur personnel, la Commission et les États membres soutenant ces efforts | EUR-Lex, lu le 2026-11-06 ; texte modifié de l'article 4 non lu | M |
| E10 | Étude Stanford sur des outils d'IA de recherche juridique : réponses erronées plus de 17 % du temps pour Lexis+ AI et Ask Practical Law AI, plus de 34 % pour Westlaw AI-Assisted Research, sur plus de 200 questions ouvertes ; deux types d'erreur : erronée, ou correcte mais appuyée sur une source qui ne la soutient pas | hai.stanford.edu, page lue le 2026-11-06 ; publication dans une revue à comité de lecture en 2025 selon une source secondaire | M |
| E11 | Guide de l'ANSSI, recommandations de sécurité pour un système d'IA générative, publié le 29 avril 2024 ; il porte sur la sécurité de l'architecture et exclut la qualité des données, l'éthique et la protection des données personnelles ; 35 recommandations selon une source secondaire | messervices.cyber.gouv.fr, page de présentation lue le 2026-11-06 ; PDF non lu | M |
| E12 | Moffatt c. Air Canada, 2024 BCCRT 149 : un tribunal de Colombie-Britannique juge la compagnie responsable de l'information inexacte donnée par son agent conversationnel (déclaration inexacte par négligence) ; décision d'un tribunal de petites créances | commentaires de cabinets d'avocats lus le 2026-11-06 ; décision non lue | M |
| E13 | Code des relations entre le public et l'administration, article L312-1-1 : les administrations publient en ligne les documents qu'elles communiquent en application du titre, les bases de données et données d'intérêt, sauf collectivités de moins de 3 500 habitants et personnes morales sous un seuil d'agents ; ce seuil est de 50 agents en équivalent temps plein (article D312-1-1-1) | Légifrance, article L312-1-1 lu le 2026-11-06 ; seuil de l'article D312-1-1-1 lu dans un extrait de recherche, article non ouvert | M |
| E14 | Code général de la fonction publique, article L253-5 : le comité social territorial est compétent sur l'organisation et le fonctionnement des services et l'évolution des administrations | résumé de recherche du 2026-11-06 ; page Légifrance bloquée par une vérification anti-robot, non lue | B |
| E15 | OWASP LLM01 Prompt Injection : injection directe ou indirecte (contenu externe qui contient des instructions) ; 7 mesures citées : contraindre le comportement, valider les formats de sortie, filtrer entrées et sorties, moindre privilège, approbation humaine des actions à risque, isoler et étiqueter le contenu non fiable, tests adverses ; aucune méthode n'est infaillible | genai.owasp.org, page lue le 2026-11-06 | H |
| E16 | OWASP LLM08 Vector and Embedding Weaknesses : fuites entre contextes, accès non autorisé, inversion d'embeddings, empoisonnement ; 4 familles de mesures : contrôle d'accès fin par permission, validation et authentification des sources, revue des données fusionnées et classification, journalisation infalsifiable | genai.owasp.org, page lue le 2026-11-06 | H |

Valeurs calculées (D) :

| ID | Élément | Valeur | Source | Date | Confiance |
|---|---|---|---|---|---|
<!-- D:debut -->
| D01 | Scénario pessimiste : gains sur 3 ans / coûts sur 3 ans / net | 444 k€ (443 520 €) / 1 620 k€ (1 620 000 €) / -1 176 k€ (-1 176 480 €) ; gain annuel en régime 177 k€ | calcul/business_case.py, entrées H03 à H06, H17 à H24 | 2026-11-06 | B |
| D02 | Scénario central : gains sur 3 ans / coûts sur 3 ans / net | 1 247 k€ (1 247 400 €) / 880 k€ (880 000 €) / 367 k€ (367 400 €) ; gain annuel en régime 499 k€ | calcul/business_case.py, entrées H03 à H06, H17 à H24 | 2026-11-06 | B |
| D03 | Scénario optimiste : gains sur 3 ans / coûts sur 3 ans / net | 2 851 k€ (2 851 200 €) / 460 k€ (460 000 €) / 2 391 k€ (2 391 200 €) ; gain annuel en régime 1 140 k€ | calcul/business_case.py, entrées H03 à H06, H17 à H24 | 2026-11-06 | B |
| D04 | Seuil de rentabilité : part du temps économisée qui annule le net (autres paramètres au central) | 21.2 % (21,2 % à l'écrit) | calcul/business_case.py | 2026-11-06 | B |
| D05 | Net sur 3 ans selon part économisée / adoption (autres au central), en k€ | 20%/40% : -326; 20%/60% : -48; 20%/80% : 229; 30%/40% : -48; 30%/60% : 367; 30%/80% : 783; 40%/40% : 229; 40%/60% : 783; 40%/80% : 1 338 | calcul/business_case.py | 2026-11-06 | B |
| D06 | Écart de net (pessimiste à optimiste) par facteur, en k€ | part_eco : 832; adoption : 832; cout_h : 606; run_an : 600; build : 330; pilote : 120; socle : 110 | calcul/business_case.py | 2026-11-06 | B |
| D07 | Valeurs arrondies à l'euro utilisées à l'oral dans le pitch (net sur 3 ans pessimiste / central / optimiste) | -1 176 000 € / 367 000 € / 2 391 000 € | arrondis de D01 à D03 | 2026-11-06 | B |
| D08 | Croisement : gains du scénario central avec les coûts pessimistes, net sur 3 ans | -373 k€ (-372 600 €) | calcul/business_case.py, clé croise_gains_centraux_couts_pessimistes | 2026-11-06 | B |
| D09 | Net sur 3 ans quand un paramètre varie seul de pessimiste à optimiste (autres au central), en k€ | part_eco : -48 à 783; adoption : -48 à 783; cout_h : 118 à 724; run_an : -23 à 577; build : 167 à 497; pilote : 287 à 407; socle : 297 à 407 | calcul/business_case.py ; valeurs affichées dans la figure de sensibilité | 2026-11-06 | B |
| D10 | Net du scénario central, repère de la figure de sensibilité, en k€ | 367 | calcul/business_case.py | 2026-11-06 | B |
<!-- D:fin -->
