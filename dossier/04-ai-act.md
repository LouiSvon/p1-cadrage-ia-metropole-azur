## 4. Classification AI Act et exigences associées

Sources : texte du règlement (UE) 2024/1689 sur EUR-Lex (E07) et règlement (UE) 2026/1744 qui le modifie (E05), lus le 2026-11-06. Le texte de 2024 lu n'est pas consolidé avec les modifications de 2026 : tout point d'article cité ici est à reconfirmer sur la version consolidée avant usage réel.

### 4.1 Calendrier (vérifié sur EUR-Lex)

Le règlement 2026/1744 a été publié au Journal officiel le 24 juillet 2026 et la Commission indique une entrée en vigueur le 27 juillet 2026 (E06). Les obligations des systèmes à haut risque de l'annexe III s'appliquent à partir du 2 décembre 2027, celles de l'annexe I à partir du 2 août 2028. La date générale d'application du règlement serait le 2 août 2026 (déduction du considérant 40 et de l'article 50(2) du règlement 2026/1744 ; l'article 113 modifié n'a pas été lu en entier). Seul le marquage des contenus synthétiques (article 50, paragraphe 2) bénéficie d'un délai jusqu'au 2 décembre 2026 pour les systèmes déjà sur le marché avant le 2 août 2026 (H11). Une source secondaire évoquait une conditionnalité du report à la disponibilité de normes : le texte lu n'en fait pas état dans les passages relevés, mais il n'a pas été lu en entier, donc ce point reste ouvert.

### 4.2 Rôle de la métropole

Un déployeur est un organisme qui utilise un système d'IA sous son autorité (article 3). Un fournisseur est celui qui développe un système, ou le fait développer, et le met en service sous son propre nom (article 3). L'article 25 ajoute qu'un déployeur devient fournisseur d'un système à haut risque s'il y met son nom, le modifie substantiellement ou en change la finalité.

| Option | Rôle probable | Conséquence |
|---|---|---|
| O2 : service externe | déployeur | obligations de déployeur ; le fournisseur porte la documentation du système |
| O3 : assistant hébergé | fournisseur possible, si la métropole fait développer l'assistant et le met en service sous son nom | obligations de fournisseur à examiner avec la direction juridique : information des utilisateurs (article 50, paragraphe 1), note de classification recommandée |

Ce changement de rôle est un coût de conformité caché d'O3 : il faut le décider avant le pilote. Le modèle de langage ouvert utilisé en O3 a son propre fournisseur ; les obligations propres aux modèles d'IA à usage général pèsent a priori sur lui, non sur la métropole ; ce point est à vérifier (articles non lus), notamment si la métropole modifie ou réentraîne le modèle.

### 4.3 Classification : l'assistant n'est pas un système à haut risque, sous réserve du périmètre

Un système est à haut risque s'il relève de l'annexe I (produits réglementés) ou d'un cas d'usage listé à l'annexe III ; seule l'annexe III est pertinente ici. On passe en revue ses huit domaines.

| Domaine de l'annexe III | Applicable ? | Raison |
|---|---|---|
| Biométrie, infrastructures critiques, éducation, maintien de l'ordre, migration | non | hors du cas d'usage |
| Emploi et gestion des travailleurs (point 4) | non, tant que l'assistant n'évalue ni agents ni candidats | périmètre exclut toute évaluation de personnes |
| Accès aux services publics essentiels (point 5) | non, tant qu'il n'évalue pas l'éligibilité à des prestations | aucune décision sur des usagers |
| Justice et processus démocratiques (point 8) | non, avec réserve | voir ci-dessous |

**Le point le plus proche : le point 8(a).** Il vise les systèmes destinés à être utilisés par une autorité judiciaire, ou pour son compte, afin de l'aider à rechercher et interpréter les faits et le droit et à appliquer le droit à des faits concrets, ou utilisés de façon similaire dans le règlement alternatif des litiges. Un assistant qui retrouve et résume des textes juridiques lui ressemble par sa fonction. Il n'y entre pas par son utilisateur : une direction juridique de métropole n'est pas une autorité judiciaire, et l'assistant n'est pas destiné à trancher un litige. **Incertitude assumée :** si un jour l'assistant servait à une instance de règlement de litiges (par exemple une commission chargée de traiter des recours), la classification serait à refaire. C'est pourquoi la section 7 impose une réévaluation à chaque changement de périmètre.

**Repli sur l'article 6, paragraphe 3.** Même un système de l'annexe III peut échapper au haut risque s'il n'influence pas sensiblement la décision, par exemple pour une tâche préparatoire ou pour améliorer le résultat d'une activité humaine déjà faite ; ce repli est écarté si le système fait du profilage de personnes. Le fournisseur doit alors documenter son évaluation avant la mise en service (article 6, paragraphe 4). L'assistant n'a pas besoin de ce repli : il faut néanmoins conserver une note datée de la classification, utile en cas de contrôle (modèle en annexe H).

### 4.4 Obligations qui restent, même hors haut risque

| Obligation | Source | Application à l'assistant | Mesure |
|---|---|---|---|
| Maîtrise de l'IA | article 4 ; reformulée en mesures de soutien par le règlement 2026/1744, considérant 8 (E09) | l'obligation subsiste sous cette forme ; sa formulation exacte est à confirmer sur le texte consolidé | formation des 50 agents du pilote avant l'ouverture des accès |
| Information des personnes | article 50, paragraphe 1 (E07) | les personnes qui interagissent directement avec un système d'IA sont informées qu'il s'agit d'une IA, sauf si c'est évident | bandeau permanent dans l'interface |
| Note de classification | pratique recommandée, par analogie avec l'article 6, paragraphe 4 | documenter le raisonnement de la section 4.3 | note datée, relue par le DPO |

### 4.5 Conséquence d'une erreur de classement

Si l'assistant était à haut risque, les exigences des sections 1 à 3 du chapitre III s'appliqueraient à partir du 2 décembre 2027. Un organisme de droit public devrait aussi réaliser une analyse d'impact sur les droits fondamentaux avant de le déployer (article 27) et informer les personnes concernées par des décisions assistées (article 26). Le coût d'une erreur de classement tombe sur la métropole, d'où la prudence sur le périmètre.

| Évolution d'usage | Effet sur la classification | Décision |
|---|---|---|
| Ajouter la notation de candidats à un marché | possible bascule vers l'emploi ou les services essentiels, selon le cas | interdit dans le périmètre actuel |
| Ouvrir l'assistant aux citoyens | l'article 50 pèse plus lourd ; risque de recours à des décisions individuelles | hors périmètre, nouvelle analyse |
| Mettre l'assistant à disposition d'une instance de recours | rapprochement du point 8(a) | nouvelle classification obligatoire |

### 4.6 RGPD, en parallèle

Le règlement sur l'IA ne remplace pas le RGPD. Les documents contenant des données personnelles (H13) conduisent à examiner l'inscription de l'assistant au registre des traitements du RGPD ; ce point n'est pas sourcé ici et revient au DPO. La CNIL indique qu'une analyse d'impact (AIPD) est obligatoire en cas de risque élevé pour les personnes ou de profilage (E08, page du 8 avril 2024, source antérieure à l'entrée en application du règlement IA). Position de l'auteur : réaliser une AIPD avant le pilote par précaution, car elle sert aussi de support à l'analyse de risques ; ce choix est une recommandation, pas une obligation établie ici. Le DPO tranche. Le plan de l'AIPD figure en annexe G.
