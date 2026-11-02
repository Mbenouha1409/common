# MOVEE — environnement local du Mac

Procédure commune Backend/Mobile actualisée le **25 octobre 2026** (Europe/Paris).
Les références du [dossier commun codex](../codex/README.md) restent les sources des exigences métier. Ce guide
n’autorise aucune migration, import, création de compte, activation IA/push/worker
ou opération sur le VPS.

## Utilisation quotidienne

Dans Terminal :

```sh
cd /Users/mbenmouha/Documents/Movee
./movee-dev start --with-expo
./movee-dev status
```

- Backend/admin/API : http://127.0.0.1:5050
- Aperçu Mobile : http://localhost:8081

L’aperçu web n’est pas une application native installée. Sur un téléphone,
`localhost` désigne le téléphone. Le mode par défaut reste local ; un mode iPhone
sur Wi-Fi a été ajouté et activé sur demande le30octobre2026 :

```sh
./movee-dev iphone
./movee-dev status
# Retour aux écoutes locales :
./movee-dev loopback
```

Ces deux commandes redémarrent seulement Backend+Expo, en préservant Redis et
MariaDB. Le choix persiste au redémarrage via le fichier privé network.json du
profil. Le mode iPhone utilise ExpoGoSDK58, annonce l’IP privée du Wi-Fi en0 et
injecte cette même adresse pour l’API. Après changement d’IP, relancer iphone.
Procédure, QR courant et limites : [Test iPhone](iphone-test/README.md).
Ne pas lancer de seconde instance Expo manuellement.

| Commande | Effet |
| --- | --- |
| `./movee-dev start` | Redis + Backend ; réutilise MariaDB ou relance son service Homebrew existant s’il est arrêté |
| `./movee-dev start --with-expo` | Redis + Backend + aperçu Expo web |
| `./movee-dev start expo` | Expo seulement ; ne démarre pas le Backend |
| `./movee-dev start backend` | Redis si nécessaire, puis Backend |
| `./movee-dev status` | Ports, disponibilité, services gérés ou externes |
| `./movee-dev stop` | Arrête les trois services gérés ; laisse MariaDB et les autres processus intacts |
| `./movee-dev stop expo` | Arrête uniquement l’aperçu Expo géré |
| `./movee-dev restart backend` | Recharge le code et la configuration Backend, sans arrêter Redis ou Expo |
| `./movee-dev restart --with-expo` | Redémarre les trois services ; les sessions Redis sont perdues |
| `./movee-dev logs backend` | 60 dernières lignes Backend et chemin du journal |
| `./movee-dev logs redis` | Journal Redis |
| `./movee-dev logs expo` | Journal Expo |

Un second démarrage ne crée pas de doublon. Une commande concurrente de contrôle
est refusée. Si un port appartient à un service externe, la commande refuse le
démarrage avant de toucher les services sélectionnés : arrêter l’ancien lancement
depuis son terminal/chat d’origine. Le dispositif ne tue aucun PID externe et
n’adopte pas silencieusement un ancien Flask/Expo.

Le statut « prêt » du Backend vérifie Redis, le port MariaDB et `/login` ; ce
contrôle technique ne remplace ni un login Mobile ni une recette métier.
Les démarrages attendent la disponibilité, avec délai borné ; un échec peut
laisser un job supervisé en attente. Consulter `status`/`logs`, corriger la cause,
puis relancer `start`, ou utiliser `stop` pour le retirer.

## Services et redémarrage du Mac

La supervision utilise **launchd**, fourni avec macOS, en tant qu’utilisateur.
Depuis le30octobre2026, Backend et Expo sont classés `Interactive` pour éviter
la limitation CPU/IO des tâches de fond lors des gestes utilisateur ; Redis reste
`Background`. La politique et les mesures sont documentées dans
[le rapport iPhone](iphone-test/README.md). Aucun worker supplémentaire ajouté.
Aucun sudo ni Docker. Les fichiers gérés sont :

```text
~/Library/LaunchAgents/fr.movee.dev.local.redis.plist
~/Library/LaunchAgents/fr.movee.dev.local.backend.plist
~/Library/LaunchAgents/fr.movee.dev.local.expo.plist
```

`start` installe/charge les seuls services demandés. `RunAtLoad` et `KeepAlive`
les relancent à l’ouverture de session et après une interruption, avec une
temporisation de dix secondes. Fermer Terminal ou Codex ne les arrête pas.
Ce n’est pas un démarrage avant connexion de l’utilisateur.

`stop` décharge les jobs et retire leurs fichiers de démarrage : les services
ainsi arrêtés ne repartiront pas au prochain login. `start` les réactive.
MariaDB conserve son service Homebrew séparé, déjà activé au login.
La perte/reprise de Redis invalide les sessions et quotas éphémères ; se reconnecter
au Mobile, sans toucher aux données MariaDB.

