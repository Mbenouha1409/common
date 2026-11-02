# MOVEE Mobile — référence technique spécifique

Version de consolidation : 2 novembre 2026. **Référence centralisée validée ; anciennes copies retirées après accord utilisateur.** Lire d’abord [README.md](README.md), [règles communes](AGENTS.md), [fonctionnel global](MOVEE_FUNCTIONAL_REFERENCE.md) et [technique globale](MOVEE_TECHNICAL_REFERENCE.md). Les sections issues des anciennes références conservent leur date/statut ; un constat historique ne décrit pas l’installation actuelle.

## Point de reprise actuel

Source datée : [consolidation Mobile](../movee-mobile/codex/MOBILE_PAGES_CONSOLIDATION_MOBILE_RESULT.md), [consolidation appliquée App](../movee-app/docs/MOBILE_PAGES_CONSOLIDATION_APPLICATION_ACTIVATION_RESULT.md), [cadre partagé coach](../movee-mobile/codex/COACH_SHARED_PRESENTATION_MOBILE_RESULT.md). Contrat14, trente Pages ; anciens profils et routes retirés du transport courant selon ces rapports. Les corps historiques « profil9/11/12/13 habituel » ci-dessous ne sont pas à remettre en service. Reprise des intentions historiques via contrat actuel, sans ancien transport ou nouveau command_id automatique.

Session via gestionnaire existant ; UI générique, aucun rôle/UID/entité ni calcul métier pour reconstruire un écran. Langue/thème techniques ne sont pas des writes métier. Les78 T ne sont pas recopiés dans ce document : lire le registre fonctionnel. Les chronologies d’implémentation sont datées, ne pas les confondre avec des contrats actuels.

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:503 -->

## 1. Sources et responsabilités

### État local vérifié — 21 octobre 2026 : premier parcours de connexion

Le dépôt mobile contient un écran de connexion e-mail/mot de passe et une confirmation d’identité avec déconnexion. [src/lib/mobile-api.ts](../movee-mobile/src/lib/mobile-api.ts) appelle exclusivement les trois contrats existants `/api/mobile-auth/login`, `/me` et `/logout` ; aucun contrat d’inscription, récupération, conversation ou notification n’est ajouté. [src/hooks/use-mobile-session.ts](../movee-mobile/src/hooks/use-mobile-session.ts) utilise Expo SecureStore sur iOS/Android, revalide l’identité au retour au premier plan et respecte l’expiration absolue sans refresh token. L’aperçu web garde le jeton en mémoire uniquement. L’URL vient de `EXPO_PUBLIC_API_URL` ; HTTPS est exigé hors développement.

Les routes et capacités métier validées des thèmes 1–8 restent une cible, distincte de cet écran de connexion. Le stockage natif, l’installation sur téléphone et le parcours utilisateur complet restent à recetter sur appareils. Les tests du client API sont exécutables avec `npm run test:auth`. La connexion locale utilise une instance Redis éphémère sans RDB/AOF ; la configuration mobile du backend local est activée, l’assistant reste désactivé. Aucune mise en production ni intégration push n’est attestée par ce lot.

- `AGENTS.md` commun : méthode, autorisations, anti-invention.
- `MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md` : besoins et parcours mobiles.
- `MOVEE_APP_FUNCTIONAL_REFERENCE.md` et `MOVEE_APP_TECHNICAL_REFERENCE.md` : règles métier et contrats backend de référence.
- SQL MOVEE App : consulter les exports **dans le projet propriétaire** pour toute affirmation physique ; le mobile ne doit jamais accéder à SQL.
- MOVEE Biz : spécifications propres, à consulter pour un flux partagé réel, sans supposer de contrats Biz.
- MOVEE Motion : projet indépendant de machine de bilan corporel et de mobilité ; consulter ses propres référentiels avant toute hypothèse de protocole ou d’API.

**Propriété :** MOVEE Mobile possède l'interface, la navigation, les états d'écran, les permissions OS, le cache local, les notifications système et l'expérience utilisateur. MOVEE App possède API, authentification serveur, agent IA, Services métier, permissions, transactions et données persistantes.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:520 -->

## 2. Architecture cible

```text
MOVEE Mobile iOS / Android
  ├─ UI conversationnelle et composants structurés
  ├─ Parcours classiques (fallback IA)
  ├─ Gestion locale de session, état et réseau
  ├─ Permissions OS / notifications / médias
  └─ Client HTTPS authentifié
             │
             ▼
MOVEE App — API Flask
  ├─ Auth mobile, droits et scopes
  ├─ API métier classiques
  └─ Agent IA natif côté serveur → OpenAI
             │
             ▼
Services métier → Repositories → MariaDB
             └─ Redis pour tokens mobiles, quotas et contexte IA
```

**Décision MOVEE App :** applications iOS et Android développées et maintenues en interne ; **Expo est l'environnement initial de développement/test**, pas une obligation permanente de distribution ni un contrat API. Ne pas figer React Native, Expo Router, stockage ou bibliothèques comme implémentés sans lire le dépôt mobile.

Le client n'accède jamais directement à MariaDB, Redis, OpenAI, aux Repositories ou aux capacités internes de l'agent. Aucun MCP n'est nécessaire entre MOVEE Mobile et l'API Flask native ; l'ASGI/MCP historique est une intégration distincte.


**Contrainte d'usage T7.8 : MOVEE Mobile n'est pas utilisé pendant les entraînements.** Consultation des programmes et résultats enregistrés, réservations/plannings, échanges, assistant, notifications et informations personnelles autorisées constituent ses usages. Les machines enregistrent indépendamment via MOVEE App. Le cache, la performance et la continuité d'interface ne servent pas à suivre des exercices en direct ; aucune connexion machine, compteur, chronomètre ou reprise de séance physique n'est introduit.

Décisions T : voir le registre unique dans [MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md](MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md).

Décisions T : voir le registre unique dans [MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md](MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md).

Décisions T : voir le registre unique dans [MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md](MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md).

Décisions T : voir le registre unique dans [MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md](MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md).

Décisions T : voir le registre unique dans [MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md](MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md).

Décisions T : voir le registre unique dans [MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md](MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md).

Décisions T : voir le registre unique dans [MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md](MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md).

Décisions T : voir le registre unique dans [MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md](MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md).

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:682 -->

## 3. Configuration et activation côté backend

L'intégration repose sur trois activations distinctes validées et codées côté MOVEE App selon le dernier rapport Codex :

| Flag serveur | Rôle |
| --- | --- |
| `MOVEE_NETWORK_ENABLED` | Réseau métier |
| `MOVEE_MOBILE_ENABLED` | Authentification et API mobiles |
| `MOVEE_ASSISTANT_ENABLED` | Assistant OpenAI |

Sans valeur explicite, `MOVEE_MOBILE_ENABLED` hérite du flag réseau. L'assistant exige le mobile ; le mobile exige le réseau. Le mobile sans IA est une configuration supportée. Le mobile actuel dépend de Redis pour ses tokens et quotas, même sans IA ; OpenAI n'est requis que lorsque l'assistant est activé. Les paramètres doivent être validés côté serveur, non pilotés par l'application cliente.

**Statut :** correctif annoncé à 355 tests réussis, 0 échec et 3 tests Redis réels ignorés ; aucune recette d'intégration Redis/OpenAI/terminal réel attestée. La base `newapp` a été diagnostiquée en lecture seule conforme à la V1, sans provisioning initial au moment de la rédaction.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:696 -->

## 4. Contrat d'intégration API : inventaire à vérifier

Les routes suivantes proviennent du diagnostic du code MOVEE App ; **leur existence doit être vérifiée dans le dépôt et dans la version déployée avant de coder le client** :

| Route / groupe observé | Usage | Condition |
| --- | --- | --- |
| `POST /api/mobile-auth/login` | Ouverture de session | Réseau + mobile |
| `GET /api/mobile-auth/me` | Identité et contexte | Bearer mobile |
| `POST /api/mobile-auth/logout` | Révocation | Session mobile |
| `POST /api/assistant/message` | Conversation IA | Assistant activé |
| `/api/assistant/reset`, `/api/assistant/confirm` | Reprise / confirmation IA | Assistant activé |
| `POST /api/business-actions/record-session-set` | Saisie de série | Mobile, permissions |
| `POST /api/business-actions/ia2b/<operation>` | Opérations métier autorisées | Dispatch fermé, permissions |
| `POST /api/business-actions/ia2b-confirm` | Confirmation d'opération | Consentement et contrôle métier |
| `POST /api/business-actions/ia2b-result` | Consultation du résultat | Reçu et droits actuels |

**Attention :** les noms de routes ne définissent ni schéma JSON, ni codes d'erreur, ni contrats de pagination, ni versions. Ces détails doivent être extraits du code/API actuel, puis contractualisés avec MOVEE App avant implémentation. Ne jamais fabriquer un endpoint pour répondre à un besoin mobile.

**Lacune fonctionnelle identifiée :** `get_bookings`, `get_program` et `get_performance_history` sont liés au registre IA ; le CRUD Front ne supporte pas automatiquement l'authentification Bearer mobile. Une solution d'API classique doit être analysée et approuvée côté MOVEE App pour garantir B8.2 ; ne pas contourner via session web ou SQL.

### 4.1 Contrats nécessaires au thème 1 — à vérifier et contractualiser

- **Fil unique et historique (T1.6) :** rattachement du fil continu à l'utilisateur, récupération des échanges précédents, chargement progressif si nécessaire, durée de conservation et reprise après fermeture ou expiration. La présence de `conversation_id` ou d'une route de reset ne démontre pas une persistance durable ; aucune création manuelle de fil ni liste de fils n'est prévue dans l'UX.
- **Contexte utilisateur et capacités (T1.3, T1.5–T1.6) :** données autorisées pour le profil et le centre actifs, changements de contexte et conditions de restitution des échanges sans divulgation hors périmètre. Aucun format de contexte n'est imposé ici.
- **Informations prioritaires (T1.7) :** source, contenu autorisé, actualisation et règles de priorité à valider côté MOVEE App ; aucun endpoint ou calcul local de priorisation n'est inventé.
- **Disponibilité IA et secours (T1.8) :** signalement de l'indisponibilité et du rétablissement de l'assistant, distinction avec erreurs réseau/backend et couverture métier classique indépendante de l'IA. Aucun endpoint de santé ni mécanisme de sondage n'est présumé existant.

Ces contrats restent ouverts malgré la validation de l'expérience T1.1–T1.8. Les API métier classiques et celles de l'assistant doivent être séparées dans leurs responsabilités ; le secours ne doit pas appeler l'assistant pour obtenir ses données ou exécuter un parcours classique.

### 4.2 Contrats identité, comptes et profils — Thème 2

**Capacités constatées dans le code, lecture seule le 17 octobre 2026 :** `api/mobile_auth_api.py` et `services/mobile_auth_service.py`, dans MOVEE App, exposent les routes de connexion e-mail/mot de passe, identité et déconnexion déjà inventoriées. Le service émet un token opaque avec expiration absolue, conserve son digest dans Redis, vérifie les credentials courants à la résolution et révoque le token à la déconnexion. Aucun renouvellement n'est défini dans ces deux fichiers. Cela ne prouve ni un déploiement ni l'absence d'autres mécanismes ailleurs dans le backend.

`GET /api/mobile-auth/me` retourne actuellement `success`, `user_id`, `full_name` et `expires_at` dans le code consulté. `services/auth_context_resolver.py` relit les affiliations courantes côté serveur en mode réseau et ne prend pas de rôles déclarés par le client ; cela ne constitue pas encore un contrat publié de sélection du couple centre + profil. Les API consultées ne suffisent donc pas à construire ce sélecteur ni à établir le statut de vérification e-mail.

| Besoin validé | État du contrat MOVEE App pour le mobile |
| --- | --- |
| Inscription libre minimale (T2.1/T2.8) | API publique et acceptation des quatre informations initiales non vérifiées ; aucun endpoint proposé ici |
| Vérification e-mail (T2.7) | Statut, mécanisme de vérification et restrictions serveur avant vérification non vérifiés ; opérations sensibles concernées à préciser |
| Recherche de centre, demande et invitation (T2.2) | API, approbation et droits résultants non vérifiés ; contrôle conservé par le centre |
| Sélection centre + profil (T2.3/T2.4) | Contextes autorisés, sélection et propagation aux API/assistant à contractualiser |
| Session persistante (T2.5) | Connexion, expiration absolue et révocation constatées ; durée cible et renouvellement éventuel à contractualiser sans présumer un refresh token |
| Code e-mail de récupération (T2.6) | API d'émission, validation et nouveau mot de passe non vérifiées ; usage unique, expiration et limitation des tentatives à contractualiser |
| Modification de profil (T2.9) | Champs autorisés, API, règles métier et confirmations sensibles à vérifier |
| Paramètres essentiels sans IA (T2.9) | Déconnexion constatée ; couverture des paramètres sécurité/confidentialité/notifications à vérifier |
| Suppression du compte (T2.10) | Vérification d'identité, confirmation, traitement, conservation et effets sur les affiliations à contractualiser ; aucune suppression immédiate ou cascade supposée |

« Non vérifié » n'est pas une preuve d'absence. Les capacités non constatées doivent être examinées avec le projet propriétaire avant implémentation mobile ; aucune route, DTO, table ou colonne n'est créée par ce référentiel.

### 4.3 Contrats parcours adhérent — Thème 3 : à vérifier

Les décisions T3.1–T3.10 sont validées ; les besoins techniques induits ci-dessous ne démontrent pas une API existante. Les observations des sections précédentes et les capacités citées dans les audits ne suffisent pas à attester une couverture complète. Aucun nouvel audit d'implémentation backend du thème 3 n'est réalisé dans cette mise à jour documentaire.

| Décision | Besoin technique induit | Contrat MOVEE App restant à vérifier |
| --- | --- | --- |
| T3.1 | Consultations interactives des prochaines séances, programme, historique et performances | Données autorisées, contexte, historique et couverture classique Bearer indépendante de l'IA |
| T3.2 | Cartes/calendrier conversationnels et calendrier classique partageant les résultats métier | Disponibilités, recherche, réservation, crédits, autorisations et résultats confirmés |
| T3.3 | Déplacement sans annulation préalable imposée | Alternatives, cohérence transactionnelle/atomicité réelle, concurrence, idempotence, conséquences et récupération du résultat ; aucune API atomique supposée |
| T3.4 | Lecture mobile du suivi machine centralisé dans App, sans saisie manuelle imposée | Disponibilité, fraîcheur et synchronisation des informations enregistrées ; aucun protocole machine inventé |
| T3.5 | Graphiques interactifs et explications des performances | Séries de données, unités, comparaisons et indicateurs calculés/validés par App ; aucun calcul métier concurrent côté mobile |
| T3.6 | Programme structuré, détails développables et démonstrations disponibles | Séances, exercices, objectifs, consignes, prescriptions et accès autorisé aux médias existants |
| T3.7 | Deux circuits distincts selon le mode d'entraînement | Mode déterminé par App ; adaptation libre autorisée avec consentement et notification coach ; adaptation supervisée avec consentement adhérent dans les limites coach préautorisées, validation coach hors cadre/protections/objectifs globaux/restrictions (AR01) ; mécanismes existants à vérifier |
| T3.8 | Transmission et restitution des échanges coach–adhérent dans le fil | Permissions, confirmations, preuve d'envoi, origine des réponses et historisation ; aucun service de messagerie présumé |
| T3.9 | Interventions sur événements d'objectif/progression/régularité | Détection et règles App, données automatiques, préférences, restitution conversationnelle et notifications selon transport disponible |
| T3.10 | Accompagnement contextualisé entre séances sans questionnaire systématique | Contexte autorisé de reprise, régularité, rapprochement des séances, récupération/fatigue, règles et préférences applicables |

Les contrats doivent respecter l'identité et le couple centre + profil actifs du thème 2, les protections métier et les parcours classiques/repli du thème 1. Ne pas inventer routes, payloads, champs, tables ou services pour combler une lacune ; transmettre les besoins au projet propriétaire.

### 4.4 Contrats parcours coach — Thème 4 : à vérifier

**Décisions validées :** T4.1–T4.10, sans preuve d'implémentation. **Besoins induits :** présentations et contrôles ci-dessous. **Capacités vérifiées :** aucune capacité backend supplémentaire n'est attestée dans cette mission documentaire ; les observations antérieures conservent leur portée limitée. Les points ci-dessous restent à vérifier avec MOVEE App, sans invention de route, payload, DTO, table, colonne ou Service.

| Décision | Besoin technique induit | Contrat backend restant à vérifier |
| --- | --- | --- |
| T4.1 | Listes/fiches conversationnelles et répertoire classique | Adhérents autorisés, données consultables, recherche et filtres selon centre + rôle |
| T4.2 | Cartes proactives et ordre de priorité, notamment à l'ouverture | Détection des absences prolongées, stagnation, progression, demandes et échéances ; données, critères et permissions App |
| T4.3 | Conception et ajustements entièrement conversationnels, consultation avant application | Génération, modification, validation métier, autorisation, application et enregistrement des programmes |
| T4.4 | Cartes de propositions, décisions et sélection groupée | Propositions existantes, permissions, états, validation explicite de chacune, conditions individuelles, résultats et historisation ; aucun mécanisme groupé présumé |
| T4.5 | Planning conversationnel et calendrier classique | Consultation/modification, disponibilités, conflits, réservations et règles de déplacement |
| T4.6 | Disponibilités conversationnelles et écran classique | Horaires habituels, exceptions, indisponibilités/congés, conflits et conséquences sur séances existantes, sans replanification/annulation automatique supposée |
| T4.7 | Réception intelligente et consultation classique des échanges | Réception, regroupement/priorisation, transmission autorisée, origine, confirmations et historisation des messages |
| T4.8 | Bilans avec graphiques, commentaires, ajustements, validation puis partage | Production, données et indicateurs App, règles de déclenchement, validation et partage autorisé ; moteur non présumé opérationnel |
| T4.9 | États des relances automatiques et accompagnement à la réservation | Absences/annulations tardives établies par App, déclenchement, autorisations/préférences, droits et crédits ; aucun seuil, délai ou canal imposé |
| T4.10 | Présentation de l'autonomie et des accords nécessaires | Classification serveur des actions, permissions, confirmation contextuelle, validations sensibles et exécution effective |

Vérifier la cohérence de ces contrats avec T3.7 : mode d'entraînement déterminé par App, adaptation libre autorisée avec notification coach, et adaptations supervisées selon AR01 : consentement adhérent dans les limites coach préautorisées ; validation coach hors cadre, protections, objectifs globaux ou restrictions. Une sélection groupée ne supprime aucun accord requis. L’autonomie des relances n’étend pas les limites coach. Les priorités opérationnelles T4.2 ne remplacent pas les niveaux de sécurité existants.

Le chemin reste **MOVEE Mobile → API HTTPS authentifiée → MOVEE App → Services métier → Repository → MariaDB**. App orchestre opérations et assistant selon ses mécanismes disponibles ; Mobile ne se connecte directement ni à SQL, Redis, MCP ou aux machines et ne réimplémente ni calculs, ni détection métier, ni permissions serveur.

### 4.5 Contrats assistant IA — Thème 5 : à vérifier

**Décisions validées :** T5.1–T5.10. **Besoins induits :** contexte sélectif, orchestration, rendus vérifiables, voix et contrôles de mémoire. **Capacités vérifiées :** aucune capacité backend supplémentaire n'est attestée par cette mission documentaire ; les routes déjà inventoriées ne prouvent ni mémoire durable, ni moteur multi-actions, ni transport temps réel. Les douze contrats suivants restent à vérifier avec MOVEE App :

1. Conservation et récupération du fil unique et de son historique complet consultable (T1.6/T5.1).
2. Gestion de la mémoire sélective, informations durables pertinentes et cycle de vie, sans présumer stockage, résumé ou récupération existants (T5.1).
3. Récupération du contexte métier actualisé sous identité et centre + rôle authentifiés ; aucune autorité des souvenirs sur les droits (T5.1/T5.3).
4. Orchestration multi-opérations avec dépendances, poursuite selon résultats et bilan des réalisations/attentes/échecs (T5.2).
5. Classification des actions et validations contextuelles, avec contrôles et accords des programmes supervisés selon AR01 et relances autorisées sans validation systématique coach (T5.2/T4.9/T4.10).
6. Vérification des résultats et suivi des opérations ; correspondance des preuves serveur avec les états de présentation (T5.4).
7. Erreurs, alternatives, idempotence, vérification d'état incertain et reprise sans doublon ; garanties existantes à démontrer (T5.5).
8. Distinction réponses informatives sport/bien-être et actions métier, avec limites santé et sécurité (T5.6).
9. Gestion des préférences de communication explicitement modifiables, sans effet sur permissions ou règles (T5.7).
10. Accès autorisé aux données et indicateurs justifiant les recommandations, sans justification inventée (T5.8).
11. Intégration vocale bidirectionnelle temps réel, interruptions et continuité texte/voix du fil unique ; transport et fournisseur non sélectionnés (T5.9).
12. Consultation, correction et suppression autorisée des informations mémorisées, par conversation et accès classique, avec confirmation du résultat, confidentialité et traçabilité (T5.10).

Ne pas inventer route, payload, DTO, table, colonne ou Service. Aucune table spécifique IA ni modification de schéma n'est proposée. Le chemin **MOVEE Mobile → API HTTPS authentifiée → MOVEE App → Services métier → Repository → MariaDB** est conservé ; l'orchestration métier et l'intégration IA relèvent d'App, jamais de règles appliquées par le frontend ni d'accès direct à SQL, Redis ou MCP.

### 4.6 Contrats notifications et proactivité — Thème 6 : à vérifier

**Décisions validées :** T6.1–T6.10. **Capacités documentées côté App :** son référentiel technique décrit inscription/révocation d'appareils, chiffrement des tokens, préférences, outbox et worker codés ; fournisseur natif non sélectionné/raccordé. Une acceptation fournisseur ou ligne outbox ne prouve pas réception téléphone. Ces constats documentaires ne sont pas une nouvelle vérification du code, de la base ou d'un service réel ; leur couverture exacte doit être contrôlée avant intégration.

Dans le tableau, « documenté » renvoie uniquement à ces références ; tous les points restent à vérifier dans le code et les contrats actuels. Les besoins futurs ne sont pas seize fonctionnalités déjà implémentées.

| Point | Besoin ou contrat à vérifier | Statut de preuve et limite |
| --- | --- | --- |
| 1 | Inventaire réel des événements disponibles | Alertes métier documentées ; inventaire exhaustif et exposition mobile à vérifier |
| 2 | Persistance et cycle de vie des notifications | Outbox documentée ; cycle des événements consultables et états à vérifier, sans nouveau modèle physique |
| 3 | Destinataires, droits et périmètres | Responsabilité App confirmée ; couverture des contextes autorisés à vérifier |
| 4 | Préférences par catégorie, canal et tranquillité | Préférences documentées ; paramètres précis non contractualisés |
| 5 | Priorité, fréquence et regroupement | Règles de sécurité App documentées ; politique transverse et exceptions à contractualiser |
| 6 | Déclenchement proactif | Besoin validé ; moteur et couverture de détection non vérifiés |
| 7 | Appareils et destinations push | Inscription/révocation et protection des tokens documentées ; contrat mobile exact à vérifier |
| 8 | Émission, erreurs et suivi push | Outbox/worker documentés ; fournisseur non raccordé, suivi et recette terminal ouverts |
| 9 | Consultation du centre classique | Besoin validé ; contrat indépendant de l'IA non vérifié |
| 10 | Lecture, modification et synchronisation des états | Besoin validé ; états persistants et cohérence multi-appareils à contractualiser |
| 11 | Confidentialité et aperçus | Protection push documentée ; classification, divulgation et paramètres à définir/vérifier |
| 12 | Navigation contextuelle et actions rapides | Besoin validé ; identifiants, liens, actions et formats non vérifiés |
| 13 | Obsolescence et réconciliation | Besoin validé ; garanties serveur et concurrence à vérifier |
| 14 | Synthèses IA d'événements autorisés | Besoin validé ; données accessibles et mécanismes non vérifiés |
| 15 | Rappels et déclenchement | Besoin validé ; conditions et contrats non vérifiés, sans délai inventé |
| 16 | Messagerie coach–adhérent | Besoin validé T3.8/T4.7/T6.7 ; intégration, origine, accès aux originaux et contrats non vérifiés |

Préserver B6.64–B6.68 : passage Élevé avec push immédiat au coach, Prioritaire sans push systématique, autres règles inchangées. AR04 valide le push Élevé même pendant les heures de tranquillité MOVEE, sans contourner les refus/autorisations/restrictions iOS/Android ni garantir la livraison ; les modalités techniques restent à vérifier avec App. Aucune table IA/notifications, évolution SQL, route, payload, DTO, colonne ou Service n'est proposé ici.

### 4.7 Contrats fiabilité, hors connexion et performance — Thème 7 : à vérifier

**Décisions validées :** T7.1–T7.10 et exclusion d'un usage mobile pendant l'entraînement. **Références App consultées :** architecture serveur, tokens mobiles à expiration absolue, revalidation des habilitations, contrats de commandes/reçus et idempotence documentés ; Q034 vise le hors ligne limité des machines, pas un suivi mobile. Ces éléments ne démontrent aucune prise en charge générale du cache, des opérations différées ou des mises à jour mobiles. Aucun nouveau contrôle du code App ou service réel n'est effectué ici.

| Point | Contrat ou besoin ouvert | Niveau de preuve et vérification requise |
| --- | --- | --- |
| 1 | Inventaire des données autorisées hors connexion | Besoin T7.1/T7.3 ; inventaire exact non contractualisé |
| 2 | Validité et expiration locales | Besoin validé ; durées et protocole de revalidation ouverts |
| 3 | Compte, centre, rôle et permissions | Autorité/relecture serveur documentées ; contrats mobiles de changement/invalidation à vérifier |
| 4 | Opérations éligibles à l'attente locale | Besoin validé sous conditions ; liste non décidée, aucune commande rendue offline implicitement |
| 5 | Validation des opérations différées | Validations métier App documentées ; couverture différée/API à vérifier |
| 6 | Détection et résolution des conflits | Concurrence/protections App documentées ; couverture par opération à vérifier sans fusion universelle |
| 7 | Doublons et idempotence | Garanties de commandes documentées pour leur périmètre ; étendue aux opérations différées à vérifier dans le code |
| 8 | Résultat incertain | Commandes/reçus documentés ; contrats exacts de vérification et reprise à vérifier |
| 9 | Protection et purge locales | Besoin T7.4 ; stockage, chiffrement, cycle des clés et purge à étudier, aucun choix retenu |
| 10 | Session et expiration hors connexion | Expiration absolue documentée ; accès local, validité et revalidation à contractualiser, aucune révocation instantanée supposée |
| 11 | Compatibilité Mobile/App | Contrats versionnés cibles documentés ; politique et mécanisme effectifs non vérifiés |
| 12 | Migration locale après mise à jour | Besoin futur non contractualisé, avec protection des opérations en attente |
| 13 | Reprise après interruption système | Besoin validé ; capacités OS et persistance/récupération à vérifier |
| 14 | Chargement et cache | Besoin validé ; stratégie, pagination et préchargement à étudier |
| 15 | Versions minimales et appareils | Contraintes des versions réellement retenues à vérifier ; aucune version minimale ni liste décidée |
| 16 | Erreurs et refus métier | Contrats App à lire par opération ; sémantique et reprise mobile à vérifier |
| 17 | Corrélation incidents Mobile/App | Besoin de diagnostic ; contrat technique non vérifié, aucun identifiant inventé |
| 18 | Collecte/confidentialité des diagnostics | Besoin validé ; périmètre, contrôle des données et conservation non contractualisés |

