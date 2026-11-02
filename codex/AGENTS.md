# MOVEE — instructions communes aux conversations et projets

Version du2novembre2026, consolidation et nettoyage validés par l’utilisateur. Ce fichier remplace les consignes communes copiées par projet. **Aucune suppression n’est autorisée par sa présence.** Les instructions humaines explicites de la conversation priment ; ne pas redemander un accord déjà donné pour le même périmètre.

## 1. Commencer une conversation

1. Lire [README.md](README.md), [MOVEE_FUNCTIONAL_REFERENCE.md](MOVEE_FUNCTIONAL_REFERENCE.md) et [MOVEE_TECHNICAL_REFERENCE.md](MOVEE_TECHNICAL_REFERENCE.md).
2. Identifier le dépôt et la couche concernés. Lire uniquement ensuite leur couple fonctionnel/technique dans ce dossier commun.
3. Pour une dépendance, lire les références du propriétaire et le contrat livré pertinent dans son dépôt. Une capacité documentée comme cible n’est pas une route disponible.
4. Vérifier le code actuel et ses classes parentes ; pour le schéma, les exports/migrations et l’état réellement appliqué. Préserver les modifications préexistantes.

| Projet | Références spécifiques centrales | Dépôt / couche |
| --- | --- | --- |
| App | [Fonctionnel](MOVEE_APP_FUNCTIONAL_REFERENCE.md), [technique](MOVEE_APP_TECHNICAL_REFERENCE.md) | movee-app ; métier/API/identité/données/IA centrale |
| Admin | [Fonctionnel](MOVEE_ADMIN_FUNCTIONAL_REFERENCE.md), [technique](MOVEE_ADMIN_TECHNICAL_REFERENCE.md) | front Web de movee-app, pas de dépôt distinct |
| Mobile | [Fonctionnel](MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md), [technique](MOVEE_MOBILE_TECHNICAL_REFERENCE.md) | movee-mobile ; iOS/Android, hors entraînement |
| Biz / Info | [Fonctionnel](MOVEE_BIZ_FUNCTIONAL_REFERENCE.md), [technique](MOVEE_BIZ_TECHNICAL_REFERENCE.md) | movee-biz ; deux hôtes, une application indépendante |
| Pod | [Fonctionnel](MOVEE_POD_FUNCTIONAL_REFERENCE.md), [technique](MOVEE_POD_TECHNICAL_REFERENCE.md) | movee-pod ; cible locale d’exécution, aucun logiciel attesté par le seul cadrage |
| MOTION | [Fonctionnel](MOVEE_MOTION_FUNCTIONAL_REFERENCE.md), [technique](MOVEE_MOTION_TECHNICAL_REFERENCE.md) | movee-motion ; analyse des exercices connus, distincte de BODY |

Le dossier commun est `/Users/mbenmouha/Documents/Movee/codex`. Il n’est pas l’ancêtre des dépôts : **son AGENTS.md n’est pas supposé être découvert automatiquement depuis movee-app ou un autre dépôt**. Une nouvelle conversation doit recevoir l’instruction de lire ce dossier (modèle dans README). Ne pas recréer des copies d’AGENTS dans les projets pour compenser ; un éventuel réglage d’amorçage est une action distincte à convenir avec l’utilisateur.

## 2. Autorité et anti-invention

- Décision validée : cible fonctionnelle ; architecture validée : direction technique ; code/migrations et environnement effectif : réalisation. Ces sources ont des rôles distincts, pas une priorité qui efface leurs divergences.
- Toujours distinguer décidé, proposé, codé, testé isolément, recetté en intégration, installé et déployé. Un test SQLite ne valide pas MariaDB, une API ne prouve pas son écran, une connexion ne qualifie pas le métier, une commande d’arrêt ne prouve pas une sécurité physique.
- Ne pas inventer fichier, chemin, table, colonne, classe, signature, route, permission, statut, mesure ou résultat. Vérifier les références avant de les transmettre. Un nom attendu non trouvé reste une inconnue.
- Ne pas recréer une décision de mémoire ni reconstituer des sources absentes. L’historique d’un chat n’est pas automatiquement chargé. Les identifiants de décision sont conservés, sans inventer une exhaustivité que la source n’a pas.
- Les états datés en annexe sont historiques. Consulter le point de reprise et les contrats actuels avant de réactiver un profil, rejouer un plan ou réimporter une base.
- En cas de conflit réel, conserver les formulations et la traçabilité ; ne demander que l’arbitrage indispensable. Ne pas rouvrir les décisions déjà closes.

## 3. Propriété, contrats et dépendances

Chaque couche modifie son périmètre autorisé. Les autres dépôts sont consultables pour comprendre les contrats ; une évolution croisée exige son périmètre explicite, sans mutation implicite de SQL/configuration/droits chez le propriétaire. Ne pas créer de conversation, contacter un autre chat, envoyer de message, archiver ou renommer un historique sans instruction humaine correspondante.

