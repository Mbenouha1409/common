# Tester MOVEE sur iPhone avec Expo Go

Configuration préparée le30octobre2026, Europe/Paris. Pas de build MOVEE, signature Apple ou installation EAS effectuée.

## Sur l’iPhone

1. Mettre l’iPhone et le Mac sur le même Wi-Fi.
2. Installer/mettre à jour Expo Go compatible SDK58. La fiche App Store consultée annonce58.0.5 (22octobre), supportSDK58 ; les anciennes documentations annonçant seulementSDK54 sont dépassées sur ce point. https://apps.apple.com/app/expo-go/id982107779
3. Quitter l’ancien projet puis scanner avec l’appareil photo le QR expo-go-qr.png de ce dossier. Cible exacte : exp://192.168.1.36:8081. Accepter l’ouverture dans Expo Go et l’accès au réseau local si demandé.
4. Si Expo Go demande une connexion Expo, utiliser le même compte que le serveur Expo du Mac. Cette connexion Expo est distincte de la connexion adhérent/coach MOVEE.
5. Se connecter à MOVEE avec le compte de recette existant. Ne pas créer ou réinitialiser de compte pour ce test.

Vérification réseau sans login : ouvrir http://192.168.1.36:5050/login dans Safari doit afficher le formulaire Backend ; cela ne remplace pas l’ouverture native par le QR.

Si un refus de SDK apparaît, mettre à jour Expo Go puis recopier le message précis. Si Safari ne joint pas le Mac, vérifier mêmeWi-Fi, isolation des invités, disponibilité du Mac et autorisations réseau locales. Aucun pare-feu ou protection système n’a été désactivé.

## Pilotage Mac

Depuis /Users/mbenmouha/Documents/Movee :

- ./movee-dev iphone : relève l’IPv4 privée du Wi-Fi en0 et redémarre uniquement Backend+Expo en modeLAN/ExpoGo.
- ./movee-dev status : indique le mode actif et les adresses.
- ./movee-dev start --with-expo : conserve le mode choisi et réutilise les services gérés, sans doublon.
- ./movee-dev loopback : revient aux écoutes locales, en redémarrant uniquement Backend+Expo.

Redis/MariaDB ne sont pas arrêtés par iphone/loopback. Les sessions Redis sont conservées. Ne pas lancer de seconde instance Expo manuellement.

Le choix réseau est conservé dans ~/Library/Application Support/MOVEE/local/network.json (0600). Après changement d’adresse Wi-Fi, relancer iphone ; l’ancienne image QR de ce dossier devra être renouvelée si l’adresse change. Le profil check ignore ce choix et reste local.

Backend écoute127.0.0.1 et192.168.1.36 sur5050. Expo utilise --go --lan sur8081 (écoute standard Metro sur les interfaces du Mac) et annonce192.168.1.36. Aucun tunnel, règle de routeur, proxy ou exposition Internet n’a été ajouté. Redis reste127.0.0.1:6380. Les écoutes MariaDB préexistantes ne sont pas modifiées.

L’URL API effective d’Expo est synchronisée à la fois dans le superviseur et dans movee-mobile/.env.local : EXPO_PUBLIC_API_URL=http://192.168.1.36:5050. ExpoSDK58 transforme les accès en un module virtuel issu de ce fichier ; la seule injection process.env ne suffisait pas. loopback rétablit aussi cette valeur locale. La vérification porte sur la valeur du module natif réellement consommé, pas seulement sur la présence de l’adresse dans le bundle.

## Vérifications et limites

- 11tests de pilotage réussis : refus d’IP publique, mode explicite, retour loopback, préservation Redis et protections historiques contre processus/plist étrangers.
- Backend/login200 sur loopback et adresseLAN ; Expo/status200 surLAN ; capacitésMobile12 sans Bearer401.
- ManifesteIOS200 : SDK58.0.0, hostUri192.168.1.36:8081, lancementExpoGo et URL bundleLAN.
- BundleIOS200 ; correction du module virtuel .env.local validée : URLAPI LAN et absence de l’ancienne URL127.0.0.1:5050. Le premier contrôle de simple présence de la valeurLAN dans le bundle ne suffisait pas et est remplacé par ce contrôle du module consommé.
- Description publique de connexion200/success, CORS local et expositionRetry-After conservés.
- Lecture du preflight :83tables, public_native_blocks_v12_v1 conforme. Aucun SQL de mutation, login ou geste métier réalisé.
- Expo install --check signale14mises à jour correctives recommandées dans SDK58 ; elles n’ont pas été appliquées par cette configuration réseau. Aucune migration/rétrogradation SDK ni modification de package/app.json.
- Modules natifs utilisés, notamment Symbols/SecureStore/Image/Crypto et navigation Expo, disponibles dans ExpoGoSDK58. expo-dev-client est installé mais le lancement --go sélectionne explicitement ExpoGo. La présence des bibliothèques et la compilation ne valent pas recette sur appareil.
- Pas de connexion Apple ou Expo effectuée, pas de validation iPhone ni du Wi-Fi depuis un second appareil. Le ralentissement intermittent des programmes n’est pas déclaré résolu par ce raccordement.

Références : https://docs.expo.dev/versions/v58.0.0/sdk/symbols/ ; https://docs.expo.dev/versions/v58.0.0/sdk/securestore/ ; https://expo.dev/go .

## Réactivité locale — 30octobre2026

Backend et Expo utilisent maintenant ProcessType Interactive dans launchd, conformément à leur rôle de serveurs répondant aux gestes de l’utilisateur. La politique Background reste appliquée à Redis. Vérification effective : launchctl affiche spawn type interactive(4) pour les deux jobs. KeepAlive, worker synchrone unique, quotas et délais restent inchangés.

Comparaison isolée, mêmeprogrammeAlice/dixexercices, un échantillon par mode : taskpolicy-b6,959s contre lancementnormal1,7678s. Cela reproduit le coût de la classification de fond ; ce n’est pas une mesureHTTPauthentifiée du job ni une mesureiPhone. Le formulaire publicHTTP répond après activation en0,015–0,031s. Deux exécutions READONLY ont préservé83tables, preflight public_native_blocks_v12_v1 conforme. Détail : performance-local.json.

Backend et Expo seuls ont été relancés ; Redis1266 et MariaDB sont préservés. Aucun code métier, droit, cache entre requêtes, nombredeworkers ou délai client modifié. La réactivité ressentie et le timeout intermittent doivent encore être confirmés depuis le téléphone.
