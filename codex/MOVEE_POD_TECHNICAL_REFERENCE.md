# MOVEE Pod — référence technique spécifique

Version de consolidation : 2 novembre 2026. **Référence centralisée validée ; anciennes copies retirées après accord utilisateur.** Lire d’abord [README.md](README.md), [règles communes](AGENTS.md), [fonctionnel global](MOVEE_FUNCTIONAL_REFERENCE.md) et [technique globale](MOVEE_TECHNICAL_REFERENCE.md). Les sections issues des anciennes références conservent leur date/statut ; un constat historique ne décrit pas l’installation actuelle.

## Passage de relais

POD-T01–POD-T12 ci-dessous sont une cible documentaire extraite de l’ancien App. Linux/Python/SQLite/interface locale et calcul par pod ne sont pas un logiciel installé. Le coordinateur Studio reste proposé, sans dépôt distinct identifié ; ses détails restent dans ce périmètre Pod jusqu’à décision explicite. Toute intégration passe par Services App et contrats à qualifier. Les formules d’arrêt, de sûreté et de reprise ne sont pas des garanties de sécurité matérielle.

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:3 -->

## Architecture logicielle MOVEE Pod — cadrage du 30 octobre 2026

### POD-T01 — Statut, nom et sources

**Nom validé : MOVEE Pod, sans X**, pour le projet de développement et l'application installée sur chaque ordinateur de pod. « Pod matériel » désigne les équipements physiques. Répertoire local confirmé : `/Users/mbenmouha/Documents/Movee/movee-pod` ; aucun changement de dossier n'est nécessaire. Les références fonctionnelles XP01–XP12 restent stables malgré le changement de nom.

Cette section est le passage de relais technique pour la conversation de développement. Elle complète les décisions Q/B/AR et XP du référentiel fonctionnel commun sans les remplacer. **Cadrage, pas preuve de code, d'API, d'installation ou de performances.** Un ordinateur autonome par pod, le calcul MOTION local, Python et l'interface tactile sont retenus pour la cible. Les mécanismes ci-dessous sont une architecture proposée à implémenter après résolution des contrats ouverts ; les bibliothèques, formats de transport et politiques de panne non arbitrés restent explicitement à valider.

Sources de cadrage : conversation de conception des pods, références App/Mobile, échanges récents App/Mobile/Admin et document BODY/MOTION fourni par l'utilisateur. Les lectures des conversations ne constituent pas une recette MOVEE Pod. La sélection des appareils reste suivie dans la conversation matérielle. Le cadrage du30octobre précédait la centralisation ; celle du2novembre place désormais les références dans le dossier commun codex. Cela ne vaut pas développement ni recette matérielle.

### POD-T02 — Répartition des responsabilités

| Composant | Responsabilité | Hors responsabilité |
| --- | --- | --- |
| MOVEE App | Identité, droits, consentements, programmes/version, limites, autorisations et historique durable via API/Services | Boucle moteur, capture vidéo temps réel |
| MOVEE Pod, un par ordinateur | Exécution locale, connecteurs, écran, données temporaires, MOTION, événements | Création libre de programme, levée des restrictions, accès SQL central |
| MOVEE Studio, coordinateur proposé | Préparation/distribution, participants, chronologie collective, supervision | Serveur d'analyse vidéo mutualisé, sécurité matérielle |
| MOVEE Mobile | Consultation et interactions autorisées hors entraînement | Pilotage, cardio direct, compteur ou chrono d'entraînement (T7.8/AR07) |
| MOVEE Admin | Administration metadata-driven selon contrats/droits App | Accès physique ou nouveaux droits implicites |
| BODY / MOTION | BODY : bilan morphologique distinct ; MOTION : analyse spécialisée intégrée localement | Assimilation du pod à la station BODY |

```text
MOVEE App : API -> Services -> Repositories -> MariaDB
        | préparation autorisée / résultats / configuration
        v
MOVEE Studio (coordination locale proposée, sans traitement vidéo)
        | réseau Ethernet : séquence, départ futur, état et commandes
        +------------------+------------------+
        v                  v                  v
    MOVEE Pod 1        MOVEE Pod 2        MOVEE Pod N
    exécution locale   exécution locale   exécution locale
    MOTION local       MOTION local       MOTION local
        |
        +-- Renhe force et tapis / cardio / boutons : Bluetooth selon protocoles
        +-- LED : API WLED sur le réseau local
        +-- Caméras RGB-D x2 : acquisition locale via SDK constructeur
        +-- Écran portrait : HDMI image et USB tactile
```