App/Admin/Mobile réutilisent le moteur metadata-driven et les Services existants. HTTP authentifie et transporte, Service contrôle droits/invariants/consentements/transactions, Repository persiste. MCP éventuel passe par les capacités/API autorisées, jamais SQL direct. Le client Mobile utilise les API natives, aucun MCP imposé sur ce chemin.

Biz conserve Flask/Blueprints → Services → db.py SQL paramétré → MariaDB et un moteur financier pur ; ne pas lui imposer le Designer ou le modèle App. Pod/MOTION restent soumis aux contrats App d’autorisation/résultat, sans accès direct à la base centrale ni création locale libre de programmes. Ne pas transposer un code de rôle, une durée, un tarif ou une règle de simulation entre applications.

## 4. Exécution et autorisations

Séparer analyse, rédaction, code, tests isolés, préparation de plan, application de données, activation de services et déploiement. Progresser dans le périmètre déjà autorisé ; présenter un résultat concret et vérifiable lorsque l’autorisation suivante est nécessaire.

Aucune migration, import, suppression, permission, activation IA/push/worker, opération VPS ou publication ne découle d’un référentiel. Pour une opération sensible, vérifier cible et autorisation effectives, sources, validité, état attendu et conséquences. Si une autorisation vise un plan précis, respecter son empreinte et son périmètre ; ne pas substituer un plan régénéré. Ne pas attribuer un accord humain à un SHA simplement calculé par un outil.

Préserver comptes, règles acquises, réservations, crédits, programmes et historiques. Ne pas utiliser des comptes/grants/politiques de recette pour rendre artificiellement un test positif. Ne pas promettre de rollback transactionnel des DDL MariaDB ; état partiel : diagnostic et reprise explicitement définie, aucune réparation automatique implicite.

Pour le développement local App, lire [le guide Mac](../docs/ENVIRONNEMENT_DEVELOPPEMENT_MAC.md). Utiliser movee-dev pour le Backend, jamais Flask manuel5050. Ne pas redémarrer MariaDB, Redis ou Expo pour un changement Python. Un fichier de configuration privé ou une adresse de tunnel ne vaut pas autorisation d’accès à une cible distante.

## 5. Conception et vérification

Réutiliser avant d’ajouter une classe, un écran ou une table. CRUD générique pour opérations simples ; actions/Services métier pour invariants sensibles. Avant une extension physique : lacune prouvée, impact, compatibilité et autorisation. Les UID identifient des instances de configuration, les IDs les objets métier ; connaître l’un ou l’autre n’autorise rien.

Liste, comptage, fiche, référentiels et mutations doivent requalifier les droits actuels. Un filtre masqué, Reset, un bouton caché ou un contexte signé n’est pas une permission permanente. Refuser les ID forgés, cibles interfrontend, droits révoqués et états divergents. Aucun cache de droits interrequêtes ajouté pour contourner une lenteur.

Consentement lié aux conséquences effectivement acceptées, intention/idempotence et versions conservées ; après timeout récupérer le résultat, pas de nouvelle soumission automatique. Ne jamais inventer solde, disponibilité, prescription, traduction ou mesure. Les exceptions sportives et financières propres aux projets se lisent dans leurs références, pas dans une règle globale supposée.

Effectuer les vérifications adaptées au changement et rapporter les commandes/résultats réels, limites et risques. Ne pas présenter simulations, mocks, benchmarks privés ou exports comme recette authentifiée ou matérielle. Préserver secrets, jetons et données privées dans tous les journaux et livrables.

## 6. Entretien documentaire

Mettre à jour la connaissance durable dans ce dossier : global si réellement partagé, spécifique chez son propriétaire. Une règle commune est liée, pas copiée dans chaque paire. Les contrats exécutables, SQL, fixtures et preuves restent à leurs emplacements réels dans les projets ; ne pas les déplacer pour une simple centralisation de connaissance.

Conserver les identifiants Q/B/T/D/S/F/AR/XP/POD-T, leurs restrictions et statuts. Q01–Q08 Biz ne sont pas Q001–Q008 réseau. Références canoniques App : ne pas recréer booking_operations ou un compteur sessions_remaining ; lire la répartition bookings/proposals/ledger et les décisions B/AR dans les deux fichiers App. Les règles détaillées n’ont pas à être copiées dans cet AGENTS commun.

Avant de supprimer un ancien document : vérifier sa couverture, ses liens et ses dépendances exécutables, préserver les plans/signatures, présenter la liste exacte et attendre l’accord utilisateur. Les15suppressions du présent lot ont été autorisées ; leur résultat figure dans [CONSOLIDATION_CLEANUP_RESULT.md](CONSOLIDATION_CLEANUP_RESULT.md). MOVEE_ADMIN_SCOPE.md reste conservé provisoirement pour sa dépendance Studios.
