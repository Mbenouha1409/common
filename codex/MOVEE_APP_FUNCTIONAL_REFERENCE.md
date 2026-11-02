# MOVEE App — référence fonctionnelle spécifique

Version de consolidation : 2 novembre 2026. **Référence centralisée validée ; anciennes copies retirées après accord utilisateur.** Lire d’abord [README.md](README.md), [règles communes](AGENTS.md), [fonctionnel global](MOVEE_FUNCTIONAL_REFERENCE.md) et [technique globale](MOVEE_TECHNICAL_REFERENCE.md). Les sections issues des anciennes références conservent leur date/statut ; un constat historique ne décrit pas l’installation actuelle.

## Particularités App et règles de lecture

Le registre Q commun est dans MOVEE_FUNCTIONAL_REFERENCE.md ; les décisions B et leurs précisions ci-dessous demeurent propriété d’App. Autorité des réservations, ledger, programmes, qualifications et droits côté Services ; aucune transposition automatique des hypothèses Biz. Préférences privées exclues de l’administration générale.

**Correction de lecture :** les paragraphes de préparation du26 octobre disant « tables non installées » sont historiques. Le rapport BOOKING_PREFERENCES_APPLICATION_RESULT.md et la section technique du26 octobre attestent l’installation autorisée ; ne pas reproposer cette migration ou initialiser des préférences par défaut. Durées60/60/60/30 ne remplacent pas les conditions acquises ni les réservations ; collectif/découverte/bilan ne deviennent pas réservables par leur paramétrage. Bordeaux08–21 n’est pas appliqué par cette consolidation.

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:147 -->

## Périmètre classique du23octobre — état et limites historiques

**Divergence de formulation conservée :** la ligne ancienne « Séance en cours » ci-dessous ne doit pas être utilisée pour introduire un usage Mobile pendant l’entraînement. T7.8/AR07 et XP04 séparent l’interface Pod en séance et la consultation Mobile hors séance. Les garanties serveur et la consultation restent applicables.

### Écrans classiques minimaux — périmètre validé le 23 octobre 2026

Le chat IA reste l'interface principale des adhérents et coachs. Les parcours
classiques sont accessibles au choix ou en secours lorsque l'IA est indisponible,
sur le moteur metadata-driven `pages`, avec rendu natif par MOVEE Mobile.
Regrouper listes, détails et fonctions pour limiter le nombre d'écrans ; ne pas
reproduire l'administration dans le mobile. Cet arbitrage définit une cible,
pas une preuve de livraison de tous ces parcours.

| Parcours | Adhérent | Coach |
|---|---|---|
| Mes séances / Mon planning | Réservations et détails | Séances et adhérents concernés |
| Réserver | Créneau et réservation | Réservation pour un adhérent autorisé |
| Détail de réservation | Annuler, déplacer, répondre à une proposition selon les règles | Actions autorisées et consentement adhérent lorsque requis |
| Programme | Consultation des exercices et consignes | Consultation pour les adhérents suivis |
| Séance en cours | Consignes, résultats, douleur | Suivi et saisie autorisés |
| Résultats et progression | Historique personnel | Historique des adhérents autorisés |
| Mes adhérents | Sans objet | Recherche et dossier des adhérents suivis |
| Mes disponibilités | Sans objet | Consultation et gestion des disponibilités |
| Mon compte | Identité, centre actif, crédits/abonnement, préférences, déconnexion | Identité, contexte centre/profil, préférences, déconnexion |

Les propositions et alertes peuvent être intégrées au chat et aux détails
concernés sans écran supplémentaire systématique. Les permissions, consentements,
invariants et politiques Q/B/AR demeurent applicables. AR02 est conservé : aucun
éditeur classique de création ou modification des programmes.

Le premier lot de code porte uniquement sur les lectures réservations,
programmes et séances/résultats. Voir le contrat technique
[Pages mobiles v1](../movee-app/docs/MOBILE_PAGES_CONTRACT.md) pour son état et ses limites.