L'option serveur vidéo/MOTION commun et l'option d'un seul pod Coaching ne sont pas la cible retenue. Le coordinateur Studio ne doit pas devenir une dépendance permanente de chaque image ou commande matérielle. Son hébergement reste à choisir ; sa panne ne doit pas entraîner la panne des processus locaux. Les autorisations de poursuite du cours en son absence restent à arrêter.

### POD-T03 — Logiciel local et exécution

**Cible : Linux + Python + SQLite + interface web locale plein écran.** Proposition de déploiement : services au démarrage avec supervision système, navigateur Chromium en mode kiosque, stockage sur SSD. Distribution/version Python et dépendances à choisir après vérification des SDK caméra et du Bluetooth ; ne pas recopier automatiquement les versions du backend de développement.

Séparer les responsabilités logicielles, sans multiplier les services réseau :

- Service Python principal : état de séance, autorisations chargées, connecteurs, journal et synchronisation. L'ordonnancement et les commandes ne dépendent pas du navigateur.
- Processus acquisition/analyse MOTION séparé : isoler les ralentissements ou plantages vidéo. Les images transitent dans des files bornées ou une mémoire partagée ; les données anciennes sont abandonnées pour éviter l'accumulation de latence.
- Interface HTML/CSS/JavaScript : consignes, vidéos, mesures et commandes tactiles. Échanges locaux avec le service Python, WebSocket proposé pour les états et requêtes locales pour les gestes. Aucune commande matérielle directe depuis le navigateur.
- Acquisition unique par caméra, distribuée à l'affichage et à l'analyse ; éviter des ouvertures concurrentes incompatibles du même appareil.

Un redémarrage du navigateur conserve l'état détenu par le service, sans démarrage implicite d'un appareil. Un redémarrage du service reconstruit l'état du journal et relit les appareils, puis reste non actif jusqu'à validation explicite. La boucle rapide moteur, les contrôleurs Renhe et les sécurités physiques restent indépendants du logiciel.

### POD-T04 — Connecteurs et commandes matériels

Connecteurs définis par capacités, états et mesures horodatées ; une absence de réponse ne signifie ni arrêt confirmé ni succès. Conserver demande, acquittement protocolaire et état observé distincts. La file par équipement respecte la cadence constructeur et priorise les demandes d'arrêt applicatif sur les réglages ordinaires. Pas de rejeu aveugle des commandes de démarrage après timeout.

| Connecteur | Fonction cible | Limite de connaissance |
| --- | --- | --- |
| Renhe commun + profil force | Charge, mode, démarrage/arrêt et données d'exercice | PDF force reçu, interprétation/CRC/échappement à confirmer sur matériel |
| Renhe commun + profil tapis | Vitesse, inclinaison, démarrage/arrêt et mesures disponibles | Protocole commun rapporté par l'utilisateur ; détail tapis attendu |
| WLED | Couleurs, luminosité, effets/préréglages via API JSON locale | Firmware et réponse réelle à qualifier |
| Cardio Bluetooth | BPM, fraîcheur, état de liaison | Service BLE standard supposé candidat, pas encore vérifié sur le bracelet |
| Boutons Bluetooth | Demande d'arrêt, augmentation selon exercice actif | Profil, identifiants, pas, anti-rebond et appuis longs à définir |
| Caméras RGB-D | Images couleur/profondeur et horodatage | Modèles, SDK et synchronisation à choisir |

Le protocole force reçu mentionne le service BLE FFF0, notifications FFF1, écriture FFF2, trames F5/FA, CRC et échappement. Ces détails décrivent la documentation, pas une intégration testée ; ne pas attribuer sans contrôle toutes les mêmes sous-commandes au tapis. Chaque équipement a sa connexion et son association au pod. Les connexions BLE passent par le service système Linux ; bibliothèque Python à sélectionner lors de l'implémentation.

Vérifier l'association bracelet-utilisateur-séance avant affichage ; ne pas exposer le BPM d'un autre adhérent. La mesure BPM n'autorise pas une adaptation automatique non validée. Les commandes tactiles et boutons passent par le même contrôle des limites locales autorisées et capacités réelles. La signification exacte de l'arrêt et le comportement sur perte Bluetooth restent des prérequis Renhe.

### POD-T05 — Interface écran et médias

Écran miroir tactile 43 pouces portrait, HDMI pour l'image et USB pour le toucher ; orientation de l'image et coordonnées tactiles cohérentes. Afficher exercice, BPM, charge confirmée pour la force ou vitesse/inclinaison confirmées pour le tapis, vidéo coach et retour vidéo utilisateur simultanés. Distinguer la consigne de la mesure observée et signaler l'obsolescence.

