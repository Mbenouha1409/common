# MOVEE Motion — référence technique spécifique

Version de consolidation : 2 novembre 2026. **Référence centralisée validée ; anciennes copies retirées après accord utilisateur.** Lire d’abord [README.md](README.md), [règles communes](AGENTS.md), [fonctionnel global](MOVEE_FUNCTIONAL_REFERENCE.md) et [technique globale](MOVEE_TECHNICAL_REFERENCE.md). Les sections issues des anciennes références conservent leur date/statut ; un constat historique ne décrit pas l’installation actuelle.

## Statut

Source unique : document Motion du31octobre, scindé avec [fonctionnel](MOVEE_MOTION_FUNCTIONAL_REFERENCE.md) qui conserve les sources S1–S6 et les réserves. Les §§6–15 conservent leurs numéros pour les renvois internes. Tout code est illustratif, les routes sont des opérations candidates, pas un contrat installé ; aucune dépendance installée ni caméra recettée ici. POC une vue n’annule pas la cible Pod deux RGB-D. Performances et seuils restent hypothétiques.

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:149 -->

## 6. Matériel : RGB, RGB-D et vues complémentaires

### 6.1 Choisir selon l’observabilité

| Montage | Apports | Limites |
|---|---|---|
| Une RGB | Pose, angles apparents, répétitions et trajectoires dans l’image ; intégration généralement simple pour une UVC. | Perspective, occultations, échelle métrique absente sans information supplémentaire. |
| Une RGB-D | Apports RGB et profondeur métrique potentielle sur surfaces visibles. | Trous, mauvais alignement, bords, IR ; ne révèle pas une articulation cachée. |
| Deux RGB calibrées | Vues complémentaires ; triangulation possible de points correspondants visibles. | Synchronisation, correspondance, calibration et géométrie de triangulation nécessaires. |
| Deux RGB-D | Complémentarité des vues et mesures de profondeur. | Coût et calcul supplémentaires ; interférences IR possibles ; aucune fusion automatique. |

Une RGB latérale peut suffire pour détecter un balancement de buste lors d’un tirage. Une seconde vue peut apporter davantage qu’une profondeur depuis le même point si le problème principal est une occultation. Une 3D estimée par un modèle monoculaire reste distincte d’une mesure 3D calibrée.

### 6.2 Nuwa-HP60C : candidate de test

Données **rapportées par S1/S5**, non revérifiées dans les manuels originaux pour cette synthèse :

| Élément | Valeur ou réserve documentaire |
|---|---|
| Identité | Nuwa-HP60C / Angstrong ; variante et firmware à confirmer sur l’appareil. |
| Technologie annoncée | Lumière structurée à référence monoculaire. |
| Profondeur | 640 × 480 ; sources contradictoires à 20/25/30 images/s. |
| RGB | Jusqu’à 1920 × 1080 ; cadence réelle et profils simultanés à confirmer. |
| Champ profondeur H × V | 73,8° × 58,8° annoncés. |
| Champ RGB H × V | 80,9° × 51,7° annoncés. |
| Portée / interface | 0,2–4 m annoncés ; USB 2 Type-C. |
| Précision annoncée | Plan < 2 mm à 1 m ; ne prouve pas l’erreur d’une articulation ni la répétabilité du système. |
| SDK | API C/C++ et calibration mentionnées ; binding Python officiel de ce modèle non établi. |
| Système | Acquisition RGB-D native macOS/Apple Silicon non confirmée ; Windows/Linux à qualifier avec SDK exact. |
| Autres inconnues | Licence de redistribution, support, latence, qualité RGB en effort, horodatages, synchronisation et disponibilité commerciale. |

La dernière recommandation technique de S1 est de tester **la même Nuwa en RGB seul puis en RGB + profondeur**, afin d’isoler le gain de la profondeur. Une UVC témoin reste intéressante pour mesurer le coût réel de cette intégration. Il ne s’agit pas d’un achat de parc validé.

### 6.3 Placement et dimensionnement

Prévoir un support rigide réglable, des câbles protégés et deux emplacements possibles. Essayer une vue latérale pour le plan sagittal et une vue frontale ou trois-quarts pour les asymétries. Le placement dépend de chaque exercice et doit inclure toute sa course, pas seulement la posture initiale.

Couverture théorique à distance `d`, pour un champ `FOV` : `L = 2 d tan(FOV / 2)`. Avec le FOV RGB rapporté de la Nuwa, à 2 m, la couverture plane est d’environ 3,40 m × 1,94 m. C’est un calcul géométrique indicatif, pas une garantie de corps entier : marges, orientation, recul du sujet, banc et champ profondeur plus étroit horizontalement comptent. Les montages proposés pour une station BODY ne sont pas transposés aux pods.