### Couverture antérieure

| Domaine | Décisions | Couverture fonctionnelle documentée | Statut attesté au 16 octobre 2026 |
|---|---|---|---|
| Réseau, identité, permissions | Q001–Q007, Q089 | Siège, franchises, centres, rattachements et droits contextualisés | Phase B déclarée en code ; recette réelle à vérifier |
| Réservations, crédits, coachs | Q008–Q015, Q058–Q064, B1–B5 | Disponibilités, crédits immobilisés, annulations, remplacement et consentement | Extensions IA 2B A livrées en code ; politiques/historiques à qualifier |
| Programmes, séances, sécurité | Q026–Q057, B6–B7 | Adaptations, prescriptions, restrictions, douleur, réévaluation | Extensions IA 2B B–C livrées en code ; parcours machines/Session complets non attestés |
| Agent IA et expérience conversationnelle | Q043–Q047, Q088–Q100, B8 | Capacités natives, confirmations contextuelles, permissions, reprise et proactivité | IA1/IA2A/IA2B partiellement livrés ; OpenAI réel et client final non recettés |
| Notifications mobiles | Q068, B5, B6.66–B6.68, B8 | Préférences, push hors application, alertes métier | Outbox/worker codés ; fournisseur Push et terminaux réels non raccordés |
| Finance, machines, réseau commercial, pilotage | Q016–Q042, Q065–Q130 | Exigences produit cibles conservées, avec modules et phasage proposés | Couverture de code globale non attestée par le rapport IA 2B |

**Règle :** la couverture documentaire d’une décision n’est pas une preuve de réalisation. Les résultats de tests indiqués sont des constats datés, pas des garanties de déploiement ni des dépendances à un rapport temporaire.

---

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:194 -->

## MOVEE — Vision produit


**Projet :** MOVEE App — référentiel de conception du 12 octobre 2026.  
**Statut :** documentation cible ; ni preuve d’implémentation ni autorisation de migration.

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:228 -->

## MOVEE — Cahier des charges fonctionnel exhaustif


**Projet :** MOVEE App — référentiel de conception du 12 octobre 2026.  
**Statut :** documentation cible ; ni preuve d’implémentation ni autorisation de migration.

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:815 -->

## MOVEE App — Brief consolidé IA 2B (V1)


**Date :** 15 octobre 2026  
**Statut :** décisions fonctionnelles consolidées, **pas** autorisation de coder ni de migrer.  
**Périmètre :** décisions B1 à B8 de la concertation IA 2B, rapprochées des documents MOVEE et du schéma SQL exporté.

> **Fiabilité du registre.** Les décisions B7.1–B7.10 et B8.1–B8.13 sont restituées individuellement à partir des validations conversationnelles disponibles. B6.61–B6.71 sont également explicites ; les autres décisions B6 et les blocs B1–B5 sont consolidés par thème à partir du contexte de travail conservé, **sans prétendre reconstituer chaque libellé ou lettre de réponse d'origine**. Avant de qualifier ce document d'« exhaustif », il faudra le rapprocher du journal complet des échanges B1–B6.

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:824 -->

## 1. Hiérarchie des décisions

Les arbitrages B1–B8 intégrés au présent référentiel précisent les décisions Q001–Q130. En cas de conflit, signaler la divergence, conserver la traçabilité et appliquer le dernier arbitrage explicitement validé ; aucune analyse temporaire n’est nécessaire pour interpréter le présent référentiel.

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:829 -->

## 2. Principes techniques non négociables

