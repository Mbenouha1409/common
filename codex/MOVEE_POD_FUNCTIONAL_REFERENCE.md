# MOVEE Pod — référence fonctionnelle spécifique

Version de consolidation : 2 novembre 2026. **Référence centralisée validée ; anciennes copies retirées après accord utilisateur.** Lire d’abord [README.md](README.md), [règles communes](AGENTS.md), [fonctionnel global](MOVEE_FUNCTIONAL_REFERENCE.md) et [technique globale](MOVEE_TECHNICAL_REFERENCE.md). Les sections issues des anciennes références conservent leur date/statut ; un constat historique ne décrit pas l’installation actuelle.

## Périmètre propre

Le répertoire movee-pod/codex est présent mais vide dans l’inventaire documentaire. Les décisions XP01–XP12 sont extraites de l’ancien référentiel App, sans créer un logiciel, une API, un schéma ou une validation matérielle. La vision et la répartition globale se lisent dans MOVEE_FUNCTIONAL_REFERENCE.md.

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:3 -->

## Périmètre commun MOVEE Pod — consolidation du 30 octobre 2026

**Source :** décisions de la présente conversation de conception des pods et lecture des références App/Mobile ainsi que des échanges récents « MOVEE App », « MOVEE Mobile » et « Movee Admin ». Le nom des conversations peut évoluer. Cette section intègre le périmètre Pod aux références destinées à la centralisation globale. Elle ne fusionne pas les 78 décisions Mobile ni les contrats Admin ; les sections historiques restent datées. Aucun développement, raccordement physique ou déploiement Pod n'est attesté.

**Centralisation du2novembre2026 :** les décisions XP sont désormais dans ce fichier du dossier commun. L’ancienne destination App et la mention d’un dossier central à choisir sont remplacées par la décision utilisateur actuelle. Aucun périmètre logiciel n’est modifié.


### XP01 — Noms et propriété

**Nom corrigé par l'utilisateur le 30 octobre 2026 : MOVEE Pod** désigne le projet de développement et l'application installée sur le mini-PC de chaque pod. Le terme « pod matériel » désigne l'ensemble physique ; « ordinateur du pod » désigne le mini-PC. Les identifiants XP01–XP12 sont conservés pour la stabilité des références, sans désigner le nom du projet. Une conversation dédiée au développement utilise ce cadrage logiciel ; le suivi du matériel reste dans la conversation de conception des pods. Le dossier `movee-pod/` existe localement mais ne constitue pas une preuve d'application développée.

MOVEE App possède les utilisateurs, droits, consentements, programmes et limites autorisées, validations métier et résultats centraux. Pod est l'exécutant local et l'interface pendant l'entraînement. Mobile consulte les données centralisées hors entraînement : aucune connexion aux appareils ni suivi physique en direct introduit dans Mobile (T7.8/AR07). Admin reste une interface du backend App, sans nouvelle habilitation implicite. Biz conserve son périmètre propre.

### XP02 — Une application MOVEE Pod autonome par pod

**Décision retenue :** un ordinateur local par pod, exécution et analyse MOTION locales. L'option serveur vidéo/MOTION mutualisé a été étudiée puis écartée pour éviter une panne commune à tous les pods. L'option d'un seul pod Coaching équipé de caméras n'est pas la cible retenue après retour au calcul local par pod.

**Orientation acceptée comme cible à valider :** Linux, service Python, interface web locale plein écran et stockage SQLite avec fichiers médias locaux. Dimensionnement économique, graphique intégré et analyse optimisée ; pas de GPU dédié imposé. Les bibliothèques, versions, frameworks web et mécanismes d'installation restent à arrêter avant développement. Le budget matériel et les performances évoqués sont des objectifs d'essai, pas des garanties.

### XP03 — Équipements vus par le logiciel

Le périmètre de connexion est une machine de force Renhe, un tapis Renhe, les LED pilotées par WLED, le bracelet cardio Bluetooth et la commande Bluetooth, plus deux caméras RGB-D. ANT+ a été écarté pour le cardio. Chaque appareil et bracelet est explicitement associé au pod et, pour la séance, à l'utilisateur ; aucune sélection du premier appareil découvert à proximité.

Renhe fournit force et tapis. **Information fournisseur rapportée par l'utilisateur : protocole commun.** Prévoir une base de communication commune et deux profils fonctionnels, sans supposer que leurs commandes sont identiques. Le document reçu décrit la force ; les commandes tapis, notamment vitesse/inclinaison, restent à confirmer dans la documentation attendue. La compatibilité WLED contrôleur/ruban a été vérifiée par l'utilisateur ; aucune recette logicielle Pod n'est revendiquée. Le service cardio standard, les données exposées et la reconnexion du bracelet restent à vérifier physiquement.

### XP04 — Interface pendant l'entraînement

