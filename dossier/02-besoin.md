## 2. Besoin, parties prenantes, périmètre

### 2.1 Le besoin

Retrouver rapidement le bon texte (délibération, article de règlement, clause d'un marché) et en obtenir un résumé qui cite précisément la source et le passage, pour que l'agent vérifie avant d'agir. L'agent reste décisionnaire.

**Trois usages types**, qui servent aussi de base au jeu de tests (annexe C) :
- **Retrouver** : « Quelle délibération a fixé le règlement de voirie applicable au quartier X ? » La réponse attendue est une liste de documents avec date, numéro et statut (en vigueur ou abrogé).
- **Résumer** : « Résume les obligations de publicité de ce marché. » La réponse attendue est un résumé court, chaque affirmation renvoyant à un passage.
- **Comparer** : « Qu'est-ce qui change entre l'ancienne version et la version actuelle du règlement intérieur ? » La réponse est une liste de différences sourcées ; c'est l'usage le plus exposé à l'erreur.

### 2.2 Périmètre

- **Dans le périmètre :** recherche et résumé sur un corpus de documents textuels, utilisateurs internes uniquement, réponses toujours accompagnées de la source.
- **Hors périmètre, par choix :** service aux citoyens ; décision, notation ou classement de personnes (agents, candidats, titulaires de marchés) ; rédaction d'actes à signer ; données de santé, sociales ou RH. Ce choix a une conséquence réglementaire (section 4) : sortir du périmètre ces usages garde l'assistant hors des catégories à haut risque.
- **Pilote :** 3 mois et 50 utilisateurs (H08).

### 2.3 Le corpus

Le corpus n'est pas homogène. Le tableau classe les familles de documents et la prudence qu'elles appellent. Il n'y a pas de volumes par famille : ils sont à relever en phase 0.

| Famille | Exemples | Statut de publicité | Prudence |
|---|---|---|---|
| Délibérations et actes réglementaires | délibérations du conseil, arrêtés, règlements | publicité à vérifier acte par acte : le CRPA fait publier en ligne les documents que les administrations communiquent, hors collectivités de moins de 3 500 habitants et personnes morales sous un seuil d'agents (E13) | vérifier le statut de chaque acte ; textes abrogés à signaler |
| Pièces de marchés publics | avis, règlements de consultation, cahiers des charges, rapports d'analyse | mixte : certaines parties relèvent du secret des affaires | exclure les offres des candidats du périmètre du pilote |
| Documents internes | notes, procédures, comptes rendus | internes | droits d'accès par service |
| Documents contenant des données personnelles | noms d'agents, de candidats, de titulaires | variable | pseudonymiser à l'ingestion ; part estimée à 30 % (H13) |

**Point d'attention.** Un document publiable n'est pas un document dont l'assistant peut faire un usage libre : le droit de publier ne règle ni le statut des données personnelles qu'il contient ni les droits d'accès internes. Le dossier traite ces deux questions séparément.

### 2.4 Parties prenantes

| Rôle | Intérêt | Point de vigilance |
|---|---|---|
| Direction juridique et commande publique (porteur) | gain de temps, fiabilité | réponses fausses sur le droit des marchés |
| DSI | hébergement, intégration, sécurité | dépendance fournisseur, fuite de données |
| DPO | RGPD, registre des traitements | données personnelles dans les pièces |
| Direction générale et élus | budget, image | erreur visible, coût |
| Agents utilisateurs | utilité, charge de travail | surconfiance, déqualification |
| Représentants du personnel | impact sur le travail | consultation à prévoir : le comité social territorial est compétent sur l'organisation et le fonctionnement des services (E14, non vérifié sur le texte) |

### 2.5 Contraintes de cadrage

Les réponses doivent être vérifiables par l'agent. Le pilote vise 90 % de réponses correctes et sourcées (H14), cible mesurée sur les 170 questions hors pièges (H34) d'un jeu de 200 questions (H26, répartition en H30) ; les questions pièges sont notées à part (H29). Un refus de répondre est préféré à une réponse inventée.