- Applications mobiles iOS/Android → API Flask → Services → Repositories → MariaDB (Expo pour tests initiaux) ; orchestration du modèle OpenAI côté serveur.
- L’agent IA natif est orchestré par Flask et invoque uniquement des capacités métier autorisées ; aucun accès SQL direct depuis le modèle ou l’orchestrateur.
- CRUD metadata-driven pour les opérations simples ; Services/actions métier dédiés pour réservation, crédits, changements de programme, consentements, décisions coach et idempotence.
- Autorisations effectives vérifiées côté serveur à **chaque** action, selon utilisateur, rôle et périmètre centre.
- Pas de tables `clients`, `organizations`, `sessions_remaining` ni de table IA dédiée ; utiliser notamment `proposals` et `session_credit_transactions` lorsque adaptés.
- Toute extension SQL doit être motivée par une lacune physique prouvée ; aucun DDL n'est approuvé par ce brief.

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:838 -->

## 3. B1 à B5 — Réservations, crédits, centres et coachs (synthèse validée)

### B1 — Créneaux, capacité et offres
- Réservation d'un créneau de séance dans un centre, non d'une machine individuelle.
- Inventaire des machines physiques MOVEE par centre, avec état opérationnel ; capacité tenant compte des machines, contraintes et plafond du centre.
- Séances accompagnées par coach et autonomes ; durée, coût en crédits, horizon de réservation et pas de grille définis par l'offre/configuration métier.
- Horaires, fermetures et fuseau horaire du centre respectés.
- Coach compétent et habilité pour le centre ; affectation manuelle ou automatique suivant le contexte.

### B2 — Crédit et allocation
- Ledger `session_credit_transactions` comme source du solde ; crédits entiers.
- Immobilisation à la réservation, consommation à la séance réalisée, restitution selon les règles d'annulation.
- Priorité d'allocation : abonnement, puis pack, puis séance unitaire ; combinaison de plusieurs engagements possible.
- À priorité égale, expiration la plus proche puis ancienneté.
- Politiques d'expiration, report et validité selon l'offre.
- **Arbitrage IA 2B définitif, synchronisé avec Q011 :** éligibilité/validité vérifiée à la date de réservation ; crédits immobilisés lors de la réservation. Une réservation confirmée reste valable si les crédits immobilisés expirent avant la séance ; l'expiration ne doit pas supprimer ou rendre indisponibles les crédits déjà réservés. Les restitutions après annulation restent régies par B3.

### B3 — Annulation, modification et exceptions
- Délai de gratuité et pénalités de retard/no-show configurables par offre ; no-show distinct de l'annulation.
- Annulation par le centre ou coach : restitution intégrale ou alternative acceptée explicitement.
- Prolongation exceptionnelle du crédit selon la formule décidée : `max(expiration initiale, date d'annulation) + prolongation prévue par l'offre`.
- Dérogations réservées aux personnes autorisées, motivées et auditées.
- Une séance commencée ne peut plus être annulée ou déplacée par l'adhérent.
- Changement de réservation atomique, avec revalidation de disponibilité, crédits et contraintes du coach ; hors délai gratuit, appliquer les conséquences métier avant accord.
- Une modification initiée par le coach exige le consentement explicite de l'adhérent.

### B4 — Intercentres et continuité
- Accès intercentres conditionné par l'offre ; même coût pour une prestation équivalente entre centres.
- Transfert refusé si les crédits **initialement réservés** ne sont pas éligibles dans le centre cible, même si d'autres crédits existent.
- Priorité à la continuité avec le coach habituel ; alternatives d'abord dans le même centre, puis options compatibles dans le périmètre défini.
- Proposer jusqu'à trois créneaux proches dans un horizon de sept jours ; permettre de privilégier date la plus proche ou horaire similaire.
- Vérifier déplacements, temps de transition et indisponibilités du coach.

### B5 — Remplacement du coach et consentement
- En cas d'indisponibilité, une proposition de remplacement à la fois ; créneau temporairement réservé suivant les règles de durée.
- Consentement explicite de l'adhérent, avec information push et dans l'application.
- Refus : remboursement/restitution prévue et possibilité d'une recherche exceptionnelle supplémentaire.
- Proposition expirée non réactivable automatiquement.
- Aucune substitution de coach imposée.

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:878 -->

