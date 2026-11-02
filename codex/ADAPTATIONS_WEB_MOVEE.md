# Adaptations Web MOVEE — Biz et Info

Choix utilisateur du 31 octobre 2026 : les deux variantes Biz (1/2) et Info (3/4)
sont retenues, sélectionnables par un bouton Light / Black en haut comme Mobile.
Sources finales : `design-web-2026-10-31/biz-clarte-editoriale-v2.png`,
`biz-immersion-structuree.png`, `info-clarte-editoriale.png` et
`info-immersion-structuree.png`. La correction Biz v2 remplace sa première planche.

Référence commune : DESIGN_SYSTEM_MOVEE.md v1.2, inchangée. Aucune nouvelle
couleur, police, règle métier, bibliothèque d'icônes ou règle commune ajoutée.
L'étude ETUDE_BIZ_INFO.md et ses limites restent applicables aux images générées.

## Présentations retenues

Light : Clarté éditoriale, titres Manrope, fond F4F5F0, surfaces blanches,
texte encre, photo distincte du texte. Black : Immersion structurée, titres Sora,
fond 10131A, surfaces 1B202A, texte F7F8F2. Boutons EFFF4F/encre dans les deux.
Échelle marketing Web : titre 48–56 px desktop, 32–36 px mobile ; lecture16/24.
Conteneur1200px, grille4px, contrôles52px et zones48px minimum. Les valeurs
de tokens sont une extraction de la charte, pas une nouvelle charte.

Mobile Light : texte/CTA puis photo. Mobile Black : photo puis texte/CTA.
Formats Biz en lignes en Light, côte à côte en Black ; entraînements Info
en colonnes en Light, en lignes image/texte en Black. En petit écran, pile unique.
Les images restent des illustrations et conservent leur légende.

## Préférence d'affichage

Bouton natif Light / Black dans le bandeau supérieur, présent sur mobile aussi.
État Black annoncé par aria-pressed. Première visite : système ; choix explicite
mémorisé localement par origine, jamais dans un compte ou cookie d'identité.
En cas de stockage indisponible, le bouton fonctionne en mémoire. La préférence
ne transporte aucune donnée entre Info et Biz ; chaque origine garde son choix.
Changer le thème conserve DOM, saisies, consentement, simulation et position.
Sans JavaScript, Light reste utilisable et la commande inactive est masquée.

## Parcours conservés

One-pagers et ancres, FAQ dernier bloc, FR/EN/ES, CMS en BDD. Hero Biz nomme
l'action « Simuler mon projet » depuis le libellé CMS déjà existant. Info nomme
« Trouver mon studio » et propose le concept en secondaire. Liens circulaires
retirés. Recherche vide avec lien contact, aucun studio ou prix inventé.
Conditions d'accès professionnel, modèle financier, cinq métriques, aides,
consentement et confidentialité complets conservés. Aucun transfert implicite
de simulation ni suppression de garde d'accès.

Le lot concerne les deux sites publics seulement. Mobile et Admin restent
inchangés ; la palette historique de l'administration sera alignée séparément.
Pas de déploiement. L'intégration réutilise Flask/Jinja, CSS et JS natifs.

## Ressources partagées

`movee-web-tokens.css` et `fonts/` sont les sources communes Web. Copies de
distribution identiques dans `movee-biz/movee_biz/public_static/`, nécessaires au
service local des assets sans exposer tout le dossier codex. Manrope/Sora et
licences OFL reprises des fichiers déjà embarqués par Mobile ; aucune requête
de police externe. La recette vérifie l'identité des copies.
