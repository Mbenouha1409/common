# MOVEE App — référence technique spécifique

Version de consolidation : 2 novembre 2026. **Référence centralisée validée ; anciennes copies retirées après accord utilisateur.** Lire d’abord [README.md](README.md), [règles communes](AGENTS.md), [fonctionnel global](MOVEE_FUNCTIONAL_REFERENCE.md) et [technique globale](MOVEE_TECHNICAL_REFERENCE.md). Les sections issues des anciennes références conservent leur date/statut ; un constat historique ne décrit pas l’installation actuelle.

## État documentaire le plus récent et preuves à consulter

D’après les rapports livrés du31octobre/2novembre : schéma0004_programme_planning_v1,83tables ; consolidation Mobile30Pages/profil14, raccourcis Admin29listes puis mise à jour de présentation coach278. Dernier rapport de cette conversation : [COACH_WORKSPACE_APPLICATION_ACTIVATION_RESULT.md](../movee-app/docs/COACH_WORKSPACE_APPLICATION_ACTIVATION_RESULT.md), reconnaissance coach_workspace_chrome_v1. Ces états sont datés et doivent être recontrôlés dans l’environnement avant une nouvelle opération ; aucun service ou SQL inspecté pour le chantier documentaire actuel.

La baseline physique73tables reste historique et immuable, pas la base actuelle à réimporter. Contrats/installateurs/empreintes restent dans movee-app/docs, sql, services et scripts. Ne pas supprimer les anciens contrats nécessaires à la chaîne de reconnaissance.

## Architecture et décisions spécifiques conservées

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:464 -->

## IA 2B — Persistance des opérations de réservation

**Décision architecturale validée le 16 octobre 2026 : ne pas créer la table `booking_operations`.** Cette décision remplace la proposition antérieure de table dédiée dans le plan SQL IA 2B. Elle ne modifie aucune décision fonctionnelle Q001–Q130 ou B1–B8.

Répartition des responsabilités de persistance :

- `bookings` conserve l'état courant de la réservation et porte le contrôle de concurrence.
- `proposals` conserve les commandes métier, propositions, consentements, révisions historiques, créneaux temporairement retenus et reçus durables des opérations de réservation.
- `session_credit_transactions` conserve les allocations et mouvements de crédits liés à la réservation et à l'opération portée par `proposals` ; aucun compteur de crédits n'est ajouté.

**La validation d'une proposition ne signifie pas son exécution effective.** L'accord de l'adhérent, la validation métier éventuelle et l'application effective doivent être distingués. Un succès n'est annoncé qu'après confirmation du résultat backend ; une proposition validée ne vaut ni réservation confirmée ni mouvement de crédit exécuté.

Garanties obligatoires des Services et des extensions SQL préparées, à confirmer par recette sur le schéma effectivement déployé :

- **Idempotence et reprise :** identité de commande stable, empreinte des paramètres et reçu initial durable. Même identité et mêmes paramètres : restitution du résultat initial après contrôle des permissions actuelles ; paramètres différents : conflit. Un incident ou retry ne doit pas répéter les effets métier.
- **Consentement :** accord explicite de l'adhérent lorsqu'il est requis, lié au contenu exact et aux conséquences acceptées, avec auteur et date traçables. Une modification de ces conséquences impose une revalidation et un nouvel accord lorsque nécessaire.
- **Historique immuable :** conserver les créations, annulations, déplacements, remplacements et décisions successives ; ne pas écraser les révisions historiques, contenus acceptés ou reçus terminaux. Distinguer les informations de cycle de vie modifiables de ces preuves immuables.
- **Concurrence :** vérifier l'état attendu et les droits sous contrôle transactionnel ; garantir une seule proposition de remplacement active par réservation et empêcher les doubles effets fonctionnels, y compris pour des commandes distinctes.
- **Créneaux temporaires :** conserver le créneau et son échéance, comptabiliser sa retenue dans les contrôles de disponibilité et revalider son expiration sous verrou. Une proposition expirée n'est pas réactivée automatiquement.
- **Atomicité avec le ledger :** appliquer l'état de réservation, l'état d'exécution et le reçu de la commande, ainsi que les mouvements de crédits associés, dans une transaction unique sur une même connexion ; rollback complet en cas d'erreur, sans commit intermédiaire.
- **Sécurité :** appliquer les permissions et scopes actuels dans les Services ; la présence d'une proposition, d'un consentement ou d'un reçu ne constitue jamais une autorisation permanente. Aucun accès SQL direct depuis l'assistant IA ou agent IA.

Les structures correspondantes sont désormais intégrées à la baseline V1. Leur présence ne prouve pas à elle seule les garanties métier : vérifier les Services et tests actuels. Cette documentation n'autorise aucune application SQL.


---

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:491 -->

## MOVEE — Architecture technique cible


**Projet :** MOVEE App — référentiel de conception du 12 octobre 2026.  
**Statut :** documentation cible ; ni preuve d’implémentation ni autorisation de migration.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:521 -->

## Sous-systèmes à concevoir sans préjuger des classes

1. Réseau, centres, exploitants et contrats datés (Q001–Q007, Q024–Q025).
2. Offre, adhésion, booking, capacité et ledger (Q008–Q015).
3. Séance, machine, événements, adaptation de programme et reprise hors ligne (Q026–Q042).
4. Coach, bilan accompagné, planning et rémunération (Q053–Q065).
5. Compensation financière centralisée, clôture et corrections (Q016–Q025).
6. Communication, CRM, communauté, B2B et marketplace (Q066–Q071, Q109–Q116).
7. Gouvernance IA, consentements, modèles, coûts, workflows et audit (Q044–Q052, Q084–Q100).
8. Déploiements progressifs, supervision, qualité et support (Q117–Q129).

### Périmètres mobiles validés des sous-systèmes — AR05

**AR05.1 — Bilans sportifs.** Adhérent : consultation, évolution, explications IA ; coach autorisé : création, complément, modification et validation **conversationnels** via Services App. Acquisition des mesures externe.

**AR05.2 — Abonnements.** Consultation et demandes conversationnelles de souscription, renouvellement ou modification ; **accord explicite** avant engagement financier/contractuel ; exécution App.

**AR05.3 — Rémunération coach.** Consultation des contrats, commissions, rémunérations, factures et paiements autorisés ; explication IA et signalement d'anomalies ; pas de gestion comptable complète dans Mobile.

**AR05.4 — Réclamations.** Dépôt, justificatifs, suivi, échanges et décision restitués via IA ; décisions de remboursement/litige réservées aux personnes/Services habilités.

**AR05.5 — Communauté.** Groupes, échanges et événements autorisés, avec recherche IA, confidentialité et modération App ; pas de réseau social généraliste.

**AR05.6 — Parrainage.** Lien/code partageable, invitations, suivi et avantages via IA ; éligibilité et récompenses exclusivement calculées/attribuées par App.

**AR05.7 — Marketplace.** **Hors Mobile** : ni boutique, panier ni achat ; l'IA peut orienter vers le canal commercial distinct, sans transaction.

**AR05.8 — B2B.** Administration entreprises/partenaires **hors Mobile** ; les adhérents bénéficiaires voient/utilisent leurs droits dans Mobile.

**AR05.9 — Portabilité.** Demande et export de données personnelles **via canal externe**, non intégrés au Mobile ; IA d'orientation uniquement ; App contrôle l'exécution.

**AR05.10 — Langues.** **Mobile entièrement multilingue dès V1** : interface, IA, notifications et contenus disponibles localisés ; documents contractuels uniquement en versions officiellement validées. Langues initiales et politique de repli à définir.

**AR05 :** capacités de lecture/action par profil et permission, confirmations contractuelles/financières, pièces justificatives, modération, parrainage, canal externe marketplace/B2B/portabilité et internationalisation V1.

**Qualité de contrat :** formats et erreurs API, idempotence des actions sensibles, authentification Bearer, pagination, localisation, scénarios de tests iOS/Android et absence de dépendance à une route inventée.

Ces capacités restent à vérifier/contractualiser ; elles ne constituent ni endpoints disponibles ni calendrier de livraison serveur. Les autres écarts techniques Q/T relevés par l’audit restent ouverts.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:560 -->

## Capacités natives de l’agent IA

L’agent IA utilise un registre natif fermé de capacités explicitement autorisées, avec contrats d’entrée/sortie stricts, vérification des permissions et activation par centre. Les métadonnées peuvent aider à décrire des capacités mais ne publient pas automatiquement des actions au modèle. Les intégrations héritées ne définissent pas l’architecture cible.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:594 -->

## MOVEE — Modèle de données : existant et écarts


**Projet :** MOVEE App — référentiel de conception du 12 octobre 2026.  
**Statut :** documentation cible ; ni preuve d’implémentation ni autorisation de migration.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:600 -->

## Source physique et limites

La baseline canonique V1 et [sql/baseline/V1_STRUCTURE.json](../movee-app/sql/baseline/V1_STRUCTURE.json) décrivent les 73 tables et leurs définitions complètes, y compris index, FK, CHECK et options. Ils remplacent l'ancien inventaire de colonnes antérieur aux migrations. Pour éviter une seconde définition divergente, consulter ces sources directement avant toute évolution. Aucun changement de schéma n'est autorisé par ce référentiel.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:604 -->

## Inventaire physique V1

`actions`, `appointments`, `assessment_tests`, `assessments`, `bookings`, `cities`, `commission_rules`, `commissions`, `configs`, `consent_templates`, `contact_activities`, `contact_consents`, `contact_documents`, `contacts`, `contracts`, `conversations`, `engagements`, `entities`, `equipment_asset_states`, `equipment_assets`, `exercise_equipments`, `exercise_media`, `exercise_muscle_groups`, `exercises`, `fields`, `franchisee_locations`, `franchisees`, `goal_progress`, `goals`, `invoices`, `location_relations`, `locations`, `measurement_types`, `measurements`, `messages`, `metadata`, `notification_preferences`, `notifications`, `nutrition_checkin_values`, `nutrition_checkins`, `nutrition_plans`, `nutrition_target_types`, `nutrition_targets`, `oauth_authorizations`, `offers`, `pages`, `payment_transactions`, `payments`, `permissions`, `programs`, `proposals`, `questionnaire_answers`, `questionnaire_options`, `questionnaire_questions`, `questionnaire_sections`, `questionnaire_templates`, `questionnaires`, `session_credit_transactions`, `session_exercises`, `session_sets`, `sessions`, `tasks`, `test_types`, `trainer_availabilities`, `trainer_availability_exceptions`, `trainer_certifications`, `trainers`, `user_affiliations`, `user_locations`, `user_push_devices`, `users`, `workout_exercises`, `workouts`.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:608 -->

## Matrice d’adéquation fonctionnelle — hypothèses de travail