Les dix-huit lignes ne sont pas des fonctionnalités livrées. Toute évolution backend doit être étudiée chez App ; aucune API, DTO, identité d'opération, table, colonne ou Service n'est défini ici. L'éligibilité locale ne remplace jamais l'autorisation et le résultat serveur.

### 4.8 Contrats accessibilité et expérience utilisateur — Thème 8 : à vérifier

**Décisions validées :** T8.1–T8.10. **Confirmé dans les références :** architecture API/Services, droits/contextes et validations serveur, cible Q104 d'accessibilité/adaptation et parcours classiques sans IA. Aucune réalisation des besoins suivants n'en découle. Aucun nouvel audit code/backend n'est effectué ; distinguer les capacités à vérifier et les besoins futurs non contractualisés.

| Point | Besoin ouvert | Niveau de preuve et vérification requise |
| --- | --- | --- |
| 1 | Accessibilité des composants utilisés | Besoin T8.1 ; code réel à vérifier : sémantique, focus, texte, interactions |
| 2 | Graphiques VoiceOver/TalkBack | Besoin validé ; rendus/alternatives à vérifier, aucune conformité acquise |
| 3 | Préférences système et choix applicatifs | Besoin T8.2/T8.8 ; articulation et conflits à analyser |
| 4 | Stockage/synchronisation de préférences de compte | Besoin validé ; capacités backend non vérifiées, aucun schéma générique acquis |
| 5 | Capacités natives disponibles | Environnement/appareils réels à vérifier avant choix d'intégration |
| 6 | Permissions calendrier/caméra/partage/voix | Besoin T8.3 ; permissions nécessaires à vérifier par plateforme et capacité |
| 7 | Contenus conversationnels structurés | Cible documentée ; formats API et composants accessibles réels à vérifier |
| 8 | Recherche classique/contextuelle | Besoin T8.5 ; backend par périmètre à vérifier, aucun index/endpoint global acquis |
| 9 | Contexte/progression de découverte | Besoin T8.6 ; données disponibles et persistance éventuelle non contractualisées |
| 10 | États d'exécution d'action | Résultats/reçus App documentés ; couverture et contrats exacts à vérifier |
| 11 | Lecture/modification des paramètres | Besoin T8.8 ; API/capacités backend non vérifiées |
| 12 | Base de connaissances/centre d'aide | Besoin T8.9 ; contenus et disponibilité à vérifier |
| 13 | Contact support humain | Besoin validé ; canal non contractualisé, aucun ticketing présumé |
| 14 | Transmission des diagnostics au support | Besoin validé ; accord, minimisation et conditions non contractualisés |
| 15 | Événements d'usage mesurables légitimement | Besoin T8.10 ; inventaire/finalités à valider avant collecte |
| 16 | Consentement/préférences de confidentialité | Besoin validé ; modalités et mécanismes à vérifier/définir |
| 17 | Conservation/suppression des mesures | Besoin futur non contractualisé, aucune durée inventée |
| 18 | Frontière diagnostics T7.10 / analyse produit T8.10 | Distinction validée ; modalités et contrôles à définir |

Ces points ne sont pas un inventaire de fonctionnalités existantes. Aucun endpoint, DTO, Service, schéma SQL, fournisseur ou SDK n'est défini ; tous les contrats ouverts des thèmes antérieurs restent conservés.

### 4.9 Contrats des périmètres validés AR05 — à formaliser

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

Les validations de périmètre ne prouvent ni routes, ni fournisseur, ni réalisation. Aucune transaction marketplace, gestion administrative B2B ou demande/export de portabilité n’est intégrée au Mobile. L’orientation IA vers les canaux externes n’exécute pas leurs opérations. La suppression de compte T2.10 reste distincte de la portabilité externe AR05.9.

**AR05 :** capacités de lecture/action par profil et permission, confirmations contractuelles/financières, pièces justificatives, modération, parrainage, canal externe marketplace/B2B/portabilité et internationalisation V1.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:911 -->

## 5. Authentification et sécurité

- Utiliser uniquement les mécanismes mobiles officiellement exposés par MOVEE App ; ne pas réimplémenter la preuve HMAC serveur côté client.
- Conserver le token opaque dans un stockage sécurisé adapté à la plateforme **après choix de bibliothèque validé** ; ne pas le mettre dans les logs, analytics ou URL.
- Envoyer les appels en HTTPS, Bearer selon contrat vérifié ; refuser les certificats non valides en production.
- Gérer expiration, révocation, reconnexion, changement de profil/centre et refus d'accès sans persister des droits obsolètes.
- Ne pas stocker le secret `MOBILE_AUTH_HMAC_SECRET`, `OPENAI_API_KEY`, les credentials MariaDB ou Redis dans l'application.
- Appliquer la minimisation des données et supprimer le cache sensible à la déconnexion ou au changement de contexte.
- Traiter les réponses 401/403/409/429/503 selon leur sens **après confirmation du contrat serveur** ; ne pas inventer de sémantique d'erreur.
- Ne jamais considérer l'état de l'UI comme une preuve de permission métier ; revalidation serveur à chaque opération.

### 5.1 Session persistante et protection locale (T2.5)

La première connexion utilise e-mail et mot de passe. Maintenir ensuite la session de manière sécurisée pour éviter les reconnexions inutiles, uniquement dans les limites d'expiration et de révocation du serveur. Conserver les tokens dans un stockage sécurisé ; le choix de bibliothèque reste soumis à validation technique. Ne pas déduire de cette exigence l'existence d'un renouvellement automatique ou d'un refresh token. À la déconnexion, nettoyer les éléments d'authentification et les données locales sensibles ; après expiration ou révocation, ne plus traiter l'état local comme une session autorisée.

Face ID, Touch ID ou biométrie Android sont facultatifs et protègent l'accès local. Un déverrouillage biométrique ne prolonge pas une session expirée, ne contourne pas une révocation et ne remplace pas l'authentification serveur. Aucun SDK ou mécanisme de renouvellement n'est imposé ici.

### 5.2 Inscription, vérification et récupération (T2.1, T2.6–T2.8)

Prévoir les parcours d'inscription avec prénom, nom, e-mail et mot de passe seulement, puis de complétion progressive. La création du compte n'accorde pas de droits sur un centre. Le client doit pouvoir représenter une session immédiatement ouverte après inscription avec e-mail non vérifié et capacités limitées ; MOVEE App reste responsable de leur restriction effective, notamment avant rattachement effectif et opérations sensibles contractualisées.

La récupération du mot de passe permet demande du code e-mail temporaire à usage unique, saisie du code et définition du nouveau mot de passe dans l'application. Génération, validation, expiration, limitation des tentatives et sécurité relèvent exclusivement de MOVEE App. Les contrats restent ceux à vérifier en section 4.2 ; le mécanisme de vérification e-mail n'est pas déduit de celui de récupération.

### 5.3 Modifications et suppression du compte (T2.9–T2.10)

Les modifications personnelles et sportives, principalement conversationnelles, passent par les API autorisées et les confirmations proportionnées. Prévoir les paramètres essentiels sécurité, confidentialité, notifications et déconnexion, ainsi que la demande de suppression, en parcours classiques indépendants de l'assistant. La suppression exige vérification d'identité et confirmation explicite avant traitement serveur autorisé. Le client ne commande aucune cascade SQL ni suppression physique immédiate ; les données éligibles, conservations obligatoires et effets sur les affiliations restent à contractualiser.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:938 -->

## 6. Client réseau et contrats typés

**Cible technique proposée, à valider avec le dépôt mobile :**

- Une couche d'accès API centralisée avec configuration d'URL par environnement.
- DTO typés et validateurs de réponse pour messages, cartes, commandes, confirmations, reçus et erreurs.
- Contrats versionnés et tests de compatibilité entre les projets MOVEE Mobile et MOVEE App.
- Identifiant stable d'opération / clé d'idempotence selon le contrat serveur pour toute commande à effet métier.
- Timeout, annulation et retry limités ; aucune répétition automatique d'une commande non démontrée idempotente.
- Traces techniques sans données sensibles ; corrélation avec les identifiants de requête autorisés.

La validation d'une proposition ne constitue pas la preuve d'exécution. Pour les réservations, les résultats et reçus durables appartiennent au backend ; le client présente les états et les confirmations reçus.

**Qualité de contrat :** formats et erreurs API, idempotence des actions sensibles, authentification Bearer, pagination, localisation, scénarios de tests iOS/Android et absence de dépendance à une route inventée.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:953 -->

## 7. Architecture UI : modules de responsabilité

**Découpage logique proposé, non noms de fichiers/classes imposés :**

1. **Session et contexte :** login, profil actif, centre, déconnexion, expiration.
2. **Accueil :** synthèse proactive issue des données autorisées.
3. **Conversation :** messages, streaming si le contrat le permet, cartes de résultats, suggestions, questions ciblées.
4. **Actions et consentements :** résumé des conséquences, confirmation, attente, reçu, reprise.
5. **Réservations :** créneaux, détails, alternatives, annulation, remplacements.
6. **Crédits :** soldes, allocations et mouvements serveur.
7. **Programmes et séances :** exercices, séries, progression, historique et protections.
8. **Demandes coach / sécurité :** réévaluations, restrictions, priorités et réponses autorisées.
9. **Notifications :** boîte de réception, préférences, enregistrement et révocation appareil.
10. **Parcours classiques :** navigation indépendante de l'IA pour les opérations supportées.

Les composants métier doivent être réutilisables entre conversation et écrans classiques (T1.4) et consommer la même source métier serveur ; aucune règle de calcul concurrente dans le client.

### 7.1 Navigation Expo Router (T1.1–T1.5)

Utiliser **Expo Router** pour la navigation, avec routes et layouts dans [src/app/](../movee-mobile/src/app) et composants/état hors des fichiers de routes. La conversation constitue l'écran principal pour adhérent et coach. Aucune barre d'onglets permanente n'est prévue : un bouton ouvre le menu latéral coulissant, accessible sur iOS et Android, adapté aux capacités serveur du profil actif et refermé après sélection.

Les écrans métier restent indépendants de l'assistant et sont accessibles directement depuis le menu ou les cartes interactives. Les informations simples restent dans le fil ; les détails et opérations complexes utilisent ces écrans dédiés avec les validations métier existantes. Les écrans métier proposent un bouton IA flottant, discret et identifiable, de retour direct au fil ; la navigation arrière classique est conservée. Le menu reste disponible sans IA.

Le mécanisme concret du panneau latéral doit être choisi dans le socle Expo Router existant ; aucune nouvelle bibliothèque n'est imposée par ces décisions. Les onglets de démonstration actuels ne constituent pas la navigation cible ; leur remplacement relève d'un futur lot de code autorisé.

### 7.2 État de navigation, fil et contexte (T1.5–T1.7)

Le cycle de vie de la conversation doit être indépendant du montage des écrans métier : la navigation ne doit ni vider le fil ni créer un nouveau fil. Chaque utilisateur dispose d'un fil unique continu, sans liste de fils ni création manuelle. Le retour par le bouton IA conserve l'historique et le contexte disponibles ; la consultation des anciens échanges en remontant dans le fil dépend du contrat de récupération à vérifier en section 4.1.

Séparer l'état de navigation, l'état conversationnel et le contexte utilisateur autorisé. Leur conservation ne doit pas contourner la purge de données sensibles à la déconnexion ou les contrôles lors d'un changement de profil/centre. Aucune bibliothèque de gestion d'état ni stratégie de persistance locale n'est décidée ici.

La zone compacte d'informations prioritaires est rendue en haut de l'accueil conversationnel, distinctement de la liste des messages, avec ouverture ou masquage des informations. Elle consomme les données et règles autorisées par le serveur ; elle ne synthétise pas une priorité métier locale.

### 7.3 Disponibilité de l'assistant et secours (T1.8)

Gérer séparément disponibilité de l'assistant, connectivité et disponibilité des API métier. Lors d'une indisponibilité IA, présenter automatiquement un accueil simplifié avec accès aux réservations, programmes, planning et fonctionnalités coach selon les capacités autorisées. Son rendu, son menu et ses accès métier ne dépendent pas d'une réponse de l'assistant.

Lorsque l'assistant est rétabli, rendre la conversation de nouveau accessible avec l'état disponible selon T1.6, sans imposer une nouvelle conversation. Une panne du réseau ou du backend reste signalée comme telle : le secours n'invente ni données disponibles ni succès d'opération. Les critères de détection et de rétablissement restent à contractualiser (section 4.1).

### 7.4 Contexte centralisé centre + profil (T2.2–T2.4)

Gérer centralement le couple centre actif + profil actif, distinct de l'identité authentifiée. Les affiliations, les profils disponibles et les permissions sont vérifiés par MOVEE App ; le client ne déclare pas un rôle comme preuve de droit. Permettre le changement de centre et de profil sans déconnexion ni nouvelle connexion selon le contrat serveur à établir.

À chaque changement, invalider les données liées au contexte précédent et empêcher qu'une réponse encore en cours issue de cet ancien contexte soit réutilisée dans le nouveau. Actualiser les données autorisées et adapter navigation, actions, cartes, accueil, informations prioritaires et assistant au couple sélectionné. Le contrat de propagation du contexte vers les API reste à vérifier ; aucun champ de requête ni mécanisme serveur n'est présumé.

Cette invalidation respecte le fil unique T1.6 : elle ne crée pas de conversation supplémentaire et ne vaut pas suppression de l'historique serveur. La restitution des échanges et du contexte conversationnel doit respecter les permissions courantes ; le contrat de récupération reste ouvert en section 4.1.

Les parcours de recherche de centre, demande de rattachement et acceptation d'invitation sont séparés de l'obtention effective des droits. Prévoir également l'état d'un compte sans rattachement effectif et/ou non vérifié, limité à ses capacités serveur : ne pas lui attribuer artificiellement un centre ou un profil autorisé. Les paramètres essentiels et la suppression du compte restent accessibles sans assistant selon les sections 5.2–5.3 et T1.8.

**AR03 — Centre contractuel unique, centres accessibles multiples, centre actif.** Le centre actif est un contexte opérationnel choisi, jamais une mutation contractuelle ; les droits et l'éligibilité sont revérifiés côté App à chaque action.

**Identité/centres :** centre contractuel, liste des centres accessibles, centre actif et contrôles d'éligibilité par action ; invalidation du contexte à la révocation.

### 7.5 Présentation du parcours adhérent (T3.1–T3.6)

Réutiliser les composants métier entre fil et parcours classiques : consultations d'activité, cartes de disponibilité, calendrier interactif, programme structuré, détails d'exercice et démonstrations disponibles. Ne pas ajouter de tableau de bord général « Mon activité ». Maintenir un calendrier classique et les consultations nécessaires sans IA, via les contrats métier vérifiés, avec navigation Expo Router et secours T1.8.

Hors entraînement, le mobile consulte les informations enregistrées par les machines et centralisées dans App, sans suivi de séance en direct ni saisie manuelle imposée des séries, répétitions ou charges. La route de saisie déjà inventoriée reste une capacité backend à distinguer du parcours cible, sans créer ici un nouveau scénario obligatoire de saisie.

Les graphiques interactifs présentent l'évolution, les comparaisons entre séances et les indicateurs fournis par App ; les calculs métier appartiennent à App, le rendu à Mobile. Aucun moteur graphique ou nouvelle dépendance n'est imposé sans validation technique. Le déplacement d'une réservation attend un résultat serveur cohérent ; le client ne l'implémente pas par une annulation et une recréation indépendantes.

### 7.6 Adaptations, échanges et accompagnement (T3.7–T3.10)

Le serveur détermine le mode d'entraînement et les capacités. Conserver deux circuits distincts : en libre, adaptation autorisée avec consentement adhérent, sécurité et notification coach ; en suivi coach, adaptation dans les limites préautorisées avec consentement adhérent, validation coach hors cadre/protections/objectifs globaux/restrictions selon AR01. L'IA ne choisit pas le mode et ne contourne pas les Services métier, protections, restrictions ou contrôles de concurrence. Vérifier les mécanismes existants avant de nommer un statut ou un contrat de proposition.

Le rendu distingue les réponses générées par l'assistant, les messages effectivement transmis au coach et les réponses coach reçues. Les preuves de transmission et l'historisation proviennent de MOVEE App ; l'envoi respecte les autorisations et confirmations applicables. Le fil unique reste conservé selon T1.6, sans inventer un canal ou un nouveau service de messagerie.

Les interventions proactives consomment les événements et règles App relatifs aux objectifs et performances automatiques ; les notifications respectent les préférences et les limites du transport documentées en section 9. L'accompagnement entre séances peut utiliser des questions ciblées sur reprise, régularité, entraînements rapprochés, récupération ou fatigue, sans questionnaire systématique ni sollicitation intrusive. Les conseils ne remplacent pas un avis médical et respectent le circuit de sécurité existant.

**AR01 — Autonomie encadrée des adaptations de programme supervisé.** L'IA peut appliquer une adaptation **dans les limites préautorisées par le coach** avec consentement de l'adhérent ; hors limites, exercices protégés, objectifs globaux ou restrictions de sécurité : validation coach selon les règles métier. Cette précision prévaut sur toute formule exigeant une approbation coach pour chaque adaptation.

**Programme/IA :** limites coach versionnées et vérifiées par Service, consentement adhérent, demandes hors cadre, refus et journal d'audit ; consultation classique indépendante de l'IA, écriture exclusivement IA.

### 7.7 Présentation et continuité du parcours coach (T4.1–T4.8)

Besoins de présentation réutilisables entre conversation et vues dédiées lorsque pertinentes : cartes adhérent, listes/fiches interactives, cartes de priorité et suivi, programme conversationnel, propositions avec actions de validation, calendriers, disponibilités/conflits, cartes de messages et conversations, graphiques et bilans. Il s'agit d'exigences UI, sans création de composants, fichiers source ou dépendances dans cette mission.

Conserver Expo Router, menu latéral, fil unique, retour IA et contexte centre + profil des thèmes 1–2. Le répertoire dédié couvre recherches complexes, filtres et consultation sans IA ; calendrier, disponibilités et consultation des échanges disposent aussi d'accès classiques indépendants de l'assistant. Ces vues ne peuvent dépendre d'un appel IA pour leurs données métier.

T4.3 impose l'option A : création et modification des programmes entièrement en langage naturel, proposition affichée dans le fil, ajustements successifs et consultation avant application. Les composants interactifs n'introduisent pas d'éditeur obligatoire. AR02 exclut un éditeur alternatif de création/modification sans IA : ces écritures sont exclusivement via IA ; leur consultation autorisée reste classique. Les autres parcours classiques nécessaires sont maintenus.

Pour T4.4, la sélection groupée est une facilité d'interface. Chaque proposition sélectionnée doit recevoir une validation explicite avant application et passer ses contrôles serveur de permissions, état et conditions. Ne pas confondre sélection, validation et résultat appliqué. Le protocole groupé et ses garanties de résultats/reprise restent à vérifier ; aucun endpoint, atomicité globale ou statut nouveau n'est présumé. Conserver les règles d'idempotence et de reprise des commandes déjà documentées.

Le calendrier résultant et les conflits de disponibilités sont présentés avant application, sans présumer d'annulation/replanification automatique. La boîte de réception distingue origine adhérent, envoi coach confirmé et suggestion IA ; les décisions de transmission relèvent d'App. Les bilans peuvent être commentés, ajustés et validés par le coach avant partage, sur performances machine centralisées et indicateurs App ; aucun moteur ni protocole de partage n'est tenu pour existant.

**AR02 — Création et modification de programme uniquement via IA.** En cas d'indisponibilité IA, consultation autorisée mais aucune création/modification. **Exception explicite à B8.2** ; les autres parcours classiques restent requis selon leur périmètre.

### 7.8 Actions automatiques et confirmations contextuelles (T4.9–T4.10)

Prévoir la restitution des états des actions automatiques uniquement à partir des résultats serveur, sans inventer leurs statuts. Les relances peuvent être automatiques sans sollicitation systématique du coach, dans les autorisations et préférences applicables. MOVEE App détermine absence ou annulation tardive ; aucun défaut de mesure machine ne suffit à établir une absence, et aucun seuil/délai/canal n'est imposé ici.

La classification et l'exécution restent côté Services métier : consultation autorisée directe, action courante explicitement autorisée potentiellement automatique, action sensible soumise à validation contextuelle avant exécution. Les adaptations IA de programmes supervisés suivent AR01, individuellement ou dans T4.4 : consentement adhérent dans les limites coach préautorisées ; validation coach requise hors cadre, pour protections, objectifs globaux ou restrictions. Aucune confirmation systématique de toutes les actions, aucun succès déduit d'un texte IA et aucun contournement des règles de réservation/crédits ne sont autorisés par cette autonomie.

La proactivité informative existante reste distincte du déclenchement d'une action automatique autorisée par App. Les cartes prioritaires, messages importants et relances respectent contexte actif, permissions, préférences et limites du transport push (section 9).

### 7.9 Accessibilité et présentation progressive (T8.1, T8.4, T8.7)

Prévoir VoiceOver/TalkBack, sémantique et labels accessibles, ordre de lecture/navigation, focus, texte dynamique, contrastes et réduction des animations. Cartes conversationnelles, graphiques, listes, calendriers et écrans classiques répondent aux mêmes exigences. Alternatives aux contenus exclusivement visuels, gestes complexes et conversation vocale : aucune fonction essentielle ne dépend exclusivement de voix, geste complexe ou animation. Aucune bibliothèque d'accessibilité ni conformité déjà acquise n'est présumée.

Afficher l'essentiel en priorité, détails développables et écrans dédiés pour le complexe, consultables sans IA. Réutiliser les composants entre fil et parcours classiques lorsque pertinent ; conserver contexte conversationnel, accessibilité et indication des données non actualisées, sans masquer/déformer les données App ni inventer un format API. Aucun composant créé ici.

États de présentation : action initiée, traitement en cours, action locale en attente, vérification serveur, action confirmée, refusée et résultat incertain. Ce ne sont pas des DTO existants. Une proposition approuvée n'est pas forcément appliquée. Retours proportionnés, étapes suivantes et progression si utile, accessibles sans animation obligatoire ; confirmations selon règles contextuelles, succès métier uniquement après résultat App confirmé.

**AR05.10 — localisation V1 :** prévoir les textes d’interface, contenus disponibles, réponses IA et notifications dans les langues retenues ; ne pas inventer de langues initiales ni de politique de repli. Les documents contractuels ne peuvent être affichés qu’en versions officiellement validées. Contrats de localisation et recette iOS/Android à formaliser, sans conformité ou traduction existante présumée.

### 7.10 Personnalisation et paramètres (T8.2, T8.8)

Respecter thème clair/sombre et préférences système d'accessibilité, choix explicites, réglages locaux et préférences de compte éventuellement synchronisées. Les adaptations selon rôle/usages restent modifiables et désactivables ; priorité aux choix explicites, aucun masquage de fonction autorisée ou changement de droits/règles. Respecter les exigences d'accessibilité ; étudier l'articulation et les conflits système/applicatifs sans inventer de priorité technique détaillée.

Prévoir espace classique complet sans IA et modification conversationnelle autorisée : valeurs actuelles, suggestions contextuelles, permissions, confidentialité et validations pertinentes. Paramètres d'appareil locaux, synchronisation des paramètres de compte seulement si contrat App disponible. Aucun moteur de personnalisation, schéma/API générique ou synchronisation de tous les réglages n'est présumé. Aucun changement imposé par l'IA contre un choix explicite.

### 7.11 Recherche, navigation et découverte (T8.5–T8.6)

Combiner recherche textuelle classique, conversation, menu latéral et raccourcis sous rôle/centre actifs : suggestions/résultats autorisés, résultats vides gérés et alternative fonctionnelle sans IA. Aucun index/endpoint global ni recherche locale révélant des données interdites. Les raccourcis/caches ne contournent pas App.

L'accompagnement initial utilise le contexte disponible, présente possibilités réelles, premières actions et conseils progressifs, reste ignorable/reprenable sans tutoriel bloquant. Respecter affiliation/permissions et cohérence assistant/classique ; ne pas annoncer une fonction indisponible ni imposer une persistance d'onboarding sans analyse.

### 7.12 Aide, support et mesure d'expérience (T8.9–T8.10)

Prévoir centre d'aide classique sans IA et aide conversationnelle adaptée à la navigation, sur fonctionnalités et erreurs métier réellement disponibles. Séparer cause vérifiée, hypothèse, solution proposée et action effectuée ; aucune cause inventée d'incident ou de refus. Le contact humain exige accord préalable à la transmission des informations nécessaires, minimisation et protection des données personnelles/conversations. Aucun fournisseur, ticketing ou API de support présumé.

Séparer télémétrie technique T7.10 et analyse produit T8.10 : finalités, données et règles propres. Retours volontaires, avis contextuels facultatifs, difficultés récurrentes, abandons et indicateurs d'usage uniquement lorsque autorisés, données agrégées adaptées et minimisées. Définir consentement/préférences, conservation/suppression et contrôle des informations collectées avant activation concernée. Aucune exploitation automatique des conversations privées en analyse produit, aucun fournisseur analytics sélectionné ni consentement/collecte opérationnelle supposés.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:1076 -->

## 8. Agent IA et rendus structurés

L'orchestrateur OpenAI reste côté Flask. Le client envoie la demande utilisateur, affiche la réponse et les composants structurés autorisés par l'API. Il ne choisit pas les capacités internes, n'envoie pas de requêtes OpenAI directes et ne déclenche pas d'action métier sans commande serveur explicite.

Les interfaces doivent prendre en charge :

- consultation immédiate ;
- question de clarification ;
- proposition en attente ;
- consentement explicite ;
- exécution en cours ;
- résultat confirmé / refusé / expiré / conflit ;
- alternatives et reprise contrôlée.

L'interface doit éviter les « succès optimistes » pour toute réservation, mouvement de crédit, adaptation durable ou décision coach. Le serveur reste source de vérité.

### 8.1 Contexte, mémoire et personnalisation (T5.1, T5.7, T5.10)

Séparer historique complet consultable du fil unique, messages récents/contextes transmis au modèle, mémoire sélective durable, données métier et données à conservation légale. L'envoi intégral de l'historique à chaque interaction n'est pas requis. Les objectifs, préférences et contraintes pertinents ne remplacent jamais les données métier actualisées ni le contexte authentifié centre + rôle ; droits et validations sont revérifiés par App.

L'adaptation de vocabulaire, ton, niveau technique, longueur et détail tient compte du rôle autorisé, expérience, préférences explicites et contexte. L'utilisateur peut modifier ces préférences. Leur consultation/correction/suppression doit être possible dans le fil et dans des contrôles classiques indépendants de l'IA. Seul un résultat App permet d'annoncer une modification effective. Effacer une préférence ne supprime pas automatiquement historique, données métier ou données conservées légalement. Périmètres, permissions, confidentialité, traçabilité et cycle de vie restent à vérifier avec App ; aucun stockage ou mécanisme de résumé/récupération n'est présumé.

**AR06 — Historique IA durable et mémoire sélective.** Historique, contexte éphémère et mémoire personnalisée distincts ; contrôle de consultation/correction/suppression et vérification des droits à chaque accès. Les données métier officielles demeurent dans MOVEE App.

**Conversation :** identité de fil, pagination et reprise de l'historique durable, isolation des droits, mémoire sélective corrigible/supprimable, règles de rétention et de minimisation ; stockage physique à vérifier avant toute proposition SQL.

### 8.2 Orchestration, clarification, suivi et erreurs (T5.2–T5.5)

Une demande multi-intentions nécessite identification des opérations, dépendances, consultations/actions autorisées, validations seulement lorsque requises, poursuite selon résultats et bilan réalisé/en attente/en échec. L'orchestration relève d'App selon ses mécanismes effectivement disponibles ; aucun moteur client ni multi-actions backend opérationnel n'est supposé. Conserver les deux modes T3.7, les accords requis par AR01/T4.4 selon le cadre de l’adaptation supervisée, les relances automatiques autorisées T4.9 et l'autonomie contextuelle T4.10, sans confirmation systématique.