## 4. B6 — Adaptation des programmes, douleurs, arbitrages

**Statut :** B6 clôturé à **B6.71**. La question B6.72 a été abandonnée.

### Règles fonctionnelles consolidées
- L'adhérent peut demander à l'IA des substitutions d'exercices compatibles avec objectifs, muscles sollicités, équipements, restrictions et données disponibles ; charges et performances jamais inventées.
- L'IA adapte séries, répétitions, charges et repos dans le cadre autorisé ; accord de l'adhérent, information du coach, versionnement et préservation des séances passées.
- Si la portée temporelle est ambiguë, demander « séance actuelle ou prochaines séances ? ».
- Pendant une séance, seuls les exercices **non commencés** peuvent être modifiés ; proposer substitution ou réorganisation, respecter la durée et demander accord pour retirer un exercice.
- Le coach peut verrouiller des exercices avec motif visible. Les protections persistent entre versions. Toute dérogation suit une demande de validation coach via `proposals`.
- Les conflits de version nécessitent revalidation ; ne jamais écraser silencieusement une décision concurrente ; annulation ciblée et historique conservé.
- Changement d'objectif global : validation coach ; suggestions de révision proactives mais non répétitives sans évolution significative.
- Douleur signalée : arrêt de l'exercice concerné, alerte coach immédiate, suivi structuré ; pas de substitution automatique ni de diagnostic médical. Ne pas réintroduire l'exercice sans réévaluation coach.
- Les exercices potentiellement liés peuvent être signalés ; ne pas bloquer automatiquement tout le programme. Signes d'alerte graves : orientation vers une prise en charge urgente.
- Réévaluation en rendez-vous sans débit de crédit, avec coach habituel prioritaire et remplaçant qualifié uniquement après accord ; possible dans les centres où le coach travaille.
- Le coach peut autoriser une reprise avec plafonds et critères précis ; restrictions persistantes jusqu'à nouvelle décision explicite. Progression IA seulement dans les limites fixées.
- Historique détaillé et synthèse hebdomadaire pour le coach ; possibilité de modifier plafonds, suspendre la progression, corriger et versionner ; notification et explication à l'adhérent.
- L'adhérent peut demander réexamen ou arbitrage sans suspendre la restriction ; délais configurables par centre avec défaut réseau, relances bornées, escalade responsable ; réaffectation coach seulement avec accord et nouvelle réévaluation.
- Dans l'attente, l'IA peut guider les exercices non concernés et proposer une réorganisation temporaire compatible avec consentement.
- Réouverture après décision seulement avec élément réellement nouveau ; une nouvelle douleur demeure toujours un nouvel événement de sécurité.

### Registre explicite B6.61 à B6.71
| ID | Décision validée |
|---|---|
| B6.61 | Ajouter les informations relatives au même exercice et à la même décision dans la demande ouverte ; historique préservé, coach informé, SLA non réinitialisé ; autre objet = demande distincte ; douleur = événement de sécurité distinct. |
| B6.62 | Conserver l'échéance initiale, réévaluer la priorité avec les nouveaux éléments et alerter si nécessaire, sans modifier les restrictions. |
| B6.63 | Priorité déterminée par les Services ; l'IA signale les éléments contextuels justifiant une hausse, sans baisse autonome ni levée de restriction. |
| B6.64 | Trois niveaux : Normal, Prioritaire, Élevé. |
| B6.65 | Délai par centre et par niveau, défaut réseau ; une hausse peut avancer l'échéance, jamais la repousser. |
| B6.66 | Push immédiat au coach si passage au niveau Élevé, même pendant les heures de tranquillité MOVEE (AR04), sous les autorisations et restrictions iOS/Android, sans garantie de livraison ; passage à Prioritaire visible dans MOVEE, sans push systématique. |
| B6.67 | Baisse de priorité uniquement avec validation et justification d'un coach ou responsable autorisé ; échéance non repoussée. |
| B6.68 | Adhérent voit priorité, historique et échéance ; explication d'une baisse dans MOVEE, sans push systématique. |
| B6.69 | Justification simplifiée et contextualisée, sans divulgation des critères internes confidentiels ni interprétation médicale. |
| B6.70 | Contestation intégrée à la demande existante, critères réévalués par Services, validation humaine si nécessaire, échéance conservée. |
| B6.71 | Contestations répétées conservées et regroupées sans relance systématique ; élément significatif = nouvelle évaluation ; nouvelle douleur jamais bloquée. |

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:914 -->