| Domaine MOVEE | Supports existants vérifiés par leur nom | Écart à instruire, sans présumer d’une table à créer | Questions |
|---|---|---|---|
| Identité et permissions | `users`, `permissions`, `entities`, `fields` | rôles multiples et droits centre/franchisé datés | Q001–Q006, Q089 |
| Centres et exploitation | `locations`, `cities`, `contracts` | exploitants successifs, satellites, périmètre siège/franchisé | Q001–Q007, Q025 |
| Adhérents et contrats | `contacts`, `offers`, `engagements` | rattachement centre, droits multi-centres, offres packs | Q004, Q011–Q012 |
| Réservations et crédit | `bookings`, `sessions`, `session_credit_transactions` | immobilisation, consommation, no-show, capacité machine | Q008–Q015, Q039–Q042 |
| Finances réseau | `invoices`, `payments`, `payment_transactions`, `commissions`, `commission_rules` | compensation interfranchises, ventilation, clôtures immuables | Q016–Q025, Q060–Q063 |
| Séances et programmes | `programs`, `workouts`, `workout_exercises`, `session_exercises`, `session_sets` | versions, télémétrie, fabricant, réglages, hors ligne | Q026–Q042 |
| Bilans et coachs | `assessments`, `measurements`, `trainers`, `trainer_availabilities` | équipement de bilan, coach assisté, contrats multiples | Q053–Q065 |
| Communications | `conversations`, `messages`, `notifications`, `notification_preferences` | routage externe, accusés fournisseur, audit | Q066–Q068 |
| IA et consentement | `proposals`, `contact_consents`, `consent_templates`, `oauth_authorizations` | mémoire contrôlée, capacités IA natives, modèles, audit | Q044–Q052, Q088–Q100 |
| Commerce et entreprise | `offers`, `contracts`, `invoices`, `payments` | marketplace, contrats B2B, reporting agrégé | Q112–Q116 |
| Exploitation et livraison | `tasks`, `configs`, `metadata` | pilotes, modules, maintenance et observabilité | Q072–Q085, Q117–Q129 |

**Limite de l’inventaire :** les supports historiques `contacts`/`trainers` ne remplacent pas l’identité cible `users`. La présence de tables/colonnes et permissions seedées ne prouve ni les parcours API, ni les invariants Services en exécution. Aucun support physique nommé `logs` n’est présent dans cet export ; le mécanisme réel d’observabilité reste à vérifier, sans créer de table par défaut.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:626 -->

## Interdictions et arbitrages

- Ne pas créer `clients` : `users` est l’identité cible et les rattachements datés aux centres portent le parcours commercial. Le registre historique `contacts` reste conservé comme source de migration non destructive ; il ne définit pas une seconde identité cible.
- Ne pas créer `organizations` : réseau unique ; distinguer cependant juridiquement les franchisés et leurs exploitations après analyse du besoin.
- Ne pas créer `sessions_remaining` : calculer depuis `session_credit_transactions`.
- Ne pas créer de table IA ad hoc : réutiliser `proposals` pour les propositions ; l’audit et les événements techniques devront faire l’objet d’une analyse séparée si la structure ne suffit pas.
- Le gel historique Entities 16–72 n’interdit pas de **proposer** un ajout strictement nécessaire, mais aucun ajout n’est validé sans justification, schéma, compatibilité et approbation.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:634 -->

## Étapes obligatoires avant migration

1. Identifier la règle Q et l’invariant non couvert.
2. Examiner les colonnes, clés, index, metadata et données pertinentes du schéma courant.
3. Examiner les Services/Repositories réels, un fichier à la fois.
4. Documenter alternatives sans migration, risque de régression, tests et plan de retour arrière.
5. Faire approuver séparément toute évolution SQL ; ne jamais exécuter sur production par défaut.



---

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:646 -->

## MOVEE — Modules, priorités et feuille de route


**Projet :** MOVEE App — référentiel de conception du 12 octobre 2026.  
**Statut :** documentation cible ; ni preuve d’implémentation ni autorisation de migration.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:652 -->

## Statut

Cette roadmap est une **proposition**, conformément à la section C du cadrage. Seules l’ambition différenciante de V1 (Q128), l’approche modulaire (Q124) et la validation des pilotes (Q125, Q129) sont des décisions métier ; la ventilation détaillée V1/V2/V3 n’est pas encore approuvée.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:656 -->

## V1 — capacité commerciale différenciante

| Lot | Objectif et livrables | Questions de référence | Critères de sortie |
|---|---|---|---|
| 0. Audit & contrats | Inventaire code, SQL, permissions, parcours, risques et fournisseurs | Q001–Q130 | aucun schéma inventé, gaps et décisions ouverts identifiés |
| 1. Réseau & identité | centres, exploitants datés, droits par périmètre, contacts et adhésions | Q001–Q007, Q089 | isolation des centres, historique fiable, tests de permissions |
| 2. Réservations & crédits | capacité, booking, réservations/consommations, annulations et no-show | Q008–Q015, Q039–Q042 | concurrence, idempotence, absence de double débit, tests métier |
| 3. Machines & séances | intégration pilote constructeur, authentification, événements, offline limité, programmes | Q026–Q042 | sécurité, déduplication, pannes, reprise et validation activité |
| 4. Coach IA & bilans | adaptation contrôlée, historique, bilan coach-assisté et parcours adhérent | Q029–Q033, Q043–Q057 | garde-fous, consentement, escalade, traçabilité |
| 5. Finance réseau minimale | encaissement central, répartition, compensation, clôture et audit | Q016–Q025 | rapprochement, périodes immuables, correctifs audités |
| 6. Pilotage & lancement | dashboards essentiels, observabilité, support, pilotes, sécurité et go/no-go | Q072, Q084–Q086, Q120, Q123–Q129 | critères chiffrés approuvés par siège, tests et décision humaine |

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:668 -->

## V2 — extension commerciale (proposition)

Communauté et événements (Q109–Q110), fidélité et parrainage enrichis (Q070–Q071, Q111), marketplace et SAV (Q112–Q115), offres entreprises et reporting RH agrégé (Q116), maintenance et opérations prédictives avancées (Q038, Q079–Q082), ainsi que fonctions complémentaires de coaching et de qualité. Les dépendances de sécurité, droit et contrats sont obligatoires dès l’introduction de chaque module.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:672 -->

## V3 — automatisation étendue (proposition)

Orchestration de workflows métier complexes par l’agent IA et leur création en langage naturel (Q094–Q096), optimisation multi-modèles et coûts (Q097–Q100), extension omnicanale/internationale (Q101–Q104), pilotage IA avancé du réseau (Q118–Q122) et modules complémentaires activables (Q127). Les garde-fous de l’agent IA nécessaires à V1 ne sont **pas reportés** en V3.

**Précision AR05.10 :** l’internationalisation mentionnée dans cette proposition ne reporte pas le multilingue mobile : interface, IA, notifications et contenus disponibles localisés sont requis dès V1 ; documents contractuels en versions officiellement validées seulement. Langues initiales et politique de repli restent à définir.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:678 -->

## Dépendances structurantes

- Centre/franchisé et droits datés avant calculs financiers et reporting multi-centres.
- Ledger et booking atomiques avant optimisation automatique des réservations.
- Événements machines fiables avant preuve d’achèvement et coaching adaptatif.
- Consentement, sécurité et politique de risque avant analyse vidéo ou action IA autonome.
- Contrats/PSP et conformité avant marketplace transactionnelle et B2B.
- Observabilité, tests et restauration avant généralisation à plusieurs centres.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:687 -->

## Gates de livraison

**G0 :** inventaire et arbitrages ; **G1 :** invariants Services et sécurité ; **G2 :** pilote machines/séances/crédits ; **G3 :** pilote financier et support ; **G4 :** pilote centres représentatifs ; **G5 :** approbation siège après seuils métiers/opérationnels/sécurité (Q129). Aucune IA ne lève automatiquement un critère bloquant.

## Annexe — chronologie historique, non applicable comme état courant

Les chiffres, ports, noms de versions et mentions « installé/non installé » de cette annexe décrivent leur date d’origine. Le point de reprise en tête du fichier et les contrats actuels priment pour déterminer les opérations disponibles. Cette annexe conserve la traçabilité ; elle n’autorise aucune action ni réactivation.

> **Historique daté, pas état courant.** Provenance : `movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:97`.

### Actualisation de l’état local — 21 octobre 2026

La conversation **Movee App Backend** est propriétaire de MOVEE App (`/Users/mbenmouha/Documents/Movee/movee-app`) : interface d’administration, API, identité/droits et règles opérationnelles réseau, adhérents, coachs, réservations, crédits et programmes ; orchestration IA et émission des notifications côté serveur. Mobile possède leur présentation iOS/Android ; Biz conserve ses propres prospects/franchisés, candidatures et simulations.

Le backend local et sa base V1 `movee_app_local` sont installés ; un administrateur initial a été provisionné. L’utilisateur a confirmé la connexion à l’interface web et la connexion du premier client mobile. **Ces constats ne valident pas les parcours métier, l’assistant IA, les notifications push ou la production.** La qualification des données et politiques reste à effectuer ; les décisions Q001–Q130/B1–B8/AR ne changent pas. Les preuves, paramètres, tests et limites sont consignés dans la section « Reprise sur le nouveau Mac » du référentiel technique de cette application.

---


**Consolidation du 17 octobre 2026 :** socle historique conservé, arbitrages validés AR01–AR07 et AR05.1–AR05.10 intégrés aux sections métier et techniques concernées. Ils précisent ou remplacent uniquement les formulations explicitement visées. Les autres décisions Q/B et les 78 décisions mobiles demeurent applicables. Les décisions sont des spécifications cibles, sans preuve supplémentaire d’API, d’implémentation, de recette réelle ou de déploiement. Les formats, paramètres, canaux externes et langues initiales non décidés restent à spécifier.

**Périmètre strict : MOVEE App.** Aucune source MOVEE Biz ou Body Motion n'a été utilisée.

**Statut :** référentiel fonctionnel canonique, non preuve de déploiement. Les 130 décisions Q001–Q130 et les arbitrages IA 2B sont intégrés dans ce seul document.

**Règle de lecture :** Q001–Q130 établit les décisions globales ; B1–B8 les précisent. En cas de divergence, signaler et synchroniser sans effacer la traçabilité. Les règles métier sont un index dérivé, non une source indépendante.

**Synchronisation Q011 — 16 octobre 2026 :** le registre Q011 et les règles métier sont alignés sur la décision B2 définitive : validité vérifiée à la réservation, crédits immobilisés et réservation confirmée préservée malgré leur expiration avant la séance. L'expiration ne supprime ni ne rend indisponibles les crédits déjà réservés. Les restitutions après annulation restent régies par B3. Cette règle remplace l'ancienne formulation imposant la validité à la date de la séance.

**Fiabilité IA 2B :** B1–B5 et B6.1–B6.60 sont des synthèses thématiques ; B6.61–B6.71, B7 et B8 sont restituées individuellement. Ne pas prétendre à une transcription exhaustive des questions B1–B6.


**Traçabilité des précisions :** AR01 remplace l’approbation coach systématique des adaptations supervisées par les validations selon limites préautorisées et consentement adhérent ; AR02 précise B8.2 pour l’écriture des programmes ; AR03 distingue centre contractuel et contexte actif ; AR04 résout l’exception Élevé aux heures calmes applicatives ; AR05 fixe les dix périmètres ; AR06 distingue historique durable, contexte éphémère et mémoire ; AR07 fixe acquisition externe, centralisation App et restitution Mobile. Les autres limites, permissions, validations sensibles, protections sportives et exigences de reprise restent conservées.

---

> **Historique daté, pas état courant.** Provenance : `movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:182`.

