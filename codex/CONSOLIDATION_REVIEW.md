# Consolidation MOVEE — revue préalable conservée

**Nettoyage autorisé puis réalisé :** les15fichiers de la liste ci-dessous ont été supprimés. L’exception Admin est conservée. Voir [résultat du nettoyage](CONSOLIDATION_CLEANUP_RESULT.md). Le reste de ce document conserve la proposition présentée avant l’accord, pas un état courant d’attente.

2 novembre2026. **Consolidation rédigée, aucune suppression effectuée.** Tous les fichiers source inventoriés sont conservés, avec leurs empreintes d’origine. Aucune modification de code applicatif, configuration privée, SQL, permission ou service n’a été effectuée par ce chantier. Les programmes Python utilisés pour composer/vérifier les documents sont temporaires sous /tmp, sans installation dans les projets.

## Documents à relire

Les trois références demandées sont [fonctionnel commun](MOVEE_FUNCTIONAL_REFERENCE.md), [technique commune](MOVEE_TECHNICAL_REFERENCE.md) et [AGENTS commun](AGENTS.md). [README.md](README.md) donne le parcours d’entrée et les liens des six couples spécifiques App, Admin, Mobile, Biz/Info, Pod et MOTION. Admin est le front de movee-app, pas un nouveau dépôt. Aucun projet Studio/BODY autonome n’est inventé.

Le registre Q réseau est intégralement déplacé vers le global ; le détail B reste App, les78T restent Mobile, D/Q/S/F/R restent Biz ; XP/POD-T sortent d’App vers Pod. Motion est scindé entre fonctionnel et technique. Les descriptions moteur réutilisables sont communes aux fronts App ; leur emploi n’est pas imposé à Biz/Pod. Les principes de portée hérités d’un autre projet ne sont pas présentés comme du code MOVEE attesté.

Les décisions ont été conservées par transfert, plutôt que réécrites en une synthèse courte susceptible de perdre des paramètres. Les chronologies techniques datées sont séparées en annexe pour ne pas réintroduire des états obsolètes. Les répétitions exactes ont une destination unique ; l’ancien index dérivé des Q n’est pas recopié, contrairement au registre complet. Les ajouts de mise en contexte et corrections éditoriales sont décrits dans CONSOLIDATION_SOURCES.json.

## Contrôles réalisés

-17sources maîtres et de reprise inventoriées,378sections classées :261transférées,53références de doublons exacts,54sections d’organisation/suivi remplacées explicitement,10sections d’index dérivé retirées de la nouvelle référence. Les originaux ne sont pas retirés.
- Préservation :130Q (contenu complet),34lignes B6.61–71/B7/B8,78T,57D Biz,8Q Biz,10S,11F,12XP,12POD-T ; fragments B1–B5, décisions Biz et modèle financier contrôlés au-delà des identifiants. Les17sections numérotées Motion sont réparties dans le couple central.
- Liens locaux des nouvelles références vérifiés ; chemins relatifs rétablis depuis codex. Les anciennes sources absentes de Biz et BODY ne sont pas reconstituées.
- Empreintes des17sources d’origine vérifiées inchangées. Aucun test applicatif/DB ni redémarrage requis ou exécuté pour cette modification documentaire ; aucun résultat nouveau de production, de matériel ou de conformité légale annoncé.

Voir [validation structurée](CONSOLIDATION_VALIDATION.json) et [provenance/correspondance](CONSOLIDATION_SOURCES.json).

## Points de vigilance traités

| Ancienne formulation | Lecture consolidée |
| --- | --- |
| « Copier AGENTS dans chaque projet » / destination centrale encore à choisir | Décision du2novembre : dossier commun unique, liens depuis les spécificités |
| Pod rangé dans les références App | XP/POD-T deviennent le couple Pod, App conserve son autorité métier |
| Motion assimilé à une machine de bilan | MOTION analyse les exercices ; BODY demeure distinct et non reconstitué |
| Mobile « Séance en cours » ou anciennes versions9/11/12/13 habituelles | T7.8/AR07 : hors entraînement ; reprise14 datée et chaîne historique explicitement séparée |
| Préférences App « tables non installées » | Préparation historique contextualisée par l’application autorisée déjà documentée |
| Biz « pas de code », paramètres publics et budgets anciens | Livraisons B01–B09A/compléments23–31octobre ; changements versionnés et réserves R01/R02 conservés |
| « Les rapports temporaires peuvent être supprimés » | Contrats, artefacts scellés et preuves utilisées par les outils restent des dépendances à conserver |

Aucun nouvel arbitrage métier n’est tranché : seuils matériels, contrats Pod/MOTION, push, voix/offline et réserves fiscales/juridiques gardent leur statut. Les rapports récents servent de points de reprise datés, pas de preuve d’un nouvel audit en base aujourd’hui.

## Suppressions proposées — aucune exécutée

Ces15fichiers sont remplacés pour la reprise documentaire. Une éventuelle suppression doit vérifier à nouveau leurs empreintes et les renvois actifs, après votre validation de cette liste.