Un ordinateur autonome par pod est la cible locale consignée. CPU, RAM, USB, refroidissement et accélération restent à dimensionner par essais avec caméra, écran, vidéos et connecteurs actifs. Aucun GPU NVIDIA ou NPU n’est requis par décision préalable ; sa présence ne garantit pas sa compatibilité avec MediaPipe.

---

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:190 -->

## 7. Calibration et synchronisation

### 7.1 Calibration spatiale

1. **RGB :** estimer les intrinsèques `fx, fy, cx, cy` et la distorsion avec une mire de taille connue et des poses variées couvrant le champ. Conserver profil, résolution et erreur sur vues de contrôle.
2. **RGB-D :** vérifier les unités, le sens de profondeur, la distorsion, les intrinsèques de chaque capteur et la transformation profondeur → RGB. L’alignement fourni par le SDK doit être validé sur des objets à plusieurs distances.
3. **Deux caméras :** estimer leurs extrinsèques et contrôler la reprojection sur une mire indépendante. Ne pas moyenner leurs coordonnées locales sans changement de repère.
4. **Repère pod :** définir origine, verticale, axes, sens et unité ; documenter la transformation de chaque caméra vers ce repère. Une direction image ne constitue pas automatiquement la verticale réelle.
5. **Contrôle quotidien :** repère visuel fixe ou mire rapide ; après déplacement d’un support, la calibration concernée devient invalide.

Les outils OpenCV de calibration et reconstruction couvrent ce modèle de projection ; leur présence ne garantit pas une précision articulaire donnée. [Documentation OpenCV](https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html)

Après correction de distorsion, si `Z` est la profondeur axiale en mètres dans le bon repère :

```text
X = (u - cx) Z / fx
Y = (v - cy) Z / fy
P_pod = R_cam_vers_pod P_cam + t_cam_vers_pod
```

Si le SDK fournit une distance radiale plutôt que `Z`, il faut adapter la projection. Lire une profondeur au pixel d’un landmark ne localise pas automatiquement le centre anatomique de l’articulation : peau, vêtement, arrière-plan et bords créent un biais. Employer une zone locale robuste sur le sujet, rejeter les incohérences et évaluer ce biais.

### 7.2 Synchronisation temporelle

Chaque observation porte l’identifiant de source, le temps de capture si disponible, le temps de réception monotone local, un numéro de séquence et la qualité d’horodatage. UTC sert à rapprocher les séances ; une horloge monotone sert aux durées locales.

Distinguer exposition, transmission USB, inférence et réception BLE. Le temps d’arrivée n’est pas nécessairement le temps de mesure. Estimer les décalages et dérives par un événement observable simultanément ou par corrélation de signaux sous contrôle ; vérifier régulièrement. Aucun déclenchement matériel commun des caméras n’est établi dans S1/S5.

Apparier au voisin le plus proche dans une tolérance validée, conserver l’écart résiduel et rejeter les associations trop éloignées. Interpoler seulement des signaux continus sur de petits intervalles observés ; ne pas inventer une répétition ni franchir une coupure ou un changement de charge.

Budget temporel : si un segment tourne à `ω` degrés/s, une erreur temporelle `Δt` peut créer environ `ω × Δt` degrés d’écart. À 100°/s et 20 ms, cela représente 2° : illustration géométrique, pas seuil approuvé. Tester aussi la dérive après plusieurs dizaines de minutes.

---

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:222 -->

## 8. Pipeline et mesures biomécaniques

```text
Contexte autorisé + références versionnées + calibration
    → capture RGB / profondeur / signaux machine horodatés
    → contrôle qualité, personne et zone du pod
    → estimation de pose RGB
    → option : projection profondeur ou triangulation explicite
    → repère commun et sélection des points réellement observables
    → filtrage et caractéristiques
    → phases et répétitions
    → comparaison coach + individuelle
    → règles avec confiance, persistance et priorité
    → affichage local / synthèse / événements durables minimisés
```

### 8.1 Pose et coordonnées

MediaPipe Pose Landmarker est le premier moteur proposé. Il fournit des landmarks image et des coordonnées 3D estimées, et propose notamment les modes VIDEO et LIVE_STREAM avec horodatage. En LIVE_STREAM, l’inférence est asynchrone et des images peuvent être ignorées si le moteur est occupé. L’architecture doit accepter une cadence d’analyse inférieure à la capture. [Guide Python officiel](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker/python)

Les coordonnées image normalisées doivent être remises à l’échelle en pixels avant un angle 2D : utiliser directement `x/W` et `y/H` déforme la géométrie si largeur et hauteur diffèrent. Les coordonnées 3D estimées du modèle ne sont pas une mesure indépendante de la scène ni des coordonnées directement fusionnables entre caméras. Conserver explicitement `image_px`, `model_world_estimated` ou `pod_metric` comme espace de mesure.

### 8.2 Angles, amplitude et trajectoires

Pour les points `A, B, C`, angle interne au point B :

