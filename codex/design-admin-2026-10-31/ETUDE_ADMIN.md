# Étude Product Design — MOVEE Admin

31 octobre 2026 — **PROPOSITIONS NON VALIDÉES, NON INTÉGRÉES**.
Référence unique : [DESIGN_SYSTEM_MOVEE.md v1.2](../DESIGN_SYSTEM_MOVEE.md), [tokens Web](../movee-web-tokens.css), [adaptations Biz/Info](../ADAPTATIONS_WEB_MOVEE.md). Aucun de ces fichiers validés modifié. Aucune nouvelle charte ni copie des tokens. Cette étude ne constitue pas une validation de nouveaux composants communs.

## Périmètre examiné et sources

Interface Flask/JavaScript native de movee-app/dashboard, port5050 ; pas de frontend indépendant. Pages/Fields/Actions, FilterEngine, DataTable, ListPage, ViewPage, FormPage, TargetRenderer (components/target.js), ActionEngine/HelperBuilder et notify existent. Configurations chargées sous session web ; données et commandes recontrôlées par les Services. Le thème local movee.css est une adaptation antérieure ; il ne constitue pas la source commune et ne charge pas encore les tokens/polices canoniques. Les thèmes Light/Black sont validés communément ; leur intégration complète Admin reste distincte de cette étude.

Sources projet consultées : codex/MOVEE_ADMIN_SCOPE.md, codex/METADATA_ENGINE.md, référentiels App fonctionnel/technique, code courant app/app.js, components/header.js, engines/filter_engine.js, pages/list_page.js, view_page.js, form_page.js, styles natifs. Rapport installé ADMIN_ROW_SHORTCUTS_APPLICATION_ACTIVATION_RESULT.md :83raccourcis/29listes ; droits et recettes Backend distincts des captures.

## Utilisateurs et travail réel

- Siège/franchiseur : navigation réseau et gestion autorisée. Ne pas déduire tous les droits d'une étiquette de rôle.
- Franchisé/exploitant : mêmes modèles visuels, données et actions filtrées par les Services sur ses studios ; aucune sélection réseau libre inventée.
- Coach : seules populations/relations autorisées, notamment adhérents affectés ; aucune extension liée au design.

Seule une session siège existante a été observée dans Chrome ; pas de nouvelle connexion, simulation de rôle ou soumission. Le rapport Backend signale l'absence de compte franchisé local courant pour une recette positive : ne pas prétendre une recette graphique franchisé.

Parcours : choisir une rubrique → liste → critères/tri → consulter une ligne ou son raccourci → fiche/sous-liste → retour au contexte. Les formulaires réseau/Booking/catalogue sont des actions explicites, jamais déclenchées par leur simple présence. Le design conserve confirmations, versions et récupération prévues au contrat, y compris leurs limites actuelles.

Cinq thèmes actifs observés : Réseau ; Personnes ; Offres et souscriptions ; Planning et séances ; Accompagnement. Finance et Exploitation appartiennent au périmètre futur mais ne sont pas proposés comme fonctions actives. Framework et Paramètres sont hors du lot.

## Audit capturé dans cette étude

1. **Accueil administration — utilisable, orientation faible.** Le contenu réel se limite à « Choisissez une liste dans le menu principal. » Aucun KPI, activité ni alerte disponible sur cet écran. Les variantes réorganisent uniquement les actions de navigation autorisées en annuaire ; aucune statistique ajoutée. [Capture](references/01-accueil.png).
2. **Réservations113 — fonctionnelle, lecture difficile.**26résultats réels de recette, huit colonnes dont identités, studio et engagement tronqués. Pagination technique en anglais ; bouton filtre peu explicite et panneau masqué automatiquement après initialisation. « Réserver une séance » et « Accords à traiter » ont le même poids jaune. Le statut textuel existe : à conserver, sans classification automatique par son libellé. [Capture](references/02-reservations.png).
3. **Réservation114 — actions conservées, hiérarchie perfectible.** Fiche modale d'Alice synthétique :04/11/2026 14:00–14:30, Confirmée ; coach absent ; confirmation30/10/2026 20:13:33. Les longues valeurs sont tronquées et les lectures Personne/Studio ont le même poids que « Annuler avec aperçu ». Le tiret mélange absence/non renseigné : la formulation explicite ne doit être utilisée que si le contrat permet de distinguer ces états. [Capture](references/03-fiche-reservation.png).

4. **Petit écran390×844 — navigation dégradée.** Le bandeau comprime les rubriques/identité et les lignes deviennent fortement tronquées. Les propositions de menu repliable et résumé adaptatif répondent à ce constat. [Capture](references/04-petit-ecran-existant.png). La taille de fenêtre a été rétablie après contrôle.

Ces captures montrent les risques visuels, pas une conformité clavier/WCAG. Aucun test d'annulation ou de validation métier n'a été réalisé pour les produire. Les contenus RECETTE COMPLETE sont des données synthétiques déjà installées, pas des créations pour embellir la maquette.

## Deux mises en page, une identité

Les deux planches montrent **les mêmes trois écrans en Light**, puis la même liste adaptée à390×844. Ce choix isole la comparaison de disposition. Les déclinaisons Black doivent réutiliser les tokens communs et Sora, pas devenir une troisième identité. Les pixels et textes des images générées sont indicatifs : les contenus ci-dessus et les tokens font foi.

### A — Continuité native horizontale

[Planche provisoire](continuite-horizontale.png)

Bandeau compact noir, cinq groupes de menus existants, repère de rubrique et titre lisibles. Accueil en annuaire simple des destinations autorisées. Liste pleine largeur, filtres explicitement accessibles, tri de colonnes et pagination conservés. Fiche dans la modale existante, valeurs sans troncature essentielle, actions secondaires horizontales, annulation distincte et explicitement nommée.