La clarification exploite d'abord conversation, préférences disponibles, données métier et disponibilités réelles autorisées ; une question ne vise que l'information indispensable non déterminable fiablement. Ne pas fabriquer de disponibilité/préférence ni transformer une hypothèse en fait.

Le rendu adapte le suivi à la complexité : indicateur discret ou étapes importantes « En cours », « Terminée », « En attente de validation », « En échec ». Ces libellés sont des états de présentation, pas des statuts backend ni un protocole de suivi imposé. Associer toute réalisation annoncée à une confirmation App vérifiée ; ne pas confondre proposition, attente et exécution, ni envoi humain et contenu IA (T3.8/T4.7).

En cas d'erreur, expliquer sur les informations disponibles et présenter alternatives, correction ou reprise sûre. Vérifier côté App un résultat incertain avant toute nouvelle tentative ; aucune répétition aveugle de commande. Les garanties d'idempotence, vérification d'état et reprise doivent être établies par contrat, et non déduites des besoins de présentation.

### 8.3 Réponses informatives et justifications (T5.6, T5.8)

Prendre en charge les questions générales d'entraînement, nutrition, récupération, habitudes de vie et connaissances sportives, même hors fonctionnalité métier, sans assistant généraliste tous domaines. Distinguer réponse informative et action modifiant des données. Conseils santé prudents, sans diagnostic ni substitution à un avis médical ; protections de sécurité conservées.

Prévoir des justifications courtes développables et l'accès aux indicateurs autorisés utilisés, sur demande. Distinguer faits vérifiés, hypothèses et recommandations ; les mesures, résultats et critères justifiant une affirmation doivent être disponibles, sans fabrication. Ne pas exposer de données non autorisées ou de détails techniques internes inutiles.

### 8.4 Besoins de présentation assistant (T5.1–T5.10)

Besoins réutilisables : conversation unique et historique continu, indicateurs de traitement, états/résultats d'actions, cartes de validation contextuelle, erreurs/alternatives, justifications développables, consultation et contrôle de mémoire, interface vocale et bascule texte/voix. Aucun composant ou fichier source n'est créé ici. Les parcours classiques et le secours T1.8 restent indépendants de l'assistant, notamment pour contrôler la mémoire ; les modalités vocales sont à étudier en section 11.1.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:1122 -->

## 9. Notifications push et proactivité

Le backend MOVEE App a, selon le rapport, un mécanisme d'inscription/révocation des appareils, chiffrement des tokens, outbox et worker, mais **aucun fournisseur push réel raccordé**. Ne pas supposer que les notifications arrivent sur iOS/Android.

Contrat à stabiliser avec MOVEE App :

- permission OS demandée au moment opportun ;
- inscription/révocation d'appareil via API vérifiée ;
- liaison utilisateur/appareil et retrait à la déconnexion ;
- préférences et consentements ;
- payload minimal et absence de données sensibles sur écran verrouillé ;
- navigation vers l'objet métier après revalidation des droits ;
- déduplication et gestion des notifications périmées.

**À VALIDER :** fournisseur et SDK iOS/Android, stratégie de livraison, identifiants d'appareils et recette sur appareils physiques. Expo n'est pas une contrainte durable de fournisseur.

### 9.1 Responsabilités et chaîne logique cible (T6.1, T6.4)

Chemin conservé : **MOVEE Mobile → API HTTPS authentifiée → MOVEE App → Services métier → Repositories → MariaDB**. Mobile gère interface, réception/présentation push, permissions et mécanismes OS, navigation, actions rapides d'interface, réglages affichés, état UI réconcilié aux réponses serveur et protection des aperçus locaux. App gère destinataires/droits, règles métier et préférences métier, classification/priorité autorisées, déclenchement, états persistants, validité/obsolescence, résultats, confidentialité serveur et orchestration IA. Aucun transfert de ces responsabilités métier au client ; aucun accès direct SQL/Redis/MCP/capacités internes de l'assistant.

Chaîne conceptuelle, sans attestation d'implémentation : événement pertinent dans App → destinataires autorisés → application des préférences, confidentialité et priorités → choix des canaux appropriés → émission push si autorisée et possible → présentation dans le centre classique et/ou l'assistant → réconciliation des états et actions avec App. Aucun bus, broker, worker, scheduler, fournisseur, mécanisme de persistance ou de livraison supplémentaire n'est imposé. Les mécanismes historiquement documentés ne prouvent pas toute cette chaîne.

Distinguer événement vérifié, détection d'une situation, décision de notifier, génération éventuelle d'une formulation/synthèse, présentation et action métier demandée ensuite. La génération IA ne modifie ni droits, priorité imposée, confidentialité ni état réel. Une prédiction n'est pas une donnée métier confirmée ; absence non déduite du seul manque de données machine. Une notification autorisée peut être automatique sans validation systématique, mais n'autorise aucune action métier implicite.

### 9.2 Push et intégration OS — étude ouverte (T6.1, T6.6, T6.9)

Étudier permissions notifications iOS/Android, refus de permission, enregistrement et cycle de vie des destinations, association utilisateurs/appareils autorisés, changement de compte, déconnexion et révocation. Étudier réception au premier plan, arrière-plan et application fermée, ouverture depuis notification, contexte correct et actions rapides selon possibilités OS. Gérer push retardé, expiré ou non reçu et minimiser les données des payloads. Aucune capacité d'exécution arbitraire en arrière-plan n'est présumée lorsque l'OS la restreint.

Aucun fournisseur, SDK ou technologie de notifications n'est retenu ; Expo Notifications, APNs, FCM ou autres mécanismes pourront être étudiés séparément. Le push reste un canal d'alerte sans garantie de livraison ; ni appareil détenu ni destination push ne prouvent une autorisation métier.

### 9.3 Centre classique et présentation partagée (T6.1, T6.5, T6.10)

Prévoir liste chronologique ou priorisée, lu/non lu, détails consultables, regroupements, indication des événements traités/obsolètes, accès à l'événement ou action associée, actualisation après reconnexion ; filtres éventuels selon besoins validés. Le centre et ses accès nécessaires fonctionnent sans IA. Les états persistants proviennent d'App selon contrats à vérifier ; le cache local n'est jamais source de vérité.

Centre, zone prioritaire et fil unique peuvent présenter un même événement sous différentes formes sans créer plusieurs événements métier. Les non-urgents peuvent être regroupés par catégorie, pertinence, proximité temporelle et contexte ; préserver les originaux qui doivent rester consultables. Urgents individualisés et transmis rapidement sous règles de livraison/confidentialité, sans garantir réception. Les synthèses personnalisées adhérent/coach séparent faits vérifiés, interprétations et recommandations (T5.8).

### 9.4 Préférences, priorité, fréquence et rappels (T6.2–T6.5, T6.8)

Contrats à vérifier : catégories, canaux autorisés, périodes de tranquillité, préférences explicites, priorités métier, regroupement, limites de fréquence et exceptions autorisées. Aucun nom de catégorie, valeur technique ou énumération n'est défini ici. Les réglages classiques restent accessibles sans IA ; la personnalisation sur habitudes fiables et contexte sportif reste subordonnée aux préférences explicites et protections.

App définit/contrôle priorités et exceptions ; l'IA ne contourne pas librement les périodes de tranquillité. Rappels fondés sur préférences, type de séance, habitudes fiables, contexte temporel/sportif et changements effectifs de planning. Conseils de préparation, information de changement, proposition de report ou suggestion ne modifient aucune réservation. Aucun délai de rappel, prédiction d'absence ou automatisme de reprogrammation n'est imposé.

**AR04 — Push immédiat pour alerte de sécurité Élevé.** Exception aux heures de tranquillité configurées dans MOVEE, mais **jamais** aux refus/autorisations/restrictions iOS/Android ; émission ≠ livraison garantie. Les autres notifications respectent les préférences.

**Sécurité/push :** niveau Élevé établi par App, priorité et exception aux heures de tranquillité MOVEE, préférences ordinaires, permissions OS, identifiant d'événement, tentatives et état de livraison distincts.

### 9.5 Confidentialité, provenance et périmètre (T6.7, T6.9)

Contrôler destinataires et données autorisées, centre + rôle actifs lorsque pertinent, revalidation des droits avant ouverture et changement de permissions. Masquer par défaut les aperçus personnels sensibles, notamment écran verrouillé ; configuration des aperçus seulement dans les limites de protection, avec maintien des protections des contenus particulièrement sensibles même si les aperçus ordinaires sont autorisés. Tenir compte des réglages/possibilités iOS/Android, minimiser payloads, protéger cache et gérer purge/déconnexion. Classification exacte et politique de divulgation restent à vérifier/définir côté App ; un texte IA ou une préférence d'affichage ne confère aucun accès ni dérogation.

Pour la messagerie, distinguer message humain effectivement envoyé, résumé IA, suggestion IA et demande d'intervention humaine ; les originaux restent accessibles selon permissions. App conserve transmission et historisation T3.8/T4.7 ; les relances automatiques T4.9 restent autorisées dans leur périmètre. Mémoire sélective, historique conversationnel, notifications et données métier restent distincts : un contrôle de mémoire T5.10 ne modifie pas implicitement les événements de notification.

### 9.6 Actions rapides et continuité (T6.6)

Identifier sûrement l'événement, ouvrir au bon emplacement par Expo Router et reprendre le contexte pertinent du fil unique, sans transmettre de données devenues interdites. Vérifier droits, état métier, disponibilité, crédits et conditions actuelles via App avant action ; confirmer contextuellement si requis, puis afficher uniquement le résultat confirmé. Gérer opportunités expirées/indisponibles et sessions expirées sans présumer un succès. Aucun format de deep link, payload ou identifiant technique n'est imposé ; contrats à vérifier avant implémentation.

Un bouton n'est pas une autorisation. Les adaptations IA supervisées respectent AR01/T3.7/T4.4 : consentement adhérent dans le cadre préautorisé et validation coach lorsque requise, les relances autorisées sans accord systématique (T4.9), et autonomie/orchestration T4.10/T5.2 et reprise sûre T5.4–T5.5 restent applicables.

### 9.7 Synchronisation et résilience (T6.10)

Prévoir réconciliation lu/non lu et actions traitées entre appareils, limitation des doublons, récupération des événements non reçus en push, actualisation après perte réseau, contrôle des événements obsolètes, consultations multi-appareils, concurrence des actions, reprise après expiration de session et revalidation du contexte actif. Les états persistants et les résultats sont centralisés par App ; le mobile aligne son UI sur les réponses autorisées.

Ne pas conserver une place déjà prise comme disponibilité confirmée ni une demande traitée comme toujours en attente. Aucune synchronisation instantanée, livraison garantie ou sémantique exactement une fois n'est promise sans contrat démontré. Aucun algorithme de déduplication, identifiant technique, transport de synchronisation ou mécanisme de reprise existant n'est inventé.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:1186 -->

## 10. Offline, cache et synchronisation

La cible MOVEE App autorise des événements machines hors ligne dans un périmètre limité (Q034), **ce qui ne signifie pas que le mobile peut réserver ou modifier des crédits hors ligne**.

**Principes de cache et de synchronisation précisés par T7.1–T7.4 ; mécanismes et contrats encore ouverts :**

- Cache local limité aux lectures autorisées et identifié comme potentiellement obsolète.
- Interdire toute confirmation locale d'opération métier non confirmée par le serveur.
- Au retour réseau, rafraîchir identité, permissions, état des commandes et données affichées.
- En cas de retry, utiliser exclusivement les garanties d'idempotence du contrat API.
- Pour médias, performances et événements différés, définir séparément le protocole et la résolution de conflits avant implémentation.

**T3.4 — Frontière machines :** le suivi automatique relève des machines et de la centralisation par MOVEE App. Le chemin mobile reste **MOVEE Mobile → API HTTPS authentifiée → MOVEE App → Services métier → Repository → MariaDB**. MOVEE Mobile ne se connecte directement ni aux machines, ni à SQL, Redis ou MCP. Aucun protocole machine ou contrat de synchronisation n'est défini par cette exigence ; l'offline machine ne crée pas de droit d'écriture offline mobile.

### 10.1 Stockage, préparation et protections locales (T7.1, T7.3–T7.4)

Distinguer cache de consultation, état d'interface récupérable et persistance d'opérations en attente. Définir les données éligibles/exclues, minimisation, validité, expiration, fraîcheur affichée, protection, séparation compte et centre + rôle, changements de permissions, invalidation et purge. Préparer automatiquement les informations autorisées utiles aux prochaines consultations ; laisser choisir certaines données à conserver/supprimer localement. Les exemples programme/planning/réservations/dernières performances/préparation coach ne constituent pas une liste autorisée exhaustive et ne préparent aucun exercice en direct.

Chiffrer les données sensibles, protéger secrets et informations personnelles, isoler comptes/contextes, envisager exclusion offline des données particulièrement sensibles et déverrouillage système/biométrique optionnel (T2.5). Étudier la gestion des appareils perdus/compromis dans les limites réelles. Aucun choix de SQLite, AsyncStorage, SecureStore, chiffrement ou autre solution n'est imposé. Un appareil déconnecté ne peut connaître immédiatement les révocations distantes : contrats de validité/expiration/revalidation nécessaires, sans garantie de révocation instantanée. Les opérations métier restent contrôlées côté serveur.

### 10.2 Opérations locales, synchronisation et conflits (T7.1–T7.2)

États conceptuels de présentation possibles : locale non transmise, en attente de synchronisation, en cours de vérification, confirmée par App, refusée, en conflit, résultat incertain. Ce ne sont ni une énumération backend existante ni un protocole décidé. Aucune file persistante, API de synchronisation, DTO ou identifiant n'est présumé. Une interaction locale peut attendre seulement dans son périmètre autorisé ; aucune réservation, modification de crédit/solde ou autre effet métier n'est confirmé sans App.

Au retour réseau, revalider session, permissions, contexte métier et opérations, prévenir doublons, réconcilier avec App et informer clairement l'utilisateur. Distinguer modification toujours valide, devenue invalide, conflit résoluble selon règle métier, décision utilisateur et validation coach requise. App décide la résolution métier : pas de dernière modification gagnante universelle, fusion locale inventée, écrasement protégé ou arbitrage final par le modèle IA. Préserver T3.7/T4.4 ; une attente locale ne contourne pas ces validations. Les garanties d'idempotence et la vérification d'état incertain sont à confirmer par opération avant retry.

### 10.3 Cycle de vie, erreurs et continuité (T7.6–T7.7)

Décrire la reprise après appel, verrouillage, passage arrière-plan/premier plan, suspension OS, fermeture inattendue, redémarrage, perte/retour réseau et expiration de session. Restaurer dans les limites vérifiées navigation, formulaires, consultations, fil unique, opérations locales autorisées et vérification des résultats incertains ; aucune restauration garantie de tout état volatile et aucune synchronisation permanente en arrière-plan présumée sur iOS/Android. La reprise est une interaction UI, jamais une reprise d'exercice ; aucune série, répétition ou performance n'est fabriquée.

Distinguer perte réseau, indisponibilité API, timeout, session expirée, erreur de synchronisation, refus métier et résultat incertain ; messages compréhensibles sans données techniques sensibles. Récupération automatique seulement sûre, conservation des données locales autorisées, revalidation après reconnexion et reprise de session selon contrat. Un résultat incertain est vérifié chez App avant toute nouvelle tentative pour éviter double effet. Assistant facultatif pour expliquer, parcours classique sans IA conservé ; voix distante T5.9 non garantie offline.

### 10.4 Performance et adaptation aux appareils (T7.8–T7.9)

Prévoir chargement progressif, pagination lorsque pertinente selon contrat, contenus volumineux/graphiques/historiques adaptés, cache contrôlé et signalé non actualisé, préchargement contextuel, réduction des requêtes inutiles, navigation réactive et gestion des délais. Adapter au réseau et aux appareils moins puissants sans seuil chiffré ou bibliothèque imposés. Le cache n'est pas une confirmation métier en temps réel.

Les parcours essentiels programmes/réservations/performances/messagerie/informations autorisées doivent rester accessibles sur les smartphones iOS/Android effectivement compatibles avec les versions retenues de React Native/Expo. Étudier alternatives progressives pour les capacités exigeantes, notamment voix temps réel selon réseau/appareil ; ni toutes capacités natives universelles, ni versions minimales, ni liste d'appareils ne sont présumées. L'optimisation sert des consultations et interactions hors entraînement, jamais du suivi d'exercice.

### 10.5 Observabilité et confidentialité (T7.10)

Besoins : suivi des plantages, erreurs applicatives/réseau, ralentissements et synchronisation, journalisation technique minimale, corrélation Mobile/App, signalement utilisateur et contrôle des données envoyées au diagnostic. Définir collecte proportionnée, protection des informations personnelles et conservation. Ne collecter inutilement ni conversation IA, données personnelles adhérent, identifiants d'authentification, secrets techniques ou payloads sensibles. Aucun SDK/fournisseur de monitoring n'est sélectionné.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:1228 -->

## 11. Multimodal et capteurs

Q047–Q057 définissent une cible voix, photo, vidéo, analyse de mouvement, machines connectées et bilans corporels. Le client devra gérer permissions OS, consentement, minimisation, durée de conservation et compatibilité des appareils. **Aucun protocole de capture, de transmission, de stockage ou de calcul local/cloud n'est arrêté par ce document.** La conception nécessite un lot spécifique et des contrats validés avec MOVEE App. **MOVEE Motion** est un projet distinct pour la machine de bilan corporel et de mobilité : ne supposer ni liaison directe au téléphone, ni format de mesure, ni synchronisation backend, ni SDK sans examen et validation de ses référentiels.

### 11.1 Voix bidirectionnelle temps réel — exigences validées et étude ouverte (T5.9)

Le mode vocal naturel concerne adhérents et coachs : échanges bidirectionnels temps réel, réponses orales, possibilité d'interrompre l'assistant, passage libre texte/voix et continuité des échanges dans le fil unique. Les opérations métier autorisées restent accessibles avec les mêmes permissions et validations que le texte. La mémoire n'établit ni identité, ni centre, ni rôle.

Étudier avant toute sélection technique : autorisation native d'accès au microphone au moment nécessaire, capture/restitution audio, reconnaissance/synthèse vocales, latence et échanges bidirectionnels, interruption d'une réponse, cohérence texte/voix et contexte, interruptions système/réseau, protection et conservation des données vocales, compatibilité iOS/Android et repli vers le texte. Le refus de permission ou l'indisponibilité vocale doit permettre ce repli ; l'indisponibilité IA conserve le secours classique T1.8.

Une interruption audio n'est pas une preuve d'annulation d'une action métier : le contrat doit permettre de vérifier les résultats App incertains avant reprise. Ne sélectionner aucune bibliothèque, fournisseur, SDK, architecture de transport ou protocole de streaming ; ne présumer ni API temps réel existante ni connexion directe mobile-service IA. Les frontières existantes — intégration IA côté App, aucun accès direct OpenAI/SQL/Redis/MCP depuis le client — restent applicables. La technologie et le transport doivent être étudiés et validés séparément ; cette décision ne prouve pas une intégration vocale opérationnelle.

### 11.2 Intégrations natives contextuelles et facultatives (T8.3)

Étudier calendrier personnel, partage de documents, caméra, raccourcis, biométrie optionnelle et voix selon capacités réelles de l'environnement/appareil iOS/Android. Vérifier les permissions nécessaires pour chaque usage, les demander au moment utile, respecter refus/indisponibilité et proposer alternatives lorsque possible. Aucune activation facultative imposée ni accès permanent injustifié ; aucun SDK/bibliothèque choisi sans vérification.

Un ajout au calendrier ne confirme pas une réservation App, une permission OS ne donne aucun droit métier et un raccourci ne contourne pas les contrôles. Maintenir les alternatives accessibles sans voix et sans IA pour les parcours nécessaires. Ces possibilités ne sont pas des intégrations attestées et ne créent aucun suivi d'exercice en direct ; T7.8 reste conservée.

**AR07 — Mesures externes, résultats mobiles.** MOVEE Motion/dispositifs spécialisés acquièrent les mesures ; MOVEE App centralise les résultats validés et droits ; MOVEE Mobile restitue bilans et évolutions, sans connexion directe aux appareils.

**Bilans/Motion :** origine, validation, visibilité et évolution des mesures ; échange interprojet à contractualiser avec MOVEE Motion, jamais accès matériel direct depuis Mobile.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:1250 -->

## 12. Tests et recette

### Tests côté MOVEE Mobile

- Tests de composants et navigation iOS/Android.
- T1.1–T1.5 : accueil conversationnel adhérent/coach, absence d'onglets permanents, menu latéral accessible adapté aux capacités, fermeture après sélection, ouverture depuis menu/cartes et retour par bouton IA avec navigation arrière conservée.
- T1.6 : fil unique, absence de création manuelle/liste de fils, continuité après navigation et récupération des échanges précédents selon le contrat vérifié.
- T1.7 : zone prioritaire compacte et distincte du fil, ouverture/masquage et respect du contexte autorisé.
- T1.8 : bascule automatique vers le secours sans appel IA, maintien du menu, conversation à nouveau accessible au rétablissement ; distinction des pannes IA, réseau et backend.
- Authentification, token expiré, révocation, changements de rôle et de centre.
- Conversation et rendus structurés, états de chargement, erreurs et reprise.
- Double tap, perte de réseau et retry d'une commande à effet métier.
- Fonctionnement sans IA et sans clé OpenAI dans le client.
- Accessibilité, notifications, consentements et nettoyage du stockage local.
- Aucun secret ou donnée sensible dans logs, crash reports ou captures de test.

### Recette mobile identité, comptes et profils — Thème 2

- T2.1/T2.8 : inscription minimale, complétion progressive et absence de droits centre automatiques.
- T2.2/T2.7 : découverte et profil avant vérification, contrôle serveur des restrictions, demandes/invitations sans rattachement présumé.
- T2.3/T2.4 : contexte centre + profil centralisé, changement sans reconnexion, adaptation des écrans et assistant, invalidation du cache et rejet d'une réponse tardive de l'ancien contexte sans création de fil supplémentaire.
- T2.5 : stockage sécurisé, biométrie facultative strictement locale, maintien de session dans les limites du contrat, expiration, révocation et purge à la déconnexion.
- T2.6 : récupération intégrée par code e-mail, usage unique, expiration et limitations contrôlés par le serveur selon contrat.
- T2.9/T2.10 : modifications via API et confirmations proportionnées ; paramètres essentiels et suppression utilisables sans IA, vérification d'identité et confirmation explicite, restitution du résultat serveur sans promettre une suppression immédiate.

### Recette parcours adhérent — Thème 3

- T3.1/T3.2 : rendus conversationnels interactifs sans tableau de bord général supplémentaire, calendrier et consultations classiques disponibles sans IA.
- T3.3 : déplacement sans annulation préalable imposée, cohérence serveur vérifiée et reprise sûre en cas de double demande, conflit ou timeout.
- T3.4–T3.6 : suivi machine restitué sans saisie manuelle imposée ni connexion directe mobile-machine, graphiques fondés sur les calculs App, programme structuré et médias disponibles sous permissions.
- T3.7 : recette séparée de l'adaptation libre avec notification coach et de l’adaptation supervisée avec consentement adhérent dans le cadre préautorisé et validation coach hors cadre/protections/objectifs globaux/restrictions (AR01) ; aucune décision de mode par le client ou le modèle.
- T3.8 : origines et envoi effectif distingués, permissions/confirmations et historisation vérifiées ; réponse coach restituée dans le fil autorisé.
- T3.9/T3.10 : événements et règles App, préférences de notification, conseils contextuels et questions ciblées sans questionnaire systématique ; respect du circuit de sécurité.

Ces scénarios nécessitent les contrats de la section 4.3 puis une recette autorisée ; leur description ne vaut ni exécution ni succès de tests.

### Recette parcours coach — Thème 4

- T4.1/T4.2 : données et priorités autorisées selon centre + rôle, listes/fiches interactives et répertoire classique sans IA ; aucun critère métier local inventé.
- T4.3 : création/modification et ajustements entièrement conversationnels, consultation de la proposition avant application, absence d'éditeur obligatoire.
- T4.4 : acceptation, refus, ajustement, sélection/validation groupée avec validation explicite de chaque proposition, contrôles individuels et historisation serveur ; aucune adaptation supervisée appliquée sans les accords requis par AR01, dont consentement adhérent dans le cadre préautorisé.
- T4.5/T4.6 : planning et disponibilités avec calendrier résultant/conflits avant application, accès classiques sans IA et conséquences déterminées par App sans automatisme de replanification présumé.
- T4.7/T4.8 : origine des messages et envois réels vérifiables, consultation classique, bilans commentés/ajustés/validés avant partage autorisé ; données et indicateurs App.
- T4.9/T4.10 : relances autorisées sans validation systématique du coach, préférences respectées, absence déterminée indépendamment du seul manque de données machine ; contrôles serveur des confirmations sensibles et validations des adaptations supervisées selon AR01.

Recetter les contrats de la section 4.4 et leur cohérence avec le thème 3, notamment les modes d'entraînement, la transmission des messages, la reprise et les permissions. Ces scénarios sont à réaliser après contractualisation ; aucun test applicatif ni audit backend supplémentaire n'est attesté ici.

### Recette assistant IA — Thème 5

- T5.1/T5.7/T5.10 : fil unique, historique consultable et mémoire sélective distincts ; préférences explicites contrôlables dans le fil et sans IA ; modification annoncée uniquement après résultat App, sans effacement implicite des autres données.
- T5.2/T5.3 : dépendances multi-actions et contexte métier actualisé, clarification minimale fondée sur possibilités réelles ; aucun droit déduit de mémoire ni confirmation systématique, accord coach maintenu pour programmes coachés.
- T5.4/T5.5 : suivi adapté, réalisations/attentes/échecs fidèles aux résultats vérifiés, alternatives et contrôle de l'état incertain avant retry sans doublon.
- T5.6/T5.8 : réponses sport/bien-être distinctes des mutations, limites santé et explications justifiées avec indicateurs autorisés, séparation faits/hypothèses/recommandations.
- T5.9 : voix naturelle bidirectionnelle, interruption, texte/voix dans le même fil, autorisations microphone, confidentialité, interruptions système/réseau et repli texte sur iOS/Android ; mêmes règles métier, aucune réalisation présumée à partir de l'audio.

Vérifier les douze contrats de la section 4.5 et leur cohérence avec les thèmes précédents avant recette autorisée. Ces scénarios sont des critères à tester, sans test exécuté ni capacité backend supplémentaire attestée par cette mission.

### Recette notifications et proactivité — Thème 6

- T6.1/T6.10 : push/centre/conversation cohérents sur événements App, centre sans IA, accès aux événements malgré push non reçu, lu/non lu et résultats réconciliés entre appareils selon contrat.
- T6.2/T6.3 : réglages classiques, priorité des préférences explicites et confidentialité, tranquillité/exceptions contrôlées côté App ; exception AR04 Élevé aux heures calmes MOVEE vérifiée, sans contournement des restrictions OS.
- T6.4/T6.5 : déclenchement autonome autorisé sans confirmation systématique, aucune mutation implicite, données fiables, regroupement non urgent sans perte d'originaux, urgents individualisés et synthèses justifiées.
- T6.6/T6.7 : actions rapides sous capacités OS, revalidation actuelle et résultat serveur, continuité du fil et provenance humaine/IA explicite, originaux sous permissions ; accord coach maintenu si requis.
- T6.8/T6.9 : rappels contextuels sans report automatique, refus de permissions, changement de compte/contexte, déconnexion, protection des aperçus sensibles même générés par IA et paramètres écran verrouillé.
- Tester après contractualisation : premier plan/arrière-plan/application fermée, push retardés/expirés/non reçus, opportunité devenue indisponible, réponses concurrentes, perte réseau/session et reconnexion, sans garantie de livraison ou d'exactement une fois.

