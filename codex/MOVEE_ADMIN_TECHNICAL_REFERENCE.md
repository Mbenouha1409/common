# MOVEE Admin — référence technique spécifique

Version de consolidation : 2 novembre 2026. **Référence centralisée validée ; anciennes copies retirées après accord utilisateur.** Lire d’abord [README.md](README.md), [règles communes](AGENTS.md), [fonctionnel global](MOVEE_FUNCTIONAL_REFERENCE.md) et [technique globale](MOVEE_TECHNICAL_REFERENCE.md). Les sections issues des anciennes références conservent leur date/statut ; un constat historique ne décrit pas l’installation actuelle.

## Réutilisation du moteur commun

Lire MOVEE_TECHNICAL_REFERENCE.md pour Pages/Fields/Actions/Designer et les invariants. Les particularités Web restent dans App : contexte session web, transports distincts de Mobile Bearer et scopes imposés par Services. Les adaptateurs HTML Booking ne prouvent pas un formulaire React Native générique.

Liens natifs : ID métier de la ligne courante, bindings remappés par field_id enregistré, jamais libellé ni ID du parent par substitution. Réautoriser source/cible et conserver filtres/tri/pagination au retour. Les menus sont des conteneurs sans writer ; les commandes restent des ouvertures de formulaire avec consentement/version/récupération selon le contrat réellement livré. La présence d’un formulaire historique ne garantit pas un aperçu signé ou une reprise durable après fermeture.

Source actuelle pour83raccourcis/29listes : [application/activation](../movee-app/docs/ADMIN_ROW_SHORTCUTS_APPLICATION_ACTIVATION_RESULT.md). Le registre exact et les empreintes d’installation restent dans sql et les plans App ; ne pas les déplacer. Pour les traductions catalogue, réutiliser les contrats App par langue et guide autorisé ; un CRUD historique n’est pas un éditeur de traduction importée.

## Compléments Web datés conservés



## Annexe — chronologie historique, non applicable comme état courant

Les chiffres, ports, noms de versions et mentions « installé/non installé » de cette annexe décrivent leur date d’origine. Le point de reprise en tête du fichier et les contrats actuels priment pour déterminer les opérations disponibles. Cette annexe conserve la traçabilité ; elle n’autorise aucune action ni réactivation.

> **Historique daté, pas état courant.** Provenance : `movee-app/codex/METADATA_ENGINE.md:2`.



---

> **Historique daté, pas état courant.** Provenance : `movee-app/codex/METADATA_ENGINE.md:3`.

### Évolution menus — code du 28 octobre 2026, métadonnées locales non installées

Les menus sont des instances d’action de type `menu`. `location` conserve son
rôle de zone d’affichage ; `menu_uid` référence l’`action_uid` du menu parent
dans les `config_actions` de la même Page et de la même zone. Une valeur absente
signifie une action directe. Un menu peut contenir un autre menu ; les cycles,
parents absents et parents qui ne sont pas des menus sont refusés.

Le type `menu` est un conteneur sans endpoint, Page cible ni `next_actions`.
Les feuilles gardent leurs définitions/actions natives et leurs droits propres.
Le serveur retire les feuilles refusées puis les menus vides, sans promouvoir
leurs descendants. Le Front utilise `ActionEngine` et `HelperBuilder` pour les
menus flottants, y compris hors mainbar ; aucune liste de thèmes en JavaScript.

La définition d’action Menu, le champ virtuel Designer `menu_uid` et son ajout à
la Page de propriétés sont préparés dans [docs/admin_native_recovery_candidate.json](../movee-app/docs/admin_native_recovery_candidate.json).
Ce candidat n’est pas un plan SQL applicable. Le menu natif reste porté par les
`config_actions` d’une Page `is_home=1`. La découverte historique demeure seulement
en compatibilité tant qu’aucune Page d’accueil n’est installée.

À lire avant toute intervention. Le code reste la source de vérité sur les
signatures ; ce document donne le **modèle mental**.

---