```text
u = A - B ; v = C - B
θ = acos( clamp( (u·v) / (||u|| ||v||), -1, 1 ) )
```

Exemples : épaule–coude–poignet, hanche–genou–cheville, épaule–hanche–genou. Cet angle géométrique n’est pas toujours l’angle clinique de flexion ; la convention doit être déclarée. Un angle signé exige un plan et une orientation cohérents ; trois points ne suffisent pas à définir toutes les rotations articulaires.

- **2D :** angle projeté, utile si le plan du mouvement est proche du plan image. Comparaison interdite entre des vues incompatibles sans protocole.
- **3D :** calcul dans un repère métrique calibré, avec visibilité et incertitude ; profondeur présente ne signifie pas précision anatomique.
- **Inclinaison du buste :** axe bassin → épaules par rapport à la verticale calibrée ; une vue unique ne sépare pas toutes les rotations.
- **ROM :** maximum moins minimum sur une répétition complète valide ; des quantiles robustes peuvent limiter les pics, avec méthode enregistrée.
- **Trajectoires :** poignets, coudes, bassin et, seulement si observés séparément, barre/poignées. La pose corporelle ne détecte pas automatiquement la barre.
- **Normalisation :** translation par rapport au bassin ou au pod selon la mesure, échelle segmentaire fiable, orientation et latéralité déclarées. Garder aussi les mesures absolues pertinentes.
- **Asymétrie :** différences de caractéristiques homologues alignées dans le temps, sans conclure depuis un côté caché.
- **Vitesse/accélération :** différences temporelles sur mesures filtrées, unités explicites. Les dérivées amplifient le bruit ; l’accélération est une extension à justifier.

Exemple de vitesse : `v_i = (p_i - p_(i-1)) / (t_i - t_(i-1))`, uniquement pour temps croissants, même repère et points fiables. Aucune vitesse en m/s n’est déduite d’une trajectoire en pixels sans échelle valide.

### 8.3 Phases et répétitions

Définir par exercice une variable de progression : angle, course machine ou combinaison. Utiliser une machine à états avec seuils distincts d’entrée/sortie, temps minimal, amplitude minimale et états d’observation perdue. Une répétition est un cycle complet ; une reprise au milieu du mouvement n’autorise pas un comptage fictif.

Les phases concentrique/excentrique dépendent de l’exercice et du sens de résistance, pas simplement d’un déplacement vers le haut ou vers la caméra. Une pause isométrique peut être légitime. Les répétitions interrompues et non évaluables restent distinctes des répétitions techniquement mauvaises.

### 8.4 Filtrage et incertitude

Pour le direct, commencer par un filtre causal simple avec constante de temps et retard mesurés ; réinitialiser après une coupure importante. Pour l’analyse différée, Savitzky–Golay ou un filtre bidirectionnel peuvent être essayés. Une fenêtre centrée utilise des échantillons futurs : sa qualité hors ligne ne prouve pas la latence en direct. La documentation SciPy précise notamment les contraintes fenêtre/ordre du filtre Savitzky–Golay. [Référence SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.savgol_filter.html)

Ne pas filtrer au travers d’un trou long, d’un changement d’identité ou de calibration. Rééchantillonner seulement des segments continus sur une grille temporelle connue avant les méthodes qui supposent un pas constant.

Conserver une qualité par point et par mesure : visibilité/présence du modèle, bord de champ, flou, profondeur valide, taille du segment, reprojection, désaccord des vues, âge, état de calibration et synchronisation. Un score modèle n’est pas une probabilité calibrée de justesse anatomique.

Pour une mesure `m = f(p)`, une approximation de propagation est `Var(m) ≈ J Σ Jᵀ`, sous hypothèses locales de petites erreurs et covariance pertinente. Une perturbation Monte-Carlo peut estimer la sensibilité. Les biais systématiques ne disparaissent pas par moyennage. En pratique POC : déterminer empiriquement erreurs et répétabilité par métrique et condition, puis s’abstenir lorsque l’écart observé n’est pas distinguable de l’incertitude.

---

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:282 -->

## 9. Comparaison biomécanique et corrections

### 9.1 Comparateur proposé

1. Vérifier contexte, version, réglages et domaine de validité de la référence.
2. Masquer les métriques insuffisamment observables ; ne pas les remplacer par zéro.
3. Segmenter une répétition ou une phase ; conserver les durées réelles.
4. Comparer ROM, trajectoires, position du tronc, symétrie, pauses et tempo aux enveloppes validées.
5. Utiliser la référence individuelle dans ses adaptations approuvées ; garder les règles coach prioritaires définies pour l’exercice.
6. Produire une conclusion par critère avec valeur, tolérance, qualité, gravité et justification.

