# MOVEE — point d’entrée de la connaissance commune

Consolidation et nettoyage validés le2novembre2026. Les15anciennes références et consignes remplacées ont été supprimées sur accord utilisateur. [Résultat du nettoyage](CONSOLIDATION_CLEANUP_RESULT.md) ; [liste de revue conservée](CONSOLIDATION_REVIEW.md).

## Commencer une nouvelle conversation

Lire dans cet ordre :

1. [AGENTS.md](AGENTS.md) : méthodes, périmètres et autorisations.
2. [MOVEE_FUNCTIONAL_REFERENCE.md](MOVEE_FUNCTIONAL_REFERENCE.md) : vision, responsabilités et décisions réseau.
3. [MOVEE_TECHNICAL_REFERENCE.md](MOVEE_TECHNICAL_REFERENCE.md) : architecture et dépendances communes.
4. Le couple spécifique du projet ci-dessous, puis les contrats et le code nécessaires chez le propriétaire.

| Projet / couche | Fonctionnel | Technique |
| --- | --- | --- |
| App — Backend opérationnel | [App](MOVEE_APP_FUNCTIONAL_REFERENCE.md) | [App](MOVEE_APP_TECHNICAL_REFERENCE.md) |
| Admin — front Web d’App | [Admin](MOVEE_ADMIN_FUNCTIONAL_REFERENCE.md) | [Admin](MOVEE_ADMIN_TECHNICAL_REFERENCE.md) |
| Mobile — iOS/Android hors séance | [Mobile](MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md) | [Mobile](MOVEE_MOBILE_TECHNICAL_REFERENCE.md) |
| Biz et Info — une application | [Biz](MOVEE_BIZ_FUNCTIONAL_REFERENCE.md) | [Biz](MOVEE_BIZ_TECHNICAL_REFERENCE.md) |
| Pod — exécution locale | [Pod](MOVEE_POD_FUNCTIONAL_REFERENCE.md) | [Pod](MOVEE_POD_TECHNICAL_REFERENCE.md) |
| MOTION — analyse d’exercices | [MOTION](MOVEE_MOTION_FUNCTIONAL_REFERENCE.md) | [MOTION](MOVEE_MOTION_TECHNICAL_REFERENCE.md) |

Admin n’est pas un dépôt distinct ; Studio reste le coordinateur proposé dans Pod, pas un logiciel déjà livré. BODY est distingué de MOTION mais aucun référentiel BODY indépendant n’a été retrouvé ; ne pas le reconstruire.

## Comment amorcer Codex sans recopier la connaissance

Instruction courte à utiliser à l’ouverture d’une conversation :

> Lis `/Users/mbenmouha/Documents/Movee/codex/README.md`, puis `AGENTS.md`, les références globales et celles du projet concerné. Identifie les dépendances avant de proposer ou modifier quelque chose.

L’AGENTS central n’est pas dans les répertoires parents des dépôts : son chargement automatique depuis un projet n’est pas garanti. Aucun réglage Codex ni copie d’amorçage dans les projets n’est installé par cette consolidation. Les trois anciens AGENTS par projet ont été supprimés ; ne pas les recréer. L’ancienne référence Admin reste provisoirement présente pour une dépendance technique, sans remplacer le point d’entrée central.

## Utiliser les sources sans confondre leur statut

- Décisions durables : les références centrales. Les registres complets restent lisibles, pas remplacés par une simple synthèse.
- Protocoles, schémas, code et preuves : restent dans les projets à leurs emplacements et versions. Une référence fonctionnelle ne prouve pas l’état déployé.
- Annexe « chronologie historique » : ancienne progression, à consulter pour une trace précise ; pas une instruction de lancement ou une liste de versions actuelles.
- Registres : Q001–Q130 réseau dans le global ; B1–B8 chez App ; T1–T8 (78) chez Mobile ; D01–D57, Q01–Q08, S01–S10, F01–F11 et R01/R02 chez Biz ; XP01–XP12 et POD-T01–POD-T12 chez Pod ; décisions/propositions distinctes chez MOTION.

## Références partagées conservées

- [Charte commune Light / Black](DESIGN_SYSTEM_MOVEE.md), [adaptations Web](ADAPTATIONS_WEB_MOVEE.md), [adaptations Admin](ADAPTATIONS_ADMIN_MOVEE.md). Fichiers existants inchangés ; aucune seconde charte créée.
- [Environnement du Mac](../docs/ENVIRONNEMENT_DEVELOPPEMENT_MAC.md) et [validation locale](../dev/VALIDATION_ENVIRONNEMENT_LOCAL.md). Aucune duplication du guide opérationnel.
- [Sources et correspondance des sections](CONSOLIDATION_SOURCES.json), [rapport de validation](CONSOLIDATION_VALIDATION.json), [revue et suppressions proposées](CONSOLIDATION_REVIEW.md).

Les anciens prompts de reprise sous docs ont été supprimés ; ce README les remplace. Aucun ancien lien de chat n’est une dépendance nécessaire au démarrage si la décision locale est complète.

## Nettoyage complémentaire des dossiers projet

Les799fichiers des emplacements demandés ont été examinés individuellement. Le [rapport complémentaire](CLEANUP_REMAINING_RESULT.md) et son [audit fichier par fichier](CLEANUP_REMAINING_RESULT.json) indiquent305retraits,494conservations et leurs motifs. Les anciens rapports préparatoires cités dans des annexes historiques peuvent être retirés : ne pas les recréer ni les prendre pour des contrats actuels. Les contrats exécutables, reçus d’application utiles et migrations conservés restent dans les projets. Les conventions ASSUMPTIONS de Biz sont désormais dans sa référence technique centrale.
