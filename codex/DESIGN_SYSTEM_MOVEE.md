# DESIGN SYSTEM MOVEE

Version 1.2 — 31 octobre 2026 — référence commune

## Statut, périmètre et transmission

L’utilisateur a validé les deux directions de l’étude Mobile du31octobre : **Light / Clarté active** et **Black / Impulsion**, sélectionnables par un bouton. Cette charte est la référence commune à transmettre à MOVEE Mobile, Admin, Biz et Info. Son emplacement canonique est `/Users/mbenmouha/Documents/Movee/codex/DESIGN_SYSTEM_MOVEE.md` ; les projets doivent citer ce fichier et sa version plutôt que créer une charte concurrente. Toute copie doit porter cette version, ce chemin source et la date de synchronisation. Les changements partagés sont arbitrés ici avant diffusion ; aucun chat ne constitue une dépendance documentaire.

La palette #EFFF4F / #10131A et le logo fourni existaient déjà, validés pour Biz/Info puis repris par Mobile. Aucun autre document de charte complète commune n’a été trouvé dans les sources examinées. Ce document formalise la nouvelle base de composants validée par le choix des deux directions ; il ne prétend pas que les autres projets sont déjà intégrés.

**Lot courant : intégration Mobile seulement.** Aucun déploiement ni changement Admin/Biz/Info autorisé par ce fichier. Maquettes sources : `../output/design/movee-mobile-2026-10-31/clarte-active.png` et `impulsion.png`. Les valeurs ci-dessous priment sur les approximations d’un visuel généré. Les contenus, droits, transactions, consentements et contrats Pages restent leurs sources de vérité respectives.

## 1. Personnalité et invariants de marque communs

Movee associe énergie, précision et accompagnement. Le jaune signale l’action et les repères ; le noir structure. Éviter l’effet tableau de bord générique, les néons, les dégradés décoratifs, les boutons tous dominants et la multiplication de panneaux imbriqués. Hiérarchiser d’abord par alignement, typographie et espacement, puis séparateurs/surfaces, enfin contours. Ombres rares.

Logo : conserver strictement le fichier original, proportions et couleurs. Source Mobile `movee-mobile/assets/brand/movee-logo.png`, reprise du logo Biz. Ne pas redessiner le mot-symbole ni en fabriquer une version typographique. Espace libre minimal recommandé autour : 1/4 de la hauteur du logo. Sur fond clair, utiliser un cartouche noir pour l’original blanc/jaune. Mobile : grand logo complet au login seulement. Les usages en en-tête/pied de site restent propres aux sites. Un motif de mouvement peut être dérivé d’un véritable asset approuvé, jamais improvisé en CSS ou confondu avec un nouveau logo.

## 2. Couleurs sémantiques communes

| Token | Light — Clarté active | Black — Impulsion | Rôle |
| --- | --- | --- | --- |
| brand.ink | #10131A | #10131A | Encre de marque |
| brand.lime | #EFFF4F | #EFFF4F | Accent de marque |
| background | #F4F5F0 | #10131A | Fond général |
| surface | #FFFFFF | #1B202A | Blocs, champs et feuilles |
| media.background | #EEF0E7 | #EEF0E7 | Lisibilité des miniatures anatomiques dans les deux thèmes |
| selected | #E8EBDD | #29313C | Sélection/pression secondaire |
| text | #10131A | #F7F8F2 | Texte principal |
| text.secondary | #5B635E | #B5BDB7 | Aide, libellés secondaires |
| border | #D9DED2 | #3C4652 | Séparateurs non interactifs |
| control.border | #7B8678 | #798696 | Limites de champs et contrôles |
| action.primary | #EFFF4F | #EFFF4F | Action dominante |
| action.onPrimary | #10131A | #10131A | Texte/icône sur jaune |
| accent.text | #536000 | #EFFF4F | Texte accentué sur le fond courant |
| success.text | #245C40 | #B7E4CA | Confirmation accompagnée de texte |
| success.surface | #EAF3E9 | #173C2A | Fond sémantique succès |
| danger.text | #A02C30 | #FFB2AC | Erreur/action destructive |
| danger.surface | #FCEBEC | #402427 | Fond sémantique erreur |

Le jaune ne sert pas de texte courant sur blanc. Aucun blanc sur bouton jaune. Une valeur métier inconnue n’est ni un zéro ni un succès. Les badges génériques d’un statut non qualifié restent neutres : ne pas transformer tout statut en succès par une règle client sur son libellé.