Critères à réaliser sur iOS/Android et backend de recette autorisé après choix technique séparé. Aucun test applicatif, fournisseur raccordé ni capacité nouvelle vérifiée n'est attesté par leur documentation.

### Recette fiabilité, hors connexion et performance — Thème 7

- T7.1/T7.2 : données locales autorisées et attente clairement distinctes du succès, revalidation App et conflits expliqués ; pas d'écrasement protégé ni politique de fusion universelle.
- T7.3/T7.4 : choix/minimisation du cache, validité/expiration/fraîcheur, chiffrement sensible, comptes/contextes isolés, purge/invalidation et biométrie optionnelle ; perte/révocation distante traitée dans les limites hors réseau.
- T7.5/T7.6 : compatibilité Mobile/App, migration locale et opérations en attente protégées lors de mise à jour/interruption ; reprise UI récupérable sans garantie d'état volatile ni reprise d'exercice.
- T7.7/T7.8 : incidents distincts des refus métier, état incertain vérifié avant retry et absence de double effet ; chargement progressif/cache explicite/navigation réactive selon appareil et réseau.
- T7.9/T7.10 : parcours essentiels sur appareils compatibles et alternatives pour capacités exigeantes, signalement et diagnostics minimisés, contrôles des données et corrélation autorisée.
- Vérifier transversalement que les performances restent enregistrées par les machines via App, sans usage mobile pendant les entraînements, fonctionnalité de suivi en direct ou accès direct machine ; préserver les capacités de saisie documentées.

Ces critères nécessitent les contrats §4.7, une étude technique et une recette autorisée. Aucun test applicatif, stockage local ou mécanisme de synchronisation livré n'est attesté ici.

### Recette accessibilité et expérience utilisateur — Thème 8

- T8.1 : VoiceOver/TalkBack, labels/sémantique, focus/lecture, texte dynamique, contrastes et réduction des animations sur cartes/graphiques et écrans classiques ; alternatives sans voix/gestes complexes.
- T8.2/T8.8 : système et réglages manuels, adaptations modifiables/désactivables, choix explicites et accessibilité sans masquage de fonction autorisée ; compte/appareil distincts et synchronisation démontrée seulement.
- T8.3/T8.4 : intégrations facultatives, permissions contextuelles/refus respectés et alternatives ; présentation progressive sans déformation, détails sans IA, continuité du fil et fraîcheur visible.
- T8.5/T8.6 : recherche sous contexte/permissions, résultats vides et alternative sans IA ; accompagnement ignorable/reprenable sans blocage ni capacité indisponible annoncée.
- T8.7 : retours accessibles séparant initiation, attente locale, vérification, confirmation, refus et résultat incertain ; aucune réussite avant App ni approbation assimilée à application.
- T8.9/T8.10 : aide classique, cause/hypothèse/solution/action distinctes, accord/minimisation support ; produit séparé du diagnostic, consentement/conservation définis, aucune exploitation automatique des conversations privées.

Critères à recetter après vérification des contrats §4.8 ; aucun test applicatif, audit d'accessibilité terminal ou mécanisme de collecte opérationnel n'est attesté ici.

### Tests contractuels entre projets

- Contrats requête/réponse validés contre le backend courant.
- T1.3, T1.6–T1.8 : capacités et contexte utilisateur, persistance/récupération du fil unique, informations prioritaires et signaux de disponibilité IA, après contractualisation avec MOVEE App.
- Scopes/permissions et refus d'accès entre centres.
- Reçus/idempotence, expiration et conflit de proposition.
- Q011/B2 : crédits immobilisés et réservation confirmée protégés malgré expiration.
- B6/B7 : douleur, restrictions, validation coach, versions concurrentes.
- Redis indisponible : échec mobile contrôlé ; OpenAI indisponible : parcours classiques utilisables.
- Push réel : validation sur appareil physique **après** intégration fournisseur.

**Aucune recette réelle n'est présumée acquise** par les tests isolés du backend. La base `newapp` a été vérifiée en lecture seule, sans autorisation d'écriture générale implicite.

Les scénarios T2.1–T2.10 nécessitent une recette contractuelle avec MOVEE App après stabilisation des interfaces de la section 4.2 : restrictions e-mail réellement appliquées, contrôle des affiliations/permissions, session et révocation, code à usage unique, modifications autorisées et suppression avec conservation. Ces critères sont des tests à réaliser, pas des résultats acquis.

### Recette transverse des arbitrages consolidés

Vérifier les scénarios AR01–AR07 et les dix sous-arbitrages AR05 décrits au §14 fonctionnel, sur iOS/Android et backend de recette autorisé. Contrôler l’exception AR02 aux écritures sans IA, AR04 aux heures calmes applicatives sous contraintes OS, les limites/consentements AR01, la distinction centre contractuel/contexte, les droits de restitution d’historique et de mesures externes, ainsi que le multilingue V1. Aucun résultat de recette n’est présumé acquis ; les schémas, canaux externes et langues/repli restent à spécifier.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:1359 -->

## 13. Environnements, livraison et sécurité de publication

- Séparer explicitement développement, recette et production ; URLs API et identifiants adaptés.
- Ne jamais embarquer de secrets serveur ou accès SQL.
- Vérifier certificats, domaines, CORS si applicable au runtime, permissions OS et déclarations de confidentialité.
- Tests sur iOS et Android avant pilote, puis publication progressive et procédure de rollback client/serveur.
- Le choix des pipelines CI/CD, stores, signature et distribution est **À VALIDER** ; ne pas inventer un déploiement existant.

### 13.1 Mises à jour et compatibilité contrôlée (T7.5)

Prévoir mises à jour distantes compatibles seulement dans les contraintes techniques/plateformes, versions natives via App Store/Google Play, contrôle Mobile/App, anciennes versions, mises à jour critiques potentiellement obligatoires et déploiement progressif des non critiques. Aucune politique de versionnement API ni mécanisme OTA n'est tenu pour existant ou définitivement choisi ; aucun changement natif arbitraire à distance.

Étudier migrations de stockage local, compatibilité des opérations en attente, absence de perte silencieuse et retour à un état stable en cas d'échec lorsque techniquement possible. Le plan de livraison doit protéger ces opérations sans promettre une restauration non démontrée ; leur statut ne devient jamais succès métier à l'occasion d'une mise à jour.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:1373 -->

## 14. Contrats transverses et dépendances

| Besoin MOVEE Mobile | Projet propriétaire | Règle de synchronisation |
| --- | --- | --- |
| Identité, Bearer, scopes | MOVEE App | Lire API et référentiel technique actuels |
| Réservations, crédits, contrats | MOVEE App | Appliquer B1–B5, Q011/B2 ; aucune logique métier locale |
| Programmes, douleur, décisions coach | MOVEE App | Appliquer B6–B7 et permissions serveur |
| IA native et capacités | MOVEE App | Contrat Flask ; aucune publication automatique côté client |
| Push outbox/worker | MOVEE App | Contrat d'appareil et fournisseur à stabiliser |
| UX, stockage client, notifications OS | MOVEE Mobile | Documenter ici, sans modifier les règles App |
| Intégration éventuelle MOVEE Biz | À qualifier | Lire les spécifications Biz ; aucun couplage supposé |
| Bilans corporels et de mobilité issus de MOVEE Motion | MOVEE Motion/dispositif pour l’acquisition ; MOVEE App pour centralisation, validation et droits ; MOVEE Mobile pour restitution (AR07) | Vérifier ses référentiels, définir les contrats et valider les droits côté MOVEE App avant intégration mobile |

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:1416 -->

## 16. Gouvernance des changements

Une demande née côté mobile qui nécessite une nouvelle API ou une règle métier doit être transmise à MOVEE App comme **demande de contrat**, avec scénario, données attendues, permissions, conséquences et critères d'acceptation. MOVEE Mobile n'implémente pas de contournement local en attendant. Une évolution backend qui modifie le contrat mobile doit déclencher une analyse d'impact et la mise à jour coordonnée des deux référentiels, puis des tests contractuels.

### État d'implémentation — 29 octobre 2026, accès consultations v6

Après installation/activation et recette adhérent du lecteur6, les entrées ordinaires de MobileHome et du menu ouvrent /pages?protocol=6. Les Pages/choix/cibles restent résolus par les actions serveur ; aucune correspondance d'UID ou entité n'est ajoutée au client. Le menu ne développe plus le catalogue historique en liens répétés.

Transition explicite : « Toutes les consultations » conserve /consultations pour la lecture des réservations absente de l'entrée6 courante. Les anciens lecteurs restent disponibles, sans fallback automatique ; réservation, préférences, compte, accueil et menu métier ne sont pas réputés intégralement metadata-driven par cette bascule d'accès.105 tests et TypeScript conformes, recette Chrome member_a des deux points d'entrée et préservation de l'accès réservations ; aucune recette native/coach nouvelle, aucun SQL, droit ou service modifié. Suivi détaillé : MOVEE_MOBILE_METADATA_MIGRATION_PLAN.md.

### État d'implémentation — 29 octobre 2026, accès compte/déconnexion7

L'entrée permanente accueil/menu est désormais /pages?protocol=7 (« Consultations et compte »). La Page serveur fournit ses actions compte/déconnexion et les accès aux listes couvertes. Les boutons spécifiques de compte et de déconnexion du shell ont été retirés, ainsi que la branche compte de MobileHome. /account redirige vers l'entrée native, sans UID ni sélection métier dans le client. La session reste gérée techniquement par le gestionnaire existant, seulement après une intention valide et un geste utilisateur.

Recette Chrome member_a des deux points d'entrée, fiche d'identité et liste programmes ; session laissée connectée.115 tests/TypeScript conformes. Les fonctionnalités de réservation/préférences/confirmations et l'accueil/menu global restent en transition. Les profils6 et antérieurs demeurent explicites et aucune panne7 ne provoque de fallback. Suivi : MOVEE_MOBILE_METADATA_MIGRATION_PLAN.md.

## Annexe — chronologie historique, non applicable comme état courant

Les chiffres, ports, noms de versions et mentions « installé/non installé » de cette annexe décrivent leur date d’origine. Le point de reprise en tête du fichier et les contrats actuels priment pour déterminer les opérations disponibles. Cette annexe conserve la traçabilité ; elle n’autorise aucune action ni réactivation.

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:2`.



---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:3`.

### État courant et consolidation demandée — 31 octobre2026

Suite du diagnostic : codage/tests approuvés par « ok ». Un seul lecteur courant est accessible ; les anciens liens ne rouvrent pas leurs écrans. Récupération des résultats historiques sans renvoi automatique et fermeture volontaire du seul suivi local d’une attente connue.351testsMobile, TypeScript et exports3plateformes conformes ; voir MOBILE_PAGES_CONSOLIDATION_MOBILE_RESULT.md. Candidat30Pages en validation Backend, aucune suppression SQL ni activation par cette phase. Les mentions d’analyse seule ci-dessous sont le stade antérieur à cet accord de codage.

Le profil14 est installé et actif après autorisation du plan d882ecb6a001b838f69444c3dc56b8e9e2cd266b4edb663628d55c7e3c691591. Rapport : PROGRAMME_MEDIA_WORKING_PLAN.md et PUBLIC_GROUPED_PAGES_V14_MOBILE_RESULT.md ; les états13/préparation suivants sont historiques. L’utilisateur refuse désormais la conservation de générations de Pages pour une évolution de présentation : une Page canonique par fonction/portée réelle, métadonnées modifiées en place, sans nouvelles copies à chaque version. Il demande l’état des lieux et le plan de suppression des anciennes versions et doublons en préservant le parcours installé. Seules analyse et préparation documentaire sont autorisées par cette demande, pas les suppressions. Audit Mobile : MOBILE_PAGES_CONSOLIDATION_AUDIT_AND_PLAN.md ; inventaire Backend en préparation READ ONLY. Préserver droits, contenus, journaux/reçus et reprise d’intention ; ne pas confondre historique d’opérations et anciennes Pages actives.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:9`.

### Programmes et médias — lecteur14 codé, installation en préparation

31 octobre2026. Maquettes Light/Black validées puis implémentation autorisée. Raccordement générique14 : groupes de cellules, période, pourcentages typés, métriques2/3colonnes, galerie principale+paire. Règles et calculs côté Services.338 testsMobile et128étapesBackend isolées consommées,4langues, sans execute. Chartecommunev1.2. Rapport : PUBLIC_GROUPED_PAGES_V14_MOBILE_RESULT.md ; plan : PROGRAMME_MEDIA_WORKING_PLAN.md.

Durée par série et repos entre séries confirmés ; plusieurs séances par programme confirmées ; synthèse de chaque séance type une fois annoncée. Profil habituel13 maintenu : aucun SQL, permission ou redémarrage. Plan d’installation et recette14 connectée restent à réaliser. Sexe local non renseigné→médias indisponibles ; aucune valeur inventée. Alimentation IA des nouvelles fréquences/qualifications encore à fermer côté Backend, sans contournement deAR02 par Admin.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:16`.

### Langue dans le bandeau — 31 octobre2026

À la demande de l’utilisateur, le bouton Réglages est remplacé par un drapeau48×48 placé immédiatement avant le profil. Français initialement, puis drapeau de la langue active ; fenêtre Français/English/Deutsch/Español au clic avec sélection et fermeture. Composant technique commun LanguagePicker ; aucun nouvel écran métier ou UID embarqué. `setLocale` et la garde de brouillon existants sont conservés ; le Backend reste la source des textes traduits. Les boutons de langue dans le corps sont retirés ; Changer d’espace reste proposé quand autorisé. Charte commune mise à jour en version1.1 dans /Users/mbenmouha/Documents/Movee/codex/DESIGN_SYSTEM_MOVEE.md.

313 tests réussis, TypeScript/diff et exports Web/iOS/Android conformes. Vérification connectée390×844 : drapeau FR, ouverture des quatre choix, changement réel vers EN et retour FR, ancien bouton absent. Aucune écriture métier, migration ou redémarrage. Les textes non traduits par la source ne sont pas réinventés côté Mobile. Capture : /Users/mbenmouha/Documents/Movee/output/design/mobile-integration-2026-10-31/language-picker-light.jpg. Vérification physique iPhone distincte.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:23`.

### Design system commun Light / Black — 31 octobre 2026

Les deux directions ont été validées comme thèmes commutables. Référence canonique commune : [DESIGN_SYSTEM_MOVEE.md](DESIGN_SYSTEM_MOVEE.md), version1.0, à transmettre aux projets Admin/Biz/Info sans dépendre de ce chat. Aucune charte concurrente copiée dans Mobile.

Intégration dans les composants génériques du lecteur existant : palettes, Manrope/Sora embarquées et corps système, géométrie claire/sombre, bandeaux, boutons, blocs, dates et champs. Switch local Light/Black à la connexion et dans le bandeau d’espace ; suivi initial du système puis choix mémorisé sur l’appareil. Le switch ne remonte aucune préférence au Backend et ne réinitialise ni session, formulaires, filtres ou pile. Métadonnées et Services conservent actions, critères, libellés, ordre, icônes métier et droits ; aucune règle sur UID, rôle ou entité ajoutée. Coach : thème partagé, gabarit de navigation existant conservé.

309 tests Mobile réussis, TypeScript et exports Web/iOS/Android conformes. Vérifications navigateur téléphone390×844 et tablette834×1194, comparaison aux deux planches, planning coach en lecture seule et persistance Web. Rapport visuel : ../design-qa.md. Aucun SQL, permission, mutation métier, redémarrage de service ou déploiement dans ce lot. Recette physique iPhone/Android et globale distincte.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:32`.

### Installation et activation — 31 octobre 2026

Plan révisé explicitement autorisé, SHA256 `36e0fcce8db0ac45b290f4c7a1e68053d78d998ecb094d498bee31a0c37a87dd` : 97 insertions et 22 mises à jour de métadonnées appliquées ; vérification après application conforme, rejeu sans écriture. Backend seul arrêté puis démarré via movee-dev ; Redis, MariaDB et Expo préservés. Preflight public_member_chrome_v13_v1 conforme. Profil habituel désormais13.

Les contrôles d’installation ont préservé les83 tables hors delta autorisé. La connexion navigateur normale de recette effectuée ensuite peut modifier les audits techniques users ; aucune réservation, annulation, décision ni préférence enregistrée pendant ces vérifications.

302 tests Mobile, TypeScript, diff et exports Web/iOS/Android réussis après bascule et correction purement visuelle des boutons étroits. Rendu connecté Web390×844 vérifié : bandeaux, onglets, modales, blocs et pictogrammes. Parcours mesurés depuis l’accueil : annulation jusqu’au formulaire en3 clics ; programmes→programme avec exercices→démonstration en3 clics, animation lancée puis arrêtée explicitement ; compte en1 clic. Grand logo réservé au login. Aucun consentement ou aperçu métier supprimé.

Captures : MEMBER_SHELL_HOME_2026-10-31.png, MEMBER_SHELL_BOOKINGS_2026-10-31.png, MEMBER_SHELL_MODAL_2026-10-31.png et MEMBER_SHELL_PROGRAMME_2026-10-31.png. Recette métier globale et vérification physique iPhone restent à réaliser. Les compteurs expirés deviennent « Compteur à actualiser », jamais un zéro inventé. Les muscles absents de la réponse restent non renseignés ; aucune donnée inventée côté Mobile.

Le premier plan a été refusé avant DML sur divergence users. Seul le plan révisé ci-dessus a été appliqué. Les ajustements visuels et ce rapport sont postérieurs à l’installation : ne pas rejouer l’ancien artefact scellé sur ces sources modifiées.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:44`.

### Parcours adhérent validé — 31 octobre 2026

Chat et voix IA restent l’entrée principale cible ; écrans complets en secours ou par préférence. Réalisation autorisée : bandeaux supérieur crédits/notifications/compte et inférieur Accueil/Réservations-Séances/Programmes, grand logo seulement sur login, en-tête unique retour/titre/rafraîchissement aux positions fixes, modales sans navigation du bas, blocs compacts et actions avec icônes groupées. Tout reste piloté par Pages/Fields/Designer. Plafond validé : trois clics de navigation jusqu’au formulaire ou à l’action finale ; choix métier et confirmations exclus. La pastille crédits affiche le disponible pour réserver. L’IA actuellement désactivée n’est pas activée par ce lot. Plan courant : MOBILE_MEMBER_SHELL_WORKING_PLAN.md.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:48`.

### État courant — 31 octobre 2026 : profil 12 actif, correction coach

Le profil 12 est installé et actif par défaut. L’accès iPhone via Expo Go SDK 58 est configuré sur le Wi-Fi local ; Backend et Expo utilisent la politique Interactive de launchd. Le refus initial du planning coach dans le lecteur 12 est corrigé : paramètres validés selon les métadonnées publiées, cardinalité du profil 11 conservée et erreurs/reprise visibles avant la première configuration.

Rapport : PUBLIC_NATIVE_BLOCK_PAGES_V12_COACH_NAVIGATION_FIX.md. 277 tests Mobile réussis, 40 DTO réels des deux coachs consommés, navigation Web du coach A exercée sans mutation métier. La confirmation iPhone et la recette globale restent à faire. Les états de préparation ou de non-activation ci-dessous sont historiques.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:54`.

### Présentation en blocs : réalisation relancée, métadonnées seules sources — 30 octobre2026

Maquette révisée exec-4499e357-5243-428a-943c-c632e9264b19.png validée par l'utilisateur. Après interruption de la conversation APP, reprise explicitement autorisée. Filtres, valeurs par défaut, choix et actions sont déclarés dans Pages/Fields/Designer ; le template Mobile les représente en boutons/blocs, sans règles Futures/Passées ou statuts codés en dur. Cette précision utilisateur s'impose à la réalisation.

Plan courant : MOBILE_DECLARATIVE_BLOCKS_WORKING_PLAN.md. Lecteur12 raccordé et 273 tests Mobile réussis ; TypeScript/diff conformes, exports finaux à relever. APP a rapporté l’autorisation humaine d’installation/redémarrage/bascule dans son chat ; Mobile attend son rapport de contrôles avant toute bascule. Le jeu de recette2coachs/4adhérents est bien installé et ses accès simplifiés ; les paragraphes antérieurs sur sa préparation sont historiques. Le runtime habituel reste11. Raccourcis d'accueil différés.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:60`.

### État courant : v11 actif et jeu de recette complet en préparation — 30 octobre 2026

Installation et bascule11 effectuées par APP sous autorisation humaine. Accueil adhérent réellement vérifié dans l'onglet connecté après correction Backend de l'action session_logout : réservation et quatre accès visibles sans erreur. Rapport : PUBLIC_MOBILE_WORKSPACES_V11_HOME_FIX_ACCEPTANCE.md. Les anciens états « non installé » et valeur9 ci-dessous sont historiques.

L'utilisateur a validé le périmètre du nouveau groupe fictif (2coachs/4adhérents,8programmes de10exercices avec médias, résultats, planning, crédits et préférences) et demandé explicitement le chargeur et le plan exact. APP prépare code/tests/plan ; aucune application de ce jeu autorisée. Matrice de suivi : MOBILE_COMPLETE_DATASET_ACCEPTANCE_MATRIX.md. Les comptes et données historiques doivent rester intacts. Recette globale différée jusqu'à installation autorisée ; aucun changement de parcours Mobile engagé par cette préparation de données.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:66`.

### Espaces adhérent/coach v11 : code et tests livrés — 30 octobre 2026

Le « ok » utilisateur a validé le codage de la proposition commune. Raccordement Mobile complet au contrat effectif11 : choix explicite multiespace, navigation persistante, sujet scellé, planning par jour et annuaire natifs, formulaires hérités sous sujet verrouillé, garde des brouillons et journal conservé. Aucun écran métier spécifique ni attribution de rôle côté client.

255 tests Mobile réussis ; TypeScript, diff et exports Web/iOS/Android conformes. Huit parcours publics Backend synthétiques consommés. Rapport : PUBLIC_MOBILE_WORKSPACES_V11_MOBILE_RESULT.md. Backend rapporte séparément198 tests distincts. Aucun test authentifié ou visuel d'appareil revendiqué ; recette globale différée selon la consigne utilisateur.

Code prêt, aucune installation ni activation11. Le point commun DEFAULT_PAGES_PROTOCOL reste9. MOVEE App prépare ensuite le plan résolu ; application, redémarrage Backend et bascule Mobile attendent une autorisation unique sur le plan exact. Aucune donnée métier, préférence, droit ou service modifié par ce raccordement. Les paragraphes suivants conservent la chronologie antérieure.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:74`.

### Parcours : décisions planning et multirôle validées — 30 octobre 2026

Réponses explicites : planning coach limité aux séances qu’il encadre ; une personne coach et adhérente peut choisir et changer d’espace. Ces décisions ont été transmises à MOVEE App pour finaliser la proposition de contrat commune. Aucun ordre implicite de rôle, agrégat de toutes les réservations des adhérents ou droit supplémentaire. Changement d’espace : anciennes lectures/sujet/aperçus retirés, journal/demandes/reçus conservés ; aucune écriture métier ni déconnexion automatique.

Le plan MOVEE_MOBILE_ROLE_JOURNEYS_WORKING_PLAN.md est actualisé. Les arbitrages ne sont plus en attente ; les anciens paragraphes ci-dessous décrivent leur état historique. Contrat technique toujours en préparation avant codage ; aucun code, SQL ou service modifié pour cette mise à jour documentaire.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:80`.

### Parcours par usage : séparation validée — 30 octobre 2026

L’utilisateur a approuvé (« ok ») l’organisation distinguant adhérent réserver→séance→exercices/animations et coach planning→adhérent→programme/suivi, au sein du même framework. Plan de travail réel : MOVEE_MOBILE_ROLE_JOURNEYS_WORKING_PLAN.md. Le diagnostic App MOBILE_ROLE_NAVIGATION_DIAGNOSTIC.md a été lu intégralement : les menus existants seuls ne réalisent pas le planning coach, l’annuaire public, le binding sujet vers tous les formulaires ni une tabbar persistante.

Deux arbitrages fonctionnels ont été demandés : périmètre du planning coach et comportement des comptes multirôles. Proposition technique complète demandée à MOVEE App, sans codage des capacités dont le contrat reste à valider. Aucun rôle/UID embarqué, harmonisation artificielle des scopes ou droit supplémentaire ; journal et Services existants conservés. Pas d’installation, code ou service modifié par cette préparation. Recette globale toujours en fin de chantier.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:86`.

### Correctif connexion : renouvellement du formulaire — 30 octobre 2026

Signalement utilisateur : formulaire remplacé prématurément par « Actualisez le formulaire avant de vous connecter ». Diagnostic vérifié : AppState invalidait définitivement le formulaire au passage en arrière-plan, sans reprise sur active. Correction et tests explicitement autorisés par l’utilisateur après présentation du diagnostic.

SessionEntryScreen recharge désormais uniquement la description publique au retour au premier plan et à son expiration. Les saisies obsolètes restent retirées, version/TTL de cinq minutes et gestionnaire de connexion existants conservés ; aucun identifiant envoyé, aucune connexion automatique. Retry-After empêche tout nouveau chargement avant l’échéance ; un échec n’entraîne pas de boucle de retry. Les réponses antérieures sont ignorées par le nettoyage de requête existant. Quatre tests de régression ajoutés : retour, expiration/échec, quota et réponse tardive. Tests catalogue10 indépendants de l’heure réelle grâce à l’horloge synthétique de leur fixture.

213 tests Mobile réussis, TypeScript et git diff --check conformes. Formulaire anonyme vérifié dans un onglet Chrome distinct, après aller-retour entre onglets ; aucune connexion réelle, modification Backend/SQL, permission ou redémarrage de service. Accueil habituel9 conservé. Sources Mobile modifiées après application du plan catalogue historique, MOVEE App informé.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:94`.

### Catalogue : métadonnées installées et Backend actif — 30 octobre 2026

Rapport App CATALOGUE_PRESENTATION_V10_APPLICATION_ACTIVATION_RESULT.md lu après autorisation humaine vérifiée dans le chat MOVEE App : plan bf0848faf47f0451efe59626d9b0e003a907a2074230642f4a217dd57b6d8d91 appliqué,14INSERT/2UPDATE,préflight public_catalogue_presentation_v10_v1 conforme,83 tables/counters conformes au plan et rejeu sans écriture. Backend seul redémarré ;20 contrôles HTTP anonymes conformes, parcours Services READ ONLY dans les quatre langues. Cela ne vaut pas recette HTTP authentifiée ou appareil.

Le plan autorisé conserve explicitement l’entrée habituelle9 ; aucune bascule par défaut effectuée dans Mobile. Le lecteur installé est accessible explicitement via /pages?protocol=10. Aucun login, téléchargement de média dans un navigateur ou geste métier réalisé ici. Code Mobile209tests et exports précédemment conformes inchangés. La recette reste reportée à la recette globale, conformément à l’instruction utilisateur. Catalogue global réservé aux acteurs déjà habilités ; exercices liés sous droits existants. Le solde est la recette connectée langue/médias et la décision de bascule habituelle, pas une nouvelle installation Backend.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:100`.

### Catalogue multilingue et médias — code prêt, 30 octobre 2026

Autorisation explicite « Oui, coder ce raccordement et ses tests ». Lecteur commun10 raccordé au contrat effectif App : sélecteur FR/EN/DE/ES en mémoire, langue capturée et vérifiée par réponse, retrait de pile et saisies au changement, médias protégés explicitement déclarés dans les Fields, images intégrées et animations sur geste. Type6 et ReadSchema historiques conservés ; aucun écran d’exercice, UID métier, affectation de programme ou dépendance ajouté.