## 5. B7 — Application et validation des modifications (10 décisions, clôturé)

| ID | Décision validée |
|---|---|
| B7.1 | Autonomie IA encadrée pour les modifications autorisées, avec accord adhérent ; protections et changements sensibles soumis au coach. |
| B7.2 | Clarification conversationnelle de la portée ponctuelle/durable lorsqu'elle est ambiguë. |
| B7.3 | Proposition globale de plusieurs remplacements compatibles, avec récapitulatif et validation unique. |
| B7.4 | Appliquer seulement les modifications autorisées ; expliquer les exclusions ; demande séparée au coach pour les exercices protégés. |
| B7.5 | Annulation ciblée ou globale, revalidation des restrictions et nouvelle version sans effacement d'historique. |
| B7.6 | Détection des modifications concurrentes ; revalidation et nouvelle proposition soumise à l'adhérent. |
| B7.7 | Modification durable appliquée aux séances futures ; séance en cours préservée sauf demande explicite sur les exercices non commencés. |
| B7.8 | Visibilité immédiate pour le coach et synthèse hebdomadaire ; alertes urgentes selon circuits dédiés. |
| B7.9 | Progression autonome encadrée par données fiables, plafonds du coach et accord de l'adhérent ; hors cadre = validation coach. |
| B7.10 | Réorganisation hebdomadaire autonome encadrée : objectifs, volume, restrictions et protections conservés ; accord adhérent, validation coach si hors cadre. |

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:929 -->

## 6. B8 — Fiabilité, gouvernance et déploiement (13 décisions, clôturé)

| ID | Décision validée |
|---|---|
| B8.1 | Récupération conversationnelle après échec ; contexte conservé, alternatives proposées, réussite seulement après confirmation backend. |
| B8.2 | Continuité des interfaces métier classiques lorsque l’IA est indisponible, sauf création et modification de programmes exclusivement via IA (AR02) ; leur consultation reste autorisée sans IA. |
| B8.3 | Permissions métier existantes appliquées côté API/Services, sans privilège IA supplémentaire. |
| B8.4 | Confirmations contextuelles : lecture directe, validations métier ordinaires, confirmation explicite des conséquences sensibles ou irréversibles. |
| B8.5 | Historique métier avec origine IA, acteur, action, résultat et références ; pas de journalisation exhaustive systématique des conversations. |
| B8.6 | Résoudre les ambiguïtés par le contexte ; question ciblée uniquement si plusieurs interprétations entraînent des actions différentes. |
| B8.7 | Alternatives proactives compatibles ; ne jamais réserver une alternative non demandée sans accord. |
| B8.8 | Données métier vérifiées ; signaler les manques ; ne jamais inventer solde, disponibilité ou prescription. |
| B8.9 | Idempotence garantie côté API/Services, avec vérification du résultat réel et prévention des doublons. |
| B8.10 | Reprise contrôlée des opérations sûres/idempotentes ; revalidation métier et nouvel accord si conséquences modifiées. |
| B8.11 | Minimisation des données transmises au modèle, après contrôle des permissions. |
| B8.12 | Activation/suspension indépendante des grandes capacités IA par administrateurs, sans affecter les interfaces classiques. |
| B8.13 | Déploiement progressif par centre pilote, extension après validation. |

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:947 -->