Viser WCAG AA : texte normal4,5:1 ; grand texte3:1 ; contours essentiels, focus et pictogrammes3:1. Mesurer les combinaisons réelles, y compris les états d’erreur et de sélection. L’opacité désactivée n’est jamais la seule indication de disponibilité : état accessible et absence d’exécution obligatoires.

## 3. Typographie commune

| Usage | Taille / interligne | Graisse |
| --- | --- | --- |
| Titre de page | 24 /32 ; titre long18 /24 multiligne, sans troncature | 600 |
| Titre de section | 24 /32, variante compacte20 /28 | 600 |
| Titre de bloc | 18 /24 | 600 |
| Action principale d’un accueil | 20 /26 | 600 |
| Corps | 16 /24 | 400 |
| Texte secondaire de bloc | 15 /22 | 400 |
| Bouton | 16 /24 | 600 ; primaire700 |
| Action secondaire compacte | 13 /18 | 600 |
| Libellé court / onglet | 13 /18 | 500–700 |
| Badge | 13 /18 | 700 |

Titres Light : **Manrope**. Titres Black : **Sora**. Corps et contrôles : police système de la plateforme (SF sur iOS, Roboto/système sur Android, pile système sur Web). Deux familles actives au maximum dans un thème. Ne pas dépendre d’un téléchargement de police au moment de l’utilisation. Mobile embarque les TTF variables Manrope et Sora et leurs licences SIL OFL dans `assets/fonts/`. Provenance : dépôt officiel `google/fonts`, répertoires `ofl/manrope` et `ofl/sora` ; les licences livrées avec ces fichiers font foi.

Les grands titres marketing des sites pourront avoir une échelle responsive dédiée sans modifier les tokens de lecture produit. Respecter l’agrandissement système ; pas de hauteur fixe bloquant le texte, pas de troncature des valeurs essentielles.

## 4. Grille, géométrie et élévation communes

Unité4px/dp ; pas4,8,12,16,20,24,32,48,64. Marge Mobile20, padding bloc16, espacement blocs12–16, espacement sections24. Largeur de lecture Mobile/tablette720maximum centrée ; fond et navigation occupent l’écran, pas une fausse coque de téléphone.

| Élément | Light | Black |
| --- | --- | --- |
| Carte | rayon16 | rayon8 |
| Bouton/champ/segments | rayon12 | rayon8 |
| Contour | 1px | 1px |
| Focus | contour contrasté2px, décalage2 | idem |
| Ombre carte | aucune | aucune |
| Feuille flottante si nécessaire | 0,8,24, noir8% | séparation par contour/surface |

Les badges numériques seuls peuvent être ronds. Éviter les pilules pour chaque donnée. Aucune carte dans une carte sans raison fonctionnelle. Les séparateurs simples conviennent aux détails et formulaires.

## 5. Icônes et médias communs

Icônes sémantiques cohérentes,24px, petit pictogramme de donnée18–20px ; traits visuels proches de2px. Le prototype utilise l’esprit Material Symbols Rounded/Outlined ; Mobile conserve la bibliothèque native déjà intégrée `expo-symbols` : SF Symbols sur iOS et équivalents Material sur Android/Web. Ne pas introduire une seconde bibliothèque pour simuler un changement cosmétique de trait. Les libellés accessibles et les clés symboliques restent identiques entre thèmes. Pas d’emoji comme icône produit, ni d’URL de police/asset exécutable reçue des métadonnées.

Exercices : véritables médias autorisés du catalogue, miniatures à proportions conservées, fond neutre clair pour les mannequins anatomiques, images sans étirement. Animation sur geste explicite et possibilité d’arrêt, nettoyage au changement de contexte. Conserver l’attribution/licence exacte fournie par le serveur ; les illustrations générées de la planche ne remplacent pas les médias réels. Toute photographie commerciale doit rester distincte des données d’exercice et ne pas être présentée comme preuve de résultat.

## 6. Composants communs

**Bouton primaire :** lime/encre, icône24, hauteur minimale52, padding horizontal16, vertical14, gap8. Un choix dominant par groupe lorsque la configuration le permet. **Secondaire :** surface, contour de contrôle, texte/icône principaux. **Discret :** fond transparent, icône+texte ; réservé aux opérations secondaires et commandes d’interface. **Danger :** libellé explicite et couleur danger ; ne jamais supprimer consentement ou aperçu.

