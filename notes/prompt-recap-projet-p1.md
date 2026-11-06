---
titre: Prompt de reprise du projet P1 (récapitulatif complet)
date_maj: 2026-11-06
---

Tu reprends le projet P1 de Louis. Lis ce document en entier avant d'agir. Il décrit le but, l'état exact, les décisions, ce qui est vérifié ou supposé, et ce qui reste à faire. Réponds en français, phrases courtes, sans emoji ni tiret cadratin.

# 1. Qui, pourquoi

Louis Savon est étudiant en informatique. Il vise un stage en conseil IA à partir d'avril 2027 (alternance en 2028), cabinet prioritaire : Wavestone Marseille, stratégie valable pour d'autres cabinets. P1 est la pièce maîtresse de son profil : prouver une posture de conseil (décider avec des hypothèses assumées), pas une compétence de code. Supports concernés : GitHub, portfolio, CV, LinkedIn.

# 2. Le projet

Dossier de cadrage d'un cas d'usage IA pour un client fictif, "Métropole Azur" (métropole de plusieurs centaines de milliers d'habitants). Cas d'usage : assistant IA interne qui aide les agents à retrouver et résumer délibérations, règlements et pièces de marchés publics. Le caractère fictif est écrit en première page de tout livrable.

Emplacement : `/Users/louis/Desktop/Dev local/espace-de-travail-optimisation/p1-cadrage-ia/` (dépôt git local, branche `feature/p1-dossier-cadrage`, commits `71771f0` et `98ecca4`, aucun remote, rien de publié).

# 3. Les 10 critères de réussite (cahier.md, source de vérité)

1. Dossier PDF de 15 pages au plus, plus synthèse de 2 pages et script de pitch de 5 minutes.
2. Caractère fictif écrit en première page.
3. Registre des hypothèses d'au moins 15 lignes (valeur, source ou "hypothèse", date, confiance).
4. Aucun chiffre du dossier absent du registre.
5. Matrice d'au moins 10 risques reliés à OWASP LLM Top 10 2025, NIST AI 600-1 ou AI Act, avec gravité, probabilité, mesure, responsable.
6. Classification AI Act argumentée, avec date de la source juridique et incertitudes.
7. Business case en fourchettes (bas, central, haut) et sensibilité sur les 2 hypothèses les plus influentes.
8. Au moins une option "ne pas faire" ou "faire autrement" comparée.
9. Relecture par une personne extérieure, retours notés.
10. Dépôt public avec README, PDF, registre, licence, sans donnée personnelle.

État : critères 1 à 8 tenus (v1). Critère 9 non tenu : la relecture externe dépend de Louis (demande déjà en retard sur son plan). Critère 10 non tenu : publication interdite sans demande explicite de Louis.

# 4. Contenu du dossier v1 (9 pages)

Fichiers `dossier/00-page-de-garde.md` à `08-plan-et-decision.md`, plus `synthese.md` (2 pages) et `pitch-5-minutes.md` (environ 685 mots). PDF dans `livrables/` : `dossier-cadrage-metropole-azur.pdf` et `synthese-2-pages.pdf`.

- Contexte : 500 000 habitants, 4 000 agents, 600 utilisateurs potentiels, 3 h par semaine de recherche documentaire (hypothèse), 200 000 documents.
- Options : O0 ne rien faire, O1 améliorer la recherche existante (sans IA générative), O2 assistant sur service externe, O3 assistant hébergé en environnement maîtrisé. Recommandation : O1 en socle puis pilote d'O3 ; O2 écartée pour le pilote à cause des données personnelles (environ 30 % des documents, hypothèse). Meilleur contre-argument : O1 seule peut suffire.
- AI Act : l'assistant n'est pas à haut risque tant que son périmètre exclut l'évaluation de personnes et tout usage par une instance juridictionnelle (annexe III point 8(a) le plus proche). Obligations restantes : article 4 (maîtrise de l'IA, reformulée en mesures de soutien) et article 50(1) (information des utilisateurs). Avec O3, la métropole peut devenir fournisseur (articles 3 et 25). RGPD : AIPD recommandée avant le pilote.
- 14 risques (R01 à R14) : réponse fausse sur le droit, texte abrogé cité, surconfiance, fuite de données personnelles, accès non autorisé, injection indirecte, etc.
- Business case sur 3 ans, calculé par `calcul/business_case.py` : pessimiste -1 176 k€, central +367 k€, optimiste +2 391 k€. Seuil de rentabilité à 21,2 % de temps économisé (central supposé : 30 %). Facteurs les plus influents ex aequo : part de temps économisée et adoption (écart de 832 k€ chacun). Croisement gains centraux et coûts pessimistes : -373 k€.
- Gouvernance et indicateurs : jeu de 200 questions dont pièges, seuil de 90 % de réponses correctes et sourcées, 100 % des pièges refusés, gain mesuré d'au moins 10 % à la fin du mois 2, désactivation possible par le propriétaire métier, la DSI ou le DPO.
- Décision demandée au comité : phase 0 de mesure (4 semaines, 30 agents), pilote plafonné (3 mois, 50 utilisateurs), aucun déploiement général avant la décision d'extension. Conditions d'arrêt écrites.