Une distance pondérée possible est `d² = Σ w_k ((x_k-r_k)/s_k)² / Σ w_k`, sur les seules caractéristiques valides. `s_k` est une tolérance ou une échelle de variabilité validée, strictement positive. Ne pas agréger silencieusement des unités hétérogènes ou des métriques absentes. Le score ne constitue pas une mesure universelle de « bonne posture ».

### 9.2 Alignement temporel et DTW

Un rééchantillonnage de phase sur 0–100 % est un premier comparateur simple pour une répétition terminée. **DTW** est une proposition supplémentaire pour des trajectoires de vitesses différentes :

```text
D(i,j) = coût_local(i,j) + min(D(i-1,j), D(i,j-1), D(i-1,j-1))
```

Contraindre le chemin : bande autour de la diagonale, pente et étirement limités, phases compatibles et durée plausible. Standardiser les caractéristiques avec des échelles fixes de référence. Le coût doit être rapporté à la longueur du chemin choisi et à la couverture ; conserver le chemin pour expliquer les écarts.

DTW peut masquer un tempo incorrect en alignant excessivement : comparer les durées et vitesses séparément. Il ne doit pas aligner une répétition incomplète comme si elle était complète. Le DTW global convient d’abord au différé ; pour le direct, privilégier des règles causales de phase, puis évaluer séparément un alignement en ligne borné. SciPy n’est pas présenté ici comme fournissant un DTW complet prêt à l’emploi : une implémentation ou dépendance dédiée serait à sélectionner seulement si nécessaire.

### 9.3 Corrections directes et différées

| Mode | Usage proposé |
|---|---|
| Direct | Écart simple, visible et persistant ; consigne courte prévalidée, une priorité à la fois. |
| Fin de répétition | Amplitude, durée et cycle complet ; évite une conclusion prématurée. |
| Fin de série | Variabilité, asymétries persistantes, évolution entre répétitions et revue coach. |

États explicites : `évaluable`, `conforme aux critères observés`, `écart détecté`, `observation insuffisante`, `analyse indisponible`. « Conforme aux critères observés » ne certifie pas une sécurité globale.

Exemples candidats : « Stabilise le buste » pour un balancement démontré ; « Reviens dans l’amplitude validée avec ton coach » si cette amplitude est disponible. Définir persistance, hystérésis, délai entre messages et annulation si la mesure devient douteuse. Éviter les injonctions de charge et les diagnostics. Une douleur déclarée appelle le protocole humain prévu, jamais une correction algorithmique de la posture pour continuer à tout prix.

Le POC affiche d’abord mesures et écarts pour le coach ; la voix automatique vient après validation de la pertinence et de la fréquence. Un LLM n’est pas nécessaire au moteur de règles ; une éventuelle reformulation ne modifie ni seuils ni commandes.

---

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:321 -->

## 10. Fusion avec les capteurs machine

La vision renseigne la cinématique ; la machine peut renseigner la charge, la force, la course ou la vitesse **si ces mesures sont réellement exposées et qualifiées**. Les sources locales évoquent un protocole Renhe, sans démontrer une intégration ni toutes les grandeurs disponibles.

| Signal candidat | Apport | Réserve |
|---|---|---|
| Charge ou résistance confirmée | Contexte de comparaison et prescription. | Consigne, affichage et mesure physique peuvent différer. |
| Force mesurée | Effort externe le long d’un axe connu. | Unité, étalonnage, direction et fréquence à vérifier. |
| Course câble / encodeur | Segmentation et amplitude machine. | Ne représente pas directement l’amplitude d’une articulation. |
| Vitesse machine | Phases et tempo. | Peut être dérivée, filtrée ou retardée par le firmware. |
| Cardio éventuel | Contexte de séance dans Pod. | Ne corrige pas la précision de pose et n’autorise aucune adaptation automatique implicite. |

Commencer par une fusion de caractéristiques et contrôles de cohérence : course machine pour aider les phases, vision pour le buste, désaccord signalé si leurs cycles divergent. Pondérer selon la qualité empirique ; une moyenne arbitraire de scores hétérogènes n’est pas une fusion validée.

Calculs optionnels, seulement si les grandeurs sont mesurées et synchronisées : `P = F·v` pour force et vitesse au même point ; `W = ∫ F·dx` sur la course. Une résistance en kg affichée n’est pas directement une force en N sans modèle ; poulies, rapports, frottements et résistance électronique peuvent changer le transfert. Le moment externe `τ = r × F` exige axe, point et vecteur de force connus et ne mesure pas le moment articulaire interne ou l’effort musculaire.

En perte BLE, distinguer absence de mesure et valeur nulle. Continuer une analyse vision seule uniquement pour les métriques qui restent valides et l’indiquer ; aucune mesure ancienne présentée comme actuelle.

---

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:339 -->

## 11. Stack logicielle et architecture locale