Chargement binaire fixe et borné8MiB, Bearer/credentials omit/no-store, statut/MIME/WebP contrôlés, timeout/annulation et quota/session communs. Sources mémoire seulement, Blob libérée sur Web, cachePolicy:none ; arrêt par démontage en quittant/arrière-plan. Journal10 conserve langue/profil/intention d’origine et reprises explicites ;8/9 conservés.

209 tests Mobile réussis, TypeScript/diff et exports Expo Web/iOS/Android conformes. Quarante étapes catalogue/guide/médias App issues de MariaDB jetable consommées dans les quatre langues ; tests métier hérités sous enveloppes10 synthétiques distingués de ces preuves. Rapport : PUBLIC_CATALOGUE_PRESENTATION_V10_MOBILE_RESULT.md.

Installation et bascule non effectuées : accueil normal9 conservé, route préparatoire /pages?protocol=10. App prépare le périmètre metadata sous droits actuels ; catalogue global autorisé au siège testé, refusé aux coachs/adhérents testés, aucun droit ajouté. Les exercices liés restent soumis aux droits existants.128médias d’exercice couverts par le binding futur ;40images de référence sans Field média dans ce lot. Aucun SQL, service, login ou geste métier effectué par Mobile. Prochaine étape : plan exact et autorisation incluant redémarrage/contrôles, puis bascule ; recette globale/connectée/native toujours reportée.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:110`.

### Libellés communs appliqués et activés —30octobre2026

Autorisation humaine explicite : « Oui, appliquer et activer les libellés », plan e73ec770e3053007b68082c5c8af974a57ed48607be068c4c80be2e614f94783. Application85UPDATE exacts (61Fields et24référentiels), aucune Page/action/droit/donnée métier modifiée. Vérification indépendante et rejeu0DML conformes. Preuve App common_french_labels_activation_result.json lue : common_french_labels_v1, état final exact des75tables aprèsHTTP, tablesprivées/structure/compteurs/auditsconnexion préservés ; Backend seul redémarré,16contrôlesHTTP lecture conformes. Redis/Expo/MariaDB inchangés.

Projections Services confirment les61libellés et28valeurs attendues (dont4conservées) pour les3profils de recette, codes inchangés ; aucune connexion réelle ou mutation de recette. Huit libellés de conséquences communs activés, renderer Mobile déjà compatible sans nouvelle traductionlocale.185tests Mobile précédemment réussis, aucun codeMobile changé pendant application/activation. Pas de nouvelle recetteauthentifiée/native revendiquée. Les écrans/contextes/curseurs anciens doivent être relus normalement ; journal/intentions consenties conservés, aucun fallback.

Nettoyage des composants et correction des libellés du périmètre validé clôturés. Les seules compatibilités conservées sont explicites et protègent notamment les demandes historiques non réconciliées. Prochaine étape : préparer la recette globale (matrice parcours/profils/erreurs/reprises/accessibilité/appareils, données/gestes précisément autorisés). La recette globale reste à réaliser, pas exécutée par les contrôles de cette installation.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:119`.

### Vérification du schéma commun de crédits —30octobre2026

Fixture App common_credit_effects_labelled_fixture.json issue du schéma commun effectivement codé, copiée dans tests/fixtures/common-credit-effects-labels.json. Test du renderer générique réel : les8libellés sont affichés, aucune clé machine credit_cost/reserved_credits/restored_lots/quantity/expires_at n’est rendue ; zéros préservés, lot/date lus via dialecte2, showLabelsfalse respecté. Aucun changement de code de rendu Mobile ou dictionnaire local nécessaire.

185tests Mobile réussis après ajout du contrôleconsommateur ; TypeScript/diff conformes, exportweb du même codeapplicatif valide. Code et tests Mobile terminés pour ce lot. MOVEE App poursuit les tests Backend et la préparation du plan exact des intitulés/référentiels ; aucune application locale ni activation du nouveau schéma revendiquée.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:126`.

### Traductions communes autorisées —30octobre2026

Utilisateur : « Oui, corriger au niveau commun ». Le périmètre validé est celui du diagnostic App MOBILE_LABELS_DIAGNOSIS_PROPOSAL.md :61intitulés de Fields partagés, valeurs de référentiels proposées (sans réécrire celles déjà identiques), et8libellés de conséquences sur les crédits dans le schéma commun. Impact Web/Admin explicitement accepté. Codes/UID/types/unités/relations/droits/Services métier et intentions signées restent inchangés ; les versions et curseurs incluant les textes peuvent changer et doivent être relus normalement.

MOVEE App code les labels du schéma, teste et prépare une reconnaissance globale/un plan précis ; aucune application SQL ni activation autorisée. Mobile réutilise ReadValue et le suffixe de libellé type10 existants ; pas de dictionnaire métier local ou nouveau profil. Fixture effective demandée pour vérification des8labels. Recette globale toujours reportée.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:133`.

### Nettoyage des composants et libellés —30octobre2026

Chantier explicitement autorisé. Graphe des imports depuis toutes les routes Expo inspecté, références runtime et tests vérifiées.13fichiers de composants hors parcours retirés : app-tabs natif/web, animated-icon natif/web/CSS, hint-row, web-badge, external-link, themed-text, themed-view, ui/collapsible, anciens booking-suggestions/upcoming-bookings. Aucun asset/dépendance native supprimé sans nécessité ; routes historiques de redirection conservées.

Bloc SpecializedContent/ServiceFields/Details/cartes par content_type et dictionnaire local de libellés métier retirés de mobile-page-content. Les tests de rendu spécifiques supprimés avec leurs composants, tests de contrats/transports historiques maintenus ; renderer6–9/ReadValue demeure la source du rendu métier actuel. LegacyRequestRecovery et gestionnaires/journaux persistants inchangés.

Chargement systématique du catalogue historique supprimé du Provider. usePagesCatalog ne lit qu’à la demande, dans le composant historique monté pour les profils2/3 explicitement demandés ; /pages sans version ouvre désormais9. Profils inconnus refusés sans fallback. Quota/invalidation/session/critères et lectures privées restent gérés par les hooks communs. Tests du parcours9 sans catalogue et refus de version inconnue ajoutés.

Libellés techniques des contrôles communs humanisés : Actualiser l’écran/la liste/les détails. Aucun rawreason_code affiché pour les actions indisponibles ; message générique, bouton/droits inchangés et test anti-fuite ajouté. Les libellés de Fields et statuts restent ceux du serveur, sans nouvelle traduction métier locale. MOVEE App inventorie leur projection réelle en lecture seule et prépare une proposition avant/après ; aucune correction SQL/contrat de statut effectuée à ce stade.

184tests Mobile réussis, TypeScript/diff/exportweb conformes. Diminution du total due au retrait de4tests de composants disparus et ajout de2tests du chemin courant ; aucune suppression des tests métier/journal/session. Aucune connexion réelle, mutation métier, permission, schéma ou service modifié ; recette globale reportée. Solde : libellés métier metadata et éventuel contrat générique de restitution des statuts à valider après diagnostic App.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:146`.

### Connexion déclarative installée et basculée —30octobre2026

Autorisation utilisateur explicite portant sur le plan759a2dd76c4b0daf9818c7fb06f026050c0f8bf86177a20bb858f0ec2db4b940. Rapport App docs/MOBILE_SESSION_ENTRY_APPLICATION_ACTIVATION_RESULT.md lu :6INSERT/0UPDATE exacts, préflight public_mobile_session_entry_v1 conforme, rejeu0DML/DDL et préservation des75tables hors ajouts ; Backend redémarré seul et16contrôlesHTTP lecture conformes, sans login/logout réel.

Après feu vert et levée du gel convenu, index.tsx remplacé par SessionEntryScreen ; ancien formulaire écrit en dur retiré. /session-entry reste un alias technique du même lecteur. Aucun fallback, UIDembarqué ou catalogue anonyme.186tests Mobile réussis après bascule, TypeScript/diff/exportweb conformes. Le contrôle visuel anonyme est effectué dans un onglet distinct, sans toucher à une session utilisateur ni saisir/envoyer d’identifiants. Expo a nécessité un redémarrage géré après erreur Metro de graphe incrémental ; aucune seconde instance lancée.

Recette globale/authentifiée/natifs toujours reportée. Le prochain solde du plan est le nettoyage des reliquats et libellés techniques, puis la préparation de la recette globale ; ne plus présenter la connexion comme formulaire métier codé.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:155`.

### Connexion/reconnexion déclarative — code Mobile prêt,30octobre2026

Complément validé et contrat effectif App raccordé : présentation publique fermée, rôles/contrôles natifs, header fixe de version au login, récupération technique indépendante du bootstrap, secret non persisté et effacé au geste. Gestionnaire existant corrigé contre les effets réseau/SecureStore concurrents ; journaux métier préservés.186 tests passent, TypeScript/diff/exportweb conformes. Route préparatoire /session-entry, connexion normale conservée jusqu’à installation/activation et bascule convenue. Aucune connexion réelle/SQL/droit/service effectué ; recette globale reportée. Rapport : PUBLIC_MOBILE_SESSION_ENTRY_MOBILE_RESULT.md.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:160`.

### Accueil/menu déclaratifs, retrait des écrans et ergonomie — 30 octobre 2026

Chantier autorisé avec amélioration visuelle par l’utilisateur. Recette métier finale explicitement reportée à la recette globale. Le contrat9 et les métadonnées installées suffisent : MOVEE App confirme en lecture seule les huit actions plates d’accueil, sans menus imbriqués installés. Aucun regroupement métier par libellé ou UID fabriqué. Le shell fixe ne contient plus de menu métier parallèle : marque et accès technique Mon espace ; les destinations, ordre et libellés sont ceux des Pages/actions. Le bouton Mon espace ouvre une entrée9 fraîche ; retour local des cadres conservé.

Ergonomie commune : cartes d’actions adaptatives avec chevrons, titre accentué lime, contrôles de relecture allégés, boutons/icônes techniques accessibles. Filtres et tri repliés sous un bouton commun, critères et relations conservés, indicateur des critères actifs, retour du focus après fermeture. Paramètres de collections et période de recherche regroupés également. Respect des show_icon/show_label/show_actions : les icônes métier actuellement masquées ne sont pas forcées ; registre symbolique local pour open.png/view.png/edit.png/save.png et repli neutre, aucune URL exécutée. Palette#EFFF4F/#10131A maintenue.

Anciens écrans spécifiques supprimés des routes /booking,/preferences,/consultations, remplacés par l’entrée9. Les anciens formulaires de nouvelle réservation/annulation/édition de préférences et le lecteur spécifique de consultations ont été retirés de ces fichiers. Un seul composant LegacyRequestRecovery est conservé exclusivement pour un journal historique non réconcilié : lookup, renvoi volontaire de même intention, abandon de préférences après relecture, accord historique avec protections/consentement conservés. Aucun nouvel envoi métier ne part automatiquement. Les parseurs/gestionnaires historiques nécessaires à la récupération et les lecteurs à profil explicitement demandé restent disponibles ; aucune panne9 ne provoque de fallback.

165 tests réussis après remplacement des tests d’écrans retirés par ceux du parcours commun/de compatibilité ; TypeScript et diff conformes. Export web contrôlé. Vérification Chrome connectée, sans écriture : accueil/cartes, ouverture Programmes, panneau Filtres et tri ouvert/replié, retour conservé. Tests de récupération et consentement historiques préservés. Aucun test sur appareil natif ni recette globale nouvelle revendiqués. Aucun SQL, droit, dépendance projet ni code Backend modifié ; aucun redémarrage de service requis dans ce chantier.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:171`.

### Recette Chrome member_a — 30 octobre 2026

Recette authentifiée9 effectuée depuis l’accueil permanent : entrée et actions natives ; sélection adhérent/prestation ; suggestions vides cohérentes avec les préférences absentes ; Choisir plus, calendrier et lecture des créneaux du31/10 ; sélection18h–18h30 et aperçu signé avec durée30min, coût1, immobilisation1, pénalité0, Europe/Paris et absence d’accord supplémentaire. Consentement laissé désactivé, confirmation bloquée et jamais soumise.

Préférences : lecture globale et portées autorisées visibles, brouillon local lundi18h/Europe/Paris valide et enregistrable, abandonné sans sauvegarde. Correctif générique : resélectionner la même valeur scalaire conserve la version lue ; les choix scellés conservent leur invalidation/revalidation. Libellé de la portée nulle sélectionnée affiché. Test de non-régression ajouté.

168 tests réussis, TypeScript/diff/export web conformes après correction. Retour à la liste des réservations : une seule réservation future,31/10à10h–10h30, centre principal, Confirmed/version1. Aucune création, remplacement de préférences, annulation ou décision effectuée.

Limites : suggestions positives non recettées faute de préférence enregistrée ; exécution réelle de création/enregistrement, reprise réelle après timeout9, profils délégués et appareils natifs restent non recettés. Le calendrier initial peut retourner une page sur la fenêtre avant sélection du jour ; les dates de chaque ligne sont explicites, le choix d’un jour restreint correctement la lecture. La configuration de recette actuelle propose des horaires nocturnes : aucune restriction8h–21h/Bordeaux n’a été installée ici.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:182`.

### Bascule intégrée v9 — 30 octobre 2026

Plan App c651d9b34c29b87748a4b3ed83ddd38aeed096d205562701345e0daa9bc27c21 explicitement autorisé, appliqué et activé : 13 ajouts de métadonnées et une mise à jour, rejeu sans écriture, préflight global conforme et 29 contrôles HTTP de lecture. Rapport App réellement lu : docs/BOOKING_COMPOSITION_PAGES_V9_APPLICATION_ACTIVATION_RESULT.md.

Après levée du gel des sources, MobileHome affiche directement ProcessPageHost9. Les actions métier viennent des Pages ; le menu technique conserve l’accueil sans raccourcis métier fixes. /account et les anciennes adresses /booking et /preferences ouvrent9, sauf journal historique non réconcilié qui conserve son canal de récupération. Les profils antérieurs restent explicites, sans fallback automatique. Aucun UID métier ajouté.

167 tests Mobile réussis, TypeScript et export web conformes. Aucune réservation ni préférence personnelle initialisée. Recette authentifiée9 encore à terminer ; suggestions positives et exécution réelle nécessitent des valeurs humaines et une autorisation de recette précise.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:191`.

### Poursuite groupée autorisée — 30 octobre 2026

L’utilisateur demande en une seule passe la bascule8, la création/suggestions/calendrier et les préférences via le framework commun. Avertissement préalable effectué et coordination directe avec MOVEE App explicitement autorisée. Lot engagé, suivi courant dans MOVEE_MOBILE_METADATA_MIGRATION_PLAN.md. Contrat8 reste fermé ; création et édition de préférences nécessitent un complément Backend effectif avant raccordement, sans exception d’écran spécifique. Ne pas confondre cette autorisation de développement/coordination avec l’application d’un futur plan SQL non présenté.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:195`.

### Accueil/navigation : prochain lot engagé — 28 octobre2026

L’utilisateur valide la suite par accueil et navigation metadata-driven. Réutiliser is_home/front_type, les propriétés natives, config_actions et menu_uid du moteur, sans catalogue substitué à un menu ni bouton métier inventé. Le profil v3 actuel reste limité aux actions de ligne vers fiche ; ouverture de liste sans ligne source et conteneurs publics à livrer dans un contrat versionné explicite avant raccordement. Demande : MOVEE_MOBILE_HOME_NAVIGATION_BACKEND_REQUEST.md ; suivi : MOVEE_MOBILE_METADATA_MIGRATION_PLAN.md. Aucun code applicatif, SQL, service ou test modifié/exécuté dans ce cadrage.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:199`.

### front_type installé et lecture native v3 recettée partiellement — 28 octobre2026

Rapports App d’application/activation lus : pages_front_type_v1 installé, Backend prêt. Lecture Mobile READ ONLY confirme les six Pages91–96 front_type2, UID opaques et actions natives101/click_action ; mobile_read/detail_page_uid retirés. Chrome sous coach : trois listes, fiche réservation en modale via View native, retour filtre/tri et relecture, refus sections programme et fermeture Échap. Aucun mapping codé en dur ni fallback/bascule par défaut.

Neuf tests Mobile ciblés et14 tests Backend isolés repassés avec succès ; pas de refus hors scope/conflit réel provoqué dans le navigateur, autre profil ou natif recetté. Aucun changement métier, permission ou service effectué par Mobile ; le lien temporaire de recette est retiré. Détails : NATIVE_PAGES_V3_AUTHENTICATED_ACCEPTANCE.md ; suivi : MOVEE_MOBILE_METADATA_MIGRATION_PLAN.md. Accueil/menu, choix/formulaires, sections, calendrier et processus déclaratifs restent à livrer.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:205`.

### Actions natives v3 raccordées en préparation — 28 octobre2026

Contrat App NATIVE_PAGES_V3_DELIVERED_CONTRACT.md reçu et code consulté. Mobile prend en charge le profil natif open_page par action_uid, catalogue v3, versions, cible page/modale et retour avec critères, via le même renderer que la v2 explicite de transition. Aucun detail_page_uid reconstruit dans la v3, mapping codé en dur, sélection de frontend client ou fallback automatique. /pages?protocol=3 est le point d’accès préparatoire, sans bascule par défaut. Entry/menu au transport ne constituent pas un accueil/menu Mobile configuré ; capacités non livrées refusées.

71 tests Mobile réussis, TypeScript et export web conformes. Schéma/UID encore non installés et Backend v3 non activé selon livraison App ; aucune recette locale v3 ou native revendiquée. Reconnaissance globale et nouveau plan résolu à préparer côté App ; ancien candidat non applicable. Rapport : NATIVE_PAGES_V3_MOBILE_RESULT.md ; avancement : MOVEE_MOBILE_METADATA_MIGRATION_PLAN.md. Aucun SQL, droit, code Backend ou service modifié ici.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:211`.

### Préparation front_type reçue, runtime manquant — 28 octobre2026

Rapport App PAGE_FRONT_TYPE_PREPARATION.md consulté :143 Pages classées137 Web/6 Mobile, candidat structure/métadonnées/Designer/actions natives préparé, non applicable. Cinq tests de transformation pure et inventaires75 tables identiques rapportés par App ; ils ne qualifient ni runtime ni installation. La colonne front_type et les UID candidats ne sont pas installés. Le client v2 actuel reste inchangé ; contrat natif effectif versionné/négocié requis avant raccordement. Suite : MOVEE_MOBILE_FRONT_TYPE_RUNTIME_NEXT_STEP.md ; avancement dans MOVEE_MOBILE_METADATA_MIGRATION_PLAN.md. Aucune modification applicative, SQL ou service par cette prise en compte.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:215`.

### Sélection du frontend validée — 28 octobre 2026

Décision utilisateur : pages.front_type avec1 Web et2 Mobile, ce dernier couvrant téléphone/tablette et aperçu web du frontend Mobile. Propriété de configuration, sans droit implicite ni déduction par appareil. Préparation coordonnée autorisée : registre/metadonnées/Designer, accueil/navigation, UID opaques, suppression des marqueurs mobile_read et detail_page_uid au profit de la sélection frontend et des actions natives. Contrat public d’actions et compatibilité à livrer avant installation ; ne pas retirer de garde métier sans remplacement équivalent.

Demande App : MOVEE_MOBILE_FRONT_TYPE_BACKEND_REQUEST.md ; étape1bis du suivi MOVEE_MOBILE_METADATA_MIGRATION_PLAN.md. Aucun SQL/code Backend ou changement de Pages appliqué par cette prise en compte. Les listes/fiches v2 recettées ne constituent pas une reprise des UID ni de page_config.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:221`.

### Recette partielle du lecteur v2 — 28 octobre 2026

Trois listes vérifiées dans Chrome sous coach, navigation réservation→fiche→liste avec filtre/tri conservés et données relues ; état vide filtré et refus de sections programme confirmés. Pas de bascule par défaut. Neuf tests Mobile ciblés, TypeScript et24 tests Backend isolés réussis. Refus hors scope et conflit de version non provoqués dans le navigateur authentifié ; pagination multi-page, autres profils et natif à recetter. Aucun changement métier/base/permission ni redémarrage. Rapport : PUBLIC_PAGES_V2_AUTHENTICATED_ACCEPTANCE.md ; suivi : MOVEE_MOBILE_METADATA_MIGRATION_PLAN.md.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:225`.

### Lecteur commun v2 préparé — 28 octobre 2026

Le premier incrément de lecture du framework commun est raccordé en code Mobile : listes/fiches simples, filtres, tri et navigation serveur versionnée. Accès générique /pages préparé sous authentification, sans bascule des liens actuels. Actions, accueil et contenus détaillés ne sont pas déclarés repris ; les sections non prises en charge sont refusées, pas affichées partiellement. Backend v2 encore non activé selon sa livraison, aucune recette connectée effectuée.

Rapport et limites : PUBLIC_PAGES_V2_MOBILE_RESULT.md ; suivi durable : MOVEE_MOBILE_METADATA_MIGRATION_PLAN.md.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:231`.

### Reprise intégrale sur le framework — 28 octobre 2026

Décision utilisateur : tous les écrans Mobile, y compris accueil, compte, connexion, réservation et préférences, doivent être décrits par le framework MOVEE. Les différences de support sont ergonomiques ; toute capacité manquante est généralisée, pas traitée par une exception métier Mobile. Le diagnostic a été présenté et le démarrage autorisé. Les anciens parcours dédiés décrits ci-dessous restent l’existant à reprendre, pas la cible validée. Aucun changement des règles métier, scopes, consentements ou reprise sur timeout.

Suivi durable : MOVEE_MOBILE_METADATA_MIGRATION_PLAN.md. Première étape en cours : contrat commun et dépendances App, cadrées dans MOVEE_MOBILE_METADATA_FRAMEWORK_HANDOFF.md. Aucun écran basculé ni métadonnée installée dans ce premier lot.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:237`.

### Préférences et propositions raccordées — 26 octobre 2026

Le rapport Backend BOOKING_PREFERENCES_APPLICATION_RESULT.md confirme l'installation autorisée des deux tables privées et du marqueur, sans préférence initialisée ; purge des reçus active côté Backend/Codex. Ces opérations sont rapportées par Backend, non réexécutées ici. Ce point remplace l'état « schéma non installé » des entrées historiques ci-dessous.

Mobile propose désormais « Mes préférences horaires » depuis l'accueil/menu : lecture, ajout, correction et retrait explicites, jour/heure/fuseau visibles, maximum vingt entrées, vérification puis confirmation avant enregistrement. Portée globale personnelle ou centre connu ; les préférences globales restent en lecture seule dans le contexte centre. Depuis une prestation ou une réservation connue, le lien conserve l'adhérent et le centre ; le recueil professionnel dépend des droits Backend. Aucun annuaire ou parcours découverte complet supplémentaire n'est livré.

Après choix d'une prestation, les suggestions exactes précèdent le calendrier : jusqu'à cinq correspondances réelles sur quatorze jours maximum, bornées par l'horizon acquis. Zéro, une ou deux correspondances restent affichées telles quelles ; indisponibilité réseau distincte d'un résultat vide. « Choisir plus » conserve adhérent, prestation et centre dans le calendrier existant. La sélection reprend l'aperçu signé et le consentement habituels, sans retenue ni réservation automatique. Les propositions expirées nécessitent une actualisation.

Un timeout conserve la demande exacte pour vérification/rejeu volontaire ; conflit de version : relecture sans fusion silencieuse. Au-delà de vingt-quatre heures, pas de rejeu de l'ancienne demande ; l'abandon explicite relit d'abord l'état courant. Aucun apprentissage ou assistant activé. Le lot Bordeaux 08:00–21:00 reste non appliqué, indépendamment du schéma de préférences installé.

Validation Mobile : 53 tests synthétiques réussis, TypeScript sans erreur, export web Expo réussi. Aucune préférence/réservation réelle créée ou modifiée ici ; recette authentifiée utilisateur et appareils natifs encore à effectuer. Procédure : MOVEE_MOBILE_BOOKING_PREFERENCES_RECIPE.md.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:249`.

### Préférences Backend codées, installation requise — 26 octobre 2026

Contrat effectif `../../movee-app/docs/MOBILE_BOOKING_PREFERENCES_DELIVERED_CONTRACT.md`, rapport de tests et préparation de migration consultés. Préférences privées, suggestions exactes et écritures assistant liées à une intention humaine structurée actuelle sont codées côté Backend ; l’interprétation libre d’une phrase comme autorisation automatique n’est pas livrée. Adaptation explicit_only, pas d’apprentissage des habitudes. Les deux tables sont absentes localement : routes authentifiées indisponibles (preferences_schema_unavailable), outils correspondants masqués ; aucune préférence initialisée.

Prochaine dépendance : plan résolu de migration avec compatibilité des contrôles physiques/registre, à autoriser séparément avant application. Aucun SQL, paramètre Bordeaux ou code Mobile modifié dans cette prise en compte. Le calendrier demeure utilisable ; l’interface préférences/suggestions n’est pas encore raccordée ni présentée comme opérationnelle. Consigne Backend préparée dans `MOVEE_MOBILE_BOOKING_PREFERENCES_MIGRATION_NEXT_STEP.md`. Les exemples/tests Backend isolés ne constituent pas une recette locale ou native. Bordeaux reste en attente.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:256`.

### Préférences et suggestions v1 validées pour codage — 26 octobre 2026

Après lecture du contrat proposé `../../movee-app/docs/MOBILE_BOOKING_PREFERENCES_CONTRACT_PROPOSAL.md`, l’utilisateur valide explicitement la première version : au plus cinq créneaux réels, heure locale exacte sans tolérance, fenêtre de quatorze jours maximum également bornée par l’horizon acquis, préférences de même poids et fuseau IANA explicite par entrée. Le bouton Choisir plus conserve le calendrier ; moins de trois correspondances n’est pas complété artificiellement. Modification classique ou sur demande humaine explicite à l’IA ; aucun apprentissage automatique des habitudes dans ce premier lot. L’adaptation automatique demeure une étape ultérieure distincte.

Accord pour le codage Backend sur la base du contrat proposé, y compris préparation de la structure privée dédiée et tests isolés. Cet accord n’autorise pas l’application d’une migration, l’installation de Pages/permissions ou l’initialisation de préférences dans la base locale. Bordeaux reste en attente. Les limites techniques et contrats du document sont la base d’implémentation ; toute divergence métier ultérieure doit être signalée. Consigne prête dans `MOVEE_MOBILE_BOOKING_PREFERENCES_CODING_AUTHORIZATION.md`, non envoyée automatiquement. Aucune implémentation ni test supplémentaire effectué dans cette conversation pour cette validation documentaire.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:263`.

### Préférences horaires avant Bordeaux — 26 octobre 2026

L’utilisateur demande de traiter ce préalable avant d’appliquer le lot centre Bordeaux : recueillir à la découverte plusieurs préférences hebdomadaires d’adhérent (exemples lundi 18 h, mercredi 13 h), puis les ajuster avec l’IA à l’usage selon les habitudes. Réservation conversationnelle : propositions selon ces préférences ; réservation manuelle sans IA : d’abord 3 à 5 créneaux réellement disponibles correspondant aux préférences, puis bouton « Choisir plus » donnant accès au calendrier/créneaux existants. Même aperçu signé, validations et soumission ; aucune réservation automatique ou récurrence implicite.

Les préférences sont contrôlables par l’utilisateur et ne remplacent ni droits, ni disponibilité, ni durée acquise ou règles centre. Moins de trois correspondances ne produit pas de faux créneaux ; absence de préférence/correspondance et erreur sont distinctes, avec accès au calendrier. Tolérance horaire, fuseau/portée des préférences, classement et mécanisme précis d’apprentissage restent à formaliser : aucune valeur chiffrée ou écrasement automatique des préférences explicites n’est décidé ici. Le recueil pendant la découverte ne livre pas la réservation de discovery_session.