### Reprise sur le nouveau Mac — état vérifié le 21 octobre 2026

**Outils Apple : correction vérifiée le 21 octobre.** Command Line Tools sélectionnés ; Git et Homebrew fonctionnent normalement. Le blocage de licence signalé lors de l’installation de Xcode est résolu pour le développement courant. Xcode reste facultatif pour le parcours EAS cloud.

### Couche propriétaire et emplacement

- Dépôt : `/Users/mbenmouha/Documents/Movee/movee-app`.
- Conversation propriétaire : **Movee App Backend**. Responsabilités : interface web d’administration, API, authentification, règles métier, Services, Repositories, MariaDB, orchestration IA et émission serveur des notifications. MOVEE App est l’autorité métier, pas le client mobile.
- Interface web et API locales : `http://127.0.0.1:5050`. Flask est lancé sur la boucle locale, sans debugger ni reloader ; il ne s’agit pas d’un déploiement de production.
- Python Homebrew **3.13.16**, environnement recréé dans `venv/`, dépendances de `requirements.txt` installées ; `pip check` valide. L’environnement copié depuis l’ancien Mac n’est plus utilisé.

### Base et configuration effectives

- MariaDB **11.4.13**, boucle locale, port **3306**. Le service Homebrew a été activé au login ; état à vérifier après redémarrage.
- Base locale **`movee_app_local`**, compte non-root **`movee_local`@`127.0.0.1`**, privilèges limités à cette base. DBeaver est installé et l’utilisateur a confirmé voir la base.
- Import neuf autorisé : SCHEMA puis DATA canoniques ; 73 tables et 1 773 lignes de référence initiales vérifiées. Les valeurs ont été comparées au socle avant provisionnement du premier administrateur. Les données d’audit peuvent donc avoir évolué légitimement depuis ce contrôle.
- Premier administrateur créé par l’utilisateur avec [scripts/provision_initial_admin.py](../movee-app/scripts/provision_initial_admin.py). Lecture du 21 octobre : **1 utilisateur, 1 affiliation, 1 reçu `provisioning.initial_admin.v1`**. Ne pas réimporter la base ni rejouer ce provisionnement.
- Preflight réel en lecture seule : origine/niveau **V1**, `structural_prerequisites_satisfied=true`, `metadata_conform=true`, aucune migration en attente. **`data_ready=false` reste une limite métier**, pas une installation SQL à relancer ni une permission de supprimer/recréer la base.
- Configuration privée chargée par le code dans **`/Users/mbenmouha/Documents/Movee/.env`**, au-dessus du dépôt ; accès restreint. Ce fichier appartient à la couche Backend. Ne pas le déplacer vers `movee-app/.env` ni le remplacer par la configuration de Biz.
- Configuration locale vérifiée : `ENV=development`, `DB_ENGINE=mariadb`, `DB_HOST=127.0.0.1`, `DB_PORT=3306`, `DB_NAME=movee_app_local`, `MOVEE_NETWORK_ENABLED=1`, `MOVEE_MOBILE_ENABLED=1`, `MOVEE_ASSISTANT_ENABLED=0`. Cette activation sert au raccordement local de l’authentification ; elle ne qualifie pas les parcours métier du réseau.
- Redis **8.10.2**, processus local sur **127.0.0.1:6380**, `ASSISTANT_REDIS_URL=redis://127.0.0.1:6380/0`. `CONFIG GET` confirme `save` vide et `appendonly=no`. Le secret HMAC mobile dédié est configuré côté serveur, sans valeur reproduite ici.
- Redis et Flask sont des processus de développement à relancer après arrêt/redémarrage ; ne pas démarrer à leur place le service Redis standard avec une persistance implicite. Perdre Redis invalide les sessions mobiles.

### Contrats raccordés et vérifications datées

- Contrats mobiles existants : `POST /api/mobile-auth/login` (e-mail/mot de passe), `GET /api/mobile-auth/me` (Bearer), `POST /api/mobile-auth/logout` (Bearer et objet JSON vide).
- `login` retourne `success`, `token_type=Bearer`, `access_token`, `expires_at`, `user.user_id`, `user.full_name` ; `me` retourne l’identité et l’expiration. Le client ne déduit ni rôle ni droits depuis un simple succès de connexion.
- Tests isolés exécutés le 21 octobre : **358 recensés, 355 réussis, 3 Redis ignorés**. Les **3 tests Redis ont ensuite réussi séparément** sur une instance éphémère isolée, sans clé restante, arrêtée après test. Ce n’est pas une exécution unique de 358 tests avec Redis.
- MariaDB réelle : démarrage, connexion, import V1 et reconnaissance structure/metadata vérifiés. Cela ne remplace pas la recette des transactions, concurrence, compensations et invariants métier sur MariaDB.
- Connexion à l’interface web puis connexion Mobile→API confirmées par l’utilisateur sur le navigateur du Mac. Aucun test sur téléphone ni appel OpenAI réel attesté.
- Restent à qualifier : données/politiques métier, parcours adhérent/coach, API classiques indépendantes de l’IA, intégration OpenAI, fournisseur push, appareils physiques et déploiement. L’assistant est désactivé ; ne pas présenter la connexion comme une livraison des réservations/programmes/IA.

### Reprise

Commandes de lancement et de test, état des outils Apple et règles de secrets : [environnement du Mac](../docs/ENVIRONNEMENT_DEVELOPPEMENT_MAC.md). Ne pas lancer de migration, de worker, de provisioning ou de connexion au VPS en reprenant une conversation sans l’autorisation correspondant à l’opération et à sa cible.

### Règle de séparation des conversations

Cette conversation travaille exclusivement dans le dépôt indiqué ci-dessous. Les deux référentiels de ce même dépôt et [codex/AGENTS.md](AGENTS.md) font autorité dans leur périmètre. Les autres dépôts peuvent être consultés en lecture seule pour vérifier un contrat ; une évolution nécessaire dans une autre couche doit être décrite comme demande d’intégration à transmettre à sa conversation, sans y modifier du code, de configuration ou de SQL. Ne pas copier une règle, un schéma ou un Service d’une application à l’autre. Le compte administrateur de test ne valide pas les parcours adhérent/coach.

Les anciens chemins `/Users/mehdi.benmouha/Documents/Projects/newapp/...` désignent l’ancien Mac ; les chemins de travail actuels sont sous `/Users/mbenmouha/Documents/Movee`. Les sections historiques et résultats antérieurs restent datés ; l’état local ci-dessous ne prouve aucun déploiement sur le VPS.

---


**Consolidation du 17 octobre 2026 :** socle historique conservé, arbitrages validés AR01–AR07 et AR05.1–AR05.10 intégrés aux sections métier et techniques concernées. Ils précisent ou remplacent uniquement les formulations explicitement visées. Les autres décisions Q/B et les 78 décisions mobiles demeurent applicables. Les décisions sont des spécifications cibles, sans preuve supplémentaire d’API, d’implémentation, de recette réelle ou de déploiement. Les formats, paramètres, canaux externes et langues initiales non décidés restent à spécifier.

**Périmètre strict : MOVEE App.** Aucun document MOVEE Biz ou Body Motion.

**Statut :** architecture cible, baseline SQL V1 et roadmap **proposée** ; état de livraison IA 2B actualisé au 16 octobre 2026. Aucun des éléments ci-dessous ne prouve qu'un Service, une migration ou une fonctionnalité est déployé.

**Arbitrage d'intégration actualisé :** applications mobiles iOS et Android développées et maintenues en interne → API Flask → Services → Repositories → MariaDB. Agent IA natif et orchestration OpenAI côté Flask, via un registre fermé de capacités métier. Expo sert au développement et aux tests initiaux, sans verrouiller la cible mobile. Les API métier peuvent également appeler les Services directement ; aucun protocole intermédiaire d'outils n'est prévu.

**SQL :** les sources canoniques sont [sql/MOVEE_APP_SQL_SCHEMA.sql](../movee-app/sql/MOVEE_APP_SQL_SCHEMA.sql) et [sql/MOVEE_APP_SQL_DATA.sql](../movee-app/sql/MOVEE_APP_SQL_DATA.sql) : baseline V1 complète, 73 tables, 1234 colonnes, 695 index nommés (PK incluses), 123 FK, 57 CHECK et 1773 lignes de référence, sans utilisateur. La reconstruction indépendante sur `newapp` a été validée par comparaison physique et des valeurs sélectionnées à `newapp_sql_test`. Aucun SQL n'est rejoué pendant le nettoyage du dépôt. Voir [sql/README.md](../movee-app/sql/README.md) pour l'installation et les contrôles.

**Identité :** la cible MOVEE est `users` unique ; les tables historiques `contacts`/`trainers` demeurent dans l'inventaire exporté et servent à la migration non destructive. Ne pas interpréter leur présence comme une identité cible distincte.

**Planification :** la ventilation V1/V2/V3 reste une proposition non approuvée, malgré les exigences V1 validées.


**Traçabilité des précisions :** AR01 remplace l’approbation coach systématique des adaptations supervisées par les validations selon limites préautorisées et consentement adhérent ; AR02 précise B8.2 pour l’écriture des programmes ; AR03 distingue centre contractuel et contexte actif ; AR04 résout l’exception Élevé aux heures calmes applicatives ; AR05 fixe les dix périmètres ; AR06 distingue historique durable, contexte éphémère et mémoire ; AR07 fixe acquisition externe, centralisation App et restitution Mobile. Les autres limites, permissions, validations sensibles, protections sportives et exigences de reprise restent conservées.

---

> **Historique daté, pas état courant.** Provenance : `movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:244`.

### Architecture mobile et contrats conversationnels — décision actuelle

### Pages mobiles en lecture — lot du 23 octobre 2026

Le moteur `pages` sert aussi les parcours classiques mobiles validés dans le
référentiel fonctionnel. Le premier lot ajoute un transport Bearer dédié,
indépendant de l'assistant : `GET /api/mobile-pages`, et
`POST /api/mobile-pages/config`, `/data`, `/record`. Les lectures réutilisent
l'hydratation Page, les Services/Repositories génériques, les scopes métier et
les Services spécialisés Program/Performance pour les contenus détaillés.
Le contexte mobile est lié explicitement aux Services et Repositories ; aucun
cookie web ne fournit l'identité de ces appels.

Publication explicite seulement : `page_config.mobile_read=1`, types liste/fiche
et entités réservations/programmes/séances dans ce lot. Aucun HTML, endpoint ou
script de Page n'est exécuté par le mobile ; aucune action d'écriture n'est
publiée par ce transport. Les routes Front et OAuth restent distinctes.

Les six définitions liste/fiche sont préparées dans
[[docs/mobile_pages_v1.json](../movee-app/docs/mobile_pages_v1.json)](../movee-app/docs/mobile_pages_v1.json), avec les quatre
autorisations de liste programme/séance manquantes dans le seed V1 pour les
rôles coach/adhérent. **Ce fichier n'est pas chargé automatiquement. Son
installation locale sur `movee_app_local` a été explicitement autorisée puis
exécutée le 23 octobre 2026** ; aucune autre base n'a été modifiée.
Toute installation reste une opération de données distincte, avec contrôle
des refus explicites et des définitions existantes.
Aucune baseline ni empreinte SQL V1 n'est modifiée.

