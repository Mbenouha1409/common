# Adaptations MOVEE Admin

Choix utilisateur du31octobre2026 : **navigation latérale dans les deux thèmes**, sélecteur **Light / Black dans le menu principal**. Source commune DESIGN_SYSTEM_MOVEE.md v1.2 ; les deux maquettes initiales ne deviennent pas deux modes de navigation. La disposition latérale est retenue, le thème change uniquement les couleurs, la famille de titres et les rayons publiés.

## Implémentation locale

Flask/dashboard existant, JavaScript/CSS natifs. Aucun nouveau framework, transport, permission ou règle métier. Les groupes/feuilles de navigation sont rendus depuis les actions autorisées reçues, avec ActionEngine.menuActions/renderAction/bind. Groupes repliables natifs details/summary ; sélection aria-current et soulignement, pas couleur seule. Les menus flottants de ligne restent inchangés. Designer conserve son montage natif. Aucun thème métier ni destination n'est codé en dur.

Bandeau avec logo original local, langue catalogue et compte ; navigation latérale240px sur ordinateur, repliable à1000px via Menu. Sélecteur d'apparence en bas du menu. Escape ferme la navigation mobile et rend le focus au bouton Menu. Le choix de thème est une préférence locale non sensible `movee.admin.theme`, système au premier usage, choix explicite mémorisé, stockage indisponible → fonctionnement en mémoire. Aucune reconstruction de Page ni appel métier au changement ; filtre, saisie et session conservés.

Les cibles modales existantes sont présentées en feuille latérale sur ordinateur, sans réécriture de leur target ni nouvelle route. Plein écran sur petit écran. Boutons d'action horizontaux avec retour à la ligne ; valeurs longues en lecture multilignes. Les règles de focus historiques des modales restent à auditer, pas une conformité totale revendiquée.

## Ressources et différences de densité

Source Web canonique : movee-web-tokens.css et fonts/ ici. Copies de distribution identiques dans movee-app/dashboard/assets/css, contrôlées par comparaison ; pas de deuxième charte. Logo distribué depuis l'original Mobile/Biz, sans redessin. Corps système et titres Manrope/Sora locaux. Les assets métier/icônes déclarés restent ceux du moteur ; aucune nouvelle bibliothèque.

Adaptation Admin : contrôles compacts desktop36–44px, cibles48px sur petit écran. Ce choix de densité est propre à Admin et ne change pas les règles communes Mobile. Les autres pages/formulaires conservent leurs dimensions natives ; les champs52px, le clavier complet, le zoom200% et toutes les combinaisons de contraste ne sont pas annoncés recettés par ce lot.

## Limites maintenues

Accueil actuel conservé sans KPI ni annuaire inventé en code à partir d'un UID métier. Les priorités et couleurs sémantiques des actions restent déclaratives : pas de classement primaire/danger déduit des libellés. L'annuaire d'accueil et la hiérarchie métier de la planche nécessitent une présentation native contractualisée séparément si la configuration ne la fournit pas. Aucun changement aux limites de reprise des formulaires réseau, aux confirmations ou aux droits. Aucun SQL, redémarrage ou déploiement dans ce lot.

Étude/propositions historiques : design-admin-2026-10-31/ETUDE_ADMIN.md. Ce fichier porte le choix validé et ses adaptations ; DESIGN_SYSTEM_MOVEE.md reste inchangé.

## Vérifications réalisées

Session siège Chrome existante : navigation Accueil→Réservations26résultats, sélection perceptible, fiche Alice en feuille latérale avec valeurs longues visibles et actions horizontales. Light→Black sans rechargement ; Black restauré après reload ; retour Light conserve la liste. Petit écran390×844 : Menu ouvre/ferme la navigation avec sélecteur visible ; viewport restauré. Captures dans design-admin-2026-10-31/recette/. Aucun formulaire soumis. Pas de recette de tous les rôles ni de conformité WCAG exhaustive.

Tous les scripts tests/*_check.js réussis, dont le contrôle ajouté de préférence d'apparence (rechargement, aria-pressed, stockage indisponible) et le contrôle de navigation adapté au rendu latéral natif. Syntaxes JS et git diff --check conformes. Tokens/polices distribués identiques aux sources communes. Aucun test Backend réexécuté ni nouvelle affirmation d'empreintes de base.