Demande Backend préparée dans `MOVEE_MOBILE_BOOKING_PREFERENCES_REQUEST.md`, non envoyée ; aucun contrat effectif de préférences/suggestions identifié dans la recherche ciblée. Aucune nouvelle table, route ou migration présumée. Lot Bordeaux explicitement mis en attente d’application à la demande de l’utilisateur ; le calendrier et les données existants sont conservés. Mise à jour documentaire seulement, aucun code/base/service ni test supplémentaire.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:272`.

### Centre de test Bordeaux : horaires demandés — 26 octobre 2026

L’utilisateur choisit un centre de test situé à Bordeaux, de 08:00 à 21:00 tous les jours. Fuseau de restitution : Europe/Paris ; fin de séance au plus tard à 21:00. L’identité du centre existant éventuel n’est pas établie par les documents consultés ; aucune fixture n’est relocalisée par supposition. Préparation Backend demandée dans `MOVEE_MOBILE_BORDEAUX_CENTRE_REQUEST.md`, incluant résolution de cible, compatibilité avec les horaires/fermetures existants et plan d’impact. Aucun nouveau paramètre d’offre, capacité, adresse ou droit inventé. Décision consignée sans application ni changement de code/base ; les durées acquises et réservations restent inchangées.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:277`.

### Catalogue et formulaires installés — 26 octobre 2026

Rapport `../../movee-app/docs/BOOKING_SETTINGS_APPLICATION_RESULT.md` consulté : application locale autorisée à 11:16:36 Europe/Paris, cinq ajouts (Pages 97–99, catalogue 224, reçu 19), rejeu zéro ajout, lignes préexistantes des 73 tables préservées selon la comparaison du rapport. Catalogue effectif avec défauts 60/60/60/30 ; formulaires administratifs installés. Le contrôle de leurs gardes ne constitue pas une recette visuelle authentifiée.

Aucune offre/durée acquise ni plage de centre modifiée. Les prochaines publications de centres/offres nécessitent leurs cibles et valeurs explicites et des lots séparés. Collectif/découverte/bilan restent non réservables ; Mobile reste sur le lecteur v1 compatible. Aucun changement de code, test supplémentaire ou application de données effectué dans cette conversation pour cette mise à jour documentaire. Les états « non installé » plus bas sont historiques.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:284`.

### Paramétrage Backend livré, application en attente — 26 octobre 2026

Contrat `../../movee-app/docs/BOOKING_SETTINGS_DELIVERED_CONTRACT.md`, résultats et plan d’application consultés. Code Backend livré : catalogue de prestations, durées/dérogations par offre, plages journalières/pauses/exceptions par centre, revalidation des conditions. Catalogue et trois Pages d’administration préparés mais non installés ; aucun nouveau réglage appliqué au jeu local. Les défauts 60/60/60/30 validés ne sont pas des fallbacks d’exécution et ne modifient pas les offres/engagements/réservations acquis. Une offre explicite de 30 minutes reste à 30 minutes tant qu’un changement ciblé n’est pas préparé et appliqué selon le contrat.

Collectif, découverte et bilan périodique restent non réservables : leurs références administrables ne constituent pas une livraison de ces parcours. Aucun bouton ou libellé Mobile ne doit reclasser une politique acquise historique non classée. Le mode autonome/accompagné est distinct du type de prestation.

Le lecteur Mobile courant get_booking_options version1 est conservé par le Backend ; il fournit déjà les durées effectives et les créneaux filtrés. Rien à modifier dans ce raccordement pour bénéficier des nouveaux contrôles lorsque les politiques sont effectivement publiées. Le lecteur optionnel get_booking_service_options version2 permettrait ultérieurement d’afficher une classification explicite et sa provenance ; il n’est pas raccordé par cette prise en compte.

Suite Backend : préparer le plan résolu du lot minimal d’administration/catalogue, puis recueillir l’autorisation d’application sur ce plan concret. Le compteur conditionnel de cinq ajouts du plan préparatoire n’est pas une autorisation. Horaires de centre et requalification d’offres restent des lots ciblés séparés avec leurs valeurs explicites. Aucun code ou paramètre métier modifié ici ; aucun nouveau test ni nouvelle recette revendiqué.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:295`.

### Durées et horaires paramétrables — décision du 26 octobre 2026

L’utilisateur demande un paramétrage Backend des durées, avec valeurs de départ : séance individuelle 60 min, cours collectif 60 min, découverte 60 min, bilan périodique 30 min. Les heures de début et de fin des séances de la journée doivent être paramétrables par centre. Aucun horaire chiffré n’est choisi. Mobile doit reprendre les durées effectives et créneaux serveur, sans constantes métier locales ni apparition fictive de prestations non livrées.

Les services Backend consultés lisent déjà une durée dans la politique acquise et les plages/fuseaux/fermetures du centre ; le formulaire de gestion et la correspondance de ces quatre prestations ne sont pas attestés ici. Demande précise : `MOVEE_MOBILE_SESSION_SETTINGS_REQUEST.md`. Décision consignée sans application aux politiques, engagements ou réservations existants, ni modification de code/base. La plage réservable et les horaires d’entrée physique ne sont pas assimilés silencieusement. Les valeurs du jeu local restent celles installées jusqu’à une application explicitement préparée dans la conversation Backend.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:302`.

### Réservations à venir raccordées — 26 octobre 2026

Le complément Backend est livré puis raccordé dans le périmètre planning déjà autorisé. Contrat vérifié dans `../../movee-app/docs/MOBILE_UPCOMING_BOOKINGS_CONTRACT.md`, résultats Backend consultés sans relancer sa suite. La vue « Réservations à venir » est accessible depuis accueil/menu et parcours planning. Elle interroge uniquement le lecteur dédié, sans condition de crédit, offre, disponibilité ou droit de création, et reste lisible même si le journal d’écriture est indisponible ou porte une intention incertaine.

Statut/libellé, sujet, centre/fuseau, coach lisible, horaires et phase proviennent du serveur. La phase « horaire en cours au moment de la lecture » ne devient pas une preuve de démarrage effectif. Les créneaux déjà commencés mais non terminés selon l’horaire sont conservés selon le contrat ; aucun état n’est déduit d’un libellé, d’un numéro d’équipement ou d’un bouton d’annulation. Le lien de fiche n’est présenté que s’il est publié, puis les lectures Pages actuelles recontrôlent leur accès. Aucun UID métier codé en dur.

Lecture par périodes de 30 jours dont les bornes UTC sont affichées, périodes suivantes accessibles au-delà de l’horizon commercial. La sélection coach est celle renvoyée par le lecteur, indépendante des choix de création. Pagination de 20 éléments, référence/expiration/inventaire conservés ; changement/expiration/échec retire le contenu de la requête courante et propose une reprise depuis le début, sans mélanger les pages. Après expiration de deux minutes, navigation suivante bloquée jusqu’à actualisation. En cas de borne de résultats, réduction volontaire à sept jours puis une journée, sans faux inventaire complet.

Validation Mobile : 39 tests synthétiques (6 upcoming, 6 planning, 14 réservation, 8 Pages, 5 auth), TypeScript, contrôle de diff, compilation web HTTP 200. Aucun nouvel essai navigateur authentifié ou natif revendiqué, aucun appel réel de mutation ni modification de données. Les réservations à venir ne sont plus bloquées sur le contrat mentionné dans les sections historiques ci-dessous. Nouvelle recette : `MOVEE_MOBILE_BOOKING_RECIPE.md`.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:313`.

### Planning : calendrier et horaires — 26 octobre 2026

L’utilisateur confirme les tests du lot visuel puis autorise la proposition de planning. La sélection par fenêtres de quelques heures est remplacée par un calendrier mensuel dans le parcours Nouvelle réservation, après choix de la prestation/du sujet autorisés. Les jours sont bornés à aujourd’hui et à l’horizon du choix, dans le fuseau du centre. Un jour sélectionnable n’est jamais présenté comme disponible avant lecture des horaires. Créneaux regroupés en matin/après-midi/soir ; libellés d’heure avec décalage UTC pour distinguer les heures répétées lors du retour à l’heure d’hiver. Dates/horaires exacts du serveur conservés pour l’aperçu et la soumission.

Les jours de 23/25 heures et les créneaux traversant minuit sont traités en dates civiles du centre, indépendamment du fuseau de l’appareil. Les recherches tronquées sont subdivisées sans montrer d’inventaire partiel ; en cas d’erreur/quota/limite technique, l’ensemble du résultat reste indisponible. Actualisation volontaire, aucune retenue ni écriture automatique. Aperçus signés, crédits, consentements, versions et journal idempotent inchangés.

**Périmètre restant :** le bloc dédié aux réservations à venir ne peut pas être alimenté proprement par le catalogue Pages générique livré : sémantique de liste/champs et fuseau par réservation manquants. Aucune déduction par nom de Page, ID, premier champ date ou liste des choix créables. Demande Backend préparée dans `MOVEE_MOBILE_UPCOMING_BOOKINGS_REQUEST.md`, non envoyée ; listes/fiches existantes maintenues dans Consultations. Cette étape n’est donc pas annoncée comme réalisée.

Validation : 6 tests planning synthétiques + 13 réservation + 8 Pages + 5 auth (32), TypeScript et diff. Compilation web de `/booking` HTTP 200 ; rendus calendrier isolés, pas de nouvelle recette authentifiée ou native. Aucun appel réel de création/annulation/accord, donnée métier ou service modifié. La recette utilisateur de ce nouveau calendrier reste à effectuer.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:324`.

### Identité visuelle MOVEE — 26 octobre 2026

Direction proposée puis explicitement autorisée par l’utilisateur : bleu nuit `#10131A`, jaune `#EFFF4F`, logo existant et inspiration du site Info local `http://movee.info.localhost:5051/fr/`, effectivement consulté. Connexion, accueil/compte, navigation/menu, listes/fiches et réservation/annulation/accords harmonisés : surfaces claires ou sombres selon le système, en-tête/menu de marque sombres, actions principales jaunes, actions secondaires encadrées/discrètes, cartes et conséquences en crédits mieux regroupées. Le jaune ne sert pas de texte courant sur fond clair. L’accueil donne accès à la réservation déjà livrée et ne déclare plus les actions métier indisponibles ; l’assistant reste signalé indisponible.

Le logo raster existant est repris sans retouche du dépôt Biz vers `assets/brand/movee-logo.png` ; aucun contenu commercial, droit ou règle métier Biz transféré. Pas de nouveau filtre, chiffre d’activité inventé, appel d’écriture ou changement Backend. L’utilisateur avait confirmé « ça fonctionne » avant ce lot ; conserver ce retour sans l’étendre à une recette native ou à tous les scénarios d’erreur.

Vérifications : 26 tests existants réussis (13 réservation, 8 Pages, 5 auth), TypeScript et contrôle de diff. Aperçu navigateur de connexion vérifié à largeur mobile : logo, composition, labels, état désactivé du bouton et passage clavier e-mail → mot de passe. Contrastes calculés des principaux textes/actions conformes aux seuils testés en clair et sombre ; cela ne constitue pas un audit complet d’accessibilité. Écrans connectés vérifiés par rendus isolés existants, sans nouvelle session authentifiée ni recette native. Aucune réservation réelle modifiée.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:333`.

### Ajout, annulation et accords de réservation — 25 octobre 2026

Lot autorisé dans la conversation Mobile après livraison du contrat Backend. Le menu et les consultations ouvrent « Nouvelle réservation » ; une fiche réservations permet de vérifier les possibilités d’annulation. Les prestations, sujets, centres, durées, coûts, modes et disponibilités viennent exclusivement du serveur. Aucune saisie d’ID, règle d’éligibilité locale ou sélection manuelle de coach ajoutée. Les fenêtres de recherche sont bornées par l’horizon fourni et se chevauchent de la durée afin de conserver les créneaux à cheval sur deux fenêtres. Une recherche tronquée doit être réduite avant sélection.

Un aperçu explicite restitue sujet, centre/fuseau, horaires, coach communiqué, motif, immobilisation/libération/pénalité, crédits non restitués et lots nets avec leurs échéances. Sa durée utilise l’intervalle serveur avec une horloge monotone locale conservatrice. Expiration ou changement de conditions impose une nouvelle lecture et un nouvel accord. Seul `/api/business-actions/booking-submit` soumet les nouvelles créations/annulations avec le jeton signé. Aucun succès avant reçu serveur effectif. Les accords sont récupérables après reconnexion ; confirmer demande une sélection explicite des conséquences, refuser reste possible. La confirmation d’anciens accords sans détail complet des crédits est bloquée.

Une intention non résolue par compte est conservée dans un stockage protégé, sans mot de passe/Bearer. Pas de file d’envoi automatique. Double clic bloqué, clé stable et arguments conservés pour récupération/rejeu volontaire ; une décision de confirmation/refus incertaine conserve aussi sa décision exacte et, le cas échéant, sa clé initiatrice. Un 403 de récupération ou la disparition d’un accord reste ambigu. Une réussite acquise reste visible si le nettoyage/actualisation échoue ; les consultations sont invalidées pour relire liste et fiche. Quota partagé avec Pages, 401 expire la session, données locales masquées lors de revalidation/changement de compte.

Vérifications : 13 tests réservation synthétiques, 5 auth, 8 Pages, TypeScript et contrôle de diff. Compilation web HTTP 200 de la route ; aucun nouvel essai authentifié complet ni recette native attesté. Aucune mutation métier réelle ni ajout au jeu Backend existant. Procédure : `MOVEE_MOBILE_BOOKING_RECIPE.md`. Les créneaux datés peuvent être échus ; leur renouvellement n’est pas effectué par Mobile.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:344`.

### Lisibilité des fiches programme et résultats — 25 octobre 2026

Lot proposé puis autorisé dans cette conversation. Les fiches spécialisées présentent un résumé puis des informations générales dépliables. Programme : nom réel des exercices lorsqu’il est fourni, séances structurées, prescription résumée, consignes/détails et médias accessibles sur ouverture volontaire. Les protections communiquées et l’avertissement de médias partiels restent visibles même lorsque les détails sont fermés. Résultats : séries regroupées par exercice avec résumé des mesures (par exemple « 12 répétitions · 20.50 kg »), détails complets et état de l’exercice dépliables ; l’avertissement d’historique partiel reste visible.

Le résumé ne calcule aucun résultat ni conversion : décimaux exacts et unités stockées conservés, zéro distinct d’une absence, unité manquante signalée lorsqu’une mesure est présente. Les répétitions de « Non renseigné » sont limitées au détail complet ; les mesures absentes ne deviennent jamais zéro. Aucun état de protection ni succès métier n’est déduit de l’absence d’un champ. Les fiches réservations, contrats API et règles d’autorisation sont conservés.

Fichiers adaptés : [src/components/mobile-page-content.tsx](../movee-mobile/src/components/mobile-page-content.tsx), [src/app/consultations.tsx](../movee-mobile/src/app/consultations.tsx), [src/lib/mobile-pages.ts](../movee-mobile/src/lib/mobile-pages.ts), assertions de [tests/mobile-pages.test.mjs](../movee-mobile/tests/mobile-pages.test.mjs), et les deux références Mobile. Vérifications : 8 tests Pages, 5 tests auth, TypeScript et contrôle du diff réussis. Les tests rendent les composants repliés et dépliés en isolation, avec fixtures synthétiques ; ce n’est pas une interaction navigateur ou une recette native. L’aperçu existant a été consulté en lecture seule et affichait la connexion, sans session utilisable pour ouvrir les fiches. Aucun identifiant privé utilisé, aucune nouvelle recette authentifiée annoncée. Aucun service relancé, aucun Backend/base/configuration modifié.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:353`.

### Retour de recette utilisateur — 25 octobre 2026

L’utilisateur déclare avoir terminé la recette puis confirme explicitement « Oui, sans anomalie » dans la conversation Mobile. Ce retour concerne la recette locale navigateur suivie dans cette conversation ; aucun compte rendu détaillé par scénario, trace JavaScript de Retry-After ou résultat natif n’est fourni ici. Conserver cette confirmation utilisateur sans la transformer en tests supplémentaires exécutés par l’agent ni en validation iOS/Android/VoiceOver/TalkBack. Le prochain lot proposé concerne la lisibilité des fiches programmes/résultats ; il reste soumis à accord avant modification de code.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:358`.

### Environnement supervisé et recette web — 25 octobre 2026

La procédure commune est désormais `../../ENVIRONNEMENT_DEVELOPPEMENT_MAC.md`, pilotée par `../../movee-dev` et launchd. Utiliser `./movee-dev start --with-expo`, `status`, `logs expo` ou `logs backend` depuis la racine MOVEE ; pour Expo seul : `start expo`, `restart expo`, `stop expo`. Ne plus lancer une seconde instance Expo manuellement sur 8081, ni tuer un processus externe pour libérer un port. Sources Mobile surveillées ; redémarrer Expo après changement de configuration publique ou dépendances.

État vérifié via `./movee-dev status` : MariaDB 3306 disponible, Redis 6380, Backend 5050 et Expo 8081 gérés et prêts. Backend Flask sous Gunicorn, Redis sans persistance ; assistant/worker métier/push restent désactivés selon la procédure commune. Les services démarrés repartent à l’ouverture de session ; `stop` retire leur démarrage automatique et laisse MariaDB intacte. Perte de Redis : reconnexion Mobile nécessaire. API locale `http://127.0.0.1:5050`, aperçu `http://localhost:8081`, aucun accès téléphone/LAN ajouté.

L’utilisateur confirme connexion et accès aux trois listes dans le navigateur. Les contrôles HTTP CORS/absence de cookies sont rapportés par la couche infrastructure ; ils ne prouvent pas à eux seuls la lecture JavaScript de Retry-After. Restent à recetter sur le Backend réel : fiches détaillées, Retry-After via fetch et navigation sous quota, accessibilité et terminaux natifs. Les tests synthétiques Mobile antérieurs restent distincts. Aucun service redémarré ni changement applicatif effectué pour cette prise en compte ; les changements locaux sont conservés. Les états d’arrêt et commandes manuelles datés ci-dessous sont historiques, remplacés par cette procédure.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:367`.

### Simplification UX des consultations — 25 octobre 2026

Lot présenté puis autorisé dans la conversation Mobile. Les tris et filtres techniques ont été retirés de l’interface des trois consultations ; les requêtes gardent `sort: null` et `filters: []`, avec l’ordre Backend. Aucun rôle, champ SQL ou ID de Page codé en dur. Le catalogue reste fourni par le serveur.

Les listes utilisent des cartes compactes : un texte court ou une date publiés dans la configuration sont mis en évidence, avec leur libellé serveur ; tous les autres champs autorisés restent visibles en présentation secondaire. Accès « Voir le détail » uniquement si le serveur fournit un lien de fiche. Nombre de résultats lisible, numéro de page simple et navigation précédente/suivante uniquement si utile, sans texte technique offset/limit. Les fiches détaillées et contenus spécialisés sont conservés.

Les futurs filtres statut/centre attendent des choix libellés et autorisés du Backend. Ne pas réintroduire un champ demandant un identifiant numérique, inventer les valeurs possibles ou bâtir des choix incomplets à partir de la seule page de résultats chargée. Aucun nouveau contrat n’est considéré livré par cette décision UX.

Fichiers adaptés : [src/app/consultations.tsx](../movee-mobile/src/app/consultations.tsx), [src/components/mobile-page-content.tsx](../movee-mobile/src/components/mobile-page-content.tsx), suppression de l’aide de tri inutilisée dans [src/lib/mobile-pages.ts](../movee-mobile/src/lib/mobile-pages.ts), assertions existantes de [tests/mobile-pages.test.mjs](../movee-mobile/tests/mobile-pages.test.mjs), et les références Mobile. Vérifications : 8 tests Pages et 5 tests auth réussis, TypeScript et contrôle du diff valides. Le rendu compact est vérifié par le rendu TSX isolé des tests ; aucune nouvelle recette navigateur authentifiée ou native n’est annoncée. Backend, données, session et règles d’autorisation inchangés.

Les sections datées du 23 octobre ci-dessous décrivent les étapes précédentes ; la présente section remplace leur présentation du panneau et des filtres.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:380`.

### Consultations classiques Pages v1 — 23 octobre 2026

Présentation des listes simplifiée après accord utilisateur : tri et filtres regroupés derrière un bouton discret « Filtrer / Trier », panneau replié par défaut et refermé après application ; indication lorsque des options sont actives. Aucune modification des contrats ni des permissions. Vérifications de cette adaptation : TypeScript, 8 tests Pages et contrôle du diff réussis ; pas de nouvelle recette native.

Implémentation Mobile autorisée dans cette conversation : accès volontaire depuis le menu latéral et l’accueil aux listes publiées par `GET /api/mobile-pages`, puis configuration, données et fiche via les trois POST du contrat Backend Pages v1. Catalogue et libellés viennent du serveur ; aucun menu par rôle, ID de Page ou schéma SQL n’est figé dans le client. Le chat demeure l’expérience principale cible ; ce lot ne simule ni assistant ni disponibilité IA.

Réservations, programmes existants et séances/résultats sont consultables selon les Pages et droits renvoyés. Listes paginées, tri annoncé et un filtre typé à la fois ; fiche uniquement si `detail_page_uid` est fourni. Programmes : séances, prescriptions, médias ouvrables explicitement en HTTP(S) et protections communiquées ; aucune édition. Résultats : séries regroupées par exercice, unités et chaînes décimales conservées, avertissement si historique partiel. Valeur absente distincte de zéro/faux, type inconnu signalé. Dates affichées dans le fuseau du téléphone/navigateur avec indication du fuseau, sans filtre de date implicite.

Chargement, catalogue/liste vide, refus et pannes sont distingués. Les lectures sont en mémoire, liées à la session et à l’écran actif ; elles sont invalidées à la déconnexion, revalidation de session, changement de Page ou perte de focus. Un 401 expire la session, un 403 retire le contenu concerné ; pas de retry automatique, délai `Retry-After` partagé entre lectures de la session lorsqu’il est accessible.

Validation locale : cinq tests auth et huit tests Pages passent, TypeScript et contrôle de diff valides. Essai navigateur avec API synthétique isolée : catalogue/menu, liste, fiche programme/résultats, protections, pagination, filtre vide, refus 403, quota 429, expiration 401 et déconnexion vérifiés. Ces essais ne sont ni une recette HTTP/MariaDB/Redis du Backend réel ni une recette adhérent/coach ou native VoiceOver/TalkBack/SecureStore. Les fixtures ne sont jamais affichées par le produit connecté au Backend réel.

Suivi CORS — retour Backend reçu le 23 octobre : correctif confirmé en lecture dans `movee-app/app.py` et `docs/MOBILE_PAGES_CONTRACT.md` : `Authorization` autorisé au préflight, `Retry-After` exposé au navigateur, restrictions d’origine de production conservées. Aucun changement du client Mobile requis. Contrôle des ports lors de cette reprise : aucun listener sur 5050, 6380 ou 8081 ; recette navigateur sur Backend réel non exécutée. Les comptes/données adhérent/coach restent à préparer selon le plan Backend, sans création dans cette conversation. Les contrats centre/profil, IA, historique conversationnel, informations prioritaires et actions métier restent ouverts.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:395`.

### Lot local accueil et navigation — 21 octobre 2026

Lot de code autorisé : session partagée au niveau du layout, menu latéral avec accueil/compte/déconnexion, route compte protégée et ancienne route Explore redirigée vers l’accueil. L’accueil connecté indique les fonctions encore indisponibles, sans conversation ni résultat métier simulé. Le compte affiche l’identité connue et la déconnexion, sans prétendre fournir tous les paramètres essentiels cibles.

Les seuls appels restent login/me/logout. Aucun centre, profil ou droit n’est inventé. Le délai dépassé est distingué d’une erreur réseau. Le menu et les vues connectées suivent le thème système ; aucune recette VoiceOver/TalkBack, installation native ou persistance SecureStore sur appareil n’est attestée par ce lot. L’écran de connexion conserve son thème clair actuel.

Accueil conversationnel, fil unique, zone prioritaire, menu métier contextuel et secours automatique attendent les contrats Backend. Voir `MOVEE_MOBILE_BACKEND_CONTRACT_REQUEST.md` : demande préparée, non envoyée. Aucune évolution des décisions T/AR ni modification Backend.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:404`.

### Actualisation de l’état local — 21 octobre 2026

La conversation **Movee App Mobile** est propriétaire de `/Users/mbenmouha/Documents/Movee/movee-mobile`, client iOS/Android des adhérents et coachs. Elle traite l’interface, la navigation, les états locaux et les interactions avec les API ; les autorisations et effets métier restent exclusivement décidés par MOVEE App Backend. Aucun accès direct Mobile à SQL, Redis ou OpenAI.

Un premier parcours connexion e-mail/mot de passe → identité → déconnexion est implémenté. L’utilisateur a confirmé la connexion à son compte local **dans l’aperçu navigateur du Mac**. Le stockage sécurisé natif est codé mais reste à tester sur téléphone ; les 78 décisions T et AR restent les exigences cibles, sans équivalence entre un écran de connexion et l’accueil conversationnel complet.

Le parcours de développement/distribution retenu est Expo/React Native avec EAS Build cloud ; Xcode est facultatif. Apple Developer est commandé, activation en attente. Aucune installation iPhone/Android ni livraison push n’est attestée ; inscription, récupération, contexte centre/profil, réservations, programmes et IA ne sont pas livrés par ce premier lot. Voir le référentiel technique Mobile pour l’infrastructure, les contrats réellement raccordés et les validations effectuées. Aucune décision fonctionnelle antérieure n’est modifiée.

---


**Consolidation du 17 octobre 2026 :** socle historique conservé, arbitrages validés AR01–AR07 et AR05.1–AR05.10 intégrés aux sections métier et techniques concernées. Ils précisent ou remplacent uniquement les formulations explicitement visées. Les autres décisions Q/B et les 78 décisions mobiles demeurent applicables. Les décisions sont des spécifications cibles, sans preuve supplémentaire d’API, d’implémentation, de recette réelle ou de déploiement. Les formats, paramètres, canaux externes et langues initiales non décidés restent à spécifier.

**Version : 17 octobre 2026 — mise à jour après validation des thèmes 1 à 8 (T1.1–T1.8, T2.1–T2.10, T3.1–T3.10, T4.1–T4.10, T5.1–T5.10, T6.1–T6.10, T7.1–T7.10, T8.1–T8.10).** Les autres arbitrages ouverts conservent leur statut À VALIDER.  
**Application :** MOVEE Mobile, clients iOS et Android destinés aux adhérents et aux coachs du réseau MOVEE.  
**Nature :** spécification fonctionnelle dédiée au client mobile, dérivée des décisions MOVEE App. Ce document ne prouve ni la disponibilité des API, ni l'existence d'une application distribuée. Les décisions de conception mobile non encore arbitrées sont explicitement marquées **À VALIDER**.

