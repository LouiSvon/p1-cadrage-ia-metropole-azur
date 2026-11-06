## Annexe E. Cartographie croisée OWASP, NIST, risques du dossier

Les 10 catégories de l'OWASP LLM Top 10 2025 (E03) et leur traitement dans le dossier.

| OWASP | Intitulé | Risque du dossier | Risque NIST proche | Pourquoi |
|---|---|---|---|---|
| LLM01 | Prompt Injection | R06 | Information Security | injection indirecte par des documents |
| LLM02 | Sensitive Information Disclosure | R04 | Data Privacy | données personnelles dans les pièces |
| LLM03 | Supply Chain | R08 | Value Chain and Component Integration | modèle et composants tiers |
| LLM04 | Data and Model Poisoning | R09 | Information Security | corpus altéré |
| LLM05 | Improper Output Handling | R10 | Information Security | sortie jamais interprétée |
| LLM06 | Excessive Agency | R11 | Human-AI Configuration (indirect) | assistant en lecture seule |
| LLM07 | System Prompt Leakage | R07 | Information Security | consignes sans secret |
| LLM08 | Vector and Embedding Weaknesses | R05 | Data Privacy | droits d'accès au niveau du document ; mesures de l'OWASP (E16) |
| LLM09 | Misinformation | R01, R02 | Confabulation | réponses fausses, textes abrogés |
| LLM10 | Unbounded Consumption | R12 | Environmental Impacts (indirect) | quotas, plafond budgétaire |

Les risques R03 (surconfiance), R13 (propriété intellectuelle) et R14 (classification) n'ont pas d'équivalent OWASP : ils relèvent du NIST (Human-AI Configuration, Intellectual Property) et de l'AI Act.

**Limite.** Cette cartographie est un classement de l'auteur pour organiser l'analyse. Elle n'est pas une correspondance officielle entre référentiels.