Les actions multiples de ligne sont côte à côte si l’espace le permet, minimum136 de largeur indicative et flex adaptatif ; passage à la ligne autorisé, jamais de clipping. Les champs ont label visible lorsque les métadonnées l’autorisent, placeholder non substitut du label, aide/erreur accessibles ; minimum52 de hauteur.

**Cartes :** informations nécessaires d’abord, une action de lecture explicite, statut textuel, pictogrammes utiles, chevron si navigation. Une date/heure structurée peut utiliser une colonne de date générique à partir du format et du fuseau publiés. Ne jamais reconnaître une réservation à son nom de Page ou recalculer ses règles métier dans le gabarit.

**Filtres :** conserver les segments de période publiés et regrouper les autres critères sous un seul bouton Filtres et tri ; afficher leur état actif, préserver les critères au retour et réinitialiser la pagination sans perdre le contexte relationnel. Ne pas ajouter des filtres uniquement décoratifs.

**Navigation :** icône+libellé, sélection perceptible par forme et texte. Light : surface sélectionnée douce et repère lime ; Black : icône/libellé accentués et soulignement lime. Ne pas dépendre uniquement de la couleur.

## 7. Adaptations Mobile

### Présentation déclarative

Pages, Fields, Designer et Services restent les sources des contenus, droits, actions, icônes métier, critères, valeurs initiales, ordre et destinations. Le template traduit ces métadonnées en blocs, boutons et champs. Aucune condition sur UID, nom d’entité, libellé ou rôle pour produire un parcours spécifique. Aucun endpoint, écriture ou droit ajouté pour une variation graphique.

Le premier élément visible de `presentation.action_uids` donne l’action dominante du groupe de Page ; une `primary_action_uid` explicite prime si elle appartient à ce groupe (jamais si elle désigne seulement la lecture d’une ligne). Pour l’accueil/action (`page_type=7`), les boutons suivent aussi l’ordre de cette liste déclarée. Les autres actions conservent leur ordre déclaré. Les actions de ligne restent secondaires et conservent configuration, version, contexte et preuve de ligne d’origine. Cette convention de présentation n’accorde aucun droit et ne déclenche rien au rendu.

Le bouton **Light / Black** est une préférence locale d’affichage, comme les commandes techniques de langue/thème ; il ne représente pas une action métier Pages et ne modifie aucune donnée de compte. Il est proposé à la connexion et dans le bandeau d’espace, aux côtés du compte, y compris pour le coach. L’état accessible indique si Black est activé. Première ouverture : suivre le système ; après sélection explicite : conserver le choix sur l’appareil. Web : stockage local de cette seule préférence non sensible ; natif : stockage de préférence via le mécanisme SecureStore déjà disponible. Une indisponibilité de stockage ne bloque pas le changement d’apparence en mémoire. Aucun cookie d’identité ni jeton ajouté au stockage Web.

### Choix de langue Mobile — version1.1

Le choix de langue est un bouton drapeau48×48 dans le bandeau supérieur, immédiatement avant le profil. Français par défaut, drapeau correspondant à la langue active. Au clic : fenêtre de choix Français, English, Deutsch, Español avec vrais assets de drapeaux embarqués, langue courante cochée et bouton de fermeture en haut. Le changement réutilise le contexte de langue et la garde de saisie existants ; aucune écriture de compte, aucun appel métier supplémentaire. Choisir la langue déjà active ou fermer ne réinitialise pas l’espace.

L’ancien bouton « Réglages de l’application » et le bouton de langue sous le bandeau sont retirés. Le changement d’espace autorisé reste disponible séparément ; il ne doit pas disparaître avec ce déplacement. Une langue est toujours nommée en texte dans la liste et le bouton a un libellé accessible : le drapeau n’est jamais la seule information. Les assets FR/GB/DE/ES proviennent de FlagCDN et sont servis localement, pas téléchargés par le téléphone à chaque ouverture. Le drapeau GB représente ici le choix English, sans modifier les règles de locale du catalogue.

### Parcours et placement

Grand logo au login seulement. Après connexion adhérent : crédits disponibles et notifications à gauche, compte à droite ; boutons retour gauche et actualiser droite dans un en-tête unique. Trois destinations inférieures existantes : Accueil, Réservations/Séances et Programmes, toutes fournies par les Pages. Centre défilant entre bandeaux. Modales : titre/retour/actualiser en haut, aucune barre de navigation inférieure ; actions dans le contenu, pas de pied de boutons imposé. Le coach garde les destinations et droits de son espace, habillés par les mêmes composants.

