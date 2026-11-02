# MOVEE Motion — référence fonctionnelle spécifique

Version de consolidation : 2 novembre 2026. **Référence centralisée validée ; anciennes copies retirées après accord utilisateur.** Lire d’abord [README.md](README.md), [règles communes](AGENTS.md), [fonctionnel global](MOVEE_FUNCTIONAL_REFERENCE.md) et [technique globale](MOVEE_TECHNICAL_REFERENCE.md). Les sections issues des anciennes références conservent leur date/statut ; un constat historique ne décrit pas l’installation actuelle.

## Lecture du corpus scindé

L’ancien document unique MOVEE_MOTION_REFERENCE.md est réparti sans transformer propositions en décisions. Fonctionnel : source/statuts, concept, catalogue candidat, découverte, références coach, confidentialité, registre final. Technique : §§6–15 d’origine (caméras, calibration, mesures, comparaison, fusion, stack, contrat proposé, modèle conceptuel, exemples et POC). Lire le second fichier pour ces numéros. Aucun document BODY autonome retrouvé dans ces dossiers, aucun développement BODY déduit.

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:2 -->

**Version documentaire : 1.0 — 31 octobre 2026**  
**Périmètre : analyse des exercices sur pods MOVEE, uniquement MOTION.**  
**Statut : synthèse de conception et base de POC ; aucune recette matérielle ou implémentation MOTION attestée.**

Ce document permet de reprendre le projet dans une conversation dédiée. Il rassemble le contexte accessible de « Movee Pod Vision », les références locales effectivement consultées et des propositions techniques explicites. Les exemples sont pédagogiques : ils ne constituent ni un moteur prêt à déployer, ni une prescription sportive, ni un contrat API existant.

---

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:29 -->

## 1. Sources, portée et statuts

### 1.1 Sources réellement accessibles

