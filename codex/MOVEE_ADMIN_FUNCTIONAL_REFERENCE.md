# MOVEE Admin — référence fonctionnelle spécifique

Version de consolidation : 2 novembre 2026. **Référence centralisée validée ; anciennes copies retirées après accord utilisateur.** Lire d’abord [README.md](README.md), [règles communes](AGENTS.md), [fonctionnel global](MOVEE_FUNCTIONAL_REFERENCE.md) et [technique globale](MOVEE_TECHNICAL_REFERENCE.md). Les sections issues des anciennes références conservent leur date/statut ; un constat historique ne décrit pas l’installation actuelle.

## Propriétaire et état de lecture

Admin est le front Web de movee-app, pas un nouveau dépôt. Sept thèmes/dix-huit listes restent la cible ; les douze Pages Finance/Tâches inactives ne sont pas activées par la consolidation. Affiliations courantes6/5, engagements/ledger siège pour les lots qualifiés, aucune délégation financière rétroactive.

Les mentions « candidat non installé » du28octobre sont des étapes historiques. Pour la reconnaissance/installations ultérieures : [Contrat natif Admin effectivement livré](../movee-app/docs/ADMIN_COMPLETION_INTEGRATION_RESOLVED_CONTRACT.md) si disponible et [raccourcis appliqués](../movee-app/docs/ADMIN_ROW_SHORTCUTS_APPLICATION_ACTIVATION_RESULT.md). Aucun bouton ne qualifie une mutation inachevée ; aucun droit implicite sur les préférences privées ou données de santé.

<!-- provenance: movee-app/codex/MOVEE_ADMIN_SCOPE.md:3 -->

## Reprise validée le 28 octobre 2026 — périmètre du lot courant

Le menu métier comporte sept thèmes et dix-huit listes principales :

| Thème | Listes |
| --- | --- |
| Réseau | Franchisés, Studios |
| Personnes | Adhérents, Coachs, Utilisateurs |
| Offres et souscriptions | Offres, Engagements |
| Planning et séances | Réservations, Rendez-vous, Séances réalisées |
| Accompagnement | Exercices, Programmes, Bilans |
| Finance | Factures, Paiements, Rémunérations coachs |
| Exploitation | Équipements, Tâches |

Framework et Paramètres sont hors du lot métier. Les décisions globales historiques
ci-dessous restent tracées ; elles ne justifient pas d’ajouter ces rubriques au lot.
Les sous-listes s’ouvrent depuis leur objet parent. Les Pages et leurs instances
de configuration utilisent les UID opaques générés par le moteur, sans nom métier
en guise d’UID. La notion de menu est ajoutée génériquement aux actions, à côté
de `location`, avec référence à l’instance du menu parent ; aucun système de menu
spécifique aux sept thèmes dans le frontend.

L’utilisateur autorise le code du moteur et la préparation/reprise des parcours.
Cela n’autorise pas de nouvelle permission, migration ni mutation des données
métier existantes. Finance/Exploitation attendent les contrats Backend manquants ;
les écritures non closes ne sont pas activées par la présence d’un formulaire.

Décision utilisateur du 26 octobre 2026. Navigation native metadata-driven : listes, filtres, fiches et actions ; aucun frontend séparé à créer pour ce lot. Les règles communes restent dans les Services App. Mobile est préservé.

| Rubrique | Pages principales | Franchiseur | Franchisé |
| --- | --- | --- | --- |
| Tableau de bord | Activité, réservations, alertes, tâches | Réseau et filtre studio | Ses studios |
| Studios | Liste, fiche, horaires, fermetures, plages réservables, capacité | Tous les studios | Ses studios |
| Adhérents | Liste, fiche, rattachements, engagements, crédits, réservations | Selon habilitations réseau | Adhérents accessibles dans ses studios |
| Coachs | Liste, fiche, affectations, qualifications, disponibilités, exceptions, planning | Vue réseau | Coachs intervenant dans ses studios |
| Réservations | Liste, calendrier, fiche, actions métier | Vue réseau | Réservations de ses studios |
| Offres et engagements | Catalogue, conditions, engagements souscrits | Références réseau et périmètres autorisés | Offres et engagements autorisés |
| Équipements | Parc, fiche, disponibilité, incidents, maintenance | Vue réseau | Équipements de ses studios |
| Programmes et exercices | Bibliothèque, programmes, versions | Selon droits | Selon droits |
| Finance | Encaissements, factures, reversements, rémunérations coachs | Pilotage et rapprochements réseau | Finances de son exploitation |
| Exploitation | Incidents, demandes, réclamations, tâches | Suivi réseau | Suivi de ses studios |
| Utilisateurs et accès | Comptes, affiliations, fonctions, périmètres | Accès autorisés | Gestion déléguée à préciser |
| Paramètres | Prestations, durées, paramètres réseau et locaux | Paramètres réseau | Réglages locaux autorisés |