## 7. Contrats métier et responsabilités à implémenter

| Domaine | Comportement attendu | Couche responsable |
|---|---|---|
| Recherche de créneaux | Capacité, horaires, coach, offre, droits centre, alternatives | Service de disponibilité dédié |
| Réserver / modifier / annuler | Transactions atomiques, réservation des crédits, politique d'annulation, consentements | Services Booking et crédits dédiés |
| Solde et allocations | Ledger, priorité des sources, expiration, remboursement, idempotence | Service crédits + Repository |
| Programmes | Propositions, restrictions, versions, revalidation, application/annulation | Service Program et workflow `proposals` |
| Douleur et réévaluation | Alerte, exclusion de l'exercice, décision coach, restrictions persistantes | Services métier et notifications |
| Assistant IA | Compréhension, dialogue, choix d'outils, alternatives, synthèses | Orchestrateur IA côté Flask |
| Autorisation et audit | Permissions, scopes, confirmations, reçus, origine IA | API/Services, persistance existante |
| Pilotage | Capacités activables, pilotes par centre, désactivation rapide | Services de configuration/gouvernance |

**Important :** ces intitulés décrivent des responsabilités fonctionnelles, **pas des classes existantes attestées**. Ne pas créer de nouvelles classes avant inspection des fichiers source un par un.

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:962 -->

## 8. Vérification SQL ciblée (export joint)

Tables **présentes dans l'export** : `bookings`, `engagements`, `session_credit_transactions`, `programs`, `workouts`, `workout_exercises`, `sessions`, `session_exercises`, `session_sets`, `proposals`, `permissions`, `notifications`, `locations`, `trainer_availabilities`, `trainer_availability_exceptions`, `configs`, `users` (sous réserve des noms exacts de toutes les tables à contrôler à chaque implémentation).

L'analyse IA 2B du 15 octobre identifie notamment les **lacunes non résolues dans le code/SQL analysé** : parc physique de machines, horaires et fuseaux centre, capacités, Service de disponibilité, immobilisation de crédits par booking, allocation multi-engagements, version persistée des programmes, reçus durables d'idempotence et permissions à élargir de façon contrôlée. Ces constats doivent être **revérifiés dans le dépôt actuel** ; elles ne justifient pas automatiquement une nouvelle table.

Ne pas confondre `prescription_hash` (empreinte de lecture IA 2A) et version persistée de programme. Ne pas considérer les migrations proposées comme exécutées.

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:970 -->

## 9. Dépendances, séquencement et recette

1. **Inventaire actuel** : vérifier les classes Services/Repositories/API et le schéma effectivement déployé ; relever les migrations appliquées.
2. **Contrats métier** : figer règles de capacité, crédits, annulation, versionnement, permissions et erreurs ; appliquer Q011 synchronisé avec B2.
3. **Persistance minimale** : comparer l'existant aux invariants ; proposer uniquement les évolutions SQL indispensables, avec audit de données et rollback.
4. **Services atomiques** : implémenter d'abord réservation/crédits et programme/propositions ; contrôles de concurrence et d'idempotence.
5. **API/outils IA** : publier les outils après stabilisation des Services ; confirmations, permissions, minimisation et reçus.
6. **Client Expo** : intégration conversationnelle, choix, consentements, statuts, alternatives et fallback vers interfaces classiques.
7. **Recette** : tests unitaires et d'intégration réels MariaDB, Redis, OpenAI, Expo ; tests de concurrence, doubles demandes, interruptions, crédits, permissions intercentres, conflits de version et douleur.
8. **Pilote** : activation par centre/capacité, métriques d'erreur, retour arrière, puis généralisation.