**Traçabilité des précisions :** AR01 remplace l’approbation coach systématique des adaptations supervisées par les validations selon limites préautorisées et consentement adhérent ; AR02 précise B8.2 pour l’écriture des programmes ; AR03 distingue centre contractuel et contexte actif ; AR04 résout l’exception Élevé aux heures calmes applicatives ; AR05 fixe les dix périmètres ; AR06 distingue historique durable, contexte éphémère et mémoire ; AR07 fixe acquisition externe, centralisation App et restitution Mobile. Les autres limites, permissions, validations sensibles, protections sportives et exigences de reprise restent conservées.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:1183`.

### 15. Arbitrages mobiles restant ouverts

**À VALIDER, sans bloquer la rédaction des référentiels :** design system, détail des écrans et rubriques dans le cadre de navigation validé T1.1–T1.8, technologies finales de distribution iOS/Android, modalités techniques d'accessibilité dans le cadre validé T8.1 et articulation détaillée des préférences système/applicatives T8.2/T8.8, modalités techniques et contrats de cache/offline dans le cadre validé T7.1–T7.4, phasage et modalités techniques du vocal temps réel validé T5.9, prise en charge photo/vidéo par phase, fournisseur push et calendrier de publication. Aucune de ces propositions ne modifie les règles métier MOVEE App.

La navigation principale, le fil unique, la zone prioritaire et le secours automatique sont validés par T1.1–T1.8 et ne sont plus des arbitrages ouverts. Restent à contractualiser avec MOVEE App : persistance/récupération du fil et de l'historique, contexte utilisateur et capacités, informations prioritaires, disponibilité de l'assistant et couverture des parcours classiques.

Les décisions T2.1–T2.10 sont validées. Restent ouverts les contrats d'inscription publique, de vérification e-mail et d'opérations sensibles restreintes, d'approbation des rattachements/invitations, de sélection du couple centre + profil, de cycle de session, de récupération du mot de passe, de modification du profil et de suppression/conservation des données et effets sur les affiliations. Ces inconnues techniques ne rouvrent pas les décisions produit.

Les décisions T3.1–T3.10 sont validées. Restent à vérifier avec MOVEE App les consultations et calculs de performances, les données machine centralisées, les programmes et démonstrations, la réservation et le déplacement cohérent, les deux modes d'adaptation avec notification ou validation coach, la transmission/historisation des messages et les événements proactifs. La saisie manuelle précédemment évoquée ne doit pas être interprétée comme obligatoire pour les séances suivies par machines (T3.4). Toute divergence avec les règles métier App doit être arbitrée côté App avant intégration, sans réécriture locale de ses règles.

Les décisions T4.1–T4.10 sont validées. Les contrats coach à vérifier sont détaillés dans le référentiel technique (§4.4) : adhérents autorisés, détection/priorité, programmes, propositions/validation groupée, planning, disponibilités/conflits, messages, bilans, absences/relances et classification des actions. Les priorités T4.2 ne redéfinissent pas les niveaux de sécurité de la section 8. AR01 et AR02 règlent l’autonomie et l’exclusivité IA de T3.7/T4.3–T4.4/T4.10 ; leurs contrats d’exécution restent à vérifier chez App, sans réouvrir ces choix.

Les décisions T5.1–T5.10 sont validées. Le mode vocal temps réel est une exigence acquise, tandis que technologie, transport et calendrier restent ouverts. Les douze contrats assistant à vérifier avec MOVEE App sont recensés au §4.5 du référentiel technique ; mémoire, historique et données métier restent distincts, avec contexte authentifié faisant autorité.

Les décisions T6.1–T6.10 sont validées. Les seize contrats notifications à vérifier avec MOVEE App sont recensés au §4.6 technique. Les paramètres précis de préférences, les modalités de l’exception Élevé validée par AR04, la classification de confidentialité et les garanties de synchronisation restent à contractualiser ; aucun fournisseur de notifications n'est sélectionné.

Les décisions T7.1–T7.10 sont validées, y compris l'absence d'utilisation du mobile pendant les entraînements. Les dix-huit contrats techniques/backend ouverts figurent au §4.7 technique ; l'inventaire précis des lectures et opérations locales autorisées n'est pas arrêté par les exemples. Les données machine restent du ressort d'App, et les garanties de reprise, révocation hors réseau, mises à jour et compatibilité restent à démontrer.

T8.1–T8.10 clôturent l'intégration documentaire des huit thèmes, soit 78 décisions validées. Les exigences d'accessibilité et d'expérience sont acquises ; les dix-huit points techniques ouverts figurent au §4.8 technique, sans remplacer les contrats antérieurs. Aucune implémentation, collecte, intégration native ou ouverture de chantier backend n'est autorisée par cette clôture.

**AR01–AR07 validés :** ne plus rouvrir autonomie supervisée, exclusivité IA de création/modification de programmes, centre contractuel/actif, exception Élevé, périmètres AR05, historique durable ni responsabilités des mesures externes. Restent à spécifier les contrats, droits détaillés, paramètres, canaux externes, langues initiales/repli et recettes. AR05 ne fixe pas un calendrier des capacités serveur. Les autres écarts de l’audit ne sont pas réputés clos.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:3`.

### État courant et consolidation demandée — 31 octobre2026

Suite du diagnostic : codage/tests approuvés par « ok », entrée14unique et reprise actuelle de journaux8–14 codées ;351testsMobile, TypeScript et exports3plateformes conformes. Rapport MOBILE_PAGES_CONSOLIDATION_MOBILE_RESULT.md. Backend prépare candidat30Pages et plan exact ; aucune suppression SQL, activation Backend ou redémarrage encore autorisé par cette phase. Les paragraphes « analyse seulement » ci-dessous décrivent le stade initial, avant cet accord de codage.

DEFAULT_PAGES_PROTOCOL vaut14 après installation/bascule autorisées ; les états de préparation13 ci-dessous sont historiques. L’utilisateur demande une consolidation sans anciennes générations de Pages ni doublons : identité canonique stable, évolution des métadonnées en place, aucun nouveau profil15/copie ou mapping permanent pour cette consolidation. Analyse/documentation seulement à ce stade. Audit MOBILE_PAGES_CONSOLIDATION_AUDIT_AND_PLAN.md : anciennes routes explicites2–14, dépendances partagées du lecteur14, reprise des journaux8–14 et reconnaissance Backend des états historiques doivent être traitées ensemble avant suppression. Conserver preuves de migration/reçus ; le préflight actif ne devra plus exiger l’existence des Pages retirées. Les nombres finaux et rebindings seront établis par inventaire READ ONLY coordonné avec MOVEE App. Aucun changement runtime, SQL ou redémarrage dans cette préparation.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:86`.

### Parcours adhérent/coach : diagnostic ergonomique — 30 octobre 2026

Signalement utilisateur : parcours mélangés et peu ergonomiques. Inspection graphique actuelle en lecture seule de la session ouverte : accueil, liste Programmes et fiche programme, captures sauvegardées et inspectées dans codex/ux-audit-2026-10-30. Accueil restauré, aucun login/logout ou geste métier. Comparaison Services App actuelle : adhérent70 et coach68 reçoivent la même entrée210 et huit actions plates en9/10 ; les réservations affichent les lignes propres à l’adhérent mais une sélection d’adhérent au coach. Les préférences sont celles de réservation, pas des disponibilités professionnelles. Diagnostic ciblé, pas une recette graphique coach ou un audit complet d’accessibilité.

Constats : absence de priorité à l’accueil, compte/déconnexion au même niveau que réserver, listes et fiches très techniques, versions/identifiants inutiles pour l’adhérent, actualisations répétées et navigation par données plutôt que par tâches. Retour et filtres repliés déjà présents. Un seul programme terminé dans la session de recette ; ne pas en déduire l’absence générale de programme courant.

Cible proposée, non validée et non implémentée : adhérent Accueil/Réserver/Mon entraînement/Mon compte ; coach Aujourd’hui/Adhérents/Suivi/Mon compte, avec contexte de l’adhérent maintenu. Accueil résumé et planning coach ne sont pas réputés livrés. Conserver Pages/Fields/actions comme source serveur, droits/scopes inchangés, aucun écran/UID métier codé selon le rôle ; toute extension de présentation doit être commune. Ne pas exposer les protocoles techniques dans le parcours normal. Prochain chantier proposé : organisation des parcours avant la recette globale ; pas de nouvel ajout fonctionnel isolé avant clarification. Rapport de travail : codex/ux-audit-2026-10-30/diagnostic-parcours.html.

Aucun code, SQL, permission, service ou test métier modifié/exécuté par cette analyse. L’audit graphique complet coach, téléphone/tablette, focus et lecteur d’écran reste à faire. MOVEE App poursuit le diagnostic des scopes et capacités disponibles, sans codage.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:120`.

### Catalogue d’exercices multilingue et médias — diagnostic engagé

Demande utilisateur après installation RepDB côté App. Rapport REPDB_APPLICATION_ACTIVATION_RESULT.md et contrat REPDB_DELIVERED_CONTRACT.md effectivement lus :22exercices/88contenus/168assets installés, niveauphysique0003,83tables, préflight exercise_catalogue_i18n_v1 et Backend actifs selon rapport ; aucun ajoutMobile ou affectationdeprogramme automatique.

Contrat textuel existant : X-MOVEE-Locale fr/en/de/es (frpardéfaut, aucunreplisilencieux), types et profils4–9fermés ; les4paires value_schema/value de repdb_provider_examples sont acceptées par le validateurMobile dialecte2 (contrôleisolé exécuté). Actuellementtype6URL renducommevaleur, pascapacitéimageintégrée explicite.

Demande de diagnostic/proposition ciblée transmiseà MOVEE App : langue capturée parrequête/lecture, invalidationversions/curseurs/réponsesobsolètes ; ressources protégéesetanimations déclarées viaframeworksansbrancheparentité/écran, droitsrevalidés, pasdejetondansURL/journaux ni cachepersistant, attributionconservée ; vérifier accès normalaucatalogueparactionsnativesetdroitsactuels. Expo-image déjàinstallé offrecachePolicy:none/autoplay etstart/stopAnimating vérifiés dans lestypeslocaux ; aucunenouvelledépendancejustifiée.

AucuncodeMobile/SQL/droit/service modifié pour ce diagnostic ; nouvelle capacité deprésentation àvalideravantcodage selon AGENTS.md. Aucuneconnexionréelle,recetteHTTPauthentifiéeouappareilnatif effectuée. Recetteglobale toujoursreportée.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:216`.

### Autorisation commune application et redémarrage — 30 octobre 2026

Consigne explicite de l’utilisateur : pour les prochaines opérations, l’autorisation d’appliquer un changement inclut le démarrage/redémarrage du Backend nécessaire via movee-dev et les contrôles de disponibilité/lecture qui suivent. Ne plus demander une seconde autorisation pour cette activation. Si le Backend est arrêté pour l’application, le remettre en service après succès et contrôles conformes ; en cas d’échec ou de divergence, diagnostiquer avant toute reprise incompatible.

Cette règle n’autorise pas l’application d’un plan non accepté, périmé ou divergent, ni des annulations/confirmations métier, ni le redémarrage de MariaDB/Redis/Expo sans nécessité autorisée. Elle ne modifie pas rétroactivement les rapports ni les anciennes consignes ponctuelles. Pas de redémarrage inutile pour un lot de données qui n’en nécessite aucun. Transmettre cette autorisation commune dans les prochaines consignes à MOVEE App ; aucune nouvelle demande d’accord d’activation à l’utilisateur pour le même lot autorisé.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:223`.

### Lecteur des processus Pages v8 préparé — 29 octobre 2026

Contrat PUBLIC_BOOKING_PROCESS_PAGES_V8_DELIVERED_CONTRACT.md amendé pris en charge. Entrée explicite /pages?protocol=8 : collections à curseur, contexte/ligne signés, formulaires natifs préparer/exécuter, champs et paramètres par UID, décision et récupération depuis decision_reference publique. Profil fermé sans création ni fallback ; dialecte movee_read_value_v2 explicitement séparé des anciens lecteurs. Gestionnaire et journal privés existants adaptés : intention durable avant dispatch, lookup puis renvoi volontaire de la même intention depuis un contexte frais, session remplacée protégée, aucun Bearer/contexte de Page stocké. Anciens canaux et accès usuels7 conservés.

136 tests Mobile réussis, TypeScript et export web conformes. Métadonnées8 non installées et Backend8 non activé selon livraison App ; aucune recette authentifiée8/native ni mesure MariaDB effectuée ici. Aucun SQL, droit, code Backend ou service modifié. Détails et limites : PUBLIC_BOOKING_PROCESS_PAGES_V8_MOBILE_RESULT.md ; suite dans MOVEE_MOBILE_METADATA_MIGRATION_PLAN.md.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:259`.

### Lecteur commun v2 préparé — 28 octobre 2026

Contrat réel PUBLIC_PAGES_V2_DELIVERY.md pris en compte : src/lib/public-pages.ts, components/public-page-reader.tsx et route générique protégée pages.tsx. Transport Bearer v2 fixe, config_version et cible réautorisée, filtres/tri/pagination en mémoire et relecture au retour ; refus des capacités requises manquantes, pas de fallback automatique v1. Pas de nouveau mapping UID runtime. 62 tests synthétiques réussis, TypeScript et export web conformes ; aucune activation Backend, SQL ou recette authentifiée.

Rapport et limites : PUBLIC_PAGES_V2_MOBILE_RESULT.md ; suivi durable : MOVEE_MOBILE_METADATA_MIGRATION_PLAN.md.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:265`.

### Reprise metadata-driven autorisée — 28 octobre 2026

La cible reprend PageService/PageRepository, les configurations hydratées du moteur et ses conventions natives (UID opaques, champs/actions par instances, default_config + overrides minimaux). Le transport Mobile v1 réduit aux types1/4 read_only n’est pas le contrat cible complet. Les écrans spécifiques et content_type métier constituent un écart à résorber. Les protections Bearer/session, quotas, journal et Services restent nécessaires ; aucune exposition brute de design_mode ou accès aux routes web sous cookies depuis Mobile.