Vidéos coach stockées localement et préparées avant le cours ; retour caméra local sans détour par le serveur. Le chemin de transport vidéo vers le navigateur reste à choisir selon le SDK et la latence mesurée ; WebRTC local est une option, pas une dépendance décidée. Ne pas transporter les images brutes en JSON dans le canal des commandes. Vue principale et bascule éventuelle sur la deuxième caméra à valider ; aucune fusion/mosaïque imposée.

La vidéo locale et l'affichage des mesures restent utilisables si MOTION ne peut pas produire de résultat. L'échec d'un média ou du navigateur n'est jamais interprété comme confirmation d'arrêt matériel. Gestion des interactions portrait, lisibilité et alternatives physiques à recetter pendant l'effort.

### POD-T06 — Pipeline MOTION et optimisation

```text
Exercice + configuration machine + références coach + paramètres individuels
                         |
Caméras -> RGB / profondeur horodatés -> contrôle qualité/calibration
                         +-> retour vidéo local
                         +-> sélection des images/vues -> moteur de pose
                               -> filtrage/angles/phases/trajectoires
                               -> comparaison et tolérances validées
                               -> résultats horodatés + confiance -> interface/journal
```

MediaPipe est le premier moteur à tester ; OpenCV/NumPy et, si justifié, SciPy sont des pistes pour acquisition/traitement/analyse. Les SDK natifs peuvent être appelés depuis Python : Python orchestre, il n'impose pas de calcul pixel par pixel en Python. Aucun GPU NVIDIA dédié ni NPU n'est requis par décision préalable ; toute accélération nécessite une compatibilité réelle du moteur retenu.

Réduire la résolution d'analyse indépendamment de l'affichage, utiliser un modèle léger et sélectionner la vue pertinente. La seconde vue et la profondeur doivent être exploitées lorsque les critères d'observation l'exigent ; le nombre de vues analysées simultanément dépend des exercices. MediaPipe ne fusionne pas automatiquement les deux caméras ni leur profondeur. Calibration spatiale et alignement temporel à concevoir avant des mesures combinées.

Pas de reconstruction 3D complète permanente ni de reconnaissance générique de mouvement nécessaire pour cette cible. Les références et tolérances proviennent des coachs et de la calibration individuelle validée. Retour explicite « observation insuffisante » si occlusion/confiance insuffisante ; ne pas fabriquer une correction ou lever une restriction. L'analyse ne commande jamais directement le driver moteur.

Les objectifs précédemment évoqués (affichage/acquisition 30 images/s, analyse autour de 15 résultats/s, latence vidéo inférieure à 150 ms) sont des hypothèses de POC, pas des seuils de recette approuvés. Mesurer latence de bout en bout, qualité, pertes de flux et charge thermique avec tout le pod actif avant de figer le matériel économique.

### POD-T07 — Stockage, dossier de séance et résultat durable

| Niveau | Stockage proposé/existant | Données |
| --- | --- | --- |
| App | MariaDB existante ; stockage médias à contractualiser | Autorité métier, programmes, droits, résultats validés et références contrôlées |
| Studio | SQLite et fichiers proposés | Séquences préparées, affectations, état du cours, médias et événements en transit |
| Pod | SQLite et fichiers locaux proposés | Configuration appareils, dossier autorisé, état, événements non réconciliés, cache médias |

Aucune base SQLite n'est partagée sur le réseau. Aucun Pod n'accède directement aux données SQL centrales. Aucun schéma local ni extension MariaDB n'est déclaré créé. Auditer le modèle central avant proposition de table ou colonne ; ne pas déduire d'un besoin de synchronisation une nouvelle table métier.

Le dossier de séance proposé porte : version du contrat, identifiants séance/centre/pod/utilisateur, programme et séquence versionnés, liste des étapes et durées, consignes individuelles et bornes, possibilités d'ajustement, références/empreintes médias, restrictions/consentements nécessaires et durée/conditions d'autorisation. Contrat à publier par les Services App ; pas d'URL, signature ou jeton inventé comme existant. Un cache ne devient jamais une autorisation sans durée de validité et périmètre explicites.

Le journal local enregistre identifiants uniques, ordre logique, origine, heure/repère local, version de séance, demandes/résultats/erreurs et état d'envoi. Accusé local après écriture durable ; accusé Studio après stockage durable ; accusé App après acceptation métier durable. Distinguer « reçu au studio » et « intégré dans App ». Définir qui conserve les copies jusqu'à intégration centrale, avant toute purge.