| Couche | Choix ou proposition | Statut |
|---|---|---|
| Orchestration | Python | Orientation cible locale. |
| Acquisition RGB UVC | OpenCV | Proposition POC. |
| Acquisition RGB-D | SDK constructeur, adaptateur vers tableaux NumPy | À qualifier ; OpenCV seul n’assure pas le support natif Nuwa. |
| Pose | MediaPipe Pose Landmarker | Premier moteur à essayer, non recetté sur pod. |
| Géométrie | NumPy | Proposition pour angles, repères et trajectoires. |
| Signal | SciPy si utile | Proposition pour filtrage et analyse différée. |
| Alignement | Phases normalisées puis DTW si gain démontré | Proposition, aucune bibliothèque DTW imposée. |
| UI de POC | Affichage Python simple | Proposition minimale. |
| UI Pod cible | Interface web locale tactile, retour vidéo distinct des mesures | Cadrage Pod ; transport vidéo à choisir. |
| Central | API Flask → Services → Repositories → MariaDB | Architecture App consignée ; intégration MOTION à contractualiser. |
| Temporaire local | Fichiers et éventuellement SQLite | Proposition ; aucun schéma créé. |

### Séparation des traitements

```text
Pod autonome
 ├─ contexte autorisé et interface locale
 ├─ acquisition RGB-D / pose / comparaison (processus isolé)
 ├─ connecteurs machine et limites autorisées
 ├─ journal de résultats et reprise de synchronisation
 └─ échange authentifié avec App

App centrale
 API Flask → Service métier → Repository → MariaDB
```

Le moteur d’analyse ne commande pas directement un driver moteur. Utiliser des files bornées ; abandonner les images anciennes au profit d’une observation fraîche. Conserver l’identifiant de contexte avec chaque image et résultat pour éliminer les retours d’inférence tardifs après changement d’exercice ou d’adhérent.

La vidéo locale reste disponible indépendamment du comparateur lorsque c’est techniquement possible ; afficher l’absence d’analyse. Éviter de transporter les images brutes en JSON. Aucun serveur vidéo/MOTION commun n’est la cible retenue dans les références Pod. Le coordinateur Studio éventuel ne doit pas être une dépendance par image.

Hors ligne : seuls contexte et droits préalablement autorisés selon une politique encore à préciser ; journal durable, limites de taille, expiration, reprise idempotente. Ne pas inventer une politique de poursuite illimitée. Au retour du réseau, envoyer les résultats minimisés, pas toute la vidéo par défaut.

---

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:375 -->

## 12. Intégration et contrat API proposé

**Aucune route ci-dessous n’est attestée existante.** Il s’agit d’un contrat sémantique candidat à adapter aux mécanismes App, à ses droits et aux modèles réels après audit. Aucun nouveau type de frontend, rôle ou objet SQL n’est créé par ce document.

| Opération logique | Données essentielles | Contrôles |
|---|---|---|
| Préparer une analyse | Séance, adhérent pseudonymisé, pod, exercice, réglages, prescription, références et versions, droits et expiration. | Autorisation utilisateur/pod/séance ; références compatibles. |
| Charger une référence | Identifiant, version, métriques, tolérances, contexte, médias autorisés. | Statut validé, intégrité, visibilité. |
| Recevoir des résultats | Identifiants uniques, contexte, répétitions, métriques, qualité, versions, horodatages. | Schéma, unités, tailles, autorisation et déduplication. |
| Faire revoir une référence | Validation/rejet et motif par coach habilité. | Workflow, traçabilité et version immuable. |
| Consulter une synthèse | Résultats autorisés et état de revue. | Cloisonnement adhérent/centre/coach selon droits réels. |

Enveloppe illustrative d’un résultat, non schéma physique :

```json
{
  "contract_version": "proposition-1",
  "event_id": "identifiant-unique-stable",
  "session_ref": "opaque-session",
  "subject_ref": "opaque-subject",
  "pod_ref": "opaque-pod",
  "exercise_ref": "opaque-exercise-variant",
  "context_revision": 3,
  "reference_versions": {"coach": "v2", "individual": "v1"},
  "calibration_ref": "calibration-A",
  "engine_version": "poc-not-deployed",
  "rep_index": 4,
  "status": "insufficient_observation",
  "metrics": [
    {"key": "elbow_rom", "value": null, "unit": "deg",
     "coordinate_space": "image_px", "valid": false,
     "reason": "wrist_occluded"}
  ],
  "capture_window": {"start_monotonic_ms": 1000, "end_monotonic_ms": 4200},
  "clock_domain": "pod-boot-opaque",
  "captured_at_utc": "2026-10-31T10:00:00Z"
}
```

Les temps monotones ne sont comparables qu’au sein du même domaine d’horloge. Une valeur non mesurable reste `null` avec motif ; aucune substitution par zéro. Les clés et versions de cet exemple n’impliquent aucune table existante.