macOS peut demander à **Python** ou **Node** l’accès au dossier Documents pour
ce lancement indépendant de Codex. L’utilisateur doit l’autoriser. L’accès Python
a été accordé et le lancement launchd a effectivement fonctionné le 25 octobre.
En cas de refus, vérifier Réglages Système → Confidentialité et sécurité →
Fichiers et dossiers ; ne pas déplacer/recréer les sources ou modifier TCC pour
contourner le refus. Une mise à jour des interpréteurs peut imposer une nouvelle
autorisation ou un redémarrage des jobs.

Après modification de Python Backend ou de son `.env` :

```sh
./movee-dev restart backend
```

Gunicorn n’utilise ni préchargement ni reloader automatique ; un redémarrage
réimporte le code courant. Expo fonctionne sans `CI=1`, avec surveillance des
sources ; les changements Mobile suivent le rafraîchissement habituel d’Expo.
Après modification de sa configuration publique/dépendances, redémarrer Expo :

```sh
./movee-dev restart expo
```

## Architecture locale

| Service | Adresse | Gestion |
| --- | --- | --- |
| MariaDB 11.4.13 | Port 3306 | Service Homebrew existant `mariadb@11.4`, jamais arrêté par `movee-dev` |
| Redis 8.10.2 | `127.0.0.1:6380` | launchd, sans RDB/AOF, données éphémères |
| Flask sous Gunicorn 26.2.0 | `127.0.0.1:5050` | launchd ; 1 worker WSGI synchrone, sans debug/reloader |
| Expo / Node 24.22.0 | `localhost:8081` | launchd ; aperçu web, boucle locale |
| Biz | Port 5051 observé | Hors du dispositif ; ses processus/configurations restent sous sa couche |

Gunicorn est installé uniquement dans `movee-app/venv` ; version fixée dans
`dev/requirements-local.txt`. La configuration est `dev/gunicorn.local.py`.
Nginx n’est pas installé : pour ces tests sur boucle locale, Gunicorn suffit.
Ce choix ne reproduit pas un reverse proxy/TLS ni la configuration réelle du VPS,
qui n’a pas été inspectée. Un futur proxy ou déploiement fera l’objet d’un lot
séparé. Aucun serveur MCP/ASGI ni worker métier n’est démarré.

Le contrôle du 25 octobre a observé MariaDB sur `*:3306` et un service Biz sur
une adresse LAN. Ces écoutes sont préexistantes et n’ont pas été modifiées.
Redis reste en boucle locale. Gunicorn/Expo restent locaux sauf activation explicite du mode iPhone décrit ci-dessus. Ce mode conserve une écoute Backend locale et ajoute son IP Wi-Fi ; Expo utilise l’écoute LAN standard de Metro.

## Emplacements, configurations et données

Racine : `/Users/mbenmouha/Documents/Movee`, hors synchronisation Google Drive.

| Couche | Dossier | Instructions |
| --- | --- | --- |
| Backend | `movee-app` | [AGENTS commun](../codex/AGENTS.md), [fonctionnel App](../codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md), [technique App](../codex/MOVEE_APP_TECHNICAL_REFERENCE.md) |
| Mobile | `movee-mobile` | [AGENTS commun](../codex/AGENTS.md), [fonctionnel Mobile](../codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md), [technique Mobile](../codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md) |
| Biz | `movee-biz` | [AGENTS commun](../codex/AGENTS.md), [fonctionnel Biz](../codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md), [technique Biz](../codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md) |

Chaque conversation préserve les changements de sa couche ; consultation des
contrats des autres couches en lecture seule. Le [README central](../codex/README.md)
remplace les anciennes consignes de reprise et donne la vue globale et les références spécifiques.
Ne pas repartir du dossier historique vide `Documents/ChatGPT/Newapp`, de l’ancien
Mac ou de ses environnements copiés.

- Backend : `.env` **parent**, `/Users/mbenmouha/Documents/Movee/.env`, privé 0600,
  chargé par le code existant. Base `movee_app_local` sur `127.0.0.1:3306`, compte
  applicatif limité `movee_local`. Réseau/mobile activés, assistant désactivé.
- Le pilotage refuse une configuration Backend hors de cette cible locale.
  Il ne réécrit aucun secret, flag métier ni quota. Redis cible 6380/0.
- Mobile : `movee-mobile/.env.local`, ignoré par Git, URL publique
  `EXPO_PUBLIC_API_URL=http://127.0.0.1:5050`. Aucun secret serveur dans
  `EXPO_PUBLIC_*`. Le jeton web est en mémoire et les appels utilisent
  `credentials: omit` ; ne pas se reposer sur les cookies web d’administration.
- Biz a sa configuration et ses bases propres ; le guide du 21 octobre qui le
  décrivait sans code n’est plus l’état courant. Ce lot ne qualifie pas Biz et ne
  modifie ni son code, ni ses bases, ni ses services.
- Connexion SQL locale privée : `~/.config/movee/mariadb-local.cnf`.
  Compte global DBeaver créé séparément : `movee_admin`, identifiants dans
  `~/.config/movee/mariadb-admin-local.txt`, 0600. Ne pas utiliser ce compte
  administrateur comme identité applicative.
