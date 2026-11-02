# MOVEE — résultat du nettoyage documentaire

2 novembre2026. Les15suppressions présentées ont été autorisées par l’utilisateur et exécutées après revalidation de leurs empreintes et des documents consolidés. Aucun autre fichier source n’a été supprimé.

## Fichiers supprimés

- `movee-app/codex/AGENTS.md`
- `movee-mobile/codex/AGENTS.md`
- `movee-biz/codex/AGENTS.md`
- `movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md`
- `movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md`
- `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md`
- `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md`
- `movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md`
- `movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md`
- `movee-motion/codex/MOVEE_MOTION_REFERENCE.md`
- `movee-app/codex/METADATA_ENGINE.md`
- `docs/CONTINUITE_PROJET_MOVEE.md`
- `docs/REPRISE_CONVERSATION_BACKEND.md`
- `docs/REPRISE_CONVERSATION_MOBILE.md`
- `docs/REPRISE_CONVERSATION_BIZ.md`

## Préservation et renvois

- Les références fonctionnelles/techniques et AGENTS sont désormais dans le dossier commun codex, accessibles depuis [README.md](README.md).
- `movee-app/codex/MOVEE_ADMIN_SCOPE.md` est conservé : le préparateur Studios lit encore ce chemin. Aucun changement de code n’est inclus dans ce nettoyage.
- Le guide de développement Mac pointe vers le dossier central ; les commandes et réglages opérationnels sont inchangés.
- Les statuts d’attente des documents centraux sont actualisés ; les décisions métier ne sont pas modifiées.
- Les contrats, JSON scellés, migrations, fixtures, code et charte contrôlés sont inchangés. Les citations historiques d’anciens chemins dans ces artefacts ne sont pas réécrites.
- Aucun SQL, aucune permission, donnée métier, configuration privée ou service modifié. Aucun redémarrage.

Le fichier CONSOLIDATION_VALIDATION.json conserve le contrôle effectué avant suppression ; CONSOLIDATION_CLEANUP_RESULT.json décrit l’état après nettoyage et ses contrôles. Les anciennes sources ne doivent pas être recréées depuis les scripts temporaires de composition. Aucun AGENTS dupliqué ni réglage Codex automatique installé ; l’amorçage central reste celui du README.