**Répartition proposée :** Flask valide le transport et l’authentification ; le Service contrôle droits, contexte, version, unités et idempotence, puis orchestre la transaction ; le Repository effectue uniquement les accès autorisés à la persistance réelle. Le Pod n’accède jamais directement à MariaDB.

Le serveur accuse réception de chaque événement avec identifiant canonique et résultat accepté, déjà reçu ou rejeté. Une répétition d’envoi conserve le même identifiant et le même contenu ; un même identifiant avec contenu différent est un conflit. Séparer envoi technique réussi et validation coach. Prévoir authentification de pod, rotation des secrets, contrôle de taille, refus d’une référence obsolète et journal sans images sensibles. Le mode exact d’authentification, les routes, codes d’erreur, limites et durée de conservation restent à définir selon App.

---

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:420 -->

## 13. Modèle conceptuel de données

Ce modèle décrit des concepts et relations, **sans supposer de tables, colonnes, clés étrangères ou migrations MariaDB**. Les entités réellement présentes doivent être inventoriées avant toute traduction SQL.

| Concept | Informations utiles | Relations conceptuelles |
|---|---|---|
| Définition d’exercice/variante | Configuration, phases, métriques observables, vues requises. | Références coach et exécutions. |
| Référence coach versionnée | Séquences retenues, enveloppes, règles et validation. | Exercice, validateur, version remplacée. |
| Découverte | Protocole, charge/répétitions, réglages, observations. | Adhérent, coach, appareil et contexte. |
| Référence individuelle | Amplitudes et adaptations approuvées, domaine de validité. | Découverte, exercice et version coach compatible. |
| Calibration | Intrinsèques/extrinsèques, profils, unités, tests et validité. | Caméras, pod et mesures produites. |
| Exécution/série | Contexte autorisé, charge confirmée et versions utilisées. | Séance et répétitions. |
| Observation/mesure | Valeur, unité, repère, temps, provenance et qualité. | Répétition, source et calibration. |
| Écart/correction | Critère, gravité, preuve, message, instant et résultat de revue. | Mesure et règle versionnée. |
| Média ou séquence de points | Emplacement protégé, empreinte, durée de conservation. | Référence ou capture autorisée. |
| Validation/traçabilité | Acteur, date, décision et motif. | Référence ou résultat concerné. |
| Événement de synchronisation | Identifiant, état d’envoi, accusé et tentatives. | Résultat logique, sans imposer une table dédiée. |

Séparer média brut, points articulaires et résumé ; leurs coûts et risques diffèrent. Les séries temporelles volumineuses peuvent relever de fichiers protégés avec références et métadonnées plutôt que de lignes par image dans MariaDB : choix à mesurer et contractualiser. Pas de duplication systématique de l’identité de l’adhérent sur chaque échantillon.

---

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:440 -->

## 14. Exemples Python et pseudo-code

**Statut : exemples proposés, non intégrés et non exécutés sur matériel.** Les imports supposent un environnement préparé ultérieurement ; aucune dépendance n’a été installée pour ce livrable. Ces fonctions ne remplacent pas qualité, calibration ou validation coach.

### 14.1 Angle 2D ou 3D et conversion image

```python
import numpy as np


def angle_deg(a, b, c, min_norm=1e-9):
    """Angle interne en B ; points déjà validés dans le même repère."""
    a, b, c = (np.asarray(p, dtype=float) for p in (a, b, c))
    if a.shape != b.shape or b.shape != c.shape or a.shape not in ((2,), (3,)):
        raise ValueError("Points 2D ou 3D de mêmes dimensions requis")
    if not np.isfinite(np.stack((a, b, c))).all():
        return None
    u, v = a - b, c - b
    nu, nv = np.linalg.norm(u), np.linalg.norm(v)
    if min(nu, nv) < min_norm:
        return None
    cosine = np.clip(np.dot(u, v) / (nu * nv), -1.0, 1.0)
    return float(np.degrees(np.arccos(cosine)))


def landmark_to_pixels(landmark, width, height):
    # Exiger séparément visibilité, présence et position dans le champ.
    return np.array([landmark.x * width, landmark.y * height])
```

`min_norm` empêche seulement une division dégénérée ; un minimum physique ou en pixels, calibré à l’usage, doit aussi écarter les segments trop courts pour une mesure fiable. Une position finie ne suffit pas à déclarer l’articulation visible.

### 14.2 Déprojection élémentaire d’un pixel profondeur

```python
def deproject_axial_depth(u, v, z_m, fx, fy, cx, cy):
    """Pixel profondeur corrigé, Z axial métrique ; pas un pixel RGB brut."""
    if not np.isfinite([u, v, z_m, fx, fy, cx, cy]).all():
        return None
    if z_m <= 0 or fx <= 0 or fy <= 0:
        return None
    return np.array([(u-cx)*z_m/fx, (v-cy)*z_m/fy, z_m])
```