**Exigences explicites :** écran miroir tactile 43 pouces en portrait, image par HDMI et tactile par USB. Afficher le BPM issu du bracelet, l'exercice en cours, la charge en force ou la vitesse et l'inclinaison sur tapis, une vidéo de démonstration et un retour vidéo direct de l'utilisateur issu des caméras. La vidéo de référence est validée par un coach ; pas d'avatar personnel animé pour la démonstration.

**Conception proposée :** distinguer consignes et mesures effectivement confirmées, rendre visibles les valeurs périmées et les pertes de liaison, proposer les commandes autorisées et les étapes/temps de séance. Affichage d'une vue principale avec bascule sur la seconde caméra à valider ; ni mosaïque ni fusion de vues ne sont décidées. Le retour vidéo local doit rester distinct de l'analyse MOTION et ne pas dépendre de sa capacité à produire une correction.

### XP05 — Exécution et ajustements individuels

Pod charge le programme et les réglages de l'utilisateur depuis l'autorité App. Charge/mode de force et vitesse/inclinaison du tapis sont des consignes individuelles, bornées par les limites autorisées et les capacités réelles des appareils. La commande Bluetooth permet de demander l'arrêt ou l'augmentation prévue selon l'exercice ; affectation exacte des boutons, pas et conditions de réglage restent à définir. Les commandes tactiles respectent les mêmes limites.

AR01/AR02 et Q030–Q031 restent applicables : exécuter une séance préautorisée n'autorise pas à créer/modifier localement un programme ni à lever une restriction. Le BPM est une mesure à afficher ; son emploi pour adapter automatiquement charge, vitesse ou inclinaison n'est pas une fonction déjà validée par ce cadrage.

### XP06 — MOTION local et séparation de BODY

Deux caméras RGB-D par pod sont demandées ; modèles, placement, calibration et synchronisation restent à tester. L'exercice, la machine et sa configuration sont connus avant analyse. MOTION compare les observations à des références coach et aux paramètres individuels validés ; il ne reconnaît pas librement un exercice et n'impose pas une trajectoire universelle.

Le document fourni « MOVEE_BODY_MOTION_ARCHITECTURE_V1.md » distingue BODY (morphologie, avatar statique, station de bilan) et MOTION (exécution sur machines). Pod intègre le second périmètre ; il ne devient pas une station BODY. MediaPipe est le premier moteur de pose proposé pour les essais, avec alternatives si nécessaire. Exploitation de la profondeur et de deux vues à concevoir explicitement : aucune fusion ou précision 3D acquise par simple présence des caméras. Si la confiance est insuffisante, ne pas produire de correction affirmative.

**Optimisations proposées :** images redimensionnées pour l'analyse, choix de vue selon exercice, seconde vue lorsque nécessaire, profondeur limitée aux observations utiles, séparation acquisition/affichage/analyse/commandes. Elles ne doivent pas dégrader les critères validés par les coachs. Les fréquences et latences proposées en conversation sont des hypothèses de POC.

### XP07 — Données et échanges avec App

**Autorité conservée :** App centralise programmes versionnés, limites, consentements et historique durable. Aucun accès Pod direct à MariaDB, Redis ou aux Repositories centraux ; toute intégration passe par les API et Services autorisés. Ne pas assimiler les contrats Mobile v9 existants à un contrat Pod livré ; aucun nouvel endpoint, type de frontend, jeton ou schéma n'est décidé ici.

**Conception proposée :** dossier de séance local versionné et autorisé comprenant identité technique séance/utilisateur/pod, séquence, réglages et limites, médias référencés et conditions de validité. SQLite conserve configuration, état et événements en attente ; les médias sont des fichiers mis en cache. Ne télécharger que les informations nécessaires, pas tout le dossier adhérent.

Conserver les événements jusqu'à confirmation de leur réception durable, identifier leur origine et leur ordre, dédupliquer les renvois et traiter les conflits avant de conclure au succès. Durée de conservation, chiffrement, purge, révocation hors ligne et responsabilité exacte des accusés de réception restent à contractualiser. Le retour vidéo direct n'implique pas l'enregistrement ; tout stockage vidéo distinct reste soumis aux règles Q048–Q052 et aux consentements.

### XP08 — Cours collectifs : même séquence, réglages personnels

**Exigence retenue :** les X pods participants d'un studio suivent une même séquence, avec charges adaptées à l'utilisateur courant et consignes individuelles tapis. Les séances individuelles restent prises en charge par le même exécutant local. Cette exigence de déroulement ne rend pas le cours collectif réservable par le seul paramétrage de sa durée ; les contrats Booking restent distincts.