La préparation de l'installation est disponible dans
[scripts/install_mobile_pages.py](../movee-app/scripts/install_mobile_pages.py) : contrôle hors ligne par défaut, `--plan-db`
en lecture seule, et mode d'application locale avec cible, acteur siège et
empreinte du paquet explicitement confirmés. Le Service réutilise les primitives
Repository de préflight/verrou/transaction, refuse les conflits et ajoute
uniquement les lignes manquantes ; un rejeu identique est sans effet. Les refus
individuels sont conservés. Aucun mode `force`, mise à jour ou suppression.
L'existence de cette commande n'autorise pas son exécution en écriture.
Préparation vérifiée : le plan local en lecture seule annonce six insertions
dans `pages` et quatre dans `permissions`, sans conflit. Suite après ajout de
l'installateur : **379 tests recensés, 376 réussis, 3 Redis ignorés** (71,228 s).
Les sept tests supplémentaires utilisent SQLite isolé et un catalogue MariaDB
simulé ; ce résultat isolé précède l'installation réelle décrite ci-dessous.

**Installation locale ensuite réalisée après accord explicite :** six Pages,
IDs 91–96, et quatre permissions ajoutées dans une transaction MariaDB.
Totaux : 55 Pages et 65 permissions. Les enregistrements préexistants de
`pages`, `permissions`, `users`, `user_affiliations` et `configs` ont été comparés
avant/après et préservés. Plan post-installation conforme ; rejeu réel sans
insertion ni modification. Le paquet conserve l'empreinte
`2d4f9a3ed2bd6f594a7ee8a2adf8585142a88b96341895fd61333aa627cb8649`.
Contrôle complémentaire des Services en lecture seule sur MariaDB : trois
Pages de liste publiées, six configurations liste/fiche lisibles, trois listes
vides sans erreur pour l'administrateur. Cela valide l'installation des
métadonnées et ces lectures, pas les transactions métier de réservation,
la recette adhérent/coach, le transport HTTP/Redis ou le rendu natif Mobile.

Contrat, exemples, critères de recette et limites :
[[docs/MOBILE_PAGES_CONTRACT.md](../movee-app/docs/MOBILE_PAGES_CONTRACT.md)](../movee-app/docs/MOBILE_PAGES_CONTRACT.md).

Préparation de la recette du même lot :
[[docs/MOBILE_PAGES_ACCEPTANCE.md](../movee-app/docs/MOBILE_PAGES_ACCEPTANCE.md)](../movee-app/docs/MOBILE_PAGES_ACCEPTANCE.md) et
[[docs/MOBILE_PAGES_HANDOFF.md](../movee-app/docs/MOBILE_PAGES_HANDOFF.md)](../movee-app/docs/MOBILE_PAGES_HANDOFF.md).
Contrôle local en lecture seule : aucun coach/adhérent actif, centre ou objet
sportif de recette ; seul l'administrateur initial et son affiliation sont
présents. Le jeu synthétique décrit est proposé, non créé. La consigne Mobile
est un fichier à transmettre par l'utilisateur, sans message envoyé à un chat.

Retour Mobile ensuite transmis par l'utilisateur : raccordement Pages v1
déclaré, autres contrats toujours ouverts. Défaut navigateur CORS confirmé et
corrigé dans `app.py` : ajout de `Authorization` aux headers autorisés et
exposition de `Retry-After`, par le filtre commun aux préflights et réponses.
La politique d'origine existante reste inchangée (développement ouvert,
production limitée à `CORS_ORIGINS`), sans cookies d'identité ni exposition aux
origines refusées en production. Cinq tests ciblés isolés couvrent les sept
routes Pages/auth, succès Bearer, erreurs et quota. La recette Expo web sur le
serveur réel reste distincte ; aucun service relancé ni donnée modifiée pour
ce correctif. Voir le contrat Pages et le complément de consigne Mobile.
Suite complète après correctif CORS : **384 tests recensés, 381 réussis,
3 Redis ignorés** (74,311 s) ; `git diff --check` conforme. Aucun déploiement.

**Démarrage local ensuite autorisé et effectué le 23 octobre :** Redis 6380
sans persistance et Flask 5050 sans debug/reloader, code CORS corrigé chargé.
Contrôles HTTP réels : sept préflights Pages/auth conformes ; cinq identifiants
invalides sur une adresse de sonde fictive ont renvoyé 401 puis la sixième
tentative 429, avec `Retry-After=53` exposé. Aucune identité créée pour cette
sonde ; uniquement des quotas éphémères Redis, sans suppression de clés.
L'assistant est resté désactivé. Les comptes et données de recette sont
préparés dans [[docs/MOBILE_PAGES_ACCEPTANCE_DATA_PLAN.md](../movee-app/docs/MOBILE_PAGES_ACCEPTANCE_DATA_PLAN.md)](../movee-app/docs/MOBILE_PAGES_ACCEPTANCE_DATA_PLAN.md)
et son manifeste : 48 insertions proposées, contrôlées sur SQLite isolé et
64 FK canoniques vérifiées, non appliquées à MariaDB. Le navigateur et les
consultations HTTP réelles adhérent/coach restent à recetter.

**Après autorisation distincte, jeu synthétique appliqué :** 48 insertions
conformes au manifeste, dont cinq comptes de test et deux centres. Chargeur
local [scripts/provision_mobile_pages_acceptance.py](../movee-app/scripts/provision_mobile_pages_acceptance.py), aucun accès API/MCP.
Toutes les lignes préexistantes des 73 tables sont préservées ; rejeu réel
sans insertion ni modification. Secrets générés dans un fichier privé 0600
hors dépôt, jamais dans le manifeste, les reçus ou les messages.
Recette HTTP réelle : 81 appels, cinq profils, catalogue/listes/fiches,
refus interutilisateur/intercentre et clinique, déconnexion et décimaux exacts.
Assistant désactivé. Suite complète après ajout du chargeur : **390 tests,
387 réussis, 3 Redis ignorés** (82,582 s).
Le [rapport de résultat](../movee-app/docs/MOBILE_PAGES_ACCEPTANCE_RESULT.md) précise
les comptes et limites : navigateur et rendu natif non recettés, pas de
qualification commerciale/IA2B, `data_ready=false` inchangé comme limite métier.

Vérification du lot : suite isolée **372 tests recensés, 369 réussis,
3 Redis ignorés** (64,806 s). Les 14 nouveaux tests couvrent le transport et
les lectures Pages. Contrôle complémentaire MariaDB en transaction lecture
seule : 17 champs de configuration conformes, catalogue mobile vide avant
installation, compilation des scopes vides valide. Aucun appel OpenAI, worker,
écriture MariaDB, installation de Page, déploiement ou modification Mobile.
Ces résultats ne valident pas encore la recette métier InnoDB ni le rendu natif.

### Rappel de la cible conversationnelle

La cible est une **application mobile iOS et une application mobile Android développées et maintenues par l’équipe MOVEE**. **Expo sert uniquement de solution initiale de développement/test**, sans préjuger de la technologie finale de chaque application. Le backend doit rester indépendant du client mobile. Les composants de conversation incluent messages, consultations, résultats structurés, alternatives et cartes de confirmation ; les parcours classiques doivent rester utilisables sans IA, sauf création/modification de programmes exclusivement via IA (AR02) ; leur consultation reste disponible sans IA.

- **Transport :** API Flask authentifiée, contexte de droits, contrats versionnés et validations côté serveur.
- **Agent IA :** orchestration OpenAI serveur, capacités natives fermées et filtrées par permissions et activation de centre ; aucune action metadata automatiquement exposée.
- **Exécution :** Services métier dédiés pour les invariants, confirmations et transactions ; Repositories pour la persistance ; modèle sans accès SQL direct.
- **Reprise :** commandes et reçus durables dans `proposals`, état de réservation dans `bookings`, mouvements de crédit dans `session_credit_transactions` ; idempotence et contrôle de concurrence.
- **Proactivité :** messages d’accueil contextuels pour coach et adhérent, plus Push sur téléphone hors application sous préférences et consentements ; ne jamais présenter l’outbox comme une livraison effective.
- **Notifications :** inscription/révocation des appareils, chiffrement des tokens et worker codés ; fournisseur mobile natif non sélectionné/raccordé. Choisir le fournisseur sans coupler durablement l’API au client Expo.

---

> **Historique daté, pas état courant.** Provenance : `movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:368`.

### État réel du chantier IA 1 / IA 2A / IA 2B (16 octobre 2026)

| Bloc | Livré en code selon rapports | Non validé / limite |
|---|---|---|
| IA 1 | Auth mobile, conversations Redis, orchestration OpenAI et première consultation | Redis et OpenAI réels non recettés |
| IA 2A | Consultations de réservation/programme/performance, saisie de séries, permissions et confirmation préparée | Permissions SQL intégrées à V1 ; recette métier réelle non attestée |
| IA 2B A | Disponibilités, réservation, crédits, coach, annulations, dérogations, compensations | Qualification des historiques, politiques réelles et MariaDB |
| IA 2B B–C | Adaptations, restrictions, douleur, réévaluations et synthèses | Parcours complets de séance/machines et données historiques non attestés |
| IA 2B D | Appareils, sécurité Push, outbox, worker, reprises et expirations | Fournisseur Push réel, scheduler et tests terminaux |

**Résultats historiques déclarés par le rapport consolidé IA 2B (avant validation SQL isolée) :** 245 recensés, 242 réussis, 0 échec, 3 ignorés (Redis réel). 34 tests ciblés supplémentaires ont été rejoués ; ne pas les additionner. **Verdict CODE PARTIAL.** À la date de ce rapport historique, aucun SQL exécuté ni environnement réel validé ; voir ci-dessous la validation SQL isolée ultérieure. Ces résultats ne constituent toujours pas une recette Redis/OpenAI/Push ni un déploiement.

**Couverture :** Q001–Q130 et B1–B8 sont les décisions cible, pas un inventaire de fonctions opérationnelles. Les limites de réorganisation hebdomadaire, politiques commerciales, données historiques, calendrier de publication et cycle complet des séances demeurent explicites. Le phasage V1/V2/V3 reste proposé, sauf arbitrages validés.

---

> **Historique daté, pas état courant.** Provenance : `movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:382`.

### Exploitation et reprise — informations conservées après archivage (16 octobre 2026)

Les onze rapports déplacés sont indexés dans [docs/archive/README.md](../movee-app/docs/archive/README.md). Ils restent historiques : les anciennes propositions PWA, transports MCP, questions B1–B8 et résultats de tests de chaque livraison ne remplacent ni les décisions fonctionnelles actuelles ni l’état du code. Cette conservation historique ne modifie pas les autres règles Q001–Q130/B1–B8 ; les précisions AR01–AR07 et l’exception AR02 à B8.2 sont intégrées dans leurs sections.

### État SQL attesté et limites

Les validations antérieures sur `newapp_sql_test` (MariaDB 11.4.12) ont confirmé MOVEE001–004, IA2A001–002 et IA2B001–007, les 420 conditions du postflight corrigé, les treize marqueurs et les 61 permissions. La reconstruction V1 sur `newapp` est ensuite passée, avec les transformations de référence documentées dans [sql/baseline/SELECTION_MANIFEST.json](../movee-app/sql/baseline/SELECTION_MANIFEST.json). Ces constats ne valent ni activation, ni déploiement, ni recette métier de phase C. Aucune connexion MariaDB pendant cette consolidation ; les bases existantes ne doivent pas être réimportées.