Il faut auparavant résoudre l’alignement RGB/profondeur, rejeter les profondeurs hors plage et vérifier que le pixel appartient au sujet. La fonction ne constitue pas une fusion RGB-D complète.

### 14.3 Acquisition et inférence : pseudo-code de cycle

```text
initialiser le contexte autorisé, les références et la calibration
ouvrir la caméra via OpenCV (UVC) ou le SDK exact (RGB-D)
initialiser Pose Landmarker avec le modèle et les options qualifiées

à chaque image :
    associer contexte, séquence et temps de capture / réception
    vérifier fraîcheur, format, qualité et domaine d'horloge
    convertir BGR vers RGB si la capture OpenCV est BGR
    soumettre l'image au mode VIDEO ou LIVE_STREAM approprié
    conserver un appariement borné timestamp → contexte de capture

à chaque résultat :
    rejeter résultat ancien ou relatif à un contexte remplacé
    sélectionner la personne dans la zone autorisée ; sinon s'abstenir
    évaluer les points utiles à cet exercice
    déprojeter / trianguler seulement si calibration et temps valides
    filtrer de façon causale, mettre à jour phases et répétitions
    comparer uniquement les caractéristiques observables
    appliquer persistance, hystérésis et priorité des règles
    afficher résultat horodaté et qualité
    enregistrer le résumé autorisé sans vidéo par défaut

à l'arrêt : fermer caméra, moteur et fichiers ; vider les références sensibles
```

Pour le mode VIDEO, l’appel synchrone reçoit des timestamps strictement croissants. Pour LIVE_STREAM, le callback traite les résultats asynchrones ; ne pas compter un résultat par image capturée. Ne pas combiner les modes dans une même instance par supposition.

### 14.4 DTW borné pour comparaison différée

```python
def dtw_mean_cost(x, y, band):
    """Coût euclidien moyen sur le chemin minimisant le coût total.

    x et y : tableaux (temps, caractéristiques), complets et standardisés
    avec les échelles fixes de la référence. Exemple hors ligne uniquement.
    """
    x, y = np.asarray(x, float), np.asarray(y, float)
    if x.ndim != 2 or y.ndim != 2 or x.shape[1] != y.shape[1]:
        raise ValueError("Dimensions incompatibles")
    if not x.size or not y.size or not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ValueError("Séquences finies et non vides requises")
    n, m = len(x), len(y)
    if band < abs(n-m):
        return None  # Ne pas élargir silencieusement la contrainte.
    cost = np.full((n+1, m+1), np.inf)
    count = np.zeros((n+1, m+1), dtype=int)
    cost[0, 0] = 0.0
    for i in range(1, n+1):
        for j in range(max(1, i-band), min(m, i+band)+1):
            predecessors = [(i-1, j-1), (i-1, j), (i, j-1)]
            a, b = min(predecessors, key=lambda p: cost[p])
            if not np.isfinite(cost[a, b]):
                continue
            cost[i, j] = cost[a, b] + np.linalg.norm(x[i-1] - y[j-1])
            count[i, j] = count[a, b] + 1
    return float(cost[n, m] / count[n, m]) if count[n, m] else None
```

Ce code illustre la récurrence et la bande ; il ne gère ni masque de données manquantes, ni pente maximale, ni chemin retourné, ni alignement par phase. Il minimise un coût total puis le normalise, pas un coût moyen optimal. Mémoire `O(nm)` ; séquences courtes de répétitions seulement. Avant usage réel, ajouter les contraintes du §9, conserver le chemin, limiter la taille et comparer le gain au simple rééchantillonnage.

### 14.5 Validation d’une correction : pseudo-code

```text
si contexte incompatible ou mesure périmée : analyse indisponible
sinon si visibilité / calibration / synchronisation insuffisante : abstention
sinon si écart dépasse la tolérance coach + marge d'incertitude :
    accumuler la durée d'observation valide de cet écart
    si durée suffisante et message non récemment émis :
        proposer la consigne prévalidée de plus haute priorité
sinon : réarmer selon le seuil de sortie et les règles d'hystérésis
```

Une perte d’observation remet à zéro ou suspend explicitement la persistance selon la règle validée ; elle ne confirme jamais l’écart. Les valeurs numériques de ces règles doivent provenir du protocole de validation, pas d’un exemple de code.

---

<!-- provenance: movee-motion/codex/MOVEE_MOTION_REFERENCE.md:563 -->

## 15. Plan de POC et critères de validation

### 15.1 Étapes et livrables

