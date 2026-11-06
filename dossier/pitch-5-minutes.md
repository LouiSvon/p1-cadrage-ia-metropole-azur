---
titre: Script de pitch de 5 minutes, assistant IA documentaire pour Métropole Azur
date_maj: 2026-11-06
---

Durée visée : 5 minutes à voix claire. Repères de temps entre crochets. Cas fictif : à dire dès l'ouverture.

**[0:00] Ouverture et cadre**

Bonjour. Avant de commencer, un point de transparence : Métropole Azur est un client fictif que j'ai inventé pour cet exercice de conseil. Les chiffres que je vais citer sont des hypothèses, que j'ai déclarées dans un registre, avec leur source quand il y en a une. Ce qui est réel, c'est la démarche.

**[0:30] Le problème**

Imaginez une métropole de 500 000 habitants et de 4 000 agents. Environ 600 d'entre eux, juristes, acheteurs, services administratifs, cherchent chaque semaine des délibérations, des règlements, des pièces de marchés. Mon hypothèse de départ : 3 heures par semaine et par agent. Sur 200 000 documents répartis dans plusieurs outils.

Un repère pour garder les pieds sur terre : une étude de Stanford sur des outils commerciaux d'IA de recherche juridique a trouvé des réponses erronées plus de 17 % du temps. Un assistant juridique doit donc être conçu en supposant qu'il se trompera.

La question du comité est simple : faut-il lancer un assistant IA qui retrouve et résume ces textes, en citant ses sources ?

**[1:15] Les options**

J'en compare quatre. Ne rien faire. Améliorer la recherche existante, sans IA générative. Un assistant sur le service d'un fournisseur externe. Ou un assistant hébergé en environnement maîtrisé.

Mon choix pour le pilote : la recherche améliorée comme socle, puis l'assistant hébergé. J'écarte le service externe parce que, selon mon hypothèse, près d'un tiers des documents contient des données personnelles, et que le comité doit pouvoir dire où elles sont traitées.

Et le meilleur argument contre moi, je le dis tout de suite : la recherche améliorée seule pourrait suffire. Si le temps est perdu à retrouver plutôt qu'à lire, l'assistant n'apporte rien de plus.

**[2:00] Le cadre réglementaire**

Côté AI Act, j'ai lu le règlement sur EUR-Lex, dans sa version modifiée en juillet 2026. L'assistant n'est pas un système à haut risque, à condition que son périmètre exclue l'évaluation de personnes et tout usage par une instance juridictionnelle. Le point le plus proche, c'est l'aide à la recherche juridique pour une autorité judiciaire. Une direction juridique de métropole n'en est pas une. Mais si l'usage change, tout est à refaire. Les obligations des systèmes à haut risque s'appliquent de toute façon à partir du 2 décembre 2027.

**[2:45] Les risques**

J'ai analysé quatorze risques, reliés à l'OWASP et au NIST, chacun avec une mesure et un responsable. Quatre comptent vraiment. La réponse fausse sur le droit, parce qu'un agent pourrait agir dessus. La fuite de données personnelles. L'accès à un document qu'on n'a pas le droit de lire. Et l'injection d'instructions cachées dans un document. Mes réponses : toujours citer la source, refuser de répondre sans source, des droits d'accès au niveau de chaque document, un assistant en lecture seule, et un jeu de 200 questions de test, avec des pièges.

**[3:30] Le business case**

Sur trois ans, le scénario central donne un net de 367 000 euros, entre un pessimiste à moins 1 176 000 et un optimiste à plus de 2 391 000. L'incertitude est donc plus grande que le résultat. Deux facteurs décident : la part du temps réellement économisée, et le taux d'adoption. Le central ne couvre ses coûts que si on économise au moins 21,2 % du temps de recherche, contre 30 % supposé. C'est fragile. Et ces deux facteurs sont justement ceux qu'un pilote peut mesurer.

**[4:15] La décision demandée**

Je ne demande donc pas un déploiement. Je demande trois choses. Un : lancer maintenant une mesure préalable de 4 semaines, avec l'analyse d'impact et une consultation du marché pour avoir de vrais devis. Deux : autoriser un pilote de 3 mois et 50 utilisateurs, avec un budget plafonné. Trois : aucun déploiement général avant d'avoir comparé les résultats à des seuils fixés à l'avance. On arrête si le gain mesuré reste sous 10 % à la fin du deuxième mois, si moins de 90 % des réponses sont correctes et sourcées, ou en cas d'incident de confidentialité.

**[4:50] Clôture**

Ma recommandation est fausse si la mesure montre que le problème est l'indexation, ou si les devis tombent dans la zone pessimiste. C'est le but : décider avec des hypothèses assumées, et se donner les moyens de les corriger. Merci.
