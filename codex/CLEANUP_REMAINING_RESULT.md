# MOVEE — nettoyage complémentaire, résultat

2 novembre2026. Autorisation utilisateur : examiner chaque fichier des sept emplacements demandés et supprimer ceux devenus inutiles. Aucun retrait de données, permission ou code applicatif. Aucun SQL ni opération de service exécuté.

## Résultat par emplacement

| Emplacement | Examinés | Supprimés | Conservés |
| --- | ---: | ---: | ---: |
| `movee-app/docs` | 653 | 240 | 413 |
| `movee-app/codex` | 2 | 0 | 2 |
| `movee-biz/codex` | 2 | 2 | 0 |
| `movee-biz/docs` | 19 | 0 | 19 |
| `movee-biz/migrations` | 29 | 0 | 29 |
| `movee-biz/ASSUMPTIONS.md` | 1 | 1 | 0 |
| `movee-mobile/codex` | 93 | 62 | 31 |

Total :799fichiers examinés individuellement,305supprimés,494conservés ; 56,575,024octets retirés (environ54.0Mio). Le journal JSON contient une ligne par fichier : empreinte initiale, taille, structure/contenu observé, références de code, décision et motif précis. Pas de suppression par date ou extension seule.

## Ce qui a été retiré

- Brouillons remplacés, propositions closes, diagnostics antérieurs corrigés, captures des anciennes transitions et instantanés avant/après non consommés.
- Quatre plans intermédiaires explicitement remplacés/non appliqués : brouillon et pré-scellement Chrome13, premier plan refusé avant DML et candidat recette déclaré superseded. Les diagnostics de refus utiles et le plan effectivement appliqué sont conservés.
- Copie Mobile du brief metadata-driven déjà consolidé au centre et journal de migration encore figé sur les anciennes étapes9/11.
- Suivi DEVELOPMENT_PROGRESS devenu redondant. Les détails d’arrondi utiles ont été repris dans la référence technique Biz.
- ASSUMPTIONS.md : contenu complet transféré dans [les conventions centrales Biz](MOVEE_BIZ_TECHNICAL_REFERENCE.md#conventions-du-moteur-financier-conservees), avec les précisions plus récentes de présentation clairement distinguées des formulations B07/B08 historiques. Renvois Biz actualisés.
- Les deux fichiers Finder .DS_Store, sans utilité projet.

## Pourquoi certains dossiers restent remplis

- **App/docs :** plusieurs JSON, contrats et reçus sont de vraies entrées des Services, tests, validateurs et préparateurs de plans. Ils ne sont pas de simples notes. Les conserver évite de casser la reconnaissance globale, le calcul des plans ou la vérification de leurs sources.
- **App/codex :** les deux fichiers restants sont lus par complete_acceptance_dataset_service.py et admin_studios_plan_service.py. Les retirer exige d’abord une adaptation de code ; aucune modification applicative incluse ici.
- **Biz/docs :** procédures actuelles d’authentification, migrations, CRM, projets, exports, conservation et mise en service ; références des médias publiés et modèles sans secret. Leur détail opérationnel complète le référentiel, sans devenir une seconde source métier.
- **Biz/migrations :** les29fichiers sont la chaîne de schéma versionnée que migrate.py charge et contrôle par checksum. « Déjà appliqué » ne signifie pas « inutile » : ils sont indispensables au contrôle et à une installation neuve. Tous ont été lus, leur instruction et leur objet SQL inventoriés, sans exécution.
- **Mobile/codex :** rapports encore utilisés dans le scellement des sources, états installés récents, contrats consommateurs et demande Bordeaux toujours non appliquée. Ils ne sont pas une autorisation de rejouer les anciens profils.

## Contrôles

- Simulation de l’absence exacte des305fichiers avant suppression :96modules Backend,991tests,aucun échec,3intégrations Redis ignorées. Connexions MariaDB interdites pendant cette simulation ; aucun test d’écriture local.
- Tous les fichiers conservés sont restés identiques pendant le retrait ; les mises à jour documentaires de renvois et de conventions ont précédé ce contrôle et sont identifiées dans l’audit.
- Sources applicatives, SQL, migrations, fixtures et manifestes protégés vérifiés inchangés. Aucun manifeste signé réécrit pour masquer une disparition.
- Liens d’entrée centraux et renvois Biz actualisés ; anciennes citations historiques en texte/JSON préservées comme provenance. Les éventuels liens déjà invalides avant ce lot sont distingués du contrôle après retrait.

Voir [audit individuel et résultat](CLEANUP_REMAINING_RESULT.json), [simulation de retrait](CLEANUP_REMOVAL_SIMULATION_TESTS.json), [transfert des conventions Biz](CLEANUP_BIZ_CONVENTIONS_TRANSFER.json). L’inventaire et les décisions préparatoires sont des états datés ; seul ce résultat indique quels fichiers existent après nettoyage.

Vérification finale : les799décisions correspondent à la présence/absence réelle des fichiers ; empreintes des494fichiers conservés conformes. Le lecteur de migrations Biz reconnaît001–029 et un journal de checksums simulé sans attente, sans connexion DB. Les trois doublons d’audit préparatoire générés pendant ce chantier ont été retirés après intégration complète dans le journal final.