Renvoyer les mêmes événements avec les mêmes identifiants ; déduplication côté récepteur et conservation des refus/conflits pour résolution. Ne pas promettre une livraison réseau exactement une fois. Une exécution physique non observée ne devient pas un résultat achevé par simple fin de chronologie. Politique de conservation/chiffrement et délais de purge à arrêter ; vidéo directe sans enregistrement par défaut de conception, stockage éventuel séparé sous consentement.

### POD-T08 — Transports, identité et supervision

Proposition : Ethernet entre ordinateurs de pods et Studio ; HTTPS authentifié App–Studio ; WebSocket sécurisé Studio–Pod pour coordination et événements. WLED reste sur le réseau local. L'accès direct Pod–App éventuel en séance individuelle n'est pas décidé : définir un seul chemin d'autorité et une réconciliation cohérente avant implémentation.

Chaque installation a une identité propre, limitée à son studio et aux séances autorisées. Provisionnement, certificats/jetons, rotation/révocation, gestion des secrets système et contrôle local de l'interface restent à contractualiser ; ne pas réutiliser les identifiants d'un adhérent comme identité permanente d'équipement. Protéger la liaison locale et refuser les commandes depuis une origine web arbitraire.

Les contrats Pages Web/Mobile existants, leurs profils v9 et les valeurs front_type 1/2 ne constituent pas un contrat Pod. Aucun nouveau type frontend ni exception au framework n'est attribué sans analyse. Réutiliser les contrats/métadonnées disponibles lorsque adaptés, et expliciter les capacités matérielles manquantes avant toute évolution App.

Supervision proposée : état de connexion, préparation, étape, décalage estimé, appareils disponibles, fraîcheur des mesures, erreurs et file en attente. Journaux techniques minimisés/corrélables, sans secret, image ou donnée de santé inutile ; accès opérateur soumis aux droits. Mises à jour compatibles avec les contrats, hors séance active, avec contrôle de santé et procédure de retour à la version précédente à concevoir.

### POD-T09 — Synchronisation des cours collectifs

**Principe : chronologie commune préchargée, réglages individuels et exécution locale.** L'horloge du cours définit l'étape commune, pas une valeur universelle de charge/vitesse/inclinaison. Une séance individuelle utilise le même exécutant avec sa propre chronologie.

1. **Préparer :** App autorise les dossiers ; Studio distribue séquence et médias. Chaque Pod vérifie versions/empreintes, identité utilisateur, limites, connexions et disponibilité. Confirmer les participants ; le coach ne doit pas voir « tous prêts » si un pod reste inconnu.
2. **Caler les horloges :** référence de temps du studio, synchronisation système et échanges aller-retour pour estimer délai/incertitude. Ne pas assimiler l'heure affichée égale à un alignement garanti. Refuser l'armement ou exclure explicitement les pods dont la préparation temporelle est insuffisante, selon seuil à valider.
3. **Armer :** annoncer identifiant de cours, génération de contrôle, version de séquence, position initiale et instant futur commun. Acquitter la réception et le stockage. Le coach voit le périmètre effectivement armé ; un participant qui manque l'ordre reste non actif. Une panne réseau empêche toute garantie de départ atomique de tous les pods : documenter ce cas, ne pas promettre une transaction physique distribuée.
4. **Exécuter :** convertir le départ commun en échéance de l'horloge monotone de chaque service Python ; calculer les étapes par temps écoulé plutôt que par accumulation de timers. Écran, vidéo et LED suivent cette position. Démarrage du cours et mise en mouvement d'un tapis restent deux opérations distinctes soumises aux vérifications locales.
5. **Observer :** échanger périodiquement état, étape, temps écoulé, incertitude, état machine et numéros de commandes appliquées. L'intervalle et les seuils restent à choisir. Objectif exploratoire d'écart inférieur à 100 ms entre chronologies ; aucune précision mécanique ni synchronisation audiovisuelle à l'image près garantie.
6. **Corriger :** ajuster progressivement les repères visuels si possible ; ne pas sauter une transition physique ni accélérer le tapis pour rattraper. Au-delà du seuil, signaler et appliquer la politique de suspension/reprise à définir. Une correction NTP de l'heure système ne fait pas sauter la chronologie monotone.

### POD-T10 — Messages, pause, arrêt et reconnexion

Enveloppe de message proposée, sans DTO/API livré : version du protocole, studio/cours/pod cible, identifiant de commande, génération de contrôle, numéro d'ordre, version de séquence, position/instant d'effet et durée de validité, type et paramètres. Contrôler identité, autorisation et ordre avant application ; réponses distinctes « reçu », « appliqué », « refusé » avec état réel ou inconnu.

