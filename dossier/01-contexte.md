## 1. Contexte et enjeux

### 1.1 Le client et son problème

Métropole Azur compte environ 500 000 habitants (H01) et emploie environ 4 000 agents (H02). Ses services juridiques, de commande publique et administratifs manipulent des délibérations, des règlements et des pièces de marchés publics. Le corpus est estimé à 200 000 documents (H07), répartis entre plusieurs outils.

**L'enjeu.** Environ 600 agents (H03) passent en moyenne 3 h par semaine à chercher des documents (H04). Ce temps est une hypothèse de départ : le dossier ne l'érige pas en fait et prévoit de le mesurer avant d'investir (section 8). Il touche la réactivité des services et la sécurité juridique, car un règlement ou une délibération manqué peut fragiliser un acte.

**Pourquoi l'IA, et pourquoi avec prudence.** Un assistant fondé sur l'IA générative permet de poser une question en langage courant et d'obtenir un résumé qui cite sa source. Il introduit aussi des risques propres, que le NIST AI 600-1 (E04) et l'OWASP LLM Top 10 2025 (E03) répertorient : réponses fausses énoncées avec assurance, fuite de données, injection d'instructions cachées dans les documents, dépendance à un fournisseur. Le règlement (UE) 2024/1689 sur l'IA, modifié par le règlement (UE) 2026/1744 (E05), fixe des obligations dont les dates ont changé (H11).

### 1.2 Ce que disent les cas réels

Trois repères externes cadrent la décision. Aucun ne prouve quoi que ce soit pour Métropole Azur : ils fixent des ordres de grandeur et des mises en garde.

| Repère | Ce qu'il établit | Limite |
|---|---|---|
| Étude Stanford sur des outils commerciaux d'IA de recherche juridique (E10) | Sur plus de 200 questions ouvertes, ces outils donnent une réponse erronée plus de 17 % du temps (Lexis+ AI, Ask Practical Law AI) et plus de 34 % du temps (Westlaw AI-Assisted Research). Deux types d'erreur : réponse fausse, ou réponse juste appuyée sur une source qui ne la soutient pas. | Droit américain, versions de 2024 des outils ; les produits ont évolué depuis. |
| Moffatt c. Air Canada, 2024 BCCRT 149 (E12) | Un tribunal juge une entreprise responsable de l'information inexacte donnée par son agent conversationnel ; elle ne peut pas le présenter comme une entité distincte. | Décision d'un tribunal de petites créances au Canada, lue via des commentaires ; sert d'illustration, non de précédent en droit français. |
| Essai britannique de Microsoft 365 Copilot dans l'administration (E01) | 26 minutes économisées par jour en moyenne, mais déclarées par les agents, sur l'ensemble des tâches. | Auto-déclaré ; ne mesure pas la recherche documentaire. |

**Lecture pour Métropole Azur.** Premier enseignement : un assistant de recherche juridique doit être conçu en supposant qu'il se trompera une fois sur plusieurs. Le taux de 17 % de l'étude Stanford ne se transpose pas tel quel, d'où l'objectif de 90 % de réponses correctes et sourcées du pilote (H14), à mesurer sur le propre corpus de la métropole (H26). Deuxième enseignement : l'erreur d'un outil engage la responsabilité de l'organisation qui l'exploite ; une réponse fausse sur une procédure de marché peut donc lui être imputée. Troisième enseignement : le gain de temps annoncé par les essais est déclaratif, d'où un business case en fourchettes (section 6) et un pilote qui mesure au lieu de croire.

### 1.3 Ce que ce dossier apporte au comité

Une comparaison de quatre options (section 3), une classification réglementaire argumentée (section 4), quatorze risques avec mesures et responsables (section 5), un business case en fourchettes avec une analyse de sensibilité (section 6), une gouvernance et des indicateurs (section 7), et une décision demandée avec critères d'arrêt (section 8). Les annexes (document séparé) détaillent le registre, le protocole de mesure, le plan de test, le plan d'analyse d'impact, les clauses d'achat et un glossaire.

**Méthode et limites.** Les chiffres du client sont inventés pour l'exercice et chaque valeur porte sa confiance dans le registre. Les coûts de construction et d'exploitation sont des hypothèses larges à confirmer par une consultation du marché, non des devis. Le dossier est fictif : sa valeur est dans la démarche, pas dans les montants.