| Identifiant | Source | Apport et limite |
|---|---|---|
| S1 | [Conversation Movee Pod Vision](chatgpt-conversation://6ace3dd7-8b50-83ed-9281-785cd964042e) | Lecture via `read_thread`, limite 10 tours ; cinq tours retournés, aucun curseur antérieur disponible. Contient les échanges RGB/RGB-D, la synthèse utilisateur des caméras et le cadrage MOTION. Ne restitue pas des pièces jointes techniques originales. |
| S2 | `codex/MOVEE_POD_FUNCTIONAL_REFERENCE.md`, XP01–XP12, notamment XP06 | Cible Pod locale ; exercice connu, références coach et individuelles ; deux RGB-D demandées dans cette cible. |
| S3 | `codex/MOVEE_POD_TECHNICAL_REFERENCE.md`, POD-T01–T07 notamment | Pipeline, séparation des processus, calcul local, contrat central, performances encore hypothétiques. |
| S4 | [AGENTS.md](AGENTS.md), centralisation et périmètre Pod | Responsabilités, anti-invention, absence de contrat Pod attesté, interdiction de confondre arrêt logiciel et sécurité matérielle. |
| S5 | `output/movee-input-cameras-2026-10-30/rapport-comparatif-cameras.html` | Rapport local présent et consulté pour les passages Nuwa/MOTION. Source secondaire issue d’une étude documentaire, pas un essai physique ni une nouvelle vérification de chaque dossier constructeur. |
| S6 | `movee-app/requirements.txt`, `movee-app/app.py`, `movee-app/repositories/abstract_repository.py` | Flask et dépendance PyMySQL déclarés, application Flask et couche Repository observées. Aucun contrat MOTION déduit de ces fichiers. |

Les chemins ci-dessus sont relatifs au dossier de travail `/Users/mbenmouha/Documents/Movee`. Ils désignent les sources consultées, pas une destination de centralisation décidée.

**Vérification Git en lecture seule :** le dossier parent Movee n’est pas un dépôt Git. `movee-app` est un dépôt, HEAD `feb3dc1415d8c98b9c445c9b61bd6f17dd27c790` (`docs: document Mac development environment and application boundaries`). Son arbre de travail comporte de nombreuses modifications et fichiers non suivis ; les références lues décrivent donc aussi un état local non nécessairement commité. Le dossier `movee-pod` existe mais n’est pas un dépôt Git et aucun fichier logiciel n’a été trouvé dans son inventaire limité à trois niveaux. Cela ne prouve pas l’absence d’un développement ailleurs. Aucun SQL exécuté, aucune connexion à la base, aucune migration, installation ou opération de déploiement effectuée pour cette synthèse.

Les anciens noms attendus `MOVEE_MOTION_FUNCTIONAL_REFERENCE.md` et `MOVEE_MOTION_TECHNICAL_REFERENCE.md` ne sont pas attestés par les recherches effectuées. Le document BODY/MOTION mentionné dans S2/S3 n’a pas été retrouvé et lu directement ; son contenu n’est pas reconstitué comme une source indépendante.

### 1.2 Convention de statut

- **Cadrage retenu :** principe établi dans les références locales ou explicitement exprimé dans le contexte. Une cible n’est pas une preuve d’implémentation.
- **Proposition :** solution à essayer ou détail ajouté pour rendre le POC réalisable.
- **Non vérifié :** disponibilité, performance, compatibilité ou comportement matériel non mesuré.
- **Non implémenté / non attesté :** aucun code ou contrat fonctionnel MOTION identifié dans les sources consultées.

**Divergence à préserver :** S1 envisage un démarrage avec une caméra et une seconde optionnelle. S2/S3 consignent une cible Pod avec deux RGB-D. Le POC minimal à une vue n’annule pas la cible à deux caméras ; le déploiement final exige une réconciliation explicite de ces cadrages après essais. Les recommandations successives de l’assistant dans S1 ne valent pas validation d’achat par l’utilisateur.

---

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:57 -->

## 2. Concept et responsabilités

MOVEE MOTION observe un adhérent réalisant un **exercice déjà connu** sur un pod équipé d’une barre ou de poulies. Il mesure des caractéristiques d’exécution, les compare à des exécutions coach validées et à une référence individuelle, puis fournit un retour compréhensible lorsque l’observation est suffisamment fiable.

Le contexte est fourni avant la série : exercice et variante, côté, appareil, accessoires, hauteur des poulies, position du banc, prise, charge ou mode de résistance, prescription de répétitions et paramètres individuels validés. La reconnaissance libre de milliers d’exercices n’est pas nécessaire.

La comparaison est triple :

1. **Référentiel coach :** technique attendue, phases, critères et variations acceptables.
2. **Référence individuelle :** amplitudes, réglages et exécutions validées pour cette personne.
3. **Observation courante :** mouvement, qualité de mesure et signaux machine synchronisés.

La référence individuelle ne doit pas rendre automatiquement acceptable un défaut appris lors de la découverte. Le coach valide ce qui constitue une adaptation utile et ce qui reste un écart.

### Responsabilités

| Composant | Responsabilité |
|---|---|
| MOTION | Mesures, qualité, comparaison, propositions de correction et synthèses. |
| MOVEE Pod | Acquisition et exécution locales, connecteurs matériels, interface pendant la séance, journal temporaire. |
| MOVEE App | Identité, autorisations, programmes, consentements, validation métier et historique central. |
| Coach | Validation technique, découverte, tolérances et adaptations individuelles. |
| MOVEE Mobile | Consultation hors entraînement selon contrats existants ; aucun pilotage caméra ou moteur ajouté par ce document. |
| Sécurités de la machine | Arrêt d’urgence et limites matérielles indépendants de MOTION et du réseau. |

MOTION ne réalise pas ici de bilan morphologique, de scan corporel, d’avatar ou de mesure de circonférences. Les longueurs utiles à la normalisation peuvent être renseignées ou estimées avec incertitude, sans introduire la chaîne BODY. Il ne pose pas de diagnostic et ne calcule pas directement les contraintes internes des articulations à partir de simples angles vidéo.

---

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:84 -->

## 3. Catalogue d’exercices connus

**Intention fonctionnelle : environ quatre à six exercices par groupe musculaire**, avec variantes connues et protocoles coach. La conversation accessible ne fournit pas de liste exhaustive validée. Le tableau suivant est un **catalogue candidat de cinq exercices par groupe**, à vérifier selon la géométrie, les ancrages, les accessoires, la course et les possibilités réelles du pod. Il ne décrit pas le catalogue existant de MOVEE App et ne constitue pas une prescription.

| Groupe principal | Cinq exercices candidats barre/poulie | Observations MOTION prioritaires |
|---|---|---|
| Pectoraux | Développé couché barre ; développé incliné barre ; développé debout aux poulies ; écarté aux poulies ; écarté haut vers bas | Trajectoire des poignets/coudes, amplitude, symétrie, inclinaison du tronc. |
| Dos | Tirage horizontal assis ; tirage vertical prise large ; tirage vertical prise neutre ; rowing unilatéral poulie ; pullover bras presque tendus à la poulie | Balancement du buste, trajectoire coudes/poignets, amplitude et différences droite/gauche. |
| Épaules | Développé épaules barre ; élévation latérale poulie ; élévation frontale poulie ; oiseau aux poulies ; face pull | Élévation des bras, inclinaison du tronc, symétrie ; rotation fine de l’épaule souvent mal observable. |
| Biceps | Curl barre ; curl poulie basse barre droite ; curl poulie basse corde ; curl unilatéral poulie ; curl haut aux poulies | Flexion du coude, déplacement du bras et compensation du tronc. |
| Triceps | Extension poulie haute barre ; extension poulie haute corde ; extension au-dessus de la tête à la poulie ; extension unilatérale poulie ; extension couchée barre | Course du coude, déplacement de l’épaule, stabilité du tronc. |
| Quadriceps | Squat barre ; front squat ; fente arrière avec résistance poulie ; split squat avec résistance poulie ; squat à ceinture reliée à une poulie basse | Flexion hanche/genou, trajectoire relative genou/pied, profondeur et équilibre visible. |
| Ischio-jambiers / fessiers | Soulevé de terre roumain barre ; soulevé de terre barre ; pull-through poulie ; hip thrust barre ; extension de hanche poulie avec sangle | Charnière de hanche, inclinaison du tronc, amplitude ; pas de déduction de courbure vertébrale précise depuis quelques points. |
| Mollets | Élévation debout barre ; élévation assise barre ; élévation debout poulie basse bilatérale ; élévation unilatérale poulie ; élévation en position de fente avec poulie | Course de cheville et du talon, stabilité ; pieds et appuis doivent être visibles. |
| Tronc / abdominaux | Crunch à la poulie ; Pallof press ; rotation contrôlée à la poulie ; woodchop haut vers bas ; woodchop bas vers haut | Mouvement bassin/thorax, amplitude et contrôle ; rotation axiale souvent impossible à conclure en 2D. |

Les exercices se recouvrent entre groupes. Une variante exige sa propre fiche si les axes, la prise, la posture ou la résistance changent sensiblement. Les mouvements nécessitant banc, ceinture, sangle cheville ou ancrage haut sont exclus tant que leur compatibilité matérielle et leur encadrement ne sont pas confirmés.

**POC recommandé :** tirage horizontal à la poulie, une variante, un pod et un placement caméra. Ajouter ensuite un curl et un exercice jambes pour explorer des contraintes différentes, sans développer immédiatement tout le catalogue.

---

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:104 -->

## 4. Découverte avec le coach et référence individuelle

### 4.1 Parcours proposé

1. Identifier l’adhérent et le pod ; vérifier les autorisations et l’accord pour les captures nécessaires.
2. Vérifier l’exercice, les accessoires, les réglages et l’absence de douleur déclarée ; le coach décide de la pertinence de l’essai.
3. Régler le banc, la hauteur et l’écartement des poulies, la prise, les appuis et la position de départ selon la morphologie et les capacités observées.
4. Déterminer une charge de travail et une plage de répétitions adaptées ; documenter le mode de résistance et ce que la machine mesure réellement.
5. Évaluer la capacité de force selon un protocole coach. La « force max » doit être définie : charge externe de 1RM, estimation submaximale ou force mesurée en newtons à un point donné sont des grandeurs différentes.
6. Enregistrer plusieurs répétitions techniquement validées, aux charges utiles, dans l’amplitude personnalisée ; première proposition de POC : environ cinq répétitions propres par prise de référence, puis plusieurs prises pour estimer la variabilité.
7. Valider avec le coach les limites d’amplitude, le tempo, les adaptations et les critères à surveiller.
8. Versionner et approuver la référence ; prévoir une réévaluation lors d’un changement de réglage, de capacité ou d’exercice.

Le test maximal réel n’est pas requis pour initialiser MOTION. Une estimation de 1RM n’est qu’un indicateur de programmation soumis au protocole et à la validation du coach ; aucune formule générique n’est imposée ici. Il faut conserver charge, répétitions réellement effectuées, qualité technique et conditions du test plutôt qu’un nombre « force max » isolé.

### 4.2 Données individuelles utiles

- Réglages reproductibles et repères de positionnement, côté et variante.
- Charge prescrite, charge confirmée et éventuelle force mesurée, chacune avec unité et provenance.
- Répétitions, tempo, amplitude confortable validée et répétitions retenues comme référence.
- Paramètres de normalisation utiles : stature ou longueurs segmentaires si fiables ; source et incertitude.
- Restrictions et adaptations validées, accessibles aux seuls rôles habilités.
- Identité du validateur, date, version, motifs de modification et contexte matériel.

Une référence à faible charge ne garantit pas une exécution identique sous charge élevée. Le domaine d’utilisation doit préciser charges et configurations validées. La mise à jour automatique d’une référence à partir de séries non revues est exclue de la première version proposée.

---

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:130 -->

## 5. Référentiel d’exécutions coach validées

Une référence est un **ensemble contextualisé d’exécutions acceptées**, pas une vidéo universelle à reproduire exactement.

Chaque fiche doit décrire :

- exercice, variante, configuration machine, accessoires et vues requises ;
- objectif du mouvement, articulations observables et limites de mesure ;
- début/fin de répétition, phases concentrique, excentrique, pauses éventuelles ;
- angles, trajectoires, amplitude, tempo et asymétries pertinentes ;
- erreurs annotées et corrections associées, avec leur niveau de priorité ;
- variantes acceptables et adaptations individuelles possibles ;
- seuils, persistance et qualité minimale exigée pour conclure ;
- répétitions de référence, annotations temporelles, validateur, versions et statut.

Cycle proposé : **brouillon → revue coach → validé → remplacé ou retiré**. Une modification conserve l’historique. Les résultats d’une séance restent rattachés à la version utilisée.

Construire une enveloppe par phase à partir de plusieurs répétitions et, progressivement, de plusieurs coachs/morphologies. Moyenne, médiane, dispersion ou quantiles ne doivent pas transformer des défauts non annotés en norme. Un score unique ne remplace pas les critères explicables.

---

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:612 -->

## 16. Sécurité et confidentialité

### 16.1 Sécurité d’usage

MOTION est une aide à l’observation. Une absence d’alerte ne certifie pas l’exécution. Prévoir recours au coach, indication claire de l’indisponibilité et consignes compatibles avec l’effort. Le moteur ne modifie pas une charge et ne commande pas l’arrêt d’urgence. Les sécurités matérielles restent indépendantes du réseau, de Python, de l’interface et d’un éventuel LLM ; aucune reconnexion ne doit réactiver implicitement un équipement arrêté.

Les points de pose ne permettent pas une analyse fine des vertèbres, tendons ou scapulas. Limiter le vocabulaire à ce qui est réellement observable. Détecter une inclinaison globale ne justifie pas un diagnostic ou une estimation de risque de blessure.

### 16.2 Protection des données : conception à valider

Appliquer minimisation, finalité explicite, durée limitée et sécurité dès le POC. Le calcul local réduit certains transferts mais ne rend pas anonymes les vidéos, points corporels ou résultats associés à une séance. Les recommandations ci-dessous sont une base de conception, pas une analyse juridique complète. [Les six grands principes du RGPD — CNIL](https://www.cnil.fr/fr/comprendre-le-rgpd/les-six-grands-principes-du-rgpd)

- Identifier le responsable du traitement, les finalités et la base légale appropriée ; faire qualifier les données et les éventuelles obligations liées aux données de santé par le référent compétent.
- Informer l’adhérent sur captation, calcul, accès, transferts, conservation et droits ; prévoir le parcours applicable sans capture selon la politique retenue.
- Traiter en mémoire et conserver des résumés par défaut ; toute vidéo de développement ou revue exige une finalité et une autorisation documentées.
- Filmer la zone utile, éviter les tiers et ne pas ajouter de reconnaissance faciale. Ne pas réutiliser les captures pour entraîner un modèle sans cadrage distinct.
- Définir des durées pour vidéos, points, références individuelles, résultats, journaux et sauvegardes ; aucune durée arbitraire n’est déclarée validée ici.
- Pseudonymiser les références locales ; authentifier les échanges, chiffrer les supports et limiter les accès selon besoin réel.
- Prévoir purge locale après synchronisation selon politique, suppression des copies temporaires, rotation des secrets et logs sans données corporelles brutes.
- Gérer les droits sur les données dans App et propager les demandes aux caches et sauvegardes selon la politique définie.
- Examiner avec le référent protection des données la nécessité d’une analyse d’impact et les risques de surveillance ou d’inférence sensible avant déploiement.

Les références coach filmées sont elles aussi des données personnelles ; leur droit d’usage et leur diffusion doivent être documentés. Le document présent ne crée aucun consentement ni habilitation.

---

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:636 -->

## 17. Registre final des décisions, propositions et inconnues

| Sujet | Statut à conserver |
|---|---|
| MOTION sur exercices connus, contexte fourni | Cadrage retenu. |
| Comparaison coach + référence individuelle validée | Cadrage retenu ; protocoles détaillés à définir. |
| Calcul local sur ordinateur du pod | Cible consignée dans les références Pod. |
| Séparation BODY/MOTION | Cadrage retenu ; aucun développement BODY dans ce document. |
| Quatre à six exercices par groupe | Intention de périmètre demandée ; tableau du §3 proposé, pas catalogue validé. |
| Découverte : capacité de force, charges/répétitions, réglages et amplitudes | Besoin fonctionnel ; protocole coach et disponibilité des signaux à confirmer. |
| MediaPipe en premier essai | Proposition technique commune aux sources. |
| Python, OpenCV, NumPy, SciPy et DTW | Stack de travail proposée ; versions, environnement et nécessité de DTW à qualifier. |
| Une caméra au POC, seconde optionnelle | Proposition de démarrage dans la conversation. |
| Deux RGB-D par pod | Cible documentaire S2/S3 ; ne pas la présenter comme équipée ou annulée. |
| Nuwa-HP60C | Candidate de test ; achat, SDK Python, profils et gain non validés. |
| Calibration, profondeur et multi-vues | Développement explicite requis ; aucune fusion automatique. |
| Capteurs machine | Fusion proposée, signaux et protocole réel à recetter. |
| Flask → Services → Repositories → MariaDB | Architecture App observée/consignée ; aucun endpoint ou schéma MOTION attesté. |
| SQLite/fichiers locaux et synchronisation | Orientations proposées, contrat et politique hors ligne ouverts. |
| Performances et seuils | Hypothèses de POC ; aucune mesure obtenue. |
| Code Python du présent document | Illustratif, non intégré, non testé sur pod. |
| Déploiement, SQL ou migration | Aucun effectué ni autorisé par cette synthèse. |

### Prochain travail concret

Préparer la fiche coach du tirage horizontal et le protocole d’annotation ; inventorier le pod et ses réglages ; vérifier le modèle exact de caméra et son SDK ; tester visibilité et acquisition ; construire une première référence coach et une référence individuelle ; comparer hors ligne les métriques simples ; quantifier ensuite le gain de profondeur et de seconde vue. L’implémentation et l’intégration App feront l’objet d’un chantier séparé à partir de contrats et de données réellement inventoriés.

### Références techniques externes consultées le 31 octobre 2026

- [MediaPipe Pose Landmarker — Python](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker/python) : modalités d’inférence, coordonnées et gestion du flux asynchrone.
- [OpenCV — Camera Calibration and 3D Reconstruction](https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html) : projection, intrinsèques, extrinsèques et calibration.
- [SciPy — savgol_filter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.savgol_filter.html) : filtrage polynomial et contraintes de fenêtre.

Les versions affichées par les documentations en ligne ne constituent pas des versions de dépendances retenues pour MOVEE. Les caractéristiques Nuwa restent attribuées aux sources locales S1/S5 et ne constituent pas une vérification constructeur actualisée.