- **Pause collective :** ordre identifié, position du cours et transition sûre par appareil. Une pause d'interface n'est pas une preuve de tapis arrêté. Acquittements individuels et supervision des absents ; pas de pause globale revendiquée tant qu'un participant reste inconnu.
- **Reprise collective :** nouvelle génération/position et nouveau départ futur, uniquement pour les pods vérifiés et explicitement participants. Un arrêt local reste verrouillé jusqu'à validation adaptée.
- **Arrêt local :** priorité dans le pod, exclusion de l'exécution active et remontée d'état. Ni étape suivante ni reconnexion ne réactive la machine.
- **Ordres obsolètes :** ne pas rejouer démarrages et réglages d'une ancienne génération. Un arrêt reçu dans une génération active doit rester prioritaire ; expiration et règles de sécurité exactes à spécifier sans le laisser bloqué derrière une commande ordinaire.
- **Reconnexion :** échange d'un instantané autorisé (génération, état, position, participants et dernières commandes), comparaison avec état local/appareils ; aucune réexécution de toutes les commandes manquées ni entrée en mouvement automatique.
- **Coordinateur :** un seul coordinateur explicitement reconnu. Pas d'élection automatique en première version ; un remplacement nécessite une reprise contrôlée sans deux autorités concurrentes.

L'exécution Renhe/Bluetooth n'est pas atomique entre pods. Des différences de délai physique doivent être observées et affichées, indépendamment de l'alignement des écrans. La synchronisation musique/son multi-pods n'est pas définie par cette architecture.

### POD-T11 — Défaillances et reprise

| Incident | Comportement de conception | Arbitrage restant |
| --- | --- | --- |
| Internet coupé | Conserver dossier et événements localement | Périmètre/durée autorisés hors ligne, révocation non instantanée |
| Studio ou réseau local indisponible | Exécutant et vidéo locaux restent opérationnels ; perte de coordination signalée | Poursuite ou arrêt du cours préchargé ; aucune commande collective garantie sur pod isolé |
| Caméra ou MOTION indisponible | Signaler absence d'analyse, ne pas fabriquer de correction ; pilotage indépendant | Exercices nécessitant observation pour rester autorisés |
| Cardio perdu | BPM indisponible/périmé, pas de valeur ancienne présentée comme actuelle | Conséquences selon séance et autorisation |
| Renhe perdu | État physique inconnu, nouvelles commandes ordinaires suspendues | Réaction constructeur et procédure opérateur à confirmer |
| Interface arrêtée | Service et état locaux indépendants, réouverture sans commande physique | Procédure si aucun contrôle utilisateur accessible |
| Ordinateur redémarré | Réconciliation, état non actif, aucune reprise motrice automatique | Validation de reprise et identité à renouveler |

L'arrêt d'urgence physique, ses connexions et sa validation relèvent du matériel. Le bouton Bluetooth permet une demande d'arrêt applicatif ; il ne prouve pas une fonction d'urgence indépendante. Aucune sécurité ne dépend du cloud, du LLM ou de l'analyse de pose. Les restrictions individuelles et les règles AR01/AR02 restent prioritaires.

### POD-T12 — Validation et passage au développement

Ne pas commencer par acheter une flotte de mini-PC ni figer une base centrale. Ordre proposé :

1. Résoudre les contrats App de préparation/autorisation/résultats et les protocoles physiques manquants ; inventaire des capacités existantes avant extension.
2. Démonstrateur local de lecture vidéo/mesures et connecteurs, avec simulateurs explicitement distingués du matériel réel.
3. Un pod complet réel : deux caméras, MOTION, vidéos, tactile, Renhe, BPM, boutons et WLED simultanément ; mesure de latence, qualité et température.
4. Deux pods puis capacité cible du studio : départ futur, dérive, pause/reprise, messages doublés/tardifs, pertes de réseau et coordinateur, interférences Bluetooth et reprise sans relance physique.
5. Valider durabilité/réconciliation des événements, autorisations expirées, séparation utilisateurs, purge, installation et mise à jour ; recette coach des indications MOTION.

Les fréquences, latences, incertitudes et tolérances, politiques de panne, format des médias et vidéos conservées doivent être arrêtés avec leurs critères mesurables. Les résultats App/Mobile/Admin historiques ne valent pas validation Pod. **La présente mise à jour modifie uniquement la documentation : aucun logiciel, SQL, droit, installation, test d'appareil ou déploiement effectué.**

---