| Fichier source proposé à supprimer | Remplacement central |
| --- | --- |
| `movee-app/codex/AGENTS.md` | [AGENTS.md](AGENTS.md) |
| `movee-mobile/codex/AGENTS.md` | [AGENTS.md](AGENTS.md) |
| `movee-biz/codex/AGENTS.md` | [AGENTS.md](AGENTS.md) |
| `movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md` | [MOVEE_APP_FUNCTIONAL_REFERENCE.md](MOVEE_APP_FUNCTIONAL_REFERENCE.md) |
| `movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md` | [MOVEE_APP_TECHNICAL_REFERENCE.md](MOVEE_APP_TECHNICAL_REFERENCE.md) |
| `movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md` | [MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md](MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md) |
| `movee-mobile/codex/MOVEE_MOBILE_TECHNICAL_REFERENCE.md` | [MOVEE_MOBILE_TECHNICAL_REFERENCE.md](MOVEE_MOBILE_TECHNICAL_REFERENCE.md) |
| `movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md` | [MOVEE_BIZ_FUNCTIONAL_REFERENCE.md](MOVEE_BIZ_FUNCTIONAL_REFERENCE.md) |
| `movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md` | [MOVEE_BIZ_TECHNICAL_REFERENCE.md](MOVEE_BIZ_TECHNICAL_REFERENCE.md) |
| `movee-motion/codex/MOVEE_MOTION_REFERENCE.md` | [MOVEE_MOTION_FUNCTIONAL_REFERENCE.md + MOVEE_MOTION_TECHNICAL_REFERENCE.md](MOVEE_MOTION_FUNCTIONAL_REFERENCE.md) |
| `movee-app/codex/METADATA_ENGINE.md` | [MOVEE_TECHNICAL_REFERENCE.md](MOVEE_TECHNICAL_REFERENCE.md) |
| `docs/CONTINUITE_PROJET_MOVEE.md` | [README.md](README.md) |
| `docs/REPRISE_CONVERSATION_BACKEND.md` | [README.md](README.md) |
| `docs/REPRISE_CONVERSATION_MOBILE.md` | [README.md](README.md) |
| `docs/REPRISE_CONVERSATION_BIZ.md` | [README.md](README.md) |

Les quatre prompts/continuité sous docs sont des consignes de transfert du21octobre : anciennes cibles, modes de lancement et états de développement. Le README central les remplace comme entrée ; ils ne doivent pas imposer une visite de chats historiques à chaque reprise. Les décisions durables qu’ils citent restent dans les registres.

## Suppression différée — dépendance réelle

**Conserver provisoirement** `movee-app/codex/MOVEE_ADMIN_SCOPE.md`, bien que son contenu soit intégré à [la référence Admin](MOVEE_ADMIN_FUNCTIONAL_REFERENCE.md). [admin_studios_plan_service.py](../movee-app/services/admin_studios_plan_service.py) lit et hache encore ce chemin. Sa suppression seule casserait la préparation Studios. Il faudra adapter cette dépendance à la référence centrale et tester le préparateur sous un périmètre de code autorisé ; ne pas réécrire les plans historiques signés pour masquer le changement.

Le scan a trouvé35fichiers portant les anciens noms :25documents,9artefacts JSON et1fichier exécutable. [Inventaire des dépendances](CONSOLIDATION_DEPENDENCIES.json). Les9artefacts scellés restent inchangés. Avant le retrait des15fichiers, actualiser les renvois d’entrée encore actifs (notamment la table des instructions du guide ENVIRONNEMENT_DEVELOPPEMENT_MAC.md), distinguer les simples citations historiques et conserver leur provenance. Aucun remplacement global de chaînes dans les contrats ou JSON scellés.

## Documents à conserver dans ce lot

- Les contrats livrés, manifests/migrations SQL, fixtures, plans résolus, reçus et preuves de validation/installations, y compris les anciens états nécessaires aux validateurs ; pas de suppression par date ou par mot « temporaire ».
- `movee-biz/codex/DEVELOPMENT_PROGRESS.md` : suivi daté avec détails de livraison/conventions à conserver pour le moment, sans statut de référentiel canonique.
- Les demandes et rapports de lots dans les dossiers des projets : inventaire/tri distinct si vous souhaitez poursuivre le nettoyage au-delà des référentiels.
- La charte, adaptations Web/Admin, polices/licences et éléments de design déjà dans le dossier commun, inchangés.
- Le guide opérationnel commun dans docs et ses validations : sa localisation n’est pas un doublon des référentiels fonctionnels/techniques.

## Validation attendue

Relire les documents et valider la liste des15suppressions proposées. L’ancienne référence Admin reste hors suppression tant que son appelant n’a pas été adapté et testé. Le chargement automatique de l’AGENTS central n’est pas garanti par son emplacement : le README fournit l’amorçage court, sans modifier les réglages Codex ni créer une copie dans chaque projet.