| Étape | Travail | Preuve attendue avant extension |
|---|---|---|
| P0 — Cadrage | Un exercice, une variante, fiche coach, critères observables, consentement et matériel. | Protocole d’essai et annotations définis. |
| P1 — Acquisition | Une vue, capture horodatée, tests RGB seul ; éventuellement Nuwa en mode comparatif. | Profils réels, stabilité USB, couverture et taux d’images exploitables. |
| P2 — Mesures hors ligne | Pose, angles, ROM, phases et répétitions sur séquences annotées. | Erreurs par métrique et motifs d’abstention. |
| P3 — Références | Coach puis découverte individuelle, versions et tolérances. | Revue coach et absence de normalisation abusive. |
| P4 — Comparaison | Règles simples, phase normalisée ; DTW seulement en comparaison. | Pertinence des écarts et taux de fausses alertes. |
| P5 — RGB-D / seconde vue | Même RGB avec/sans profondeur ; seconde caméra pour occultations. | Gain isolé, coût, latence et calibration documentés. |
| P6 — Direct supervisé | Mesures puis consignes visuelles ; voix si validée. | Latence, stabilité et compréhension en effort. |
| P7 — Intégration | Contrat App validé, simulation puis environnement d’essai dédié. | Droits, idempotence, panne réseau et séparation utilisateurs. |
| P8 — Extension | Autres exercices, morphologies et plusieurs pods. | Recette reproductible avec charge complète et interférences. |

### 15.2 Jeu d’évaluation

Inclure plusieurs personnes et morphologies, côtés, vêtements, charges et vitesses autorisées ; plans caméra variés, éclairage réel, occultations par machine et situations sans personne. Annoter répétitions, phases et écarts observables avec deux coachs sur une partie du corpus ; mesurer leur accord et arbitrer les désaccords.

Séparer les personnes et séances de réglage des seuils et celles d’évaluation. Rapporter résultats par exercice et condition, ainsi que le nombre de cas ; un score global peut cacher un échec sur un groupe. Ne pas provoquer d’exécutions dangereuses pour enrichir le corpus ; préférer variations sûres, données simulées identifiées et supervision.

Un goniomètre ou une annotation vidéo manuelle peut servir de référence pratique pour certains angles ; une 3D validée exige une référence métrologique plus solide. La même pose MediaPipe ne peut pas servir simultanément de prédiction et de vérité terrain.

### 15.3 Critères proposés à faire approuver avant essais

Les nombres suivants sont des **objectifs exploratoires**, ni des performances obtenues, ni des seuils cliniques ou de recette déjà approuvés. Ils doivent être adaptés à l’exercice et à l’incertitude de la référence.

| Domaine | Mesure / objectif exploratoire |
|---|---|
| Acquisition | Viser 30 images/s si le profil réel le permet ; publier cadence, pertes et durée d’essai. |
| Analyse | Viser environ 15 résultats/s sur les métriques utiles ; mesurer les résultats frais, pas seulement les appels soumis. |
| Vidéo locale | Hypothèse Pod antérieure : latence < 150 ms ; mesurer capture → affichage et p95. |
| Retour de correction | Proposition : p95 < 300 ms de traitement/affichage après disponibilité des observations ; déclarer séparément la persistance volontaire et l’attente de fin de répétition. |
| Angles observables | Proposition initiale : MAE ≤ 5°, p95 d’erreur absolue ≤ 10° face à une référence suffisamment précise. |
| Répétitions | Proposition : ≥ 95 % des séries avec compte exact ; détailler les répétitions partielles et les abstentions. |
| Écarts ciblés | Proposition : précision ≥ 90 %, rappel ≥ 80 % sur les seuls écarts définis et annotables ; publier aussi faux positifs par série. |
| Observation | Proposition : ≥ 90 % du temps utile évaluable dans les conditions nominales ; rapporter aussi la performance globale en incluant les abstentions. |
| Pannes | Aucun résultat ancien présenté comme actuel, aucune réactivation machine, aucune confusion d’adhérent lors des scénarios testés. |
| Endurance | Proposition : essai de 60 minutes avec vidéo, UI et connecteurs actifs ; absence d’accumulation mémoire/files, température et cadence consignées. |

L’abstention doit elle-même être testée : caméra débranchée, articulation cachée, mauvais contexte ou calibration invalide. Une abstention systématique ne permet pas d’atteindre artificiellement une bonne précision. Mesurer couverture et erreurs ensemble, avec incertitude statistique lorsque l’effectif le permet.

Pour RGB-D, comparer sur les mêmes images et mêmes personnes : erreur angulaire, stabilité, faux positifs, couverture et latence. Pour la seconde caméra, mesurer surtout les occultations résolues. La décision matérielle repose sur un gain pertinent pour les critères ciblés, pas sur une meilleure résolution annoncée.

### 15.4 Défaillances à exercer

Perte caméra/BLE/réseau ; horloge réinitialisée ; retard d’inférence ; flux gelé ; déplacement du support ; sujet hors champ ; plusieurs personnes ; changement d’exercice ou d’adhérent ; référence retirée ; stockage plein ; redémarrage ; rejouage d’événements ; interférences IR entre pods et saturation USB. Distinguer simulateur, replay et matériel réel dans chaque compte rendu.