### Installation et migrations après V1

Installer une base neuve explicitement autorisée avec SCHEMA puis DATA uniquement, sans ancienne chaîne de migrations, FK/CHECK actifs et arrêt à la première erreur. Les gardes des fichiers canoniques refusent `newapp`, `newapp_dev` et `newapp_sql_test`. Le seed inclut déjà les 61 permissions : ne pas les réinsérer. Il ne contient ni personne, ni ancien marqueur, ni activation métier ; son seul marqueur est `schema.baseline.version=MOVEE_APP_V1`. Le SCHEMA comporte des DDL implicitement committés : aucun rollback global ni reprise automatique ne sont promis.

[scripts/baseline_v1.py](../movee-app/scripts/baseline_v1.py) vérifie empreintes, valeurs et contrat physique autonome [sql/baseline/V1_STRUCTURE.json](../movee-app/sql/baseline/V1_STRUCTURE.json). [scripts/check_sql_packages.py](../movee-app/scripts/check_sql_packages.py) contrôle hors ligne cette baseline, sans ancien paquet. Les fixtures SQLite utilisent directement ce socle puis créent leurs utilisateurs et données opérationnelles ; elles ne prouvent pas le comportement MariaDB.

Le runner local [scripts/movee_migrate.py](../movee-app/scripts/movee_migrate.py), le Service et le Repository communs reconnaissent soit le marqueur V1 neuf, soit les treize marqueurs historiques exacts de [sql/baseline/HISTORICAL_ORIGINS.json](../movee-app/sql/baseline/HISTORICAL_ORIGINS.json), toujours avec signature physique et metadata conformes. Refuser origines mixtes, états partiels, empreintes divergentes et marqueurs incohérents. Les quinze paires CHECK revues sont comparées strictement, sans normalisation globale ; seules les largeurs d'affichage entières et les compteurs AUTO_INCREMENT sont ignorés lorsqu'ils ne modifient pas la structure.

Le registre [sql/migrations/manifest.json](../movee-app/sql/migrations/manifest.json) est vide. Les futurs deltas communs aux deux origines devront porter empreinte SQL, contrats physiques et metadata et marqueur `schema.migration.<id>`, sans réécrire l'historique. Le runner actuel est en lecture seule et refuse les anciennes options d'écriture ; aucun exécuteur de delta n'est activé. Voir [contrat des futurs deltas](../movee-app/sql/migrations/README.md).

Le premier Admin relève uniquement de [scripts/provision_initial_admin.py](../movee-app/scripts/provision_initial_admin.py), commande locale sans route publique, sans connexion par défaut. Après autorisation distincte : cible explicite, baseline V1 conforme, zéro utilisateur/affiliation/reçu, verrou et transaction, hachage existant, affiliation siège fixe et reçu atomique. Toute seconde exécution est refusée. Aucun provisionnement réel n'est réalisé par ce nettoyage. Les paramètres et limites sont dans [sql/README.md](../movee-app/sql/README.md).

Les anciens SQL et leurs adaptations sont sauvegardés hors Git dans une archive privée vérifiée, car ils contiennent des données personnelles. Les noms `source` du manifeste historique sont des preuves de provenance, sans dépendance aux chemins supprimés. Les rapports de [docs/archive/](../movee-app/docs/archive) restent historiques, non des instructions actives. La qualification des politiques et historiques reste requise : `data_ready=false` n'indique pas une migration manquante. Redis/OpenAI/Push et la recette métier réelle restent distincts de la validation SQL.

### Authentification mobile, API et confirmations

L’authentification mobile existante utilise des tokens opaques mv1_, stockés sous forme de digest dans Redis avec expiration absolue. Elle reste distincte des cookies Front et d’OAuth ; ces transports ne remplacent pas le Bearer mobile. Le contexte serveur relit l’utilisateur, les habilitations et les scopes actuels ; une modification des credentials ou une désactivation invalide les anciens tokens. Aucun secret OpenAI n’est envoyé au client.

Contrats backend à conserver : POST /api/mobile-auth/login (email/password), GET /api/mobile-auth/me, POST /api/mobile-auth/logout ; POST /api/assistant/message et /api/assistant/reset. Le message porte conversation_id, request_id, expected_revision et message ; les actions ajoutent la soumission structurée action_input. Les schémas fermés et composants sont définis dans les API/helpers courants, pas dans les anciens plans. Les reçus et composants proviennent des Services ; aucun succès d’écriture n’est inféré du seul texte du modèle.

IA2A conserve les consultations bookings/program/performance et record_session_set. L’API classique POST /api/business-actions/record-session-set partage le Service de saisie. La clé naturelle de série et les permissions actuelles gouvernent les rejeux. Les mesures ne sont pas inventées et une ambiguïté exige clarification. IA2B expose POST /api/business-actions/ia2b/<operation> avec command_id/arguments, /api/business-actions/ia2b-confirm avec proposal_id/request_hash/decision et /api/business-actions/ia2b-result avec operation/command_id. Les paramètres exacts restent ceux du registre fermé et du code ; aucune Action metadata n’est automatiquement publiée.

Les confirmations sensibles sont liées au sujet, aux paramètres, à leur empreinte et à leur expiration ; les droits sont revérifiés lors d’un rejeu. Redis porte le contexte temporaire, pas la preuve durable d’une écriture IA2B : proposals conserve commandes/consentements/reçus et le ledger conserve les mouvements dans la transaction métier. Après commit avec perte de contexte Redis, le reçu peut rester disponible avec context_saved=false ; réinitialiser le contexte plutôt que répéter l’effet métier. Les séries et prescriptions historiques ne sont pas réécrites silencieusement.

### Configuration et exploitation

- MOVEE_NETWORK_ENABLED et MOVEE_ASSISTANT_ENABLED sont des opt-in distincts, désactivés par défaut. La disponibilité du schéma ne les active pas ; une configuration complète et une qualification des données restent nécessaires.
- Configuration IA/mobile : OPENAI_API_KEY, OPENAI_MODEL, ASSISTANT_REDIS_URL, MOBILE_AUTH_HMAC_SECRET dédié (au moins 32 caractères), limites ASSISTANT_* / MOBILE_AUTH_*. Les noms, valeurs par défaut et validations effectives sont dans config.py ; ne pas reprendre les valeurs d’un ancien plan comme configuration de production.
- HTTPS est requis en production. ASSISTANT_TRUSTED_PROXY_IPS ne contient que les proxies effectivement maîtrisés, écrasant X-Forwarded-Proto ; aucun header client n’est une preuve de transport sécurisé. Accès direct au serveur applicatif et timeouts HTTP/proxy à contrôler avant déploiement.
- Redis doit être privé et temporaire, sans persistance des conversations par AOF/RDB/sauvegarde. Sa perte invalide tokens/contextes et peut réinitialiser les quotas ; il ne constitue pas un journal durable de facturation. Quotas d’appels et consommation mesurée ne garantissent pas un plafond monétaire ; une consommation inconnue après timeout n’est pas un coût nul. store=false ne prouve pas une absence de rétention fournisseur.
- scripts/ia2b_worker.py est un point d’entrée de maintenance à conserver : expire-proposals, review-reminders, review-summary et push-delivery. L’exécution exige --execute et MOVEE_IA2B_WORKER_ENABLED=1 ; les opérations autorisées exigent un acteur courant et, selon le contrat, des arguments et command_id. Aucun scheduler ni compte privilégié n’est installé automatiquement. push-delivery reste fermé tant que le fournisseur n’est pas raccordé.
- Push : tokens privés chiffrés AES-GCM, empreintes HMAC, préférences et révocations ; les clés et paramètres exigés restent ceux du Service courant, sans secret par défaut. Une rotation HMAC nécessite une stratégie explicite de déduplication/réinscription. Une ligne outbox ou une acceptation fournisseur ne prouve pas une réception téléphone.

**AR04 — Push immédiat pour alerte de sécurité Élevé.** Exception aux heures de tranquillité configurées dans MOVEE, mais **jamais** aux refus/autorisations/restrictions iOS/Android ; émission ≠ livraison garantie. Les autres notifications respectent les préférences.

**Sécurité/push :** niveau Élevé établi par App, priorité et exception aux heures de tranquillité MOVEE, préférences ordinaires, permissions OS, identifiant d'événement, tentatives et état de livraison distincts.

**AR06 — Historique IA durable et mémoire sélective.** Historique, contexte éphémère et mémoire personnalisée distincts ; contrôle de consultation/correction/suppression et vérification des droits à chaque accès. Les données métier officielles demeurent dans MOVEE App.

**Conversation :** identité de fil, pagination et reprise de l'historique durable, isolation des droits, mémoire sélective corrigible/supprimable, règles de rétention et de minimisation ; stockage physique à vérifier avant toute proposition SQL.

La non-persistance Redis documentée concerne les tokens, quotas et le contexte IA éphémère du mécanisme actuel ; elle ne satisfait pas à elle seule l’historique IA durable validé par AR06. La persistance durable du fil et le cycle de vie de sa mémoire doivent être contractualisés sans présumer l’usage des tables de messagerie humaine ni proposer de table nouvelle avant vérification.

### Tests à reprendre et travaux non validés