**État historique IA 2A :** 177 tests réussis, 3 ignorés sur 180. **Mise à jour au 16 octobre 2026 :** extensions IA 2B A–D codées et testées isolément ; rapport final : 245 tests recensés, 242 réussis, 0 échec, 3 ignorés (Redis réel). Verdict CODE PARTIAL : fournisseur Push mobile non raccordé, historiques non qualifiés, limites de parcours et recette réelle MariaDB/Redis/OpenAI/Push en attente. Ne pas assimiler code livré et recette de production.

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:983 -->

## 10. Critères d'acceptation prioritaires

- Aucun utilisateur ne peut contourner permissions, rattachements et restrictions par la conversation.
- Aucune réservation en double, aucun double débit ni double remboursement sur retry/concurrence.
- Toute action annoncée comme réussie dispose d'un résultat backend confirmé.
- Les propositions partielles et les conflits de versions n'écrasent jamais une décision du coach.
- Aucune donnée de performance, disponibilité ou solde n'est inventée.
- Les signalements de douleur déclenchent le circuit de sécurité, indépendamment des contestations.
- Une panne de l'IA ne bloque pas les parcours classiques.
- Une capacité IA peut être suspendue par l'administration, y compris dans un centre pilote.
- L'audit permet d'identifier acteur, origine IA, action et résultat sans stocker systématiquement les conversations complètes.

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:995 -->

## 11. Points restant à vérifier avant développement

1. **Q011 synchronisé avec B2 le 16 octobre 2026** : conflit documentaire résolu ; appliquer la règle définitive de validité à la réservation et de protection des crédits immobilisés.
2. **Exhaustivité B1–B6** : rapprocher ce brief des réponses originales pour garantir chaque détail et chaque numéro ; ne pas prétendre que la synthèse thématique remplace le registre brut.
3. **Schéma réel déployé** : export fourni et deltas de migrations peuvent différer du serveur.
4. **Champs, index, contraintes et classes** : inspecter les fichiers nécessaires **un par un** avant proposition de code.
5. **Politiques chiffrées** : valeurs exactes des offres, pénalités, durées, délais, extensions et limites doivent provenir des configurations/contrats validés, jamais être inventées.

---

**Décisions de clôture :** B6 arrêté à B6.71 ; B7 clôturé à B7.10 ; B8 clôturé à B8.13. Ces décisions constituent le périmètre fonctionnel durable IA 2B.


---

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:1227 -->

## Conflits hérités à ne pas résoudre silencieusement

- **Crédits et absence :** les anciens documents D3/D5 décrivent des décisions du coach ; MOVEE Q013–Q015 définit une politique réseau avec exceptions et restauration auditée. L’ancien comportement ne devient pas automatiquement la règle MOVEE.
- **Réseau :** l’ancien produit cible des Personal Trainers et lieux partenaires ; MOVEE cible centres franchisés, studios satellites et machines connectées (Q001–Q007, Q026–Q042).
- **Capacités IA :** les anciens catalogues d’outils ne constituent pas une autorisation de publication ; seul le registre natif contrôlé et versionné est applicable (Q088–Q093).
- **Rémunération :** les anciennes commissions liées à la séance ne suffisent pas à démontrer la compensation interfranchises et les contrats multiples (Q016–Q025, Q060–Q063).

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:1234 -->

## Paramètres non encore fixés

Délais d’annulation, seuils de validation des séances, barèmes de pénalités et de compensation, calendrier de clôture, quotas, durées de rétention, limites sportives, partenaires de paiement, protocoles machines, seuils go/no-go et règles nationales doivent être décidés explicitement. **Ne pas inventer de valeurs par défaut.**


### Décision utilisateur — durées et plages réservables, 26 octobre 2026

Valeurs initiales paramétrables Backend : séance individuelle60min, cours collectif
60min, découverte60min, bilan périodique30min. Aucune assimilation aux modes
techniques autonome/accompagné ou aux types commerciaux unité/pack/abonnement.
Aucun écrasement des durées acquises ni déplacement des réservations existantes.
Par centre/fuseau IANA, paramétrer premier début et dernière fin autorisés des
séances, en conservant jours, fermetures et exceptions. Aucun horaire chiffré par
défaut décidé ; distinguer réservation et accès physique. Une séance entière doit
tenir dans sa plage. Code, paramétrage et application non effectués à cette prise
en compte. Analyse et propositions à valider :
[Contrat de paramétrage Booking livré ; étude préparatoire retirée](../movee-app/docs/BOOKING_SETTINGS_DELIVERED_CONTRACT.md).