Le coach accède uniquement aux adhérents et ressources autorisés. Le scope est imposé côté Backend ; les filtres ne peuvent pas l’élargir. Les mécanismes sourceur/vendeur du brief METADATA_ENGINE.md proviennent d’un autre projet, pas d’une implémentation MOVEE attestée.

Les actions dépendent des droits et contrats livrés. Pas de correction CRUD du ledger, d’engagement ou de réservation contournant les Services. Les restrictions de création/modification des programmes restent applicables. Aucune permission administrative implicite sur les préférences privées ou données de santé.

---

<!-- provenance: movee-app/codex/MOVEE_ADMIN_SCOPE.md:51 -->

## Livraison progressive

Premier lot : Studios. Puis Adhérents, Coachs, Réservations, Offres/engagements et Accès ; les autres rubriques restent dans le périmètre global, sans être déclarées livrées.
Toute installation de métadonnées, migration ou modification de données suit son autorisation propre. Distinguer préparation, code, tests isolés, installation locale et recette navigateur.

---

<!-- provenance: movee-app/codex/MOVEE_ADMIN_SCOPE.md:56 -->

## Lot groupé — décision du 27 octobre 2026

L’utilisateur demande un seul lot pour Adhérents, Coachs, Réservations, Offres/engagements et Accès. Studios déjà livré est conservé. Une seule proposition de navigation et demande Backend regroupe ces cinq ensembles, avec résolution globale des contrats/droits, puis un plan d’installation unique à approuver. Ce regroupement n’autorise ni nouvelles habilitations, ni SQL, ni contournement des contrats manquants. Les douze rubriques du périmètre global restent conservées.

---

<!-- provenance: movee-app/codex/MOVEE_ADMIN_SCOPE.md:60 -->

## Arbitrages du 27 octobre 2026 — lot groupé

Validation utilisateur explicite : populations Adhérents/Coachs fondées sur les
affiliations courantes6/5, cumulables, intersectées avec les droits et périmètres
accessibles. Aucun rôle historique de login ni simple disponibilité ne qualifie
la population. Le parcours coach Adhérents vérifie l’affectation courante.

Validation utilisateur explicite : consultations des engagements et du ledger
réservées au siège habilité dans ce lot. `home_location_id` existe pour certains
engagements récents ; il n’autorise pas à inventer une propriété financière
franchisée des historiques, des consommations intercentres ou après transfert.
Aucune qualification rétroactive, nouvelle habilitation ou délégation118/119/121
n’est autorisée par ces deux arbitrages. Les droits supplémentaires restent des
propositions distinctes, sans INSERT de permission dans le plan Pages.

## Annexe — chronologie historique, non applicable comme état courant

Les chiffres, ports, noms de versions et mentions « installé/non installé » de cette annexe décrivent leur date d’origine. Le point de reprise en tête du fichier et les contrats actuels priment pour déterminer les opérations disponibles. Cette annexe conserve la traçabilité ; elle n’autorise aucune action ni réactivation.

> **Historique daté, pas état courant.** Provenance : `movee-app/codex/MOVEE_ADMIN_SCOPE.md:75`.

### Préparation validée — 27 octobre 2026 : lectures Core