- Comptes de recette Mobile existants : cinq profils décrits dans
  `movee-app/docs/MOBILE_PAGES_ACCEPTANCE_RESULT.md`. Leurs identifiants restent
  dans `~/.config/movee/mobile-pages-acceptance-credentials.json`, privé 0600.
  Ne pas les recréer, réinitialiser ou copier dans les logs.

La baseline Backend V1 a été importée le 21 octobre : 73 tables et 1773 lignes de
référence initiales, puis administrateur provisionné. Les Pages/droits et le jeu
synthétique ont été ajoutés avec autorisation le 23 octobre. **Ne pas réimporter
le seed, reprovisionner, migrer ou nettoyer la base pour démarrer.**
`data_ready=false` reste une limite de qualification métier, pas une demande de
réinstallation SQL.

## Journaux

```text
~/Library/Logs/MOVEE/local/backend.log
~/Library/Logs/MOVEE/local/redis.log
~/Library/Logs/MOVEE/local/expo.log
```

Fichiers privés 0600 ; répertoires de profil 0700. Rotation à 2 Mo, trois archives
par service. Le superviseur masque les valeurs sensibles connues de la
configuration, les jetons `mv1_…`, les lignes contenant des noms de secrets ou
en-têtes sensibles, les identifiants dans les URL et leurs paramètres.
Gunicorn n’enregistre pas de journal d’accès HTTP. Aucun dump de l’environnement,
des corps de login, de la réponse contenant un Bearer ou des cookies.

Ces protections portent sur le code actuel ; ne pas ajouter de `print` de données
privées dans les applications. Pour suivre un journal en continu :

```sh
tail -f "$HOME/Library/Logs/MOVEE/local/backend.log"
```

Les messages Expo sur `simctl` (outils Xcode non sélectionnés) ne bloquent pas
l’aperçu web. Les éventuels avertissements de versions Expo sont à traiter dans
la couche Mobile ; ce lot n’effectue aucune mise à jour npm.

## Installation et vérifications

Les dépendances applicatives existantes ne sont pas réinstallées. Pour reproduire
le seul ajout d’infrastructure, après installation des dépendances Backend :

```sh
./movee-app/venv/bin/python -m pip install -r dev/requirements-local.txt
./movee-app/venv/bin/python -m pip check
./movee-app/venv/bin/python -B dev/test_movee_dev.py
```

Vérification HTTP **explicite**, sur les comptes de recette existants :

```sh
./movee-app/venv/bin/python -B dev/check_local.py --http-acceptance
```

Elle effectue login/logout et lectures, donc actualise uniquement les champs
techniques de connexion des comptes de test et les sessions/quotas Redis. Elle ne
modifie pas les objets métier et ne force/efface aucun quota.
`--snapshot CHEMIN_PRIVE` puis `--compare CHEMIN_PRIVE` comparent les nombres et
empreintes des lignes des 73 tables. Seuls `last_login_at`, `updated_at` et
`updated_by` des cinq comptes synthétiques sont exclus de cette empreinte, car
le login les actualise réellement. Aucun contenu de ligne n’est exporté.

Pour les essais d’infrastructure isolés, `MOVEE_DEV_PROFILE=check` réserve les
ports Redis 16380, Backend 15050 et Expo 18081, des jobs/logs distincts, sans
installation au login. Il lit la même base MariaDB ; ce n’est **pas** une base de
test isolée pour des écritures métier. La configuration privée n’est pas modifiée.
Toujours retirer ces jobs après les essais :

```sh
MOVEE_DEV_PROFILE=check ./movee-dev stop
```

Les tests Redis métier destructifs ne doivent jamais cibler 6380 ; ils exigent
leur propre instance éphémère. Aucun de ces tests n’est lancé par `movee-dev`.
La suite applicative complète et les tests npm restent sous leurs couches.

## Expo/EAS et limites

Projet EAS existant : `@movees-team/movee`, ID
`afb7ec71-8942-40e8-b286-43dacb62482d`. Ne pas refaire `eas init`.
Expo/React Native + EAS Build cloud restent le choix ; Xcode n’est pas requis pour
ce parcours cloud. Command Line Tools sélectionnés sur ce Mac. L’activation Apple
Developer, la distribution, les appareils physiques et les push ne sont pas
validés par ce lot. Aucun fournisseur push ni IA n’est activé.

Voir `dev/VALIDATION_ENVIRONNEMENT_LOCAL.md` pour les résultats datés et les limites,
notamment la distinction HTTP et recette JavaScript navigateur. Un redémarrage
physique du Mac n’est pas simulé par un simple arrêt/redémarrage de services.

### Confirmation navigateur — 25 octobre 2026

L’utilisateur a confirmé la connexion et l’accès aux trois listes réservations,
programmes et séances dans Expo web. Les fiches, Retry-After via fetch, les
comportements sous quota et l’accessibilité restent à vérifier séparément.