Suivi de la décision durées/plages, 26 octobre : code Backend et tests isolés
livrés, administration préparée mais non installée. Les quatre références métier
restent distinctes des types commerciaux et des modes de coaching. Seule la
séance individuelle explicitement qualifiée s’appuie sur le parcours Booking
livré ; collectif, découverte et bilan périodique ne deviennent pas réservables
par le seul paramétrage de leur durée. Aucune donnée acquise ni recette locale
modifiée. Contrat et limites : docs/BOOKING_SETTINGS_DELIVERED_CONTRACT.md.

### Préférences hebdomadaires et suggestions — décision du 26 octobre 2026

Recueil explicite de plusieurs jours/heures préférés pendant la phase de découverte,
évolution contrôlable avec l’IA, réglage classique sans IA et aide à la réservation
fondée sur les disponibilités réelles du Backend. En manuel :3à5 propositions
correspondantes si disponibles, puis Choisir plus vers le calendrier existant avec
contexte conservé. Une sélection reprend le même aperçu signé/consentement/writer ;
aucune retenue, récurrence ou réservation automatique. Préférences exprimées et
habitudes inférées distinctes, contrôle utilisateur selon Q046/AR06. Le recueil en
phase de découverte ne livre pas la prestation discovery_session. Le lot centre
Bordeaux08:00–21:00 ne doit pas être appliqué pendant cette préparation.

Validation du codage v1 le26 octobre2026 : préférences de même poids, heure locale
exacte sans arrondi, fuseau IANA par entrée, au plus5 correspondances réelles dans
une fenêtre maximale14jours et l’horizon acquis ; une ou deux restent affichées
comme telles. Adaptation explicit_only, sans apprentissage automatique ni
reconstruction après retrait depuis un ancien fil. Les limites/DTO du contrat
proposé constituent la base validée de ce premier lot.

Services, transports et garde d’intention structurée actuelle de l’assistant codés
et testés en isolation. Contrat effectif :
[docs/MOBILE_BOOKING_PREFERENCES_DELIVERED_CONTRACT.md](../movee-app/docs/MOBILE_BOOKING_PREFERENCES_DELIVERED_CONTRACT.md). À la date de ce paragraphe de préparation, les deux tables privées étaient non installées ; ce statut a été remplacé par l’installation autorisée du26octobre décrite dans la référence technique App. Aucun état de préférences par défaut n’est initialisé par la consolidation.
L’application SQL exige un plan concret et une autorisation distincte. La disponibilité locale doit être vérifiée selon la migration appliquée et les contrats actuels ; cette phrase historique n’est pas un diagnostic de la base présente. L’IA n’est pas activée par cette consolidation.
La proposition historique reste dans
[docs/MOBILE_BOOKING_PREFERENCES_CONTRACT_PROPOSAL.md](../movee-app/docs/MOBILE_BOOKING_PREFERENCES_CONTRACT_PROPOSAL.md).

### Décisions utilisateur — 27 octobre 2026, administration groupée

Adhérents et Coachs : retenir les affiliations courantes de rôle6 et rôle5,
cumulables, sous intersection avec droits et périmètres actuels. Ne pas qualifier
une personne par le rôle historique du compte ni par une disponibilité.

Pour ce lot, engagements et ledger restent consultables au siège habilité ; pas
de scope financier franchisé reconstruit à partir des rattachements actuels.
Les propositions d’habilitations et les installations de Pages nécessitent leurs
validations séparées. Ces décisions ne constituent pas une preuve d’installation.