**Architecture proposée, à détailler techniquement :** MOVEE Studio coordonne les cours sur le réseau local, tandis que chaque Pod conserve le calcul, la vidéo et le pilotage. Le coordinateur est distinct du serveur vidéo mutualisé écarté. Son ordinateur d'hébergement n'est pas encore figé.

### XP09 — Protocole de synchronisation proposé

1. Précharger séquence versionnée, médias et paramètres individuels ; vérifier équipements et identité. Chaque Pod annonce son état de préparation ; fixer explicitement les participants avant départ.
2. Synchroniser les horloges sur une référence locale et mesurer l'incertitude et le délai réseau. Annoncer un départ futur commun avec identifiant/version du cours et accusés de réception ; ne pas démarrer selon l'ordre d'arrivée des messages.
3. Chaque service Python déroule les étapes à partir d'une horloge monotone locale ; écran, vidéos et LED suivent cette chronologie. Le mouvement d'un appareil reste conditionné à ses validations, pas au seul départ collectif.
4. Remonter étape, temps écoulé, états appareils, décalage et incidents. Distinguer synchronisation logicielle et réponse mécanique/Bluetooth. L'objectif de 100 ms évoqué reste une proposition de mesure, pas un seuil approuvé.
5. Messages identifiés, ordonnés et acquittés : pause, reprise à un nouvel instant commun et arrêt. Rejeter les commandes périmées/dupliquées ; aucune relance d'un pod arrêté par changement d'étape. Aucun rattrapage par accélération physique ou saut d'une transition nécessaire.
6. Un arrêt individuel affecte son pod ; la reprise exige les vérifications et validations prévues. Au retour réseau, échanger l'état courant sans rejouer automatiquement l'historique des commandes.

Ethernet, HTTPS App–Studio et WebSocket sécurisé Studio–Pod ont été proposés ; messages exacts, authentification des équipements, versionnage, délais et politique de pause restent à spécifier. Pas d'élection automatique de coordinateur proposée pour le premier lot. La synchronisation des étapes n'est pas une promesse de synchronisation audiovisuelle à l'image près ou de musique multi-écrans.

### XP10 — Pannes, sécurité et autonomie

**Principe retenu :** éviter qu'une panne de calcul vidéo commune rende tous les pods dépendants d'un serveur. Une séance déjà préparée peut être exécutée localement uniquement dans les conditions autorisées ; la politique précise de poursuite/arrêt en perte de Studio ou d'Internet reste à valider. Ne pas transformer une proposition d'autonomie en autorisation générale hors ligne.

Conception de reprise : perte appareil signalée, absence de mesure distincte d'une valeur valide, arrêt local prioritaire, redémarrage sans réactivation automatique. Une pause collective ne peut être garantie sur un pod déconnecté. L'arrêt d'urgence matériel et les boucles moteur restent indépendants du Pod, de MOTION, de l'affichage, du réseau et du LLM. Le comportement sur perte Bluetooth et les effets exacts d'une commande d'arrêt doivent être confirmés avec Renhe.

### XP11 — État et validation avant développement

**État attesté par cette consolidation : cadrage documentaire seulement.** Aucun code Pod, test de caméra, performance, installation Linux, service local, contrat App–Pod ou recette multi-pods n'a été réalisé ici. Les résultats de tests App/Mobile/Admin rapportés dans leurs conversations ne prouvent pas le fonctionnement Pod.

Avant implémentation : inventorier les contrats réellement disponibles côté App ; préciser les gaps sans inventer SQL/API/permissions ; définir dossier de séance, événements, synchronisation, identité et sécurité locale. Tester un pod complet avec les appareils réels et deux caméras, puis plusieurs pods pour les interférences et la synchronisation. Critères de qualité MOTION, charge soutenue, latence, déconnexions, redémarrage et rejouabilité à approuver et mesurer.

### XP12 — Points ouverts à transmettre à la conversation de développement

- Dossier central définitif à préciser ; architecture technique MOVEE Pod intégrée à `MOVEE_APP_TECHNICAL_REFERENCE.md`, section « Architecture logicielle MOVEE Pod ». Aucune copie canonique permanente à créer dans chaque projet.
- Protocoles Renhe tapis, accès cardio et boutons ; correspondance des états/erreurs et capacités réelles.
- Modèles/SDK des caméras, calibration, usages de la profondeur et observation des exercices masqués.
- Contrats App, droits par dispositif/séance, expiration et validation des consignes ; aucun type `front_type` Pod attribué.
- Hébergement du coordinateur, formats/transports exacts, politique de pause et participation dégradée ; cible de synchronisation à mesurer.
- Conservation des événements/médias, chiffrement, gestion des secrets et isolation entre utilisateurs.
- Modes d'installation, mises à jour compatibles, diagnostic et reprise sans action physique implicite.
- Choix final des bibliothèques, présentation des deux vues et critères de recette, sans nouvelle fonctionnalité BODY implicite.

---
