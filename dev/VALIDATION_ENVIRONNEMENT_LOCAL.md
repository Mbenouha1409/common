# Vérification de l’environnement local — 25 octobre 2026

Périmètre : infrastructure locale de `/Users/mbenmouha/Documents/Movee`.
Aucun accès au VPS, aucun SQL de mutation explicite, migration, import, provisioning,
changement de secret, activation IA/push ou lancement de worker métier.

## Constats et installation

- MariaDB 11.4.13 et son service Homebrew existant réutilisés.
- Redis 8.10.2 et Node 24.22.0 réutilisés ; Python Backend 3.13.16.
- Gunicorn 26.2.0 installé dans le venv existant ; `pip check` conforme.
- Nginx et Docker non installés ; serveur WSGI limité à 127.0.0.1.
- L’utilisateur a arrêté les anciens Flask/Expo et autorisé Python à accéder à
  Documents. Les anciens processus n’ont pas été tués par le nouveau dispositif.
- Les processus Biz et MariaDB sont hors du périmètre d’arrêt.

## Vérifications

- Six tests ciblés du pilotage : filtrage des secrets, refus d’un plist étranger,
  absence d’arrêt d’un processus externe, second démarrage sans bootstrap,
  refus d’un port occupé et attente du déchargement launchd avant redémarrage.
- Profil temporaire `check` : lancement réel Redis/Gunicorn/Expo sur
  16380/15050/18081, puis retrait de tous ses jobs.
- Profil normal : lancement sur 6380/5050/8081 ; second lancement avec les mêmes
  trois PID superviseurs, aucun doublon.
- 57 appels HTTP réels par profil lors des premiers passages : préflight,
  login des cinq comptes existants, catalogue, configurations et listes des
  trois parcours, logout et refus du jeton révoqué, quota réel 429 avec
  `Retry-After`. Aucun cookie d’identité reçu. Le nombre peut varier lors d’un
  rejeu si le quota de l’identifiant synthétique est encore actif.
- Préflight sans authentification : Authorization et Content-Type autorisés,
  `Retry-After` exposé, origine de l’aperçu autorisée, aucune autorisation de cookies.
- Réponse Server Gunicorn vérifiée ; les nouvelles routes Pages du code courant
  sont servies. Aucun préchargement ni cache de build Backend ; restart réimporte
  `app:app` depuis le dépôt courant.
- Comparaison de données : 73 tables, nombres et empreintes identiques, sauf audit
  technique de connexion des cinq comptes de test (`last_login_at`, `updated_at`,
  `updated_by`). L’écart initial de users a conduit à vérifier la méthode existante
  `UserRepository.update_last_login_at`, qui actualise réellement ces trois champs.
- Les contenus préexistants des trois dépôts ont été comparés à une empreinte
  prise au début : aucun fichier applicatif antérieur modifié par ce lot.

## Limites

Les contrôles HTTP avec Origin ne sont pas une recette JavaScript navigateur.
L’utilisateur a confirmé le 25 octobre 2026 une connexion réussie et l’accès aux
trois listes réservations/programmes/séances depuis l’aperçu Expo web. Cette recette
manuelle est distincte des contrôles HTTP automatisés. Le détail des fiches, la
lecture effective de Retry-After par fetch, la navigation pendant quota et
l’accessibilité restent à vérifier dans le navigateur.
Aucun outil de contrôle navigateur n’est disponible dans cette session.

Pas de redémarrage physique du Mac ni de test après mise à jour Homebrew ;
RunAtLoad/KeepAlive et le chargement réel dans le domaine utilisateur launchd
sont contrôlés, sans les présenter comme une recette de reboot.

Pas de validation VPS/Nginx/TLS, multi-workers, appareils natifs, IA, push,
transactions de réservation ou qualification commerciale des données.
MariaDB écoute déjà sur toutes les interfaces et un service Biz sur le LAN :
configuration préexistante observée, non modifiée. Le dispositif ajouté reste local.

## Contrôles de fin de lot

- Redémarrage Backend explicite réussi ; l'essai a révélé une course au
  déchargement launchd, corrigée en attendant aussi la disparition du job avant
  de le recharger. Un test ciblé couvre cette attente.
- Interruption contrôlée du seul job Backend géré par `launchctl kill SIGTERM` :
  relance automatique avec un nouveau superviseur et une réponse HTTP disponible.
- Arrêt complet : 6380/5050/8081 libérés, MariaDB toujours disponible. Relance
  complète réussie ; processus Biz 37070/37080 et MariaDB 9982 préservés.
- `plutil -lint` : trois plists valides. Redis `save` vide, `appendonly=no`,
  bind 127.0.0.1. Les seuls deux PID Gunicorn partageant 5050 sont master/worker,
  pas deux instances indépendantes.
- Permissions 0600 des journaux et fichiers de configuration privés contrôlées ;
  aucune valeur privée connue de la configuration/recette trouvée dans les logs.
- Nouvelle comparaison de contenu des trois dépôts : aucun fichier préexistant
  modifié par le lot. Les fichiers d'infrastructure sont à la racine commune,
  hors des trois dépôts. Aucun commit ni push effectué.
- Recette navigateur manuelle confirmée par l’utilisateur le 25 octobre 2026 :
  connexion et accès aux trois listes fonctionnels. Cette confirmation ne couvre
  pas les fiches, Retry-After via fetch, le quota lors de la navigation ou l’accessibilité.
