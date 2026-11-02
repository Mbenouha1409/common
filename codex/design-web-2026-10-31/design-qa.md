# Recette Product Design — intégration Biz / Info

31 octobre 2026. final result: passed

## Cibles et preuves

Sources validées : `biz-clarte-editoriale-v2.png`, `biz-immersion-structuree.png`,
`info-clarte-editoriale.png`, `info-immersion-structuree.png` dans ce dossier.
Charte commune v1.2 et choix du switcher Light / Black documenté dans
`../ADAPTATIONS_WEB_MOVEE.md`. Site existant Flask/Jinja à 5051, sans déploiement.

Captures dans `recette/` : quatre accueils `biz/info-light/black-desktop.png` et
leurs équivalents `-mobile.png`, formats Biz et entraînements Info dans les deux
thèmes, simulateur desktop/mobile/contrôles320, contact desktop/mobile.
Comparaisons réellement composées et ouvertes dans le même input visuel :

- `biz-light-comparaison.png`, `biz-black-comparaison.png` ;
- `info-light-comparaison.png`, `info-black-comparaison.png` ;
- `biz-formats-light-comparaison.png`, `biz-formats-black-comparaison.png` ;
- `info-training-light-comparaison.png`, `info-training-black-comparaison.png`.

Viewport CSS : ordinateur1440×900, mobile390×844, contrôle étroit320×844. Captures
PNG à ces dimensions, densité1. Planches sources1448×1086 : leurs quatre cadres
sont des réductions générées, pas des captures exactes1440×900. Comparaisons par
recadrage du cadre pertinent puis redimensionnement proportionnel, sans étirer
les images ; repères complets conservés. Les compositions comparatives1640px de
large ne constituent pas un nouveau viewport. Les contrôles mobiles ont aussi été
ouverts séparément à leur résolution native pour lire les textes et les champs.

## Historique des corrections

1. [P2 résolu] Le titre Biz passait initialement sur trois lignes au lieu du
   rythme attendu sur ordinateur ; ajustement des titres marketing (48 Light,
   40 Black desktop) et32px mobile, sans troncature ni police supplémentaire.
   Preuves après correction : accueils et comparaisons Biz.
2. [P2 résolu] Les vues détaillées occupaient trop de hauteur par rapport aux
   planches. Titres de section libérés de la limite de largeur des paragraphes,
   photos des formats Light recadrées en bandeau, sections réduites à48px,
   entraînements Black en lignes plus compactes. Nouvelles captures et quatre
   comparaisons détaillées réouvertes après correction.
3. [P2 résolu] Le select natif coach pouvait ellipser son libellé à320px. La
   valeur choisie est maintenant répétée intégralement en texte multiligne sous
   le select sur mobile, mise à jour au choix, sans nouvelle règle de calcul.
   Le lecteur d'écran conserve le select natif ; le doublon visuel est aria-hidden.
   Preuve : `recette/biz-simulateur-controles-320.png`, valeur coach exploitant.

Aucun P0/P1/P2 restant identifié dans le périmètre vérifié.

## Cinq surfaces de fidélité

- **Typographie :** vrais fichiers locaux Manrope/Sora déjà utilisés par Mobile,
  graisses600, corps système16/24, choix de famille confirmé au navigateur.
  Les titres marketing ont une échelle Web ; le corps et les contrôles ne sont
  pas réduits pour faire tenir artificiellement le contenu dans une planche.
- **Espacement et composition :** grille4px, conteneur1200, marges20 mobile,
  texte/photo séparés ; photo avant texte seulement en Black mobile. Formats
  Biz en lignes Light / colonnes Black, pratiques Info en colonnes Light /
  lignes Black. Aucun débordement horizontal constaté à320/390/1440px.
- **Couleurs :** copies de tokens identiques à la source commune, palettes et
  rayons de la charte v1.2, primaire jaune/encre, champs avec control.border.
  Pas de dégradé décoratif, glow ou nouvelle palette. Contrastes de référence
  calculés dans ETUDE_BIZ_INFO.md ; focus contrasté clair dans le bandeau noir.