Commande des tests isolés, sans lecture de la configuration applicative :

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHON_DOTENV_DISABLED=1 MOVEE_ASSISTANT_ENABLED=0 \
OAUTH_ISSUER=https://newapp.test OAUTH_RESOURCE=https://newapp.test/mcp \
CORS_ORIGINS=https://inspector.test ./venv/bin/python -B -m unittest discover -s tests -v
```

Les fixtures SQLite, Redis mémoire et clients OpenAI simulés ne valident pas MariaDB, Redis multi-processus ou OpenAI réel. Les tests Redis réels exigent MOVEE_TEST_REDIS_URL et MOVEE_TEST_REDIS_EPHEMERAL=1 sur une instance isolée ; ils ne doivent pas utiliser le Redis applicatif. Leur absence impose un statut ignoré, pas PASS.

Restent à recetter séparément : transactions et concurrence métier InnoDB, qualification des données et politiques réelles, Redis multi-workers, OpenAI réel et paramètres de rétention/région, VPS/Gunicorn/proxy, application mobile et confirmations sur appareils. Push fournisseur n’est pas raccordé. Les parcours machines et le cycle complet Session ne sont pas attestés terminés ; aucune date historique inconnue ni valeur commerciale ne doit être fabriquée pour les activer. Les protections sportives ne sont pas levées par simple clôture/contestation ; aucune réouverture automatique de demande close n’est déclarée livrée.

---

> **Historique daté, pas état courant.** Provenance : `movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:587`.

### Réalisation chantier 1 — phase B

Les Services réseau/affiliations et scopes MOVEE sont présents dans le code ; leurs structures sont intégrées à la baseline V1. L'activation via MOVEE_NETWORK_ENABLED reste distincte de l'installation SQL et exige la recette et la qualification métier. Aucun déploiement n'est attesté par cette consolidation.


---

---

> **Historique daté, pas état courant.** Provenance : `movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:691`.

### Registre des décisions de planification

Pour chaque Q001–Q130, l’affectation finale de version reste **à valider**, même si le domaine figure dans un lot proposé. Les décisions ne disparaissent pas lorsqu’elles sont différées.


### Raccordement des consultations au moteur web — 25 octobre 2026

Les Pages installées 91–96 servent aussi l'administration web : entrées de menu
calculées selon les permissions, listes génériques existantes, ouverture des
fiches en modale et contenu programme/résultats via `GET /api/page-read-record`.
L'adaptateur [services/web_read_page_service.py](../movee-app/services/web_read_page_service.py) réutilise le lecteur Pages et les
Services métier existants ; seuls les contextes session/OAuth sont acceptés.
Le transport mobile garde son exigence de Bearer mobile. Les contrôles de scope
et permissions enfants demeurent applicables. Aucun SQL, changement des six
métadonnées installées, droit supplémentaire ou écriture métier n'est introduit.
Détails et limites de recette : [docs/MOBILE_PAGES_CONTRACT.md](../movee-app/docs/MOBILE_PAGES_CONTRACT.md), rubrique du
25 octobre. La recette graphique web reste distincte des tests de lecture API.
Validation après raccordement : 394 tests, 391 réussis, 3 Redis ignorés
(85,111 s) ; 13 lectures HTTP locales administrateur réussies sur MariaDB.

### Préparation ajout/annulation Mobile — 25 octobre 2026

Contrat vérifié des opérations métier existantes et compléments **proposés, non
implémentés** : [docs/MOBILE_BOOKING_ACTIONS_CONTRACT.md](../movee-app/docs/MOBILE_BOOKING_ACTIONS_CONTRACT.md). Les choix libellés,
actions/version, aperçu sans effet lié à la soumission et récupération des accords
initiés par coach manquent au parcours Mobile complet. Une soumission existante
peut appliquer immédiatement l'action ; elle ne sert pas d'aperçu.

[docs/MOBILE_BOOKING_ACTIONS_DATA_PLAN.md](../movee-app/docs/MOBILE_BOOKING_ACTIONS_DATA_PLAN.md) et [docs/mobile_booking_actions_plan.json](../movee-app/docs/mobile_booking_actions_plan.json)
préparent sept scénarios (un conditionnel), sans appliquer de données. Inspection
locale READ ONLY : schéma IA2B présent mais aucune politique de réservation, crédit
ou inventaire ; historiques non qualifiés. Valeurs métier et écritures demeurent
à approuver. Deux nouveaux centres/périmètres de recette sont proposés pour ne
modifier aucune ligne préexistante ; aucun nouveau compte/droit prévu.
16 tests Booking/intégration réussis sur SQLite isolé et huit échanges HTTP isolés
capturés dans [docs/mobile_booking_actions_examples.json](../movee-app/docs/mobile_booking_actions_examples.json). Aucun test d'écriture
MariaDB, aucune activation IA/push/worker, aucun changement applicatif ou restart.

La demande utilisateur ultérieure autorise la **proposition** d'une politique
fictive de recette autonome, pas son application. Voir
[docs/MOBILE_BOOKING_ACTIONS_LOCAL_POLICY_PROPOSAL.md](../movee-app/docs/MOBILE_BOOKING_ACTIONS_LOCAL_POLICY_PROPOSAL.md) et le plan révision 2 :
7 bookings, 36 crédits et 66 ajouts prévisionnels, nouveaux périmètres adhérents
seulement. Les valeurs proposées ne constituent ni une décision commerciale ni
des défauts de production. Cinq comportements contrôlés sur SQLite isolé ; aucune
mutation MariaDB ni modification du code applicatif pour cette proposition.

Validation utilisateur du 25 octobre 2026 reçue pour la politique fictive locale,
les 36 crédits et le périmètre autonome révision 2 (66 ajouts prévisionnels).
Paramètres désormais consignés comme validés dans le manifeste. Application
MariaDB toujours non autorisée : préparation/test du chargeur et revue du plan
résolu restent nécessaires. Aucun service ni donnée métier modifié.

Chargeur local autonome préparé après demande explicite :
[scripts/provision_mobile_booking_actions.py](../movee-app/scripts/provision_mobile_booking_actions.py) (hors ligne par défaut, `--plan-db`
READ ONLY, application sous confirmations séparées) et Service
[services/mobile_booking_actions_loader.py](../movee-app/services/mobile_booking_actions_loader.py). Manifeste validé épinglé ; simulation
sur projection V1 en mémoire depuis les données locales, 66 ajouts exacts.
Plan lisible/JSON dans [docs/MOBILE_BOOKING_ACTIONS_RESOLVED_PLAN.md](../movee-app/docs/MOBILE_BOOKING_ACTIONS_RESOLVED_PLAN.md) et
[docs/mobile_booking_actions_resolved_plan.json](../movee-app/docs/mobile_booking_actions_resolved_plan.json) : dates, IDs prévisionnels non
réservés, empreinte, contrôles de source/préservation, rejet d'un plan périmé,
rejeu sans réparation des bookings modifiés ultérieurement. Début des nouveaux
états machine à T+11 minutes explicitement soumis à revue (pas d'antidatation).
Suite : 403 tests, 400 réussis, 3 Redis ignorés (97,047 s), dont neuf nouveaux tests.
Contrôle final MariaDB READ ONLY : 73 tables inchangées, reçu absent. Backend seul
redémarré par movee-dev ; aucun --execute lancé, aucune donnée métier appliquée.
Les futurs contrats d'aperçu/choix/actions Mobile restent un lot distinct.

### Application locale explicitement autorisée — 25 octobre 2026

Plan SHA256 `2c231e674de2748823627c3383b1f0b3cc24499521e08fed491bc2ad5476c52d`
appliqué dans sa fenêtre de validité : 66 ajouts, 36 crédits (6 immobilisés,
30 disponibles). Anciennes lignes des 73 tables vérifiées inchangées en READ ONLY.
Rejeu réel : zéro insertion, mêmes IDs, nouvelle vérification de préservation.
Centres 3/4 ; bookings 4–10, dont 8 déjà annulé gratuitement. Aucun redémarrage
de service, login HTTP ou activation IA/push/worker. Rapport :
[docs/MOBILE_BOOKING_ACTIONS_APPLICATION_RESULT.md](../movee-app/docs/MOBILE_BOOKING_ACTIONS_APPLICATION_RESULT.md) dans le dépôt Backend.
Les compléments API et boutons Mobile restent distincts, non livrés par ce lot.

### Compléments Mobile réservation livrés — 25 octobre 2026

Contrat actif [docs/MOBILE_BOOKING_ACTIONS_DELIVERED_CONTRACT.md](../movee-app/docs/MOBILE_BOOKING_ACTIONS_DELIVERED_CONTRACT.md) : choix
libellés autorisés, actions/version, aperçu sans écriture et récupération des
confirmations via quatre opérations classiques explicites. Nouvelle route
`POST /api/business-actions/booking-submit`, Bearer mobile, schéma fermé et aperçu
signé obligatoire. Le calcul partagé Booking/crédits est réévalué sous verrou
dans la transaction, à un instant de décision unique ; aucune règle client ou
CRUD parallèle. Consentements, versions, reçus/idempotence existants réutilisés.
Les appels historiques restent compatibles, Pages v1 demeure en lecture seule.

Rapport [docs/MOBILE_BOOKING_ACTIONS_DELIVERED_RESULT.md](../movee-app/docs/MOBILE_BOOKING_ACTIONS_DELIVERED_RESULT.md) : 419 tests,
416 réussis, 3 Redis ignorés (103,378 s), dont 16 tests dédiés ; 38 HTTP réels
sur Gunicorn, aucun submit/confirm métier local. Préservation des 73 tables,
hors audit de login normal des cinq comptes synthétiques et Redis éphémère.
Backend redémarré uniquement par movee-dev, Redis/MariaDB/Expo préservés.
Aucun SQL, nouvelle donnée de réservation, qualification coach ou flag activé.
Rendu Mobile, mutation/concurrence InnoDB du nouveau submit et appareils restent
à recetter séparément.

### Planning Mobile livré localement — 26 octobre 2026

Lecture Bearer IA indépendante `get_upcoming_bookings`, sur le transport
`/api/business-actions/ia2b/`, déléguée à MobileBookingPlanningService. Contrat
fermé version1 : sujet courant/autorisé, fenêtre <=31 jours, pages <=50, curseur
signé acteur/requête/inventaire avec référence et expiration fixes120s ; changement
visible entre pages refusé. Codes Booking1/2/3 dont horaires en cours, hors4/5/6 ;
fuseaux/libellés/lien Pages contrôlés côté serveur, aucune éligibilité de création
ou de crédits. Aucun SQL ni droit modifié. Contrat effectif et limites :
[docs/MOBILE_UPCOMING_BOOKINGS_CONTRACT.md](../movee-app/docs/MOBILE_UPCOMING_BOOKINGS_CONTRACT.md), recette :
[docs/MOBILE_UPCOMING_BOOKINGS_RESULT.md](../movee-app/docs/MOBILE_UPCOMING_BOOKINGS_RESULT.md). Données isolées distinctes du jeu local.

### Durées et plages réservables — code livré le 26 octobre 2026

BookingSettingsService utilise les configs versionnées existantes pour un catalogue
réseau de quatre prestations explicitement classées et la qualification des offres.
Défauts préparés60/60/60/30, dérogation explicite par offre, conditions acquises
conservées. IA2BPolicyService interprète reservation_hours/reservation_exceptions
en complément des horaires et fermetures historiques, avec contrôle de toute la
séance et des changements d’heure. Nouvelles confirmations Booking liées à une
empreinte des conditions ; lecteur Mobile get_booking_service_options version2,
lecteur version1 maintenu. Trois formulaires Pages type7 et leur manifeste
préparés ; administration sous session web et droits existants, sans extension
OAuth/Mobile. **Catalogue et Pages non installés, aucun paramètre local appliqué.**
Contrat : docs/BOOKING_SETTINGS_DELIVERED_CONTRACT.md ; recette isolée et limites :
docs/BOOKING_SETTINGS_DELIVERED_RESULT.md ; futur plan de données :
docs/BOOKING_SETTINGS_APPLICATION_PLAN.md. Pas de nouveau schéma ou permission.

### Installation administrative Booking — 26 octobre 2026

Plan résolu SHA25692a73cdcd619c5731b5541023b895b6162498ed327db76ae297f60164161cc2c
appliqué après autorisation explicite à11:16:36Europe/Paris, avant expiration.
Cinq ajouts : Pages97–99, catalogue224 version1, proposition/reçu19. Rejeu réel0ajout.
Comparaison des73tables : toutes les lignes préexistantes inchangées. Aucune
qualification d’offre, durée acquise, plage de centre, réservation, crédit,
permission ou compte modifié. Contrôle des gardes/formulaires par Services,
recette visuelle non effectuée. Preuve : docs/BOOKING_SETTINGS_APPLICATION_RESULT.md.


### Préférences Booking v1 — code du26 octobre2026, schéma non appliqué

Services BookingPreferencesService/BookingSuggestionsService, Repository privé et
quatre transports Bearer dédiés, sans dépendance IA pour le mode manuel. Recherche
commune par occurrences locales exactes puis moteur Booking existant. Capacités
assistant explicites et remplacement uniquement sur action_input humain actuel
exactement concordant ; aucune inférence d’habitude. Pas de cache Redis des valeurs
de réponse/arguments de mutation de ces outils ; récupération SQL minimale24h,
version monotone et retrait réel du document courant.

Paquet SQL/manifeste préparé dans sql/pending/booking_preferences_v1, non enregistré
comme migration applicable, aucune exécution sur MariaDB locale. Préparer la
reconnaissance post_structure/post_metadata et un plan résolu séparé avant toute
application. Procédure explicite de purge de reçus, aucun job installé.
Contrat et limites : docs/MOBILE_BOOKING_PREFERENCES_DELIVERED_CONTRACT.md ;
impact : docs/BOOKING_PREFERENCES_MIGRATION_PREPARATION.md ; preuves de tests et
préservation : docs/MOBILE_BOOKING_PREFERENCES_DELIVERED_RESULT.md.


### Préférences v1 — plan de migration du26 octobre2026, non appliqué

Delta0001_booking_preferences_v1 enregistré dans les fichiers avec post_structure
75tables et post_metadata V1 inchangé. Runner historique toujours SELECT-only,
outil dédié limité à une cible/empreinte/validité et état attendu. DDL/application/
rejeu/échec partiel validés sur MariaDB11.4.13 jetable, sans copie de données locales.
Garde runtime exigeant le marqueur conforme en plus des deux tables : pas
 d’activation sur structure partielle. Base locale toujours73tables et1909lignes,
marqueur absent ; aucun compte/droit/donnée métier modifié. Plan et limites :
docs/BOOKING_PREFERENCES_RESOLVED_MIGRATION_PLAN.md. Purge quotidienne automatique
acceptée par l’utilisateur, automatisation Codex créée en pause jusqu’à installation
autorisée et postflight. Aucune migration/purge/job launchd appliqué par cette préparation.


### Préférences v1 — migration locale appliquée le26 octobre2026

Plan64e465e1811a900cea7a9c797d2f815be3228cb8329afa0a96f4e71465c93f48
autorisé puis appliqué avant expiration. Deux tables privées vides et marqueur
configs225/auteur67 ;75tables reconnues au niveau0001_booking_preferences_v1.
Anciennes lignes préservées sauf ajout du marqueur autorisé. Backend arrêté puis
redémarré ; Redis/MariaDB/Expo préservés. Purge quotidienne Codex confirmée ACTIVE
après postflight, sans purge exécutée dans ce lot. IA désactivée, zéro préférence
initialisée, raccordement/recette Mobile distincts. Rapport :
docs/BOOKING_PREFERENCES_APPLICATION_RESULT.md.


### Administration Booking — enrichissement des Pages du26 octobre2026

Pages97/98/99 réutilisées : menu sous droits depuis pages/page_config, choix
centres/offres par nom avec recherche/pagination, paramètres numériques centre
existants et cible de publication stable en reprise. Aucun paramétrage métier
appliqué. Dix Pages de consultation natives (offres, engagements, ledger crédits,
disponibilités/exception coachs) préparées, non installées ; plan résolu et outil
transactionnel séparé. Pas de nouvelles permissions ni de CRUD financier.
493tests dont3ignorés, contrôle payloads JavaScript ; aucune recette visuelle
revendiquée. Voir docs/BOOKING_ADMIN_PAGES_DELIVERY.md et
 docs/BOOKING_ADMIN_PAGES_RESOLVED_PLAN.md. L’administration globale des préférences
privées adhérents, équipements sans Entity et qualification complète des centres
sans politique ne sont pas livrées par cet enrichissement.


### Administration Booking — dix consultations installées le26 octobre2026

Plan6254fd539f97bf0dc634885ec070b46ff68a94d3d4ae15efe3428d660900fb21
autorisé et appliqué avant expiration. Pages100à109, auteur67, dix ajouts exacts,
rejeu réel0ajout. Anciennes lignes des73tables et deux tables privées préservées.
Cinq nouvelles listes et trois réglages existants au menu sous droits ; pas de
recette visuelle navigateur revendiquée. Rapport :
docs/BOOKING_ADMIN_PAGES_APPLICATION_RESULT.md.


### Studios — plan de navigation préparé le26 octobre2026, non installé

Source Admin : codex/MOVEE_ADMIN_SCOPE.md et
docs/ADMIN_STUDIOS_PAGES_PROPOSAL.json. Plan séparé UPDATE81 + INSERT110,
actions natives résolues sur open_one101, overrides effectifs conservés ;
menu conditionné au marqueur booking_admin et aux droits existants. Projection
web corrigée pour l’e-mail du studio uniquement, pas les identifiants utilisateurs.
Plan bloqué pour le périmètre complet : aucune permission active Entity17
100/101/108 du rôle2 dans le registre local, aucun droit ajouté. Tests HTTP
isolés siège positifs, franchisé refusé selon permissions actuelles ; aucune
recette positive franchisé revendiquée.498tests dont3ignorés, aucun échec ;
5tests Studios repassés après résolution des labels de filtre.
75tables préservées, Page81 inchangée et fiche absente en base. Aucune
installation SQL ni donnée métier modifiée. Contrats, gaps modification générale/
horaires et Page89 : docs/ADMIN_STUDIOS_CONTRACTS_AND_VALIDATION.md ;
plan/empreinte/validité : docs/ADMIN_STUDIOS_RESOLVED_PLAN.md.

### Préparation du 26 octobre 2026 — reconnaissance exacte Studios

Le preflight global possède une révision de métadonnées `studios_authorized_v1`,
enregistrée dans le manifeste SQL avec un document scellé distinct. Elle conserve
le niveau SQL `0001_booking_preferences_v1` et son contrat d’origine ; ce n’est ni
un nouveau DDL ni un marqueur ajouté en base. L’ancienne Page81 seule reste reconnue ;
la variante exige les deux Pages81/110 et les permissions155–157 exactes du plan
Studios autorisé, audits compris. État partiel/divergent ou collision : refus.
Les autres métadonnées historiques restent soumises au contrôle initial.
L’exécuteur opérationnel ajoute un preflight global de l’état final dans la
transaction, avant commit. L’ancien plan d’installation ne doit pas être réexécuté
avec des sources différentes. La nouvelle reconnaissance se vérifie sans écriture
avec le plan d’activation séparé ; aucun retrait/restauration automatique.
Voir [Référence Admin centrale ; ancien plan préparatoire retiré](MOVEE_ADMIN_TECHNICAL_REFERENCE.md) pour les résultats et limites.

### Préparation du 27 octobre 2026 — transport des fiches natives

PageService.get_by_uid expose hors designer une route de lecture concrète pour
les Pages type4 sans endpoint stocké et résout {$entityName} des actions open_page
contre l’entité de la Page cible. Cela corrige la fiche Studios110 sans toucher
aux métadonnées installées ni à leur contrat global. Les endpoints explicites et
le mode designer sont préservés. Voir docs/ADMIN_STUDIOS_DETAIL_TRANSPORT_FIX.md
pour preuves HTTP sous session, scopes isolés, test JavaScript et limites de recette.

### Préparation du 27 octobre 2026 — Admin Core groupé

Lectures des Pages Admin marquées admin_core : session/affiliations courantes,
population6/5 liée à la Page, gardes coach affecté, financier37/55 siège seulement,
menus groupés découverts par metadata, options liées sous Page sans cache client.
Transport POST /api/admin-booking/<operation> réutilisant le cœur signé Booking,
indépendant de l’IA et des routes Bearer. Les pages sont des consultations et refusent
les mutations génériques ; les mutations non closes restent dans pending_actions.
La révision metadata exacte du lot13UPDATE/11INSERT est préparée et le writer
vérifie le preflight global dans la transaction avant commit. Aucun SQL local,
compte, droit, activation ou restart dans ce travail. Plan bloqué sur habilitations,
contrat et limites : docs/ADMIN_CORE_DELIVERED_CONTRACT.md et
 docs/ADMIN_CORE_RESOLVED_PLAN.md. Les sources des anciens plans ne sont pas réutilisables.

### Compte et intention de déconnexion Pages7 — 29 octobre2026

Runtime `SessionPublicPagesService` et transports Web/Mobile7 codés, sans
installation ni activation. Profil distinct du6 : fiche native type4 d'identité
propre (deux fournisseurs virtuels : nom nullable, connecté), aucune lecture
User arbitraire ni permission nouvelle. Action native `session_logout` résolue
par définition/instance : invocation réautorisée, intention technique fermée,
aucune révocation dans le Service Pages. Exécution par le gestionnaire client
existant, raccordement lecteur7 encore à faire. Les parcours couverts6 et la
mémoïsation limitée à dispatch sont réutilisés ; contextes/domaine/version7
distincts, aucun fallback. Absence de variante7 => entry_unconfigured.
Contrat : docs/PUBLIC_SESSION_PAGES_V7_DELIVERED_CONTRACT.md ; exemples synthétiques
et limites : docs/session_pages_v7_delivered_examples.json et
 docs/SESSION_PAGES_V7_VALIDATION.md. Définitions/Pages/instances, borne Designer
max7 et reconnaissance globale restent soumis à un futur plan résolu puis à une
autorisation distincte. Aucun DDL, ID ou nombre d'opérations n'est présumé.

Préparation d'installation Mobile7 : reconnaissance globale exacte
`public_session_pages_v7_v1` chaînée au lot6, inverse de la seule borne Designer
pour vérifier le prédécesseur intégral. Deux Pages Mobile, deux champs virtuels,
une action sans API et une mise à jour de champ Designer résolus après inventaire
READ ONLY ; aucun droit, DDL ni changement métier. Exécuteur transactionnel commun
réutilisé avec verrou, contrôle final avant commit et rejeu sans DML. Plan et
validation : docs/SESSION_PAGES_V7_RESOLVED_APPLICATION_PLAN.md. Aucune application
ou activation dans cette préparation ; le prédécesseur6 reste l'état local.

Runtime public8 codé (29 octobre 2026), sans installation ni activation :
BookingProcessPagesService réutilise Pages/actions/champs/Designer et les Services
Planning/Booking existants pour les acquis, annulation, accords d'annulation et
récupération readonly par confirmateur autorisé. Aucune création par commande ou
confirmation8 ; lecture des reçus de création existants autorisée seulement sous
qualification actuelle. execute exige consentement et intention stable ; replay
booléen explicite permet la reprise sans persister de contexte de navigation.
Contrat effectif : docs/PUBLIC_BOOKING_PROCESS_PAGES_V8_DELIVERED_CONTRACT.md ;
tests/limites : docs/BOOKING_PROCESS_PAGES_V8_VALIDATION.md. Aucun nouveau journal,
droit ou stockage métier. Adaptateur Mobile/journal et hôte formulaire Web restent
à raccorder ; reconnaissance globale et installation exigent un plan distinct.

Correction du DTO8 en préparation (29 octobre) : record d'accord expose
decision_reference readonly={kind:booking_decision,proposal_id,request_hash},
après requalification ; null sur les autres records métier. Le consommateur
construit décision/acceptation/recover depuis cette référence sans décoder les
preuves ni obtenir de clé de l'initiateur. Contrat/exemples8 mis à jour avant
installation ; aucune extension4–7, permission, migration ou activation.

Plan d'installation public_booking_process_pages_v8_v1 préparé READ ONLY depuis
l'état local7 : six Pages202–207, dix définitions transitoires1525–1534, borne
Designer1522 max7→8. Cibles programmes/séances/compte et action de session réutilisées,
aucune permission/DDL/politique/écriture métier. Reconnaissance globale exacte
chaînée7, executor transactionnel existant, preflight final avant commit, rejeu
sans DML ; validation socket MariaDB jetable distincte de la recette connectée.
Plan/limites : docs/BOOKING_PROCESS_PAGES_V8_RESOLVED_APPLICATION_PLAN.md.
Application et activation non effectuées et soumises à accords séparés.
Prévenir explicitement l'utilisateur avant le prochain lot « Création d'une
réservation, suggestions et calendrier » ; ce lot, les préférences et la bascule
complète de l'accueil ne sont pas engagés.

Installation locale public_booking_process_pages_v8_v1 effectuée le29 octobre2026
sur autorisation du plan3fade200e234b2ec8e166e56d7140c9ed363fc8ad21170faae7a70439a0f3d8c :
16 ajouts et1 mise à jour, preflight global avant commit et contrôle READ ONLY
après application. Anciennes données73 tables par inverse du delta, deux tables
privées, permissions et Pages91–96 préservées ; rejeu exact zéro DML/DDL.
Backend seul arrêté via movee-dev et laissé arrêté, activation séparée encore
requise ; MariaDB/Redis/Expo préservés. Rapport :
docs/BOOKING_PROCESS_PAGES_V8_APPLICATION_RESULT.md. Aucune recette HTTP8 ou
mutation métier locale de réservation réalisée dans cette installation.

Activation Backend8 effectuée sur autorisation séparée le29 octobre2026 via
movee-dev start backend. Preflight public_booking_process_pages_v8_v1 conforme
avant/après ; inventaire75 tables et sources strictement identiques.25 HTTP
réels sans authentification : login200 et24 refus401 JSON/no-store attendus,
aucun404/500 ; aucune mutation/login/logout. MariaDB/Redis/Expo, processus
inchangés. Backend géré prêt ; recette positive authentifiée8 et navigateur15s
non effectuée, aucune bascule des liens usuels7. Rapport :
docs/BOOKING_PROCESS_PAGES_V8_ACTIVATION_RESULT.md.

30 octobre2026 : préparation READ ONLY du jeu futur de recette8, aucune
application ou commande de service. Les cinq comptes existants n'ont aucune
réservation à venir ni accord exploitable ; A70 a7 crédits disponibles dans le
centre3, durée acquise30min. Plan append-only de13 lignes nouvelles pour trois
bookings distincts lecture/gratuit/tardif, sans crédit émis, compte, politique ou
permission nouveau ; backend et données historiques préservés. Plan concret :
docs/MOBILE_BOOKING_V8_FUTURE_DATA_PLAN.md, empreinte/validité dans l'artefact
docs/mobile_booking_v8_future_resolved_plan.json. Toute application puis les
gestes d'annulation/confirmation attendent des accords distincts sur ce périmètre.
Le recours au create_booking EXISTANT est limité aux fixtures proposées ; aucun
développement du profil public création/suggestions/calendrier n'est engagé.
Prévenir explicitement l'utilisateur avant d'engager ce prochain lot.

30 octobre2026 : jeu futur v8 appliqué sur autorisation du plan6305091ac833f08ebb24270c7bf262aa73532b4b5147bee08245dd1bbc447b21.
13 ajouts exacts, bookings12/13/14 pour A70, trois immobilisations sans émission
de crédits ; solde disponible A4. Anciennes lignes75 tables conservées,
preflight8 conforme avant commit/après, rejeu0 DML/DDL. Aucun service redémarré.
Aucune annulation ni décision d'accord exécutée/autorisée ; lecture de référence12
à conserver, gestes sur13/14 soumis à accord distinct. Rapport :
docs/MOBILE_BOOKING_V8_FUTURE_DATA_APPLICATION_RESULT.md.


30 octobre2026 — lot intégré public9 création/suggestions/calendrier/préférences,
codage autorisé par coordination explicite avec Mobile. Runtime distinct de8,
champs/actions/formulaires natifs et Services existants ; aucun journal, droit ou
stockage métier nouveau. Déclencheurs et dépendances déclarés, répétition privée
versionnée, revue readonly du preview original et consentement, reprise des reçus
originaux après contexte/session perdus. Accords9 couvrent création et annulation ;
8 reste fermé. Le lecteur commun conserve la version originale acquise d’une
création appliquée. Confidentialité préférences/suggestions Mobile-only préservée.
Contrat : docs/PUBLIC_BOOKING_COMPOSITION_PAGES_V9_CONTRACT.md ; résultats :
docs/PUBLIC_BOOKING_COMPOSITION_PAGES_V9_DELIVERY.md et JSON de validation.
772 tests élargis (769réussis/3ignorés), puis50tests9+8 après correctif final ;
18cas9. MariaDB jetable socket-only,15opérations,lectures/recover0DML et
calendrier7j/50lignes2,023s sur fixture, sans qualification de latence navigateur.
Aucune installation/activation locale, permission, préférence ou réservation de
recette modifiée, aucun service arrêté/redémarré et aucun fichier source Mobile
modifié. Reconnaissance globale et plan exact d’installation9 restent à préparer
sur l’état réel ; les empreintes de ces sources ne sont pas une empreinte de plan.

30 octobre2026 — préparation du candidat d’installation intégré9, non scellé :
13ajouts (Pages208–210,Fields1535–1544) et1updateDesigner1522,max8→9,
auteur67résolu,0permission/DDL/mutationmétier. Reconnaissance globale exacte9
en fichiers, projection locale READ ONLY conforme,75tables inchangées.79tests
ciblés réussis ; MariaDB jetable valide application14opérations, préflight global
avant commit, rollback/rejeu0DML et refus de divergence. Mobile termine ses
sources : aucun marqueur final ni plan_sha256 applicable, chargeur bloque le
scellement. Rapport docs/BOOKING_COMPOSITION_PAGES_V9_DRAFT_APPLICATION_PLAN.md.
Qualification réelle member_a :5disponibles/6immobilisés,choixautonome30min
coût1centre3,créneau disponible,préférencesversion0/aucuneentrée et édition
propriétaire éligible. Suggestions no_preferences ; aucune préférence initialisée,
aucun crédit/politique/compte ajouté. Aucune application ou service modifié.

30 octobre2026 — signal MOBILE_SOURCES_FINAL reçu et rapport final lu.77sources
Mobile figées,292sources totales dans le plan intégré9, inventaire frais et
vérification indépendante READ ONLY conformes,75tables inchangées. Plan résolu
SHA256 c651d9b34c29b87748a4b3ed83ddd38aeed096d205562701345e0daa9bc27c21,
généré09:59:21Paris,valable strictement avant10:59:21Paris le30octobre2026.
13ajouts/1updateDesigner,0permission/DDL/mutationmétier. Le périmètre de la future
autorisation inclut arrêt/démarrage du Backend seul via movee-dev et contrôles,
sans nouvelle validation d’activation séparée. Aucun accord d’application reçu
ni SQL de modification/service exécuté à ce stade. Plan lisible :
docs/BOOKING_COMPOSITION_PAGES_V9_RESOLVED_APPLICATION_PLAN.md ; artefact :
docs/booking_composition_pages_v9_resolved_plan.json.

30 octobre2026 — plan intégré9 c651d9b34c29b87748a4b3ed83ddd38aeed096d205562701345e0daa9bc27c21 appliqué sur autorisation humaine coordonnée,
après contrôles10:08:11Paris.13ajouts/1update exacts,préflight global9 avant commit
et après,rejeu réel0DML/DDL,inventaire75tables conforme et autres données/droits/
profils4–8 préservés. Backend seul arrêté/démarré via movee-dev,superviseur27353
prêt ;Redis1266/Expo1257/MariaDB3306préservés.29HTTPlecture conformes,sans login
ni mutationmétier. Mobile autorisé à poursuivre sa bascule post-activation9 ;
recette authentifiée et gestes métier séparés. Rapport :
docs/BOOKING_COMPOSITION_PAGES_V9_APPLICATION_ACTIVATION_RESULT.md.

30 octobre2026 — entrée de session déclarative codée sur validation explicite :
projection publique unique Pages/Fields/Designer, GET mobile-auth/presentation,
headerfixeX-MOVEE-Login-Config avant credentials/audit/token ;legacy/me/logout
indépendants et profils4–9fermés. Héritage refusé,clones inactifs indépendants,
aucune valeur ou donnée User dans la description.53tests ciblés et793élargis
(790réussis/3ignorés),MariaDBjetable40lectures/6,804ms,0DML/lectureUser. Aucun
SQLlocal/installation/service modifié dans le runtime. Contrat et validation :
docs/PUBLIC_MOBILE_SESSION_ENTRY_DELIVERED_CONTRACT.md et
docs/MOBILE_SESSION_ENTRY_VALIDATION.md. Mobile signale186tests et gel final ;
préparation d’inventaire/plan séparée,aucune application implicite.

30 octobre2026 — plan entrée de session préparé READ ONLY après runtime et gel
Mobile186tests.6INSERT exacts (Page211,Fields1545–1548,Action124),0update/droit/DDL/
donnée métier. Préflight actuel9 et projection public_mobile_session_entry_v1
conformes,75tables inchangées,85sourcesMobile/310total figées.74tests ciblés et
MariaDBjetable application/rejeu0DML/rollback6/divergence validés. Plan SHA256
759a2dd76c4b0daf9818c7fb06f026050c0f8bf86177a20bb858f0ec2db4b940, généré
11:03:46Paris,valable strictement avant12:03:46Paris le30octobre2026. Future
autorisation inclut arrêt/démarrage Backend seul et contrôles sans login réel.
Aucune application ni service modifié. Rapport et artefact :
docs/MOBILE_SESSION_ENTRY_RESOLVED_APPLICATION_PLAN.md,
docs/mobile_session_entry_resolved_plan.json.

30 octobre2026 — plan entrée de session759a2dd76c4b0daf9818c7fb06f026050c0f8bf86177a20bb858f0ec2db4b940 appliqué sur autorisation humaine coordonnée,
après revalidation11:08:48Paris.6INSERT/0UPDATE,préflight global
public_mobile_session_entry_v1 avant commit et indépendant,rejeu réel0DML/DDL,
anciennes données/droits/profils4–9 et75tables conformes aux images prévues.
Backend seul redémarré via movee-dev,superviseur31543 prêt ;Redis1266/Expo27755/
MariaDB3306préservés.16HTTPlecture conformes,descriptionpublique200/DTOversion
exact,meetcapabilitiesprivées401 ;aucunlogin/logout réel/token/auditconnexion.
Feuvert Mobile pour basculeindexpostactivation ;recetteglobale reste reportée.
Rapport : docs/MOBILE_SESSION_ENTRY_APPLICATION_ACTIVATION_RESULT.md.