Suivi : MOVEE_MOBILE_METADATA_MIGRATION_PLAN.md ; cadrage commun/demande App : MOVEE_MOBILE_METADATA_FRAMEWORK_HANDOFF.md. Six Pages91–96 constatées READ ONLY avec UID lisibles et config_actions vides ; leur remplacement nécessite une carte coordonnée et une évolution du preflight, sans SQL autorisé par ce démarrage. Contrat effectif commun encore à livrer ; aucun DTO v2 ni capacité générique nouvelle annoncé comme existant. Aucun écran basculé dans le lot initial.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:271`.

### Préférences Mobile raccordées au schéma installé — 26 octobre 2026

Lecture du contrat effectif et de BOOKING_PREFERENCES_APPLICATION_RESULT.md dans `../../movee-app/docs/` : migration0001 installée,75 tables et marqueur225 selon le rapport Backend, purge quotidienne active, préférences initialement vides. Ni migration, ni purge, ni écriture Backend réexécutée par Mobile. Les états « schéma absent » ci-dessous sont historiques.

[src/lib/mobile-preferences.ts](../movee-mobile/src/lib/mobile-preferences.ts) raccorde les quatre routes POST Bearer fixes, credentials omit : read/replace/result et suggestions/read. Validation DTO v1, explicite_only, sujet/portée/version, six seuls champs d'entrée, contexte et calendrier identiques, intentions et dates exactes, absence d'inférence, validité monotone. Suggestions : limit5, fenêtre14jours, durée et horizon validés serveur, sélection vers le même aperçu signé. Aucun endpoint administratif/web ni appel IA.

Écran [src/app/preferences.tsx](../movee-mobile/src/app/preferences.tsx), bloc `src/components/booking-suggestions.tsx`, liens accueil/menu et réservations connues. Édition conserve preference_id, filtre la portée modifiable ; une relecture remplace les brouillons périmés même à version identique. Pas de liste de centres/adhérents inventée ; le recueil professionnel ne remplace pas un futur parcours découverte complet.

Le provider d'écritures existant accueille les intentions kind=preferences et reçus applied : sauvegarde avant envoi, verrou anti-double clic, isolation compte/session, résultat puis rejeu volontaire à clé/paramètres identiques, refus du rejeu après24h, abandon explicite après lecture courante. Un seul écrit irrésolu par compte bloque les suivants. Conflit de version réinvalide les lectures. Journal web AES-GCM existant ; SecureStore natif découpe uniquement les grandes intentions privées en morceaux protégés, manifeste publié après écriture, marqueur de nettoyage pour reprise après interruption. Aucun jeton/mot de passe stocké dans ce journal.

Tests : `node --experimental-transform-types --test tests/*.test.mjs` (53 réussis), `npx tsc --noEmit` et export web Expo vers `/tmp/movee-mobile-preferences-web-20261026` réussis. Tests nouveaux : contrat, contexte/intentions erronées, zéro à cinq propositions, expiration, calendrier conservé, édition globale en lecture seule, validation HH:MM et confirmation, timeout403/410, conflit409, compte, verrou et stockage interrompu. `npm run test:preferences` disponible. Pas de nouvelle dépendance ; aucun redémarrage du dispositif nécessaire pour ces sources. Services gérés prêts, bundle web HTTP200 ; aucun appel authentifié ni modification des données locales, pas de recette native attestée.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:283`.

### Contrat préférences effectif, schéma non installé — 26 octobre 2026

Documents Backend MOBILE_BOOKING_PREFERENCES_DELIVERED_CONTRACT.md, MOBILE_BOOKING_PREFERENCES_DELIVERED_RESULT.md et BOOKING_PREFERENCES_MIGRATION_PREPARATION.md consultés dans `../../movee-app/docs/`. Quatre routes Bearer codées, DTO v1 ; suggestions sans IA et trois capacités assistant avec écriture humaine structurée courante. Le schéma reste absent de la base locale, donc 503 preferences_schema_unavailable et capacités masquées. Aucun fallback vers un faux état vide. Mobile reste sur son parcours actuel en attendant ce préalable de recette et son raccordement.

Paquet SQL pending non enregistré/appliqué ; runner décrit comme SELECT-only refusant --apply. La migration additive requiert un delta/plan résolu, la reconnaissance du nouvel état par preflight et les métadonnées/structure complètes, puis accord séparé pour application. Les CREATE MariaDB peuvent committer implicitement : ne pas promettre un rollback global ni appliquer directement up.sql. Le plan doit traiter DDL partiel/rejeu, conservation des 73 tables, marqueur et exploitation de la purge physique des reçus. La récupération de 24 h n’est pas une promesse de purge sans maintenance.

Demande de préparation : `MOVEE_MOBILE_BOOKING_PREFERENCES_MIGRATION_NEXT_STEP.md`. Aucune migration, test applicatif, modification de code/service/dépendance ou initialisation effectuée ici. Résultats Backend lus, non réexécutés ; Bordeaux non appliqué.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:292`.

### Contrat préférences v1 : accord de codage — 26 octobre 2026

Validation utilisateur du contrat proposé `../../movee-app/docs/MOBILE_BOOKING_PREFERENCES_CONTRACT_PROPOSAL.md` comme base de codage Backend, sans application de migration. Conserver explicit_only, maximum cinq suggestions exactes sur quatorze jours bornés par les conditions acquises, mêmes Services pour IA et sans IA, même aperçu signé/soumission. Stockage privé et reçus bornés à préparer/tester selon la proposition ; aucune table/route considérée existante avant livraison. Raccordement Mobile après contrat effectivement implémenté et exemples vérifiés. Instruction de codage préparée dans `MOVEE_MOBILE_BOOKING_PREFERENCES_CODING_AUTHORIZATION.md` ; aucune modification applicative, migration, service ou test dans ce lot documentaire. Bordeaux reste en attente.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:297`.

### Contrats préférences et suggestions requis — 26 octobre 2026

Nouveau préalable utilisateur au lot Bordeaux : préférences hebdomadaires persistées par adhérent, recueil découverte, adaptation IA contrôlable, lecteur déterministe de 3–5 créneaux personnalisés utilisable sans IA, puis accès « Choisir plus » au calendrier livré. Les contrats actuels options/disponibilité/aperçu/soumission ne fournissent pas à eux seuls ces opérations. Recherche ciblée dans Services/contrats/référentiels et export de schéma : aucun endpoint de ces nouvelles fonctions identifié, sans conclusion d’audit exhaustif ni proposition de schéma physique. Ne pas réutiliser implicitement les préférences de notification.

Le Backend doit résoudre droits, stockage/versionnement, fuseaux/portée, tolérance et classement, distinction explicite/inféré et contrôle d’adaptation ; l’IA et Mobile doivent partager les mêmes données et calcul de propositions sous Services. Lecture suggestions sans création/hold ni dépendance au modèle, puis revalidation via aperçu signé existant. La proposition de conception est distinguée des décisions dans `MOVEE_MOBILE_BOOKING_PREFERENCES_REQUEST.md` ; aucune route n’est inventée. Modification des préférences : contrat de résultat/version/reprise à livrer avant interface persistante.

Lot Bordeaux non appliqué par cette conversation et désormais en attente explicite de ce préalable. Aucun code applicatif, SQL, service ni dépendance modifié ; pas de test supplémentaire revendiqué. Le calendrier actuel reste la voie classique utilisable jusqu’au raccordement des nouveaux contrats.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:306`.

### Application du catalogue prise en compte — 26 octobre 2026

Lecture du rapport Backend `../../movee-app/docs/BOOKING_SETTINGS_APPLICATION_RESULT.md` : catalogue/Pages installés sur la cible locale, même plan autorisé SHA256 92a73cdcd619c5731b5541023b895b6162498ed327db76ae297f60164161cc2c, application à 11:16:36 Europe/Paris ; cinq ajouts, rejeu réel zéro ajout, projection des lignes préexistantes inchangée. Les contrôles sont ceux rapportés par Backend, non réexécutés par Mobile.

Aucune modification applicative nécessaire pour get_booking_options v1. Les trois API/formulaires administratifs restent hors du transport Mobile ; le lecteur v2 optionnel n’est pas raccordé. Politiques acquises, offres et horaires locaux préservés ; pas de recette visuelle des formulaires ou nouvelle recette native attestée ici. Les publications ciblées centres/offres restent à définir. Mise à jour documentaire uniquement, aucun test ni changement de service/base par Mobile.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:313`.

### Compatibilité avec le paramétrage Booking livré — 26 octobre 2026

Les trois documents Backend BOOKING_SETTINGS_DELIVERED_CONTRACT.md, BOOKING_SETTINGS_DELIVERED_RESULT.md et BOOKING_SETTINGS_APPLICATION_PLAN.md ont été lus dans `../../movee-app/docs/`. get_booking_options reste en contract_version1 et garde sa projection, utilisée par `getOptions` dans [src/lib/mobile-booking.ts](../movee-mobile/src/lib/mobile-booking.ts). Les recherches/aperçus/soumissions conservent leurs routes/arguments ; les durées restent celles acquises et les contrôles de plage sont serveur. Aucune adaptation applicative nécessaire à ce stade pour ce contrat maintenu. Les API administratives /api/booking-settings/read et /publish sont web-session uniquement et ne doivent pas être appelées par Mobile.

Nouveau lecteur optionnel get_booking_service_options : contract_version2, service nullable pour l’historique non classé, durée effective de source acquired_policy ; non raccordé dans cette prise en compte. Ne pas accepter sa version2 via le parseur v1 ni déduire individual_session d’un mode autonomous/coached_automatic. Collectif/découverte/bilan sont explicitement non réservables. Pas de repli local 60/30 minutes ni d’horaire chiffré.

Installation du catalogue/des Pages non effectuée ; plan préparatoire distinct d’un plan résolu et de son autorisation. Aucun changement de code, dépendance, service ou base par Mobile. 442 tests Backend réussis/3 ignorés proviennent du rapport consulté, non réexécutés ici. Aucun test applicatif supplémentaire justifié par cette seule documentation. La suite à transmettre est `MOVEE_MOBILE_BOOKING_SETTINGS_NEXT_STEP.md`.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:322`.

### Lecteur get_upcoming_bookings raccordé — 26 octobre 2026

Contrat livré `../../movee-app/docs/MOBILE_UPCOMING_BOOKINGS_CONTRACT.md` et code `../../movee-app/services/mobile_booking_planning_service.py` consultés en lecture seule. [src/lib/mobile-upcoming.ts](../movee-mobile/src/lib/mobile-upcoming.ts) appelle la route fixe POST `/api/business-actions/ia2b/get_upcoming_bookings` avec command_id null, arguments fermés, Bearer/credentials omit et signal partagés. Schémas validés : version, fenêtre exacte, sujets/bookings, dates affichables, statuts numériques/codes concordants, phase à reference_at, fuseau IANA, version nullable, lien Pages/rowId cohérent. Aucun appel à l’allocateur ou aux options de création.

`src/components/upcoming-bookings.tsx` : fenêtre UTC 30 jours, sujet autorisé, page 20 éléments, marque mémoire reference_at/valid_until/kind/total/position/compte cumulatif ; ordre strict sans doublon ni page incomplète silencieuse. Aucun décodage ni stockage persistant de curseur. Date limite monotone conservatrice à partir de server_time et de l’instant précédant la requête, renouvellement explicite depuis la première page. Chaque page remplace la précédente ; erreurs/401/403/429 et changement session/focus suivent usePageRead/readScope. Au retour après mutation, l’invalidation Pages du provider est également appliquée à ce lecteur. 409 de curseur nécessite une reprise explicite ; une donnée passée n’est pas présentée en même temps que l’erreur courante. Réduction de fenêtre proposée uniquement sur business_result_limit/result_limit.

Accès dans accueil/layout/booking mode upcoming. Ce mode rend le lecteur hors de la garde du journal d’écriture ; une panne SecureStore ou une intention non résolue ne masque pas les réservations. Liens de fiche réutilisent Consultations avec UID de liste et rowId servis, puis configuration/droits relus par les API Pages existantes. Les liens sont omis lorsque pages=null. Ni annulation implicite ni état de confirmation acquis depuis cette lecture.

39 tests Mobile réussis : `test:upcoming` 6, `test:planning` 6, `test:booking` 14, `test:pages` 8, `test:auth` 5 ; TypeScript/diff et compilation web HTTP 200. Tests DTO/transport, refus/quota/cancel, curseur/inventaire cohérents, ordre/count et référence fixe, rendu réel de cartes, statuts, zone, liens/null, sélection coach, vide/erreur/expiration, disponibilité du lecteur avec journal indisponible ou intention incertaine. Réponses synthétiques uniquement. Résultat Backend 427 tests/3 ignorés rapporté dans son document, non réexécuté ici. Aucun Backend, permission, donnée, dépendance ou service changé ; pas de nouvelle recette navigateur authentifiée/natif annoncée.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:333`.

### Calendrier du centre et lecture journalière — 26 octobre 2026

Lot planning autorisé ; première partie raccordée à `search_availability` / `search_coached_availability` existants. [src/lib/mobile-planning.ts](../movee-mobile/src/lib/mobile-planning.ts) gère dates civiles, mois, bornes journalières dans le fuseau IANA du choix, horaires avec décalage et regroupement de présentation. Aucune dépendance ajoutée. `BookingCalendar` utilise des Pressable/Text natifs, dates sélectionnées/désactivées et libellés complets accessibles ; `CreateForm` dans `booking.tsx` remplace offset/windowHours par un jour sélectionné et le chargement journalier. Les paramètres restent copiés des créneaux pour l’aperçu existant.

Le Service Backend `IA2BBookingService.search_availability` a été consulté en lecture seule : l’horizon borne le début d’un créneau, pas sa fin. Le lecteur conserve donc la fin réelle d’un créneau commençant à la limite. Il prolonge la recherche de la durée nécessaire, filtre les débuts au jour demandé et à l’horizon, et recoupe les sous-intervalles pour ne pas perdre un créneau traversant une frontière. Déduplication sur les timestamps/coach exacts, ordre chronologique. En cas de troncature, subdivision séquentielle, maximum 31 appels par journée et arrêt à une minute de subdivision ; limite explicite au lieu de résultat partiel. Premier 429/échec arrête la lecture et remonte au hook partagé ; le signal annule les recherches suivantes. Changement jour/session/focus invalide les réponses par usePageRead/readScope existants.

Complément « réservations à venir » bloqué sur contrat Backend, documenté dans `MOVEE_MOBILE_UPCOMING_BOOKINGS_REQUEST.md`. Sources vérifiées : catalogue/configuration/lecteur Pages v1 et contrat actions livré, sans mapping métier stable pour ce bloc. Aucun endpoint proposé n’est présenté comme livré ; aucun Backend, SQL, permission ou service changé. Ne pas reconstruire l’agenda depuis les seules disponibilités/choix de création.

Tests : nouveau `npm run test:planning` (6), réservation (13), Pages (8), auth (5), TypeScript, diff. Cas : année bissextile/mois, heure d’été/hiver et décalage de 45 min, jour civil sauté, double heure distinguée, journée dense 96 créneaux sans doublon/perte à minuit, horizon de début, quota/annulation/limite sans publication partielle, rendu calendrier avec sélection et dates désactivées. Test data uniquement dans tests. Compilation web HTTP 200 de `/booking` via Expo géré, pas de recette navigateur authentifiée ou native attestée. Aucun redémarrage ni dépendance.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:344`.

### Palette et présentation de marque — 26 octobre 2026

Lot visuel autorisé. Tokens dans [src/constants/theme.ts](../movee-mobile/src/constants/theme.ts) : couleurs de marque, surfaces, textes, séparateurs, contours de contrôles, danger, variantes clair/sombre conservées. `PageButton` propose primary/secondary/quiet/danger et un rendu inverse pour le menu ; aucun changement de handler ou de contrat réseau. `ReadStatus` accepte le rendu inverse pour garder ses messages lisibles sur menu sombre. Logo local original copié de `../../movee-biz/movee_biz/public_static/media/movee-logo.png`, affiché via [src/components/movee-brand.tsx](../movee-mobile/src/components/movee-brand.tsx) et expo-image déjà installé, avec libellé accessible. Aucune nouvelle dépendance ni police distante.

Fichiers de présentation adaptés : [src/app/index.tsx](../movee-mobile/src/app/index.tsx), `_layout.tsx`, `consultations.tsx`, `booking.tsx`, [src/components/mobile-home.tsx](../movee-mobile/src/components/mobile-home.tsx), `mobile-page-content.tsx`, palette et composant de marque. Thème React Navigation raccordé à la palette ; barre système native claire sur en-tête sombre. Copie d’accueil actualisée pour refléter les actions réservation déjà livrées. Le mock useTheme du rendu réservation isolé a été complété ; assertions métier conservées.

Tests : 13 réservation + 8 Pages + 5 auth réussis, TypeScript, diff sans erreurs. Mesure de contraste des paires principales : texte secondaire sur surface >= 6.19:1, texte de bouton principal 16.89:1, contours de contrôles sur surface >= 3.80:1. Contrôles navigateur limités à la connexion en largeur mobile et au focus clavier e-mail/mot de passe ; aucune nouvelle recette authentifiée, sombre dans navigateur, VoiceOver/TalkBack ou appareil physique annoncée. Styles surveillés par Expo existant ; aucun redémarrage de service, configuration publique, appel d’écriture métier, modification Backend ou base pour ce lot.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:353`.

### Raccordement des actions réservation — 25 octobre 2026

Lot Mobile autorisé ; contrat livré consulté en lecture seule dans `../../movee-app/docs/MOBILE_BOOKING_ACTIONS_DELIVERED_CONTRACT.md`. Le transport partagé reste Bearer, POST JSON, `credentials: omit`. [src/lib/mobile-booking.ts](../movee-mobile/src/lib/mobile-booking.ts) valide les choix/cursors, créneaux, actions/version, aperçu/arguments renvoyés, conséquences, accords et reçus numériques. Routes fixes du contrat ; soumissions exclusivement `booking-submit`, avec `expected_preview_hash`. Le hash d’accord reste distinct. Aucun droit ni état d’annulation déduit du statut Pages.

[src/hooks/use-mobile-booking.tsx](../movee-mobile/src/hooks/use-mobile-booking.tsx) conserve l’état au-dessus du navigateur : verrou immédiat, persistance avant dispatch, récupération d’intention, renvoi volontaire exact, décisions incertaines et réponses isolées par objet de session. Aucune mutation automatique à la reconnexion. `use-mobile-pages.tsx` partage le quota et une révision d’invalidation relançant les lectures actives, et celles des listes/fiches lors de leur retour au premier plan. Une réponse effective reste distincte d’un échec de nettoyage ou de relecture. Les nouvelles routes UI sont dans [src/app/booking.tsx](../movee-mobile/src/app/booking.tsx), accessibles depuis layout/consultations.

Stockage : natif [src/lib/booking-journal.ts](../movee-mobile/src/lib/booking-journal.ts) utilise SecureStore `WHEN_UNLOCKED_THIS_DEVICE_ONLY` ; plafond conservateur 2000 octets, refus avant envoi si dépassé. Une seule intention non résolue par compte, pas de queue. Web : `booking-journal.web.ts`, IndexedDB, AES-GCM, IV aléatoire et liaison authentifiée à l’owner ; clé CryptoKey locale non exportable. Cela ne protège pas d’un code compromis sur la même origine. Changement/nettoyage conditionnel à l’empreinte d’intention dans une transaction web ; un autre onglet ne peut remplacer une intention différente. Le journal contient arguments, clé, jeton d’aperçu et éventuellement décision/hash d’accord et origine, jamais token de session ni mot de passe. Aucun cache persistant de catalogue ou de données Pages ajouté.

Dépendance Expo compatible `expo-crypto` pour UUID v4 natif/web, sans tirage Math.random dans le client ; Expo géré redémarré via `../movee-dev restart expo`. Aucun service Backend/Redis/MariaDB modifié ou redémarré. Les protections et limites du journal doivent être recettées sur les plateformes réelles avant distribution.

Validation : `npm run test:booking` (13), `test:auth` (5), `test:pages` (8), `npx tsc --noEmit`, `git diff --check`. Tests de hooks avec adaptateur React contrôlé, rendus TSX isolés, SecureStore mémoire, WebCrypto réel et IndexedDB mémoire ; ils ne prouvent pas des interactions navigateur ou natives. GET web `/booking` : compilation HTTP 200 via Expo géré ; aperçu utilisateur sur connexion, aucune nouvelle recette authentifiée. Aucune écriture métier HTTP réelle ni SQL et aucun changement du jeu de 66 ajouts. Recette détaillée : `MOVEE_MOBILE_BOOKING_RECIPE.md`.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:402`.

### Client Pages v1 — 23 octobre 2026

Présentation des listes simplifiée après accord utilisateur : tri et filtres regroupés derrière un bouton discret « Filtrer / Trier », panneau replié par défaut et refermé après application ; indication lorsque des options sont actives. Aucune modification des contrats ni des permissions. Vérifications de cette adaptation : TypeScript, 8 tests Pages et contrôle du diff réussis ; pas de nouvelle recette native.

Lot autorisé et implémenté exclusivement dans Mobile. Sources Backend consultées en lecture seule : `docs/MOBILE_PAGES_CONTRACT.md`, `docs/MOBILE_PAGES_ACCEPTANCE.md`, `api/mobile_pages_api.py`, `services/mobile_page_service.py`, ainsi que les DTO de lecture de ProgramService/PerformanceService. Le contrat de lecture remplace l’ancien constat d’absence de couverture classique pour ces trois consultations seulement ; aucun déploiement ou résultat de recette métier réel n’est déduit de cette lecture.

### Fichiers de ce lot

- Ajouts : [src/lib/mobile-pages.ts](../movee-mobile/src/lib/mobile-pages.ts) (DTO/validation/formatage), [src/hooks/use-mobile-pages.tsx](../movee-mobile/src/hooks/use-mobile-pages.tsx) (catalogue et lectures), [src/app/consultations.tsx](../movee-mobile/src/app/consultations.tsx) (listes/fiches), [src/components/mobile-page-content.tsx](../movee-mobile/src/components/mobile-page-content.tsx) (rendu natif partagé), [tests/mobile-pages.test.mjs](../movee-mobile/tests/mobile-pages.test.mjs) (fixtures de test uniquement).
- Adaptations : [src/lib/mobile-api.ts](../movee-mobile/src/lib/mobile-api.ts) (transport JSON partagé, statut HTTP, annulation et Retry-After), [src/hooks/use-mobile-session.ts](../movee-mobile/src/hooks/use-mobile-session.ts) (expiration sur 401 liée au jeton attendu), [src/app/_layout.tsx](../movee-mobile/src/app/_layout.tsx) (provider Pages, route protégée et rubriques serveur), [src/components/mobile-home.tsx](../movee-mobile/src/components/mobile-home.tsx) (accès volontaire et texte actualisé), `package.json` (commande `test:pages`), `tsconfig.json` (imports TS explicites pour exécution Node des tests, avec noEmit hérité d’Expo).
- Documentation : les deux références Mobile et [codex/MOVEE_MOBILE_BACKEND_CONTRACT_REQUEST.md](../movee-mobile/codex/MOVEE_MOBILE_BACKEND_CONTRACT_REQUEST.md). Les changements locaux préexistants, notamment Explore, la connexion et les tests auth, sont conservés.

### Transport et cycle de vie

Les seules nouvelles routes sont GET `/api/mobile-pages` et POST `/api/mobile-pages/config`, `/data`, `/record`. Bearer, `credentials: omit`, JSON, timeout de 15 s, validation `success=true`, `version=1`, configuration, pagination, identifiants et structure des contenus spécialisés. Aucune exécution d’HTML, JS, action ou endpoint de métadonnées. Décimaux spécialisés validés comme chaînes et rendus sans conversion numérique. Liens métier : suffixe `_label` uniquement. Médias ouverts sur action explicite avec protocole HTTP(S) et sans identifiants dans l’URL ; pas de lecteur vidéo intégré ni de transfert automatique du Bearer.

Le catalogue appartient au provider dans la session courante. Les ressources d’écran utilisent `useIsFocused`, AbortController et un garde de publication : aucune réponse tardive n’est publiée après invalidation, même si le transport ignore l’annulation. Changement de session/revalidation, absence de focus, changement de paramètres ou nouvel essai masquent immédiatement l’ancien résultat. Pas de cache métier persistant. Le `Retry-After` en secondes ou date HTTP bloque les nouvelles lectures pendant le délai connu, y compris à travers la navigation ; aucun polling réseau/retry automatique. Sur 401 : expiration/purge native via la session existante, sans révoquer un éventuel nouveau jeton. Sur 403 : contenu retiré, refus explicite.

Le rendu utilise les `field_uid` et les types/configurations fournis. Tri seulement sortable, pagination par total/limit/offset serveur, un filtre typé à la fois parmi ceux publiés, pas de filtre date/between. Les fiches sont obtenues via le lien de détail revalidé dans la configuration de liste. `content_type` sélectionne le rendu programme ou historique ; l’empreinte de prescription n’est jamais modifiée et les résultats tronqués n’ont pas de pagination inventée. Les identifiants techniques d’exercice servent au regroupement des séries, sans lookup web complémentaire.

### Vérifications réellement effectuées

- `npm run test:auth` : 5 tests réussis.
- `npm run test:pages` : 8 tests réussis (quatre routes, authentification sans cookies, schémas/version, erreurs et délais, annulation/réponses tardives, valeurs absentes, rendu TSX des listes/fiches et contenus spécialisés).
- `npx tsc --noEmit` et `git diff --check` : réussis.
- Aperçu web compilé et essai interactif avec API synthétique isolée : menu serveur, liste, pagination, programme/prescriptions/protections, résultats/unités/troncature, filtre vide, refus, 429 partagé, retour connexion sur 401 et déconnexion. Le rendu statique TSX des tests remplace les contrôles hôtes natifs par des éléments inertes : ce n’est pas une preuve d’accessibilité native.
- L’API de test était liée à 127.0.0.1:5067 et l’aperçu à localhost:8082 ; les deux ont été arrêtés. Une surcharge publique temporaire `.env.development.local` a été retirée ; `.env.local` est préservé. Expo SDK 58 recharge les fichiers `.env` dans son module virtuel de développement, d’où cette surcharge locale de test plutôt qu’une simple variable du processus.

Pas de Backend/base/configuration privée modifié, pas de fixtures injectées dans MariaDB, pas de credentials réels utilisés, pas de build cloud/publication. La recette réelle du plan Backend, les comptes adhérent/coach, les contrôles de droits réels et les terminaux natifs restent à réaliser. La tentative de démarrage Expo signale aussi `simctl` indisponible sur ce Mac ; aucune recette simulateur n’est annoncée.

### Suivi CORS — correctif Backend confirmé dans le code, recette réelle en attente

Retour transmis par l’utilisateur le 23 octobre et vérifié en lecture seule : `movee-app/app.py`, `apply_cors_headers`, autorise désormais `Content-Type, X-Api-Key, Authorization` et expose `Retry-After`. La restriction des origines de production est conservée ; aucun cookie d’identité requis. La section CORS de `docs/MOBILE_PAGES_CONTRACT.md` confirme que les routes et payloads Pages/auth sont inchangés. Aucun changement de code Mobile requis.

Le retour Backend annonce 381 tests réussis et 3 Redis ignorés sur 384, avec couverture isolée des sept préflights et des succès/refus/quotas. Ces tests n’ont pas été relancés dans Mobile et ne sont pas une recette navigateur réelle. Le test synthétique Mobile précédent reste distinct.

Contrôle local à cette reprise : aucun service n’écoute sur 5050, 6380 ou 8081. Aucun service Backend relancé ici ; la recette devra utiliser Flask chargé avec le code corrigé, Redis et MariaDB disponibles. Les comptes/données adhérent/coach restent à préparer selon `docs/MOBILE_PAGES_ACCEPTANCE.md` ; leur absence est un constat du dernier contrôle Backend, pas une nouvelle lecture de base effectuée ici. La recette navigateur Bearer/Retry-After puis la recette métier et native restent non exécutées. Seuls les deux référentiels Mobile et le suivi de demande de contrats sont actualisés ; code client et modifications locales préexistantes préservés.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:441`.

### Lot local accueil et navigation — 21 octobre 2026

Lot de code autorisé : session partagée au niveau du layout, menu latéral avec accueil/compte/déconnexion, route compte protégée et ancienne route Explore redirigée vers l’accueil. L’accueil connecté indique les fonctions encore indisponibles, sans conversation ni résultat métier simulé. Le compte affiche l’identité connue et la déconnexion, sans prétendre fournir tous les paramètres essentiels cibles.

Les seuls appels restent login/me/logout. Aucun centre, profil ou droit n’est inventé. Le délai dépassé est distingué d’une erreur réseau. Le menu et les vues connectées suivent le thème système ; aucune recette VoiceOver/TalkBack, installation native ou persistance SecureStore sur appareil n’est attestée par ce lot. L’écran de connexion conserve son thème clair actuel.

Accueil conversationnel, fil unique, zone prioritaire, menu métier contextuel et secours automatique attendent les contrats Backend. Voir `MOVEE_MOBILE_BACKEND_CONTRACT_REQUEST.md` : demande préparée, non envoyée. Aucune évolution des décisions T/AR ni modification Backend.

Vérifications de ce lot : 5 tests client API réussis (dont timeout distinct), TypeScript sans erreur et `git diff --check` valide. Aperçu navigateur ouvert : connexion affichée et accès direct à `/account` sans session redirigé vers `/`. Menu connecté, changements d’écran authentifiés, déconnexion et accessibilité native restent à recetter ; aucun identifiant utilisateur utilisé pendant cette vérification.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:452`.

### Reprise sur le nouveau Mac — état vérifié le 21 octobre 2026

**Outils Apple : correction vérifiée le 21 octobre.** Command Line Tools sélectionnés ; Git et Homebrew fonctionnent normalement. Le blocage de licence signalé lors de l’installation de Xcode est résolu pour le développement courant. Xcode reste facultatif pour le parcours EAS cloud.

### Couche propriétaire et emplacement

- Dépôt : `/Users/mbenmouha/Documents/Movee/movee-mobile` ; conversation propriétaire : **Movee App Mobile**.
- Responsabilités : interface iOS/Android pour adhérents et coachs, navigation, accessibilité, états UI, client HTTP, session et permissions OS. Le serveur décide droits, crédits, réservations, modifications de programmes et actions IA. Aucun accès direct Mobile à MariaDB, Redis ou OpenAI.
- Node **24.22.0**, npm **11.19.1**, Expo SDK **58** (`expo ~58.0.16`), React **19.3.0**, React Native **0.88.0**, EAS CLI **25.3.0**. `node_modules` a été réinstallé avec le lockfile ; correctifs de compatibilité au sein du SDK 58 appliqués.
- Aperçu navigateur du projet mobile : **`http://localhost:8081`**. Ce port est Metro/Expo, pas le backend ni une preuve d’installation native.

### Client livré et connexion locale

- [src/app/index.tsx](../movee-mobile/src/app/index.tsx) : connexion e-mail/mot de passe, identité retournée par le serveur et déconnexion. [src/app/_layout.tsx](../movee-mobile/src/app/_layout.tsx) n’affiche plus les onglets Expo de démonstration à l’accueil ; les autres composants de démonstration ne constituent pas une fonctionnalité MOVEE livrée.
- [src/lib/mobile-api.ts](../movee-mobile/src/lib/mobile-api.ts) : trois routes réelles `/api/mobile-auth/login`, `/me`, `/logout`, validation des réponses, requêtes Bearer sans cookie web, erreurs et timeout de 15 secondes. HTTPS exigé hors mode de développement.
- [src/hooks/use-mobile-session.ts](../movee-mobile/src/hooks/use-mobile-session.ts) : jeton conservé avec **Expo SecureStore** sur iOS/Android, vérification `/me` à la reprise, expiration absolue et révocation. Aucun refresh token inventé. **Web : jeton en mémoire uniquement**, pas de persistance dans localStorage.
- `.env.local` ignoré par Git : **`EXPO_PUBLIC_API_URL=http://127.0.0.1:5050`**, uniquement pour l’aperçu sur ce Mac. `.env.example` contient un exemple sans secret. Ne jamais mettre une clé OpenAI, un mot de passe DB ou le HMAC serveur dans `EXPO_PUBLIC_*`.
- **Sur un téléphone, 127.0.0.1/localhost désigne le téléphone** : avant une build appareil, fournir une URL de backend de développement accessible et protégée, avec HTTPS pour toute distribution hors développement. Les deux serveurs actuels sont limités à la boucle locale ; aucune exposition LAN ou tunnel n’est créée automatiquement.
- L’utilisateur a confirmé la connexion depuis l’aperçu navigateur à son compte local. **5 tests client API réussis**, TypeScript sans erreur, `git diff --check` valide ; bundles JavaScript iOS/Android et export web compilés. Ces bundles ne sont pas des builds natives EAS ni une recette SecureStore sur téléphone.
- L’incompatibilité de type `ref` du composant de démonstration `app-tabs.web.tsx` a été corrigée. Les résultats anciens signalant cette erreur sont historiques.

### Expo, EAS et distribution

- Compte Expo connecté ; projet actif **`@movees-team/movee`**, ID **`afb7ec71-8942-40e8-b286-43dacb62482d`**, [tableau de bord](https://expo.dev/accounts/movees-team/projects/movee). `app.json` contient le propriétaire, le slug et `extra.eas.projectId` correspondants.
- **Ne pas refaire `eas init` ni créer un autre projet.** Le projet supplémentaire `@movees-team/movee-mobile`, créé par erreur pendant l’association, est inutilisé ; aucune suppression n’a été effectuée.
- `expo-dev-client` installé ; `eas.json` contient le profil **`development`**, `developmentClient=true`, `distribution=internal`. Aucun profil de production ni identifiant iOS/Android final n’est encore configuré. Ne pas inventer d’identifiant permanent avant vérification/validation.
- Parcours retenu : **Expo/React Native + EAS Build dans le cloud**, installation de versions de développement sur appareils, puis publication stores. **Xcode n’est pas requis pour ce parcours**, sauf choix ultérieur de simulateur/compilation locale.
- Abonnement **Apple Developer commandé par l’utilisateur, activation en attente** ; vérifier l’état réel avant build iPhone. Compte Google Play non vérifié. Aucun build cloud, certificat, provisioning appareil ou publication n’a encore été attesté.
- Push : exigence produit maintenue ; `expo-notifications` absent, fournisseur/credentials et raccordement serveur non réalisés. Expo Go ne valide pas les push du produit ; prévoir une development build. Les notifications serveur appartiennent au Backend, leur réception et interaction appartiennent à Mobile.
- L’audit npm a signalé **27 vulnérabilités (8 modérées, 19 élevées)** pendant l’installation ; pas de correction forcée ni d’attribution à une dépendance précise dans cette session. À examiner avant distribution ; ne pas annoncer une sécurité auditée.

### Reprise

`npm run test:auth`, `npx tsc --noEmit` et les commandes de lancement sont détaillés dans [l’environnement du Mac](../docs/ENVIRONNEMENT_DEVELOPPEMENT_MAC.md). Les développements futurs restent à cadrer selon les contrats vérifiés : connexion livrée ≠ accueil conversationnel, inscription, récupération, réservations, programmes IA ou push livrés. Une API manquante donne lieu à une demande au Backend, pas à une modification silencieuse de son dépôt.

### Règle de séparation des conversations

Cette conversation travaille exclusivement dans le dépôt indiqué ci-dessous. Les deux référentiels de ce même dépôt et [codex/AGENTS.md](AGENTS.md) font autorité dans leur périmètre. Les autres dépôts peuvent être consultés en lecture seule pour vérifier un contrat ; une évolution nécessaire dans une autre couche doit être décrite comme demande d’intégration à transmettre à sa conversation, sans y modifier du code, de configuration ou de SQL. Ne pas copier une règle, un schéma ou un Service d’une application à l’autre. Le compte administrateur de test ne valide pas les parcours adhérent/coach.

Les anciens chemins `/Users/mehdi.benmouha/Documents/Projects/newapp/...` désignent l’ancien Mac ; les chemins de travail actuels sont sous `/Users/mbenmouha/Documents/Movee`. Les sections historiques et résultats antérieurs restent datés ; l’état local ci-dessous ne prouve aucun déploiement sur le VPS.

---


**Consolidation du 17 octobre 2026 :** socle historique conservé, arbitrages validés AR01–AR07 et AR05.1–AR05.10 intégrés aux sections métier et techniques concernées. Ils précisent ou remplacent uniquement les formulations explicitement visées. Les autres décisions Q/B et les 78 décisions mobiles demeurent applicables. Les décisions sont des spécifications cibles, sans preuve supplémentaire d’API, d’implémentation, de recette réelle ou de déploiement. Les formats, paramètres, canaux externes et langues initiales non décidés restent à spécifier.

**Version : 17 octobre 2026 — mise à jour après validation des thèmes 1 à 8 (T1.1–T1.8, T2.1–T2.10, T3.1–T3.10, T4.1–T4.10, T5.1–T5.10, T6.1–T6.10, T7.1–T7.10, T8.1–T8.10).** Les contraintes des thèmes 1 à 8 sont validées ; les autres propositions techniques conservent leur statut à valider.  
**Périmètre :** clients mobiles MOVEE iOS et Android. Ce document n'atteste pas l'existence d'un dépôt mobile, d'une route, d'une classe ou d'un SDK installé.

**Traçabilité des précisions :** AR01 remplace l’approbation coach systématique des adaptations supervisées par les validations selon limites préautorisées et consentement adhérent ; AR02 précise B8.2 pour l’écriture des programmes ; AR03 distingue centre contractuel et contexte actif ; AR04 résout l’exception Élevé aux heures calmes applicatives ; AR05 fixe les dix périmètres ; AR06 distingue historique durable, contexte éphémère et mémoire ; AR07 fixe acquisition externe, centralisation App et restitution Mobile. Les autres limites, permissions, validations sensibles, protections sportives et exigences de reprise restent conservées.

---

> **Historique daté, pas état courant.** Provenance : `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md:1386`.

### 15. Suivi de réalisation et écarts

Pour chaque capacité, conserver : **spécifié → décidé → implémenté → testé isolément → testé en intégration → déployé**. Les statuts sont propres à chaque projet ; une API backend testée ne signifie pas qu'un écran mobile existe.

Écarts prioritaires à traiter dans des lots distincts :

1. Contrats JSON/versionnement API réellement disponibles.
2. Routes classiques Bearer pour réservations, programme et historique lorsque l'IA est coupée.
3. Contrat et fournisseur push sur appareils réels.
4. Parcours coach et permissions API effectivement publiés.
5. Choix de l'outillage mobile, design system, cache et offline.

Les contraintes de navigation T1.1–T1.8 sont validées, sans attestation d'implémentation. La bibliothèque éventuelle du menu, la gestion d'état concrète et les contrats listés en section 4.1 restent à vérifier ou à valider ; ces éléments ne rouvrent pas les décisions d'expérience utilisateur du thème 1.

Les décisions T2.1–T2.10 sont validées, sans attestation de réalisation. Les contrats de compte, de contexte et de cycle de session listés en section 4.2 restent ouverts avec MOVEE App ; la biométrie et le stockage sécurisé nécessitent une validation technique des solutions mobiles avant ajout de dépendances.

Les décisions T3.1–T3.10 sont validées ; les besoins induits et contrats non vérifiés sont distingués en section 4.3. La cible de suivi machine ne démontre pas un raccordement existant, et les contrats d’exécution des circuits T3.7 précisés par AR01 restent à vérifier côté App avant développement. La politique de validation est arbitrée ; les autres divergences éventuelles restent à traiter chez le propriétaire sans contournement mobile.

Les décisions T4.1–T4.10 sont validées ; les dix contrats ouverts sont recensés en section 4.4. La présentation de programmes reste entièrement conversationnelle (option A), les validations groupées conservent chaque accord individuel, et les relances peuvent être automatiques sans accord coach systématique (option B), dans la classification serveur des actions. La consultation classique (écriture de programmes exclusivement IA selon AR02), les garanties de validation groupée et les mécanismes de détection/relance restent à vérifier sans remettre en cause ces choix ni les validations conditionnelles d’AR01 sur les adaptations supervisées.

Les décisions T5.1–T5.10 sont validées ; mémoire, orchestration, suivi/reprise, personnalisation et voix restent soumis aux contrats ouverts de la section 4.5. Le mode vocal temps réel est acquis comme cible fonctionnelle ; aucun fournisseur ni transport n'est sélectionné. Le fil unique, le contexte authentifié indépendant de la mémoire, les parcours sans IA et les validations des programmes coachés sont conservés.

Les décisions T6.1–T6.10 sont validées ; les seize contrats ouverts et leur niveau de preuve documentaire sont distingués en section 4.6. La chaîne de notification §9.1 est une cible logique. Les mécanismes push décrits par App restent à vérifier dans le code courant ; fournisseur, paramètres et garanties ne sont pas sélectionnés ou démontrés par cette mission. Les préférences explicites et la confidentialité priment sur la personnalisation IA, App reste source de vérité, et les parcours sans IA et validations métier antérieures sont conservés.

Les décisions T7.1–T7.10 sont validées ; les dix-huit contrats ouverts figurent en section 4.7. Les principes offline/sécurité/continuité sont acquis, leurs données exactes et mécanismes restent à étudier. La contrainte d'absence d'usage pendant l'entraînement conserve les capacités machine et de saisie App sans créer un suivi mobile ; aucune technologie de cache, synchronisation, OTA ou monitoring n'est choisie.

T8.1–T8.10 clôturent l'intégration documentaire des huit thèmes : 78 décisions validées. Mobile conserve interface/navigation/accessibilité, présentation/réglages locaux, interactions et permissions OS, état UI et collecte locale seulement autorisée. App conserve authentification, centre/rôle/droits, données/règles/résultats métier, préférences de compte prises en charge et backend de support/collecte si validé. Le chemin Mobile → API HTTPS authentifiée → App → Services métier → Repositories → MariaDB est conservé, sans accès direct SQL/Redis/OpenAI/MCP/machines. Les dix-huit besoins §4.8 restent ouverts ; cette clôture n'autorise aucune implémentation ni collecte ou nouveau chantier.

Les arbitrages AR01–AR07/AR05.1–AR05.10 sont intégrés dans les sections de responsabilités et contrats. Ils ne prouvent aucune capacité backend, stockage durable IA, livraison push ou intégration Motion opérationnelle. Les écarts restants de l’audit, dont la traduction technique détaillée des décisions Q/T, restent à traiter sans rouvrir les choix fonctionnels validés.