- **Images et marque :** logo original conservé, sans reconstruction ; images
  existantes des pods réutilisées, proportions et légendes conservées. Recadrage
  selon le contexte, aucune nouvelle photographie ou preuve commerciale inventée.
  Pas de nouveaux pictogrammes artisanaux ; le menu utilise un libellé texte.
- **Contenus :** vrais contenus CMS, contrôles de lecture DB testés. Textes complets
  d'aide économique et de confidentialité préservés. CTA hero nomme l'action,
  lien contact dans la recherche vide ; aucun centre, prix ou rendement inventé.

## Écarts intentionnels, pas de reproduction des défauts de la planche

- Le switcher, demandé après les planches, et les langues à cibles tactiles48px
  rendent le bandeau plus haut. La notice de démonstration reste présente.
- Le site défile : des sections ou aides longues continuent sous le viewport.
  L'ordre réel du one-pager reste conservé, avec FAQ dernier bloc. Les aperçus de
  bas de hero dans les planches ne sont pas tous des sections complètes de900px.
- Les photographies intégrées sont les fichiers sources réels de l'étude ; les
  recompositions/crops approximatifs inventés dans les maquettes ne sont pas
  importés comme nouvelles images de studios.
- La recherche studio et le contact restent des sections successives : le
  formulaire complet et sa confidentialité sont conservés, sans les comprimer
  dans le demi-cadre synthétique de la planche. Les réserves financières aussi
  demeurent complètes. Les règles et textes CMS priment sur ces condensations.
- Deux familles de titres selon le thème, aucune préférence de thème de compte.
  Chaque origine mémorise son propre choix local, sans transfert d'identité.

## Interactions et vérifications

- Switch par clic et touche Entrée ; état aria-pressed ; restauration Black
  après rechargement, sans action métier ni requête de mise à jour de compte.
- Test de changement système avant choix explicite ; préférence explicite
  ensuite prioritaire ; stockage indisponible ou valeur invalide : tests Node.
- Menu mobile ouvert puis ancre simulateur, fermeture et focus de destination ;
  titres des destinations visibles sous l'en-tête. Slider au clavier8→7 et
  choix coach exploitant : recalcul puis valeurs/chiffres conservés au switch.
- Contact : saisies synthétiques non envoyées, consentement non coché et toujours
  requis ; valeurs conservées au switch clavier. Clic sur le switch depuis la
  section : position du titre contact conservée à200px sous le haut du viewport.
- Dimensions320/390/1440, thème Light/Black ; grilles et champs lisibles ; styles
  reduced-motion conservés. Aucun test sur appareil physique ou audit complet
  lecteur d'écran/zoom200% revendiqué.
- Console navigateur : aucun message d'erreur JS observé dans les journaux
  disponibles des pages examinées. Polices et scripts servis localement sous CSP.
- 13 tests publics (CMS/formulaires/langues/ancres et scénario JS du simulateur)
  réussis, puis2 tests Node du thème. Données synthétiques nettoyées (0 compte
  example.invalid restant en test). Vérification de syntaxe JS et diff-check OK.
- Copies tokens, deux polices et licences identiques à leurs fichiers communs.

Une première recette a révélé une dépendance du test d'ancrage à la forme exacte
du tag main ; le test accepte maintenant ses attributs d'accessibilité sans
affaiblir le contrôle de la FAQ finale. L'essai du libellé coach a aussi révélé
une mise à jour inutile sur toute saisie : elle est limitée à son changement.
La dernière exécution groupée des13tests passe.

## Finitions possibles et clôture

[P3] Une future recette sur téléphone réel et avec les textes commerciaux/juridiques
définitifs permettra d'affiner les espacements. Aucun changement métier ou
déploiement n'est requis pour consulter cette version locale.

Checklist réalisée : choix documenté, tokens/ressources communs, sites intégrés,
comparaison visuelle et corrections, interactions vérifiées, tests réussis.

final result: passed