# 5. Ce qui est vérifié et ce qui ne l'est pas

Vérifié sur source primaire (dates de lecture dans `sources.md`) :
- OWASP LLM Top 10 2025 (LLM01 à LLM10, plus LLM01 et LLM08 détaillés).
- NIST AI 600-1 (juillet 2024, 12 risques ; annexe A lue, tableaux d'actions lus par sondage).
- Règlement (UE) 2026/1744 sur EUR-Lex (lu dans le navigateur intégré, WebFetch ne l'affichait pas) : publié au JO le 24 juillet 2026, en vigueur le 27 juillet 2026, annexe III au 2 décembre 2027, annexe I au 2 août 2028, article 50(2) au 2 décembre 2026 pour les systèmes déjà sur le marché avant le 2 août 2026. Page de la Commission concordante.
- Règlement (UE) 2024/1689, texte initial (annexe III, articles 3, 4, 6, 25, 26, 27, 50(1)).
- Test britannique de Copilot (26 minutes par jour, auto-déclarées), salaire brut mensuel moyen en fonction publique territoriale (2 640 euros, année 2022), page CNIL sur l'AIPD (8 avril 2024), CRPA article L312-1-1, étude Stanford sur les outils juridiques (plus de 17 % et plus de 34 % d'erreurs), page ANSSI de présentation du guide IA générative.

Non vérifié ou supposé :
- Version consolidée de l'AI Act après 2026/1744 non lue ; article 113 modifié lu en partie ; article 4 modifié non lu ; la date générale d'application du 2 août 2026 est déduite.
- Toutes les valeurs du client et les coûts (socle, construction, exploitation, pilote) sont des hypothèses sans devis. Coefficient de charges employeur 1,4 et 1 607 h annuelles : hypothèses.
- Article L253-5 du CGFP (consultation du comité social territorial) : non lu, la page Légifrance est protégée par une vérification anti-robot que je n'ai pas contournée.
- Décision Moffatt c. Air Canada et PDF de l'ANSSI : non lus, commentaires seulement.
- Gravités, probabilités : jugement de l'auteur, aucune relecture tierce.
- Le détecteur de chiffres prouve qu'un nombre est quelque part au registre, pas qu'il est sur la bonne ligne.

# 6. Outils et fichiers

- `registre.md` : 33 hypothèses H, 16 sources externes E, valeurs calculées D (bloc entre marqueurs `<!-- D:debut -->` et `<!-- D:fin -->`, réécrit par `outils/maj_registre.py`).
- `sources.md` : sources lues, dates, état.
- `calcul/business_case.py` : calcul des scénarios, sensibilité, grille, seuil, croisement.
- `outils/tout_construire.sh <python>` : recalcule, réécrit les lignes D, régénère les PDF (Markdown vers HTML, puis Chrome sans interface), lance l'autotest et le contrôle des chiffres, affiche pages et mots du pitch. Dépendance : `markdown` (voir `requirements.txt`), Google Chrome, `pdfinfo`.
- `verification/verifier_chiffres.py` : critère 4, avec autotest positif et négatif ; couvre `dossier/*.md`.
- `notes/` (résumés NIST, fiche client, périmètre), `archives/` (versions datées).
- Licences : MIT pour le code (`LICENSE`), CC BY 4.0 pour les documents (`LICENSE-DOCS.md`, texte juridique complet non recopié, lien officiel seulement). Choix validé par Louis.

# 7. Dernière demande en cours : étoffer le dossier

Louis a jugé le dossier "pas assez bon" et veut plus de pages, de détails et de recherche. Décision prise : le dossier monte jusqu'au plafond de 15 pages (critère 1), le surplus va dans un document d'annexes séparé sans plafond.

Déjà fait pour cette demande (non commité) :
- Recherche : Stanford, ANSSI, Moffatt, CRPA L312-1-1, comité social territorial, OWASP LLM01 et LLM08.
- `registre.md` : ajout de H30 à H33 (répartition du jeu de 200 questions : 80, 60, 30, 30 ; journal de recherche de 2 semaines ; revue de 10 % des réponses ; délai de 10 secondes) et de E10 à E16. Copie datée dans `archives/registre-2026-11-06-v3.md`.
- `sources.md` mis à jour, copie dans `archives/sources-2026-11-06-v2.md`.

Reste à faire :
1. Étoffer les sections 1 à 8 jusqu'à 15 pages : cas réels en section 1 (Stanford, Air Canada, test britannique), cas d'usage et inventaire documentaire en section 2 (sensibilité des pièces, open data), architecture d'O3 en section 3, tableau article par article en section 4, scénario d'attaque, détection et test de recette pour les 4 risques principaux en section 5, détail des hypothèses et coûts non chiffrés en section 6, tableau des rôles, plan d'évaluation et consultation du comité social territorial en section 7 (sourcer ou marquer "non vérifié"), calendrier en section 8.
2. Créer `annexes/*.md` et un PDF d'annexes sans plafond : registre complet, sources, résumé NIST, croisement OWASP, NIST et AI Act, protocole de mesure préalable, 20 questions types du jeu de test, plan d'AIPD, modèle de note de classification datée, clauses pour la consultation du marché, glossaire. Étendre `verifier_chiffres.py` à `annexes/`.
3. Relancer `outils/tout_construire.sh`, viser 15 pages au plus, contrôler les chiffres, vérifier `pdfinfo` (pages et Title).
4. Faire relire par le sous-agent `relecteur` en contexte neuf (relecture interne, jamais présentée comme extérieure), corriger, commiter sur la branche `feature/p1-dossier-cadrage` avec un message `type(scope): description` en minuscules de 50 caractères au plus.

# 8. Règles à respecter

- Tout en français, sans emoji ni tiret cadratin. Chaque fichier : frontmatter avec titre et date de dernière mise à jour. Noms de fichiers en minuscules sans accents, séparés par des tirets.
- Aucune donnée inventée : preuve manquante, écrire "à fournir" ou "non vérifié". Toute affirmation sur règle légale, version, date : source et date de lecture, sinon "non vérifié".
- Une hypothèse sans source reste étiquetée "hypothèse". Pas de conseil financier personnalisé, pas de donnée réelle de personne.
- Pas de `git push`, pas de création de dépôt distant, pas de changement de visibilité, pas de publication sans demande explicite de Louis. Jamais de commit sur main, master ou dev. Ne pas contourner les hooks.
- Ne pas modifier `04-plan/plan-optimisation.md` ni `03-decisions/journal-decisions.md` sans validation : proposer les lignes.
- LinkedIn : aucune navigation, aucun scraping. Ne jamais contourner une vérification anti-robot ou un CAPTCHA.
- Aucun secret, aucun identifiant dans les fichiers. Ne rien supprimer définitivement : déplacer vers `~/.Trash`. Copie datée avant de remplacer un fichier non versionné.
- Ne jamais annoncer 10 critères sur 10 : les critères 9 et 10 dépendent de Louis. Toujours rapporter vérifié et supposé séparément, avec la preuve (commande et sortie).
- Outils de cette machine : bash 3.2 sur macOS, `/bin/ls` et `/bin/cat` dans les scripts, `curl` est refusé par les permissions (utiliser le navigateur intégré ou WebFetch), le navigateur intégré lit EUR-Lex et Légifrance quand WebFetch échoue.

# 9. Décisions encore ouvertes pour Louis

- Mention de l'assistance IA sur la page de garde (aujourd'hui : "Auteur : Louis Savon", commits avec ligne de co-auteur Claude).
- Personne de relecture externe et date de la demande.
- Publication du dépôt, après la relecture externe.