Avantages : conserve le modèle mental installé ; plus de largeur utile pour les tableaux ; réutilise directement les cibles et composants natifs. Limite : les menus horizontaux doivent se replier derrière Menu en petit écran et ne permettent pas de voir simultanément toutes les destinations.

### B — Navigation latérale persistante

[Planche provisoire](navigation-laterale.png)

Même identité, mêmes cinq groupes issus des actions autorisées, présentés dans une colonne latérale. Repère de sélection texte+forme. Accueil avec annuaire sans métriques. Liste avec zone de travail structurée ; fiche dans un panneau latéral large, liste contextuelle visible. En petit écran : navigation escamotée, panneau de détail plein écran avec retour.

Avantages : repérage constant pour un opérateur qui change souvent de domaine ; bon maintien du contexte liste/détail. Limites : moins de largeur pour les tableaux ; nouveau mode de rendu générique des menus/cibles à valider. Aucun menu métier codé en dur ; le panneau n'existe pas implicitement parce qu'il apparaît en maquette.

**Recommandation : A pour la première intégration**, amélioration nette avec le risque de reprise le plus limité. B convient à une évolution validée pour des opérateurs multi-domaines, avec vérification de largeur/tablette et de navigation.

## Principes de conception proposés, à valider pour Admin

- Tableau : texte14–16, intitulés explicites ; densité desktop proposée, lignes48–56 minimum indicatif. Contrôles tactiles48minimum et champs52 conformément à la charte. Colonnes longues lisibles via composition secondaire ou défilement local, pas suppression de données. Le serveur conserve tri/compte/pagination.
- Filtres : bouton nommé Filtres et tri avec nombre actif ; pas de recherche globale inventée. Afficher les critères existants, appliquer/réinitialiser explicitement, ne pas fermer automatiquement pendant le travail. Conserver les filtres relationnels au retour.
- Actions : un primaire par groupe lorsque les métadonnées le déclarent ; lectures secondaires, menu de ligne cohérent avec fiche. Aucune déduction de danger/priorité par UID, rôle ou libellé. Si la sémantique manque, proposer son contrat de présentation avant codage.
- Fiche/formulaire : titres de sections, labels visibles, champs longs multilignes, focus et erreurs associés au champ ; résumé d'erreurs avec liens. Conserver valeurs saisies après échec. Aucun formulaire ni droit d'édition ajouté au choix d'une fiche en lecture.
- Action sensible : ouvrir l'aperçu existant ; afficher effets fournis par le Backend, puis confirmation existante. Conflit → actualiser/revoir ; timeout à résultat inconnu → indiquer l'incertitude et mécanisme contractuel de récupération, jamais renvoyer automatiquement l'écriture. Ne pas promettre une récupération absente du contrat.
- États : chargement avec libellé et aria-busy ; vide authentique « Aucun résultat » plus action autorisée de réinitialisation ; refus/indisponibilité distincts du vide ; erreur lisible avec reprise de lecture ; succès annoncé sans inventer de résultat. Aucun de ces états fictifs n'est présenté comme observé dans les trois captures.
- Statuts : mot explicite, badge neutre par défaut ; symbole/forme si sémantique publiée ; ne pas transformer Confirmée en succès sportif ou financier.
- Clavier : ordre logique, lien d'évitement, menus flèches/Escape, focus visible2px, ouverture/fermeture modale avec focus initial/restauration et fond inerte. Ne pas revendiquer une implémentation existante sans contrôle DOM et test réel.
- Responsive :1440desktop,834tablette,390petit écran. Réorganiser filtres et actions ; cibles48, pas de tabbar adhérent copiée. Liste en défilement local ou résumé de ligne générique à valider, tous les détails restant consultables. Zoom200%, titres longs, focus et clavier virtuel à recetter.

## Après choix seulement

Documenter l'adaptation validée dans un fichier commun Admin référencé depuis cette étude, sans dupliquer DESIGN_SYSTEM_MOVEE. Réutiliser tokens Web et polices locales sous leurs licences ; distribution d'assets contrôlée sans exposer tout codex. Modifier les composants/styles natifs, pas de framework ou bibliothèque supplémentaire. Changement commun (token, icône, sémantique de présentation) : signaler et faire valider explicitement ; modification des métadonnées : plan App séparé.

Recette future : comparer mêmes contenus et viewports Light/Black ; clavier, contraste mesuré, zoom, tablette, petit écran ; menus/filtres/tri/pagination/retour ; refus sous scopes ; état inconnu après timeout ; aucune mutation métier pour une simple vérification graphique. Les maquettes ne prouvent aucun de ces résultats.

## État de livraison de cette étude

Analyse et propositions visuelles uniquement. Aucun code de production modifié ; aucune base/permission/métadonnée changée, aucun service relancé, aucun déploiement. Pas d'ajout dans la charte commune validée. Les captures existantes et planches provisoires sont stockées ici pour coordination interprojets sans dépendre du chat.

## Relecture des planches générées

Les deux planches ont été inspectées. A respecte mieux la hiérarchie lecture/annulation. B dessine encore les lectures Personne/Studio en jaune : elles devront être secondaires conformément au brief et à la charte, même si B est retenue. Les petites icônes, le mot-symbole reproduit par génération, les ponctuations et certaines dates de tableau sont approximatifs : aucune de ces approximations n'est validée. La source originale du logo sera utilisée lors de l'intégration ; aucune icône générée ne sera extraite comme asset. Les quatre lignes montrées sont un extrait des26résultats, pas une nouvelle taille de page. Aucun formulaire sensible, résultat d'annulation, chiffre ou nouveau contrat n'est déduit des images.