Navigation jusqu’à l’action finale/formulaire en trois clics maximum pour les parcours validés, sans compter choix métier et confirmations. L’IA chat/voix reste la navigation principale cible mais désactivée dans l’environnement actuel ; aucune fausse conversation, entrée vocale fonctionnelle ou nouveau raccourci métier ajouté par la charte. Les écrans manuels restent pleinement utilisables.

### Conventions iOS/Android et accessibilité

Safe areas réelles, clavier, retour Android, gestes et focus des modales conservés. Cibles48×48minimum, champs52minimum, défilement avec texte agrandi, orientation/tablette sans largeur forcée. Utiliser les vrais symboles natifs et le gestionnaire de navigation existant. Éviter de dessiner la barre système ou les appareils dans l’interface. Thème reflété dans barres système et navigation. Aucun changement de thème ne réinitialise le formulaire, le journal, la session, la navigation ou les filtres. Animations décoratives non nécessaires ; reduced motion à respecter. États chargement, erreur, quota et reprise restent visibles et conformes aux contrats.

## 8. Réutilisation ultérieure Admin, Biz, Info

Commun : marque, couleurs sémantiques, familles de titres, échelle de lecture, grille, boutons/champs, icônes sémantiques, focus, statuts, règles média et accessibilité. Adaptable : densité de tables et barres d’outils Admin, grandes compositions éditoriales/photographies Biz/Info, navigation desktop, colonnes et largeurs responsive. Ne pas copier la tabbar Mobile sur Admin ni imposer aux sites les parcours de l’adhérent.

Chaque projet réalise un inventaire de ses composants et documente les écarts motivés sous cette référence avant intégration. Aucun transfert de règles métier, permissions ou données entre projets. Les améliorations réellement communes remontent dans ce fichier, versionné ; les spécificités restent dans les référentiels du projet concerné.

## 9. Validation d’une intégration

Vérifier Light et Black sur les mêmes trois écrans, même contenu et même viewport, comparer aux deux planches ; vérifier switch sans perte d’état, restauration après rechargement, clavier/texte agrandi et tablette. Contrôler les vrais médias, attributs d’accessibilité, contrastes, contours et zones tactiles. Tests des contrats et parcours existants inchangés, compilation et exports des plateformes. Ne pas confondre export réussi et recette réelle iPhone. Documenter les limites ; aucune mutation métier implicite pour une vérification graphique.

## 10. Groupes déclaratifs de lecture — version1.2

Présentation validée par l’utilisateur pour les programmes et démonstrations. Les groupes sont des primitives communes, pas des composants liés à un UID métier. Le nouveau profil14 publie des déclarations ordonnées group_uid/kind/columns/cell_count ; les réponses fournissent les cellules matérialisées. Les bindings relation/Field/path restent au serveur et au Designer. Les anciens profils restent inchangés.

- grid : une, deux ou trois colonnes, ordre row-major, labels et pictogrammes publiés ; pas de calcul de valeur métier côté client. Les champs de deux dates utilisent le format date_range, affichagefrançais « Du JJ/MM/AAAA au JJ/MM/AAAA » sur une ligne lorsque l’espace et la taille système le permettent. Une borne inconnue reste explicitement partielle.
- Axes d’un programme : groupe3colonnes, durées Force/Cardio/Mobilité puis parts. tone=muted et status_label localisé sont publiés pour un axe explicitement absent ; un état inconnu ne devient jamais un0 ou Non prévue. Les pourcentages sont des basispoints entiers fournis par Service, seulement formatés par locale dans Mobile.
- Prescription : groupe2colonnes, répétitions/séries puis repos/durée totale. Titres lisibles, pictogrammes natifs, disposition adaptative avec texte agrandi.
- media_gallery : exactement3cellules dans l’ordre publié, principale puis paire de comparaison2colonnes. Pour la démonstration actuelle : animation explicite, Début, Fin. Sources privées et attributions conservées ; une attribution identique peut être affichée une fois pour le groupe, des attributions différentes restent distinctes. Pas de choix de sexe ni de tri par libellé dans le template.

Le calcul de durée par série et les droits/variantes de médias sont des règles métier des Services, hors charte graphique. Les groupes présents remplacent le summary traditionnel du bloc ; titre/image/statut/actions restent natifs et les détails utiles non groupés sont conservés. La carte peut placer le chevron dans sa ligne de titre pour laisser toute la largeur à la période et aux métriques. Aucune URL, police ou logique exécutable fournie par les métadonnées.

Cette version formalise le rendu codé ; elle ne prétend pas que le profil14 est déjà installé ou que les données historiques ont été qualifiées.