L’utilisateur autorise la préparation de 24 habilitations de lecture : rôle 2, entités 19/20/36/42/43/44, actions 100/101 ; rôle 5, entités 19/20/42/43, actions 100/101 ; rôles 2/5, référence Ville 16, actions 100/101. Périmètres serveur et affiliations courantes maintenus. Finance 37/55 siège uniquement, aucune délégation 77 ni nouveau droit métier de mutation. Plan unique avec 13 mises à jour et 11 ajouts de Pages ; application soumise à validation de sa nouvelle empreinte.

---

> **Historique daté, pas état courant.** Provenance : `movee-app/codex/MOVEE_ADMIN_SCOPE.md:79`.

### 28 octobre 2026 — plan de reprise native Backend

Préparation autorisée, aucune application SQL : sept thèmes/dix-huit listes, candidat 38 mises à jour/54 nouvelles Pages dont douze inactives, Menu et champ virtuel Designer. Complément demandé : enregistrement en lecture seule de programs.program_version (entier nullable existant), affichage liste/fiche, aucune initialisation/version supposée. Le plan ajoute donc deux Fields. Aucun droit ajouté, aucune délégation franchisé, aucun changement Mobile91–96 ni préférence privée. Révision globale exacte, preflight avant commit et rejeu sans écriture requis. Les contrats manquants de mutations/finance/exploitation restent signalés, sans activation implicite de fonctions.

---

> **Historique daté, pas état courant.** Provenance : `movee-app/codex/MOVEE_ADMIN_SCOPE.md:83`.

### Suite d’implémentation du 28 octobre 2026

L’utilisateur demande de terminer l’implémentation avant une recette globale. Les cinq ensembles restent la cible ; les contrats absents ne sont pas réputés livrés. Compléments frontend : [docs/ADMIN_COMPLETION_DELIVERY.md](../movee-app/docs/ADMIN_COMPLETION_DELIVERY.md), candidat natif [docs/admin_native_completion_candidate.json](../movee-app/docs/admin_native_completion_candidate.json), dépendances Backend [docs/ADMIN_COMPLETION_BACKEND_REQUEST.md](../movee-app/docs/ADMIN_COMPLETION_BACKEND_REQUEST.md). Les modifications de code et la préparation du candidat ne valent ni installation des Pages, ni autorisation SQL, ni activation des thèmes Finance/Exploitation.

---

> **Historique daté, pas état courant.** Provenance : `movee-app/codex/MOVEE_ADMIN_SCOPE.md:87`.

### 28 octobre 2026 — clôture partielle des contrats et complément natif

L’utilisateur valide le maintien inactif des douze Pages Finance/Tâches et leur traitement séparé après arbitrage. Préparation seule du successeur natif :87 UPDATE/7 INSERT de Pages, aucune permission, champ global ou action globale. Aucun SQL ni redémarrage autorisé dans ce lot. Compléments Backend : lecture relationnelle du coach choisi via user_locations datée/intersectée ; commandes catalogue Exercices/Médias/Matériels/Muscles versionnées et reçus existants proposals ; lecture de is_active limitée au catalogue47, activation explicite108 réservée au nouveau Service, pas aux comptes ni au writer MCP général ; synthèse de crédits calculée par le Service, siège uniquement. Trois Pages HTML Booking session revalidées, aucun endpoint Mobile réutilisé. Identités/onboarding/édition réseau commerciale et garanties de comptes restent distincts, non déclarés terminés par l’installation de Pages.

---

> **Historique daté, pas état courant.** Provenance : `movee-app/codex/MOVEE_ADMIN_SCOPE.md:91`.

### 28 octobre2026 — candidat d’intégration natif

Préparation seule d’un nouveau plan87 UPDATE/9 INSERT, successeur direct de admin_native_recovery_v1. Le plan76cc... n’est ni appliqué ni modifié et n’est plus utilisable sous les sources courantes. Deux Pages supplémentaires :variante native des affectés au coach choisi et formulaire d’état actif47 ; raccordement catalogue fiable et synthèse des crédits siège. Préserver tous les UID installés et les sept UID préparés. Aucun droit,champ/action global,DDL,SQL local ou redémarrage ; douze Pages Finance/Tâches restent inactives. Recette globale après clôture des contrats restants, pas de validation intermédiaire réclamée à l’utilisateur.
