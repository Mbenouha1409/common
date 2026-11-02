# MOVEE Biz — référence technique spécifique

Version de consolidation : 2 novembre 2026. **Référence centralisée validée ; anciennes copies retirées après accord utilisateur.** Lire d’abord [README.md](README.md), [règles communes](AGENTS.md), [fonctionnel global](MOVEE_FUNCTIONAL_REFERENCE.md) et [technique globale](MOVEE_TECHNICAL_REFERENCE.md). Les sections issues des anciennes références conservent leur date/statut ; un constat historique ne décrit pas l’installation actuelle.

## Point de reprise et frontières

Flask/Jinja,db.py et moteur pur, base/auth propres ; ne pas importer le Designer/Repositories App. Le dépôt contient du code, migrations, tests et contrats. Les mentions d’absence de code/DB locale et les versions Python de l’ancienne reprise sont historiques, dépassées par les livraisons B01–B09A et évolutions du23–31octobre. [Suivi consolidé dans la référence technique Biz](MOVEE_BIZ_TECHNICAL_REFERENCE.md), [contrat moteur](../movee-biz/docs/FINANCIAL_ENGINE.md), [projets](../movee-biz/docs/PROJECTS.md), [exploitation](../movee-biz/docs/RELEASE_READINESS.md). Aucun test, accès à la configuration privée, DB ou VPS Biz exécuté dans cette consolidation.

Les compléments identiques des deux anciens référentiels (design, médias, simulateur, tarifs) sont conservés une seule fois dans le fonctionnel Biz. Le moteur, ses conventions, droits, persistance et réserves sont spécifiques ci-dessous ; les statuts de l’ancien inventaire ne sont pas une preuve de l’état présent.

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:1253 -->

## 16. Historique et contrôle de couverture

| Version | Date | Évolution |
| --- | --- | --- |
| 0.1 | 17 octobre 2026 | Initialisation à partir du dépôt et du cadrage accessible |
| 0.2 | 17 octobre 2026 | Interfaces, langues et architecture cible transmises |
| 1.0 candidate | 17 octobre 2026 | Consolidation intégrale S01–S10 et F01–F11 ; réserves et contrôles de couverture |
| 1.1 | 18 octobre 2026 | D01–D57 intégrées ; Q01 encore ouverte à cette version |
| 1.2 | 18 octobre 2026 | Q01–Q08 validées et intégrées, travail/historique distingués, audit V1 et non-régression |
| 1.3 | 18 octobre 2026 | R01/R02 : annexes France et RGPD intégrées, cas conditionnels et matrices de validation ; réserves externes maintenues |

| Section source | Destination dans ce référentiel |
| --- | --- |
| S01 — Périmètre et identité | Bloc S01, contenu conservé ; corrections D explicites si applicables |
| S02 — Quatre interfaces | Bloc S02, contenu conservé ; corrections D explicites si applicables |
| S03 — Autorisations et périmètre | Bloc S03, contenu conservé ; corrections D explicites si applicables |
| S04 — Modèle métier | Bloc S04, contenu conservé ; corrections D explicites si applicables |
| S05 — Calculs, investissements et financement | Bloc S05, contenu conservé ; corrections D explicites si applicables |
| S06 — Données et persistance | Bloc S06, contenu conservé ; corrections D explicites si applicables |
| S07 — Exports, qualité et UX | Bloc S07, contenu conservé ; corrections D explicites si applicables |
| S08 — Critères d'acceptation V1 | Bloc S08, contenu conservé ; corrections D explicites si applicables |
| S09 — Points non figés — décisions d'implémentation documentées | Bloc S09, contenu conservé ; corrections D explicites si applicables |
| S10 — Internationalisation et CMS des deux landing pages — exigence V1 | Bloc S10, contenu conservé ; corrections D explicites si applicables |
| F01 — Principes de calcul | Bloc F01, contenu conservé ; corrections D explicites si applicables |
| F02 — Capacité et scénarios d'un principal | Bloc F02, contenu conservé ; corrections D explicites si applicables |
| F03 — Crédits et revenus clients | Bloc F03, contenu conservé ; corrections D explicites si applicables |
| F04 — Investissement d'un centre | Bloc F04, contenu conservé ; corrections D explicites si applicables |
| F05 — Charges et financement franchisé | Bloc F05, contenu conservé ; corrections D explicites si applicables |
| F06 — Redevances et flux intercentres | Bloc F06, contenu conservé ; corrections D explicites si applicables |
| F07 — Franchisor — revenus, charges, déploiement | Bloc F07, contenu conservé ; corrections D explicites si applicables |
| F08 — Valorisation et indicateurs | Bloc F08, contenu conservé ; corrections D explicites si applicables |
| F09 — Invariants de test et cas de référence | Bloc F09, contenu conservé ; corrections D explicites si applicables |
| F10 — Hypothèses non arrêtées | Bloc F10, contenu conservé ; corrections D explicites si applicables |
| F11 — Présentation multilingue des résultats | Bloc F11, contenu conservé ; corrections D explicites si applicables |

Contrôle V1.0 : 10/10 sections S et 11/11 sections F intégrées. Contrôle V1.1 : 11/11 blocs F conservés textuellement hors indication de provenance du CMS F11, sans changement de chiffres/formules/tableaux ; S01/S02/S03/S05/S07/S10 harmonisés avec les décisions explicites, les autres contenus historiques conservés. Les anciennes versions restent des constats datés, pas des règles supérieures aux arbitrages. Les sections V0.2 sources/statuts, présentation, écosystème, interfaces, fonctions, langues, simulateurs, sécurité, décisions et points ouverts sont reprises aux §§1–15 ; les inconnues résolues par les nouvelles sources sont actualisées et non conservées comme faux blocages. Aucun fichier source historique n’est supprimé.


### 16.1 Tableau de couverture D01–D57

« intégré » signifie présent et harmonisé dans les deux documents, **pas développé ni testé dans une application**. Aucun blocage documentaire ; précisions techniques et juridiques ouvertes au §15.2. Chaque ligne renvoie aussi à son texte complet au §14.1.

| Décision | Statut | Section fonctionnelle | Section technique |
| --- | --- | --- | --- |
| D01 | intégré | §§2.1, 3 | §2 |
| D02 | intégré | §7.1 | §11.1 |
| D03 | intégré | §7.1 | §9.1 |
| D04 | intégré | §7.1 | §9.1 |
| D05 | intégré | §5.1 | §10.1 |
| D06 | intégré | §10.1 | §13 |
| D07 | intégré | §8.1 | §11.1 |
| D08 | intégré | §8.1 | §11.1 |
| D09 | intégré | §8.1 | §11.1 |
| D10 | intégré | §8.1 | §11.1 |
| D11 | intégré | §8.1 | §9.2 |
| D12 | intégré | §7.2 | §9.2 |
| D13 | intégré | §7.2 | §8.2 |
| D14 | intégré | §6 / S02.3 | §10.1 |
| D15 | intégré | §6 / S02.2 | §11.2 |
| D16 | intégré | §6 / S02.2 | §11.2 |
| D17 | intégré | §6 / S02.2 | §11.2 |
| D18 | intégré | §6 / S02.2 | §11.2 |
| D19 | intégré | §6 / S02.2 | §9.2 |
| D20 | intégré | §6 / S02.2 | §8.1 |
| D21 | intégré | §6 / S02.2 | §11.2 |
| D22 | intégré | §6 / S02.2 | §8.1 |
| D23 | intégré | §6 / S02.2 | §9.1 |
| D24 | intégré | §§6 / S02.2, 7.1 | §8.1 |
| D25 | intégré | §6 / S02.2 | §8.1 |
| D26 | intégré | §6 / S02.2 | §11.2 |
| D27 | intégré | §6 / S02.2 | §11.2 |
| D28 | intégré | §6 / S02.2 | §8.1 |
| D29 | intégré | §6 / S02.2 | §8.1 |
| D30 | intégré | §6 / S02.2 | §8.1 |
| D31 | intégré | §6 / S02.3 | §10.1 |
| D32 | intégré | §6 / S02.3 | §10.1 |
| D33 | intégré | §6 / S02.3 | §10.1 |
| D34 | intégré | §6 / S02.3 | §7.1 |
| D35 | intégré | §7.3 | §7.1 |
| D36 | intégré | §7.3 | §7.1 |
| D37 | intégré | §7.3 | §7.1 |
| D38 | intégré | §7.3 | §9.1 |
| D39 | intégré | §7.3 | §7.1 |
| D40 | intégré | §7.3 | §15.1 |
| D41 | intégré | §7.3 | §7.1 |
| D42 | intégré | §7.3 | §8.2 |
| D43 | intégré | §7.3 | §7.1 |
| D44 | intégré | §11.1 | §15.1 |
| D45 | intégré | §11.1 | §15.1 |
| D46 | intégré | §11.1 | §15.1 |
| D47 | intégré | §11.1 | §15.1 |
| D48 | intégré | §11.1 | §15.1 |
| D49 | intégré | §11.1 | §15.1 |
| D50 | intégré | §11.1 | §15.1 |
| D51 | intégré | §11.2 | §10.2 |
| D52 | intégré | §11.2 | §10.2 |
| D53 | intégré | §11.2 | §10.2 |
| D54 | intégré | §11.2 | §10.2 |
| D55 | intégré | §11.2 | §10.2 |
| D56 | intégré | §11.2 | §10.2 |
| D57 | intégré | §11.2 | §10.2 |

### 16.2 Couverture Q01–Q08 et contrôle de non-régression

| Décision | Section fonctionnelle | Section technique | Statut |
| --- | --- | --- | --- |
| Q01 | §7.4 | §§8.3, 9.3 | intégré — spécifié, non implémenté |
| Q02 | §§7.2, 7.4 | §9.3 | intégré — spécifié, non implémenté |
| Q03 | §7.4 | §9.3 | intégré — spécifié, non implémenté |
| Q04 | §7.4 | §§8.3, 9.3 | intégré — spécifié, non implémenté |
| Q05 | §§7.4, 11.3 | §§9.3, 15.2 | intégré — spécifié, non implémenté |
| Q06 | §§7.4, 11.3 | §§9.3, 15.2 | intégré — spécifié, non implémenté |
| Q07 | §7.4 | §9.3 | intégré — spécifié, non implémenté |
| Q08 | §§7.4, 9.2 | §§9.3, 10.3 | intégré — spécifié, non implémenté |

Contrôle V1.2 : textes du registre D01–D57 et ses 57 lignes de couverture inchangés ; 11/11 blocs F conservés textuellement, tableaux/formules/montants inclus. Q01–Q08 intégrées individuellement dans le corps et les registres, anciens points ouverts harmonisés ; aucune modification de calcul financier décidée ici. Seuls les deux référentiels modifiés. L’audit documentaire n’est pas une recette applicative ni un contrôle juridique externe.

### 16.3 Couverture R01/R02 et méthode de conservation V1.3

| Mandat | Section fonctionnelle | Section technique | Statut |
| --- | --- | --- | --- |
| R01 | §§8.2, 17.1–17.6 | §§11.3, 16.3, 19.3 | intégré — spécifié, fiscal/comptable et assiette à valider |
| R02 | §§11.4, 18.1–18.6 | §§15.3, 16.3, 19.3 | intégré — spécifié, juridique/DPO à valider |

Contrôle par comparaison textuelle des blocs avant/après depuis les V1.2 locales : D01–D57 = 57/57, Q01–Q08 = 8/8, F01–F11 = 11/11. Comparer aussi les lignes D/Q des tableaux de couverture et de traçabilité technique ; les formules/chiffres/tableaux financiers sont dans les blocs inchangés. Contrôle d’empreintes des fichiers du dépôt pour limiter les modifications aux deux référentiels ; aucune modification applicative, SQL, configuration, dépendances, test ou infrastructure. Les cas arithmétiques des annexes sont des attentes documentaires, pas une recette d’application.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:389 -->

## 1. Identification, sources et conventions

Sources de la V1.3 : lecture intégrale des référentiels **locaux V1.2**, de [codex/AGENTS.md](AGENTS.md) et de `codex/CODEX_MOVEE_BIZ_ANNEXES_FINANCE_RGPD_V1.md`. Les spécifications/modèle financier séparés restent absents du dépôt ; les blocs historiques intégrés S01–S10/F01–F11 sont utilisés sans remplacement par une copie externe. La précédente instruction D01–D57 séparée n’est plus présente au nouvel inventaire ; son registre intégré est préservé. Aucune décision disparue n’est reconstituée.

Les annexes R01 et R02 sont intégrées au **fonctionnel §§17 et 18**, avec renvois techniques. R01/R02 valident la préparation documentaire : elles ne valent pas approbation fiscale/juridique de leur contenu. Les recherches officielles du 18 octobre 2026 sont datées/liées dans ces annexes, distinctes du cadrage MOVEE ; pas de validation finale déclarée. Les 65 décisions D/Q et les 11 blocs F demeurent intacts.

Sources historiques de la consolidation V1.2 : lecture intégrale des deux référentiels locaux V1.1 et de [codex/AGENTS.md](AGENTS.md), ainsi que de la consigne jointe « MOVEE Biz : consolidation Q01–Q08 et audit des blocages V1 ». Les références historiques du paragraphe suivant décrivent l’intervention V1.1, pas de nouvelles lectures de fichiers absents. Les copies externes ne remplacent pas les référentiels locaux. Q01–Q08 précisent D12/D13 sans supprimer aucune décision : travail courant mutable, historique figé hors suppression explicite Q05/Q06. Aucune autre décision métier ni configuration technique n’est inventée.

Sources de l’intervention V1.1 lues le 18 octobre : [codex/AGENTS.md](AGENTS.md), `codex/CODEX_MOVEE_BIZ_MISE_A_JOUR_REFERENTIELS.md` (57 décisions D01–D57 et Q01), les deux référentiels V1.0 du 17 octobre avant édition. Inventaire du dépôt et état Git contrôlés en lecture seule.

**Sources historiques absentes du dépôt courant :** `codex/MOVEE_BIZ_SPECIFICATIONS.md` et `codex/MOVEE_BIZ_FINANCIAL_MODEL.md`. Leur contenu S01–S10 / F01–F11, intégré en V1.0, reste disponible dans le fonctionnel et sert de base conservatoire ; aucun fichier historique n’est recréé ni prétendu relu séparément aujourd’hui. Le workflow `MOVEE_PROJECTS_CODEX_WORKFLOW.md` n’a pas été retrouvé lors de la consolidation précédente. Aucun sous-dossier codex n’est présent ; les fichiers `.DS_Store` n’ont pas de valeur normative.

Consultations historiques du 17 octobre, pour les conventions seulement : en-têtes/structure des deux référentiels MOVEE App et des deux référentiels MOVEE Mobile dans leurs dépôts respectifs. Aucune règle métier importée, aucun autre projet modifié. Les anciens échanges ChatGPT complets ne sont pas accessibles ; seules les décisions transmises sont utilisées.

**Autorité : D01–D57 prévalent sur toute ancienne formulation contraire.** Les blocs historiques corrigés citent la décision applicable ; leurs chiffres, tableaux et formules restent conservés sauf changement explicitement décidé. Q01–Q08 sont désormais validées : autosauvegarde du travail mutable, création explicite et gestion des historiques (§7.4 du fonctionnel / §9.3 du technique). Les noms de pays, villes et données économiques ne créent aucun chiffre d’affaires automatique.

La séparation fonctionnel/technique, les frontières entre projets, les registres de décisions, la recette et les réserves sur l’implémentation suivent les conventions observées App/Mobile. La numérotation Biz suit la structure commune demandée, sans reproduire leurs organisations historiques à l’identique.


- Projet : **MOVEE Biz**, application Web commerciale indépendante : promotion du réseau, développement de la franchise, candidatures et simulations financières. Aucune gestion opérationnelle des adhérents, séances, coachs, équipements ou programmes sportifs.
- Dépôt local inspecté : dossier `movee-biz`, voisin des dépôts `app` et `movee-mobile`.
- Origine Git vérifiée : `https://github.com/Mbenouha1409/movee-biz.git`.
- Branche locale : `main`.
- HEAD inspecté : `973d2e6b423af3ad3396c28a466e3bb3314d3be3`.
- Historique local : `3687a17` (« Initial commit »), puis `973d2e6` (« chore: initialize Python dependencies »), datés du 15 octobre 2026.
- Caractère privé du dépôt : communiqué par l’utilisateur, non vérifié auprès de GitHub. Aucun accès réseau ou synchronisation Git effectué.

**Décision validée :** application Flask indépendante, sans reprise automatique du framework metadata-driven, du SQL ou des Services de MOVEE App. Toute intégration future doit être spécifiée et validée explicitement.


Les faits V0.1/V0.2 et le constat d’absence de code sont historiques (18octobre), dépassés par les livraisons B01–B09A et suivantes ; ne pas les prendre pour l’inventaire du2novembre. Le fonctionnel consolidé fait autorité pour les valeurs et formules : [référentiel fonctionnel](MOVEE_BIZ_FUNCTIONAL_REFERENCE.md), blocs S/F.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:421 -->

## 2. Principes d’architecture cible

**Validé, spécifié mais non implémenté (D01) :** `Flask / Blueprints → Services Python → db.py (SQL paramétré centralisé) → MariaDB` ; moteur Python pur sans DB, services partagés.

`movee.info` et `movee.biz` = deux pages/sites publics distincts, une seule application/codebase/base, CMS/auth/backend partagés et **routage par hôte**. Info expose concept/grand public, Biz franchise/simulateur public/candidatures/projets pro/admin. Liens de pied de page : Info « Devenir franchisé » vers Biz ; Biz « Voir le site public » vers Info. Aucun composant dupliqué par domaine ni seconde base Info.

Indépendance de MOVEE App/Mobile/Motion/Newapp ; aucun framework metadata-driven, Designer, MCP, API REST ou Repository imposé. Templates Flask, SQL isolé des vues, calculs isolés de SQL. Les noms existants movee-biz/movee_biz peuvent être réutilisés ; ni obligation de renommage ni nouvelle décision de naming déduite. Aucun fichier cible n’est présenté comme existant.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:429 -->

## 3. Technologies et dépendances vérifiées


L’interpréteur `.venv/bin/python` répond et fonctionne comme interpréteur d’environnement virtuel. Version constatée : **Python 3.13.2**.

Les neuf versions déclarées dans `requirements.txt` correspondent aux distributions installées inspectées :

| Distribution | Version déclarée et installée |
| --- | --- |
| blinker | 1.9.0 |
| click | 8.5.0 |
| Flask | 3.1.3 |
| itsdangerous | 2.2.0 |
| Jinja2 | 3.1.6 |
| MarkupSafe | 3.0.4 |
| PyMySQL | 1.2.3 |
| python-dotenv | 1.2.4 |
| Werkzeug | 3.1.9 |

`pip` **26.2.1** est également installé, sans être déclaré dans `requirements.txt`. Ces constats proviennent des métadonnées locales, pas d’une vérification auprès d’un registre de paquets. Aucune installation, mise à jour ou validation d’exécution de Flask n’a été effectuée.


Gunicorn/systemd sont des choix cibles de S01 ; installation non attestée. Aucun outil frontend, graphiques, PDF, Excel ou i18n supplémentaire choisi ou installé ici.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:453 -->

## 4. Organisation réelle du dépôt et fichiers cibles

```text
movee-biz/
├── .DS_Store
├── .env
├── .env.example
├── .git/
├── .gitignore
├── .venv/
├── requirements.txt
└── codex/
    ├── AGENTS.md
    ├── CODEX_MOVEE_BIZ_ANNEXES_FINANCE_RGPD_V1.md
    ├── .DS_Store
    ├── MOVEE_BIZ_FUNCTIONAL_REFERENCE.md
    └── MOVEE_BIZ_TECHNICAL_REFERENCE.md
```

Inventaire récursif hors internes Git/venv : aucun module applicatif, template, statique, migration, test ou fichier de déploiement. README, ASSUMPTIONS.md et db.py sont des fichiers attendus, absents. Aucun sous-dossier codex constaté. Seuls .gitignore et requirements.txt étaient suivis lors de l’initialisation ; .DS_Store, .env.example et codex/ restent non suivis au contrôle courant. .env et .venv sont ignorés. Aucun chemin de Blueprint/Service n’est imposé sans implémentation.


Spécifications et modèle financier séparés absents au 18 octobre ; leurs blocs historiques restent intégrés au fonctionnel. Aucun fichier d’implémentation supplémentaire constaté ; la source annexe R01/R02 est présente et préservée ; l’ancienne instruction D01–D57 séparée est absente, registre intégré conservé.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:477 -->

## 5. Environnements local et production


Environnement observé : poste macOS avec shell zsh, dépôt local et environnement virtuel `.venv` présent. La vérification a invoqué directement `.venv/bin/python` ; elle ne prouve pas que le terminal de l’utilisateur active automatiquement cet environnement.

| Fichier | Rôle et constat |
| --- | --- |
| `requirements.txt` | Neuf distributions avec versions épinglées |
| `.gitignore` | Règles Python et outils ; exclut notamment `.env` et `.venv` |
| `.env` | Configuration locale présente ; vérification filtrée uniquement |
| `.env.example` | Exemple local présent, non suivi avant intervention |
| `.venv/` | Environnement Python local présent et inspecté |

Clés présentes dans `.env` : `FLASK_ENV`, `FLASK_DEBUG`, `SECRET_KEY`, `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`. Le mode déclaré est `development` avec `FLASK_DEBUG=1`. Une clé secrète et un mot de passe sont renseignés ; leur validité et leur robustesse n’ont pas été évaluées et leurs valeurs ne sont pas documentées.

La présence de ces variables ne prouve pas leur chargement : aucun code ne charge `.env` ni ne consomme ces paramètres. Il n’existe pas encore de commande de lancement applicatif vérifiée.


Cible S01 : développement local Mac, production sur VPS existant avec application et service propres. Tester localement les deux fronts sans DNS réel ; routage par hôte validé, configuration concrète à détailler, sans duplication des services.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:497 -->

## 6. Configuration, secrets et MariaDB


### Cadrage communiqué par l’utilisateur

- Base dédiée `movee_biz`, annoncée créée sur le VPS.
- Compte dédié `movee_biz_dev`, annoncé créé dans la synthèse V0.2 ; seul ce nom technique explicitement transmis est documenté, sans secret associé.
- Droits `ALL PRIVILEGES` sur `movee_biz.*`, annoncés comme vérifiés dans le cadrage V0.2 transmis.
- Connexion locale prévue via un tunnel SSH, port local `3307`.
- Connexion Python à MariaDB pas encore validée par un test applicatif.

La création de la base et du compte ainsi que la vérification des droits sont rapportées par la source V0.2. Aucun résultat SQL ni contrôle direct du VPS n’a été obtenu dans cette intervention ; cette provenance est distincte d’une vérification locale par Codex.

### Faits locaux vérifiés

- `.env` indique une connexion à la boucle locale IPv4, port `3307`, base `movee_biz`.
- Le compte configuré localement correspond à celui communiqué par l’utilisateur, sans restitution de l’identifiant.
- `PyMySQL` et `python-dotenv` sont installés.
- Aucun code de connexion, test applicatif, schéma ou migration n’est présent.

### Écart de configuration

`.env.example` indique le port `3306` et un compte différent de celui du cadrage et de `.env`. Il utilise des valeurs de remplacement pour les secrets. Le nom de base correspond au cadrage.

Cet exemple n’est donc pas aligné avec la connexion locale prévue par tunnel. Il n’a pas été modifié dans cette intervention documentaire. Son alignement est un point à traiter lors d’une intervention autorisée sur la configuration.

### Non vérifié

Aucun tunnel n’a été ouvert ou testé ; aucun accès MariaDB, requête SQL ou test réseau n’a été lancé. La destination SSH, le transfert distant, l’authentification SSH, l’état du service, la version MariaDB, la base physique et les privilèges effectifs ne sont pas contrôlés directement par Codex ici, malgré la vérification des droits rapportée dans le cadrage V0.2. Aucune commande de tunnel complète ne peut être consignée sans ses paramètres validés.


Secrets hors Git ; SMTP configurable et backend de test local à prévoir. Aucun secret, mot de passe ou empreinte n’est intégré. Les paramètres effectifs de production restent à vérifier, sans ouvrir de connexion ici.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:530 -->

## 7. Backend Flask et services

Routes et Blueprints pour grand public, franchise, membre et administration ; découpage concret à préciser. Services pour approbation et notifications, CRM, centres/publication, projets/snapshots, CMS, simulation et exports. Ces responsabilités sont cibles, pas des classes ou endpoints existants. Admin centralise/affecte les demandes publiques ; relances datées sans emails automatiques V1. Toute écriture multi-entités doit être transactionnelle.

### 7.1 Candidatures, fil partagé et notifications — D34–D43

Refus historisé date/auteur/motif obligatoire interne, notification sans exposition automatique du motif. Compléments, réponses et initiation des deux côtés avant/après approbation dans un fil chronologique unique par candidat, partagé entre admins autorisés, auteur individuel conservé. Aucune pièce jointe/upload en V1 ; documents éventuels par email hors application.

Messages immuables après envoi, correction par nouveau message et exception de purge légale. Premier nouveau message non lu → email, suivants regroupés jusqu’à consultation puis nouveau cycle ; empêcher doublons dans administration partagée. Détail du suivi de consultation/réinitialisation multi-admin à préciser, sans inventer de comportement métier. Aucun badge/notification in-app/compteur/alerte visuelle de messagerie ; ce suivi peut rester interne.

Notifications localisées avec lien sécurisé et authentification avant conversation. Réponse exclusivement dans Biz, aucune ingestion de réponse email. La messagerie accessible aux non-approuvés n’ouvre jamais les services professionnels et reste suspendue lors d’une demande de suppression. Relances commerciales sans email automatique V1 distinctes de ces notifications transactionnelles.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:542 -->

## 8. Frontend Web

Flask + templates communs aux langues, responsive et formulaires accessibles ; tableaux lisibles sur mobile, HT/TTC visibles, validation et erreurs explicites. Graphiques utiles pour projections et scénarios, bibliothèques à arbitrer. Contenus éditoriaux MariaDB, jamais en dur ; libellés système dans catalogues i18n. Aucune traduction fictive comme contenu validé ni centre fictif en production.

### 8.1 Simulateur public — D20, D22–D25, D28–D30

Entrées finales : sélection d’un format actif administrable (pas de saisie libre machines), ville facultative et loyer estimé modifiable. Aucun apport ni satellite ; l’ancien choix public coach n’est plus une entrée validée. Défauts nationaux ou références locales de coûts ; aucun effet sur fréquentation/CA. Recalcul dès changement sans bouton « Calculer » ni rechargement, en évitant appels inutiles ; aucun contrat d’API ou bibliothèque de requêtes imposé.

Une page responsive, deux colonnes desktop, paramètres puis résultats mobile. CTA « Obtenir mon business plan complet » vers inscription/connexion et approbation, pas de téléchargement immédiat, pas de transfert de simulation. Le renvoi intermédiaire D20 à D27 est corrigé vers D25 pour l’apport ; D27 concerne le CA HT.

### 8.2 Comparaisons et messagerie — D13, D42

Comparaison côte à côte de versions d’un projet ou projets distincts, tableaux/graphiques/hypothèses/résultats 36 mois et trois scénarios, sans mutation des versions. Messagerie manuellement consultable sans badge, compteur non lu, alerte visuelle ni notification in-app ; emails seulement. Le signalement des purges D45 reste une exigence admin distincte.

### 8.3 Interface professionnelle de travail et historiques — Q01–Q08

Autosauvegarde après bref debounce sur travail mutable, sans bouton Enregistrer ; états i18n « Enregistrement… », « Enregistré », « Erreur de sauvegarde », confirmation de succès uniquement après persistance. Avertir avant sortie avec changements non persistés ; après expiration de session préserver les sauvegardes existantes, ne pas promettre récupération de données jamais enregistrées.

Action « Créer une version », liste numéro séquentiel/date/libellé facultatif ; historique non éditable mais supprimable explicitement selon Q05. Restaurer copie ses paramètres vers travail et garde origine, confirmation avant écrasement ; suite des modifications autosauvegardée. Confirmer suppression d’historique/projet, actualiser comparaisons affectées, ne pas modifier les exports déjà produits.

Dupliquer = nouveau projet depuis travail courant, sans historique source. À quota configuré atteint, bloquer création/duplication en expliquant le refus, garder lecture/modification de l’existant ; aucun défaut quota ou archive inventé. Respect de D05 : aucune UI d’édition/restauration/suppression sur original membre par admin. Les états de sauvegarde ne sont pas des badges de messagerie interdits D42.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:564 -->

## 9. Modèle de données et persistance cible

Créer un **schéma MariaDB propre à MOVEE BIZ**, sans réutiliser ni modifier les tables Newapp. Codex doit concevoir des migrations explicites et un schéma minimal couvrant comptes/approbations, candidatures, pipeline/historique/relances, demandes d'information, centres/territoires et rattachements, projets de simulation et snapshots d'hypothèses, versions des paramètres réseau, éventuellement audit et tokens de réinitialisation. **Ne pas créer de tables de gestion opérationnelle des abonnements, crédits, séances ou dossiers clients** : elles appartiennent à MOVEE App. Aucun centre fictif en production. Index/contraintes FK/unique nécessaires, transactions sur écritures multi-tables. Ne pas créer une table par calcul financier dérivé si le calcul peut être reproduit depuis les hypothèses enregistrées.


CMS : structure normalisée par clé stable, langue et site/page, unicité appropriée, publication/repli ; ajout de langues sans changement de schéma. Historiser au minimum auteur/date d’édition. Stocker hypothèses et versions/snapshots reproductibles ; ne pas matérialiser chaque calcul dérivé. Noms physiques, colonnes et migrations à concevoir dans une intervention ultérieure : aucun schéma ni SQL créé ici.

### 9.1 Référentiels internes et dossier — D03–D04, D23, D38

Pays/commune identifient une série de références économiques saisie manuellement admin ; origine/date si disponibles, sinon estimation interne/défaut national. Aucune granularité quartier/zone/code postal ; recherche de centres par code postal distincte du référentiel économique. Formats publics : ajout, modification, activation/désactivation, ordre et défaut admin ; aucune liste figée. Fil textuel unique par candidat, auteurs et historique de décisions, sans upload. Schéma physique non défini.

### 9.2 Snapshots, versions et FX — D11–D12, D19

Conserver par version de projet hypothèses centrales/locales/fiscales/commerciales et taux exact de change utilisé pour simulation/consolidation, avec date/historique FX manuels admin. Aucun changement rétroactif automatique ; actualisation demandée = nouvelle version, précédentes intactes. Comparaisons sans écriture sur les historiques ; références actualisées après suppression explicite Q05/Q06. **Q01–Q08 validées** : autosauvegarde du travail courant mutable, historiques explicites figés hors suppressions confirmées ; voir §9.3. Aucune persistance anonyme publique, ni rattachement/transfert/récupération après approbation.

Besoins additionnels : vérification email, refus/réexamen, demande de suppression datée/statutée et échéances, exceptions légales, appareils de confiance/révocations/sessions, suivi de consultation pour regroupement des notifications. Aucun nom de table, stockage token, job ou migration créé dans cette mission.

### 9.3 Persistance des projets et invariants — Q01–Q08

- **Q01 :** persistance après debounce du travail courant mutable uniquement ; réussite effectivement confirmée, erreurs visibles, données déjà enregistrées conservées après expiration de session. Délai exact, ordre des écritures, reprise sur erreur/concurrence à préciser techniquement sans inventer une garantie de récupération non persistée.
- **Q02 :** création volontaire « Créer une version » et actualisation volontaire des hypothèses centrales = historique figé traçable. Autosauvegarde ne crée pas d’historique à chaque modification ; aucun changement central rétroactif automatique.
- **Q03 :** séquence automatique propre au projet, date de création, libellé facultatif ; numéro attribué non réutilisable même après suppression. Protéger unicité/stabilité sous concurrence, sans imposer d’objet SQL physique.
- **Q04 :** restauration par copie d’un historique vers travail après confirmation, origine conservée, historiques intacts ; aucune mutation de l’original choisi et modifications suivantes par Q01.
- **Q05 :** suppression d’un historique par propriétaire après confirmation et contrôle légal, sans modifier travail/autres historiques ; actualiser références de comparaison sans réécrire PDF/Excel déjà exportés ; aucun stockage d’exports serveur supposé.
- **Q06 :** suppression confirmée du projet incluant travail/historiques par propriétaire sous obligations légales ; copies admin indépendantes gérées séparément au regard RGPD, aucune propagation silencieuse, audit minimal non indûment identifiant.
- **Q07 :** nouvel identifiant projet et copie des paramètres/configurations/hypothèses du travail courant, aucun historique source copié, source intacte ; historique propre au nouveau projet.
- **Q08 :** maximum de projets actifs configuré/modifiable admin par candidat approuvé/franchisé ; vérifier quota sur création/duplication, exclure supprimés, laisser lecture/édition de l’existant. Protéger contre création concurrente dépassant le plafond. Valeur non configurée : gestion/diagnostic technique à préciser, aucun défaut, illimité, refus systématique ou archivage adopté tacitement.

Les besoins de travail, historique, séquence, restauration et quota sont des invariants cibles, pas un schéma définitif. Garantir cohérence des écritures multi-entités et refus sans mutation partielle ; algorithmes de conflit/reprise/idempotence à définir dans l’implémentation. Ne pas recréer un historique ou projet supprimé via une requête d’autosauvegarde tardive. Les comparaisons n’altèrent jamais leurs sources. Des historiques immuables peuvent être supprimés explicitement : l’immutabilité n’autorise ni édition interne ni contournement des obligations d’effacement.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:594 -->

## 10. Authentification et autorisations

Deux rôles member/admin, approbation distincte du pipeline commercial. Contrôle serveur rôle/statut/propriété ; paramètres réseau/pays réservés admin et hypothèses locales modifiables par propriétaire approuvé. Auth indépendante de Newapp ; mots de passe hachés robustement (Werkzeug/Argon2 si dépendance) et reset par token expirant restent acquis.

### 10.1 Inscription, approbation et projets — D05, D14, D31–D33

Cinq champs obligatoires nom/prénom/email/téléphone/mot de passe ; ville et statut coach différés, aucun apport à l’inscription. Vérification email obligatoire via lien sécurisé temporaire et renvoi possible ; aucun examen ni approbation avant vérification. Accès pro/projets/exports seulement après approbation manuelle. Compte refusé conservé sans accès pro, réexamen/réouverture puis approbation possibles sans recréation, historique conservé. Le cycle de messagerie candidat reste accessible avant approbation sous réserve de suspension/suppression.

Admin : lecture seule sur tout original membre, clonage dans son espace d’analyse et modification de sa copie uniquement. Le membre gère ses propres projets et versions ; contrôle serveur nécessaire, jamais simple restriction UI.

### 10.2 Second facteur, confiance et sessions — D51–D57

Admin doit satisfaire le second facteur requis, candidats/franchisés sans 2FA obligatoire. Après mot de passe, code à usage unique à l’email admin vérifié, valide **5 minutes** ; remplacement invalide ancien code, tentatives et renvois limités (seuils à détailler). Aucun TOTP imposé. Documenter dépendance à la sécurité de la boîte email et scénarios de sécurité/récupération sans les inventer ici.

Après 2FA, navigateur de confiance facultatif **30 jours** : jeton sécurisé spécifique au navigateur, jamais IP seule. Mot de passe requis aux connexions suivantes, nouveau code dispensé seulement si confiance valide et sans événement de sécurité. Déconnexion ne révoque pas la confiance. Inventaire type/navigateur, dates autorisation/dernière utilisation/expiration ; révocation individuelle ou globale effective côté serveur, 2FA à prochaine connexion révoquée.

Expiration serveur après activité réelle : admin **30 minutes**, candidat/franchisé **2 heures**, déconnexion/réauthentification. Polling ne renouvelle pas l’activité ; confiance navigateur ne prolonge pas une session. Algorithmes, stockage jetons/codes, événements de sécurité et mécanismes serveur à détailler, aucun code ou schéma imposé.

### 10.3 Propriété, confirmations et quotas — Q01–Q08

Contrôler serveur identité/propriété/approbation/session sur autosauvegarde, création d’historique, restauration, suppression, duplication ; CSRF et validation des entrées selon §15. Admin ne modifie jamais un original membre (D05), même par autosauvegarde/restauration/suppression de projet ; il ne travaille que sur sa copie séparée. Purges légales distinctes selon D44–D50.

Quota configurable admin n’accorde aucun droit d’écriture sur les projets membres ; contrôle sur création/duplication avec invariants §9.3. Refus de droit, quota atteint, erreur ou expiration n’est jamais un succès ni une suppression des sauvegardes acquises. Confirmation explicite pour restauration écrasant travail et suppressions ; garde serveur des obligations légales. Sous D56/D57, les requêtes de fond/polling/autosauvegarde seules ne doivent pas prolonger artificiellement la session : seule activité réelle utilisateur est considérée.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:618 -->

## 11. Services et moteur financier commun

Bibliothèque Python pure, déterministe, sans DB ; calculs pour simulation publique simplifiée, franchisé et franchiseur. Entrées cibles NetworkAssumptions, ProjectAssumptions, scénario et ouvertures. Pipeline : capacités → fréquentation → crédits → ventes → revenus HT → charges → résultat/IS → amortissements → prêts → cash/TVA → indicateurs. Sorties 36 lignes mensuelles par centre et consolidé, sources et avertissements. Les règles exactes sont intégralement dans le fonctionnel F01–F10 et S04–S05, sans modèle financier alternatif dans ce document. Même résultat numérique pour écran/graphiques/Excel/PDF et FR/EN/ES. Snapshots réseau par projet, calendrier propre à chaque centre, aucun CA/royalty avant ouverture. Les conventions non fixées seront documentées dans ASSUMPTIONS.md et testées, sans validation commerciale implicite.

### 11.1 Internationalisation économique et coûts locaux — D02, D07–D10

Moteur commun avec règles/paramètres par pays : devise, TVA/taxes, fiscalité, charges sociales, financement et conditions commerciales. **France seule active V1**, activation contrôlée ; admin peut préparer pays futurs sans les activer ni inventer de fiscalité. Conditions commerciales versionnées par pays et snapshotées, valeurs françaises historiques exactement conservées comme références initiales non universelles.

Pays/ville ne préremplissent que coûts/contexte économique modifiables et snapshotés. Repli national sans données locales ; jamais occupation, fréquentation, clients ou CA automatiques par ville. Simulations locales dans devise pays, consolidation réseau/franchiseur EUR, aucune conversion France. Taux manuels et snapshots au §9.2 ; langue et pays sont indépendants.

### 11.2 Projection publique restreinte — D15–D18, D21, D26–D27

Même moteur que le professionnel mais scénario réaliste seul et principal uniquement ; restituer uniquement investissement estimé HT et TTC distincts, CA mensuel HT à maturité et annuel HT à maturité (12 mois en rythme de croisière, pas année 1). Taxes appropriées par poste d’investissement, aucun taux unique présumé ; TTC décaissement indicatif sans présumer récupération TVA.

Aucune métrique publique de charges/marge/EBITDA/rentabilité/trésorerie/financement/seuil ni projection 36 mois, aucun CA TTC ni scénarios prudent/optimiste. Limiter la sortie publique exposée, pas uniquement masquer visuellement les métriques privées. Le moteur interne conserve projections 36 mois pour les usages autorisés ; public sans persistance ni transfert.

### 11.3 R01 — Fiche France : responsabilités et recette cible

La [fiche France du fonctionnel §17](MOVEE_BIZ_FUNCTIONAL_REFERENCE.md#17-annexe-r01--fiche-financière-france-et-recette-conditionnelle) est l’annexe maître des flux FL01–FL15, hypothèses, formules et cas FR-T01–FR-T12. Son statut est documentaire ; aucun code, schéma ni modèle fiscal validé n’est déduit de sa présence.

Conserver dans les hypothèses/snapshots les qualifications/taux effectivement retenus, événements de reconnaissance/exigibilité/paiement, conditions de déduction, régime/éligibilité, assiette de royalties et périmètre d’agrégation. Valeur incertaine = hypothèse signalée, pas taux zéro/20 % implicite ni crédit TVA remboursé automatiquement. Définir les représentations dans une intervention ultérieure, sans nom de colonne/table imposé ici.

Services et moteur commun distinguent : ventes/consommation, TVA/cash, capital/intérêts, amortissement/réserve, entité d’origine/exécutante et franchisé tiers. Trois vues : entités, agrégat économique réseau après éliminations explicites, franchiseur. Aucun réseau indépendant supposé groupe comptablement consolidé. Les 8/12 € de clearing restent provisoires, les options d’assiette du §17.3 non adoptées. Mêmes hypothèses, mêmes chiffres écran/graphiques/exports/langues selon droits ; le public ne reçoit que D16–D27. Aucune actualisation rétroactive de snapshots ni de fiscalité étrangère en V1.

Matrice de validation §17.6 à utiliser en recette : un cas conditionnel réussi arithmétiquement ne vaut pas accord expert sur sa qualification. B01 demeure la validation externe nécessaire aux chiffres concernés. Les conventions ordinaires autorisées S09/F10 restent distinctes d’un arbitrage commercial.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:644 -->

## 12. API et intégrations

Aucune API REST obligatoire ni contrat endpoint établi ; routes Flask + templates suffisants au cadrage. Aucun lien DB/auth avec MOVEE App, aucun MCP. SMTP configurable pour notifications et réinitialisation ; transport concret à préciser. Recherche de centres ville/code postal conservée ; référentiel économique interne manuel par pays/commune (D02–D04), aucune API INSEE, géocodage ou fournisseur externe obligatoire. Taux FX manuels sans API obligatoire (D11) ; aucun service tiers payant requis. Toute future intégration interprojets exige spécification et validation explicites.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:648 -->

## 13. Internationalisation technique et CMS

D06 : FR/EN/ES intégral dès V1 sur les deux sites, compte, candidatures, messagerie, professionnel, administration/CRM, franchiseur, emails, erreurs et PDF/Excel. Langue interface distincte du pays financier ; France seule active V1 (D08), aucune activation pays déduite d’une langue. CMS MariaDB pour titres, paragraphes, CTA, FAQ, sections, SEO et alternatives médias ; catalogues versionnés pour formulaires, erreurs, auth, simulateurs et exports. Éditeur admin avec aperçu, validation, publication et protection des traductions manquantes ; pas de traduction automatique obligatoire. Langue navigateur initiale, choix manuel prioritaire persisté, repli français. URLs indexables cohérentes par langue (exemples /fr/, /en/, /es/, pas routes existantes), hreflang, canonical, sitemap et SEO localisés. Recherche/formulaires indépendants de la langue, langue des demandes enregistrée si utile. Métriques/calculs indépendants des libellés et formats ; langage ne modifie jamais hypothèses/résultats. Bibliothèque i18n et organisation physique à préciser.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:652 -->

## 14. Exports et génération de documents

Excel : hypothèses, CAPEX, financement, compte de résultat mensuel 36 mois, cash-flow, indicateurs, scénarios et tableaux synthétiques; feuilles avec formules ou valeurs traçables et unités. PDF : business plan clair (~10 pages cible, longueur adaptée aux données), contexte, hypothèses, rentabilité, trésorerie, risques et avertissements. Chaque export mentionne scénario, date, version des paramètres et distinction prévision/non garantie.


Excel/PDF consomment les mêmes résultats que l’écran. Identifier scénario, date, version du projet et version des hypothèses/paramètres ; distinguer prévisions et garanties. Libellés, avertissements, nombres, devises et dates localisés. Bibliothèques et précision/arrondis techniques à préciser sans modifier les valeurs sources. Aucun fichier export généré dans cette intervention.

D12 : versions/hypothèses et taux FX utilisés figés, exports historiques reproductibles sans actualisation rétroactive automatique ; D06 : Excel/PDF entièrement localisés, calculs numériques invariants. Aucun export professionnel avant approbation (D14) ; CTA public sans téléchargement immédiat (D30).

Q02/Q03/Q05 : identifier le projet/la version et les hypothèses de l’export, sans modifier les fichiers déjà exportés après suppression d’un historique ou projet. Aucune conservation automatique des PDF/Excel côté serveur n’est spécifiée ; ne pas en déduire un archivage. L’obligation de reproductibilité porte sur les historiques conservés, sous réserve des suppressions explicites et obligations légales.

Annexes R01/R02 : exports doivent porter les hypothèses/versions et avertissements financiers applicables, sans annoncer une fiscalité certaine si conditionnelle. Q05/Q06 gardent les fichiers déjà remis inchangés ; les copies de documents réellement détenues par MOVEE restent à inventorier pour l’effacement légal (fonctionnel G08), sans ajouter une conservation serveur. Pas de données personnelles indues dans un export de diagnostic/recette.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:665 -->

## 15. Sécurité technique

CSRF ; cookies sécurisés HttpOnly/SameSite ; limitation des tentatives ; validation des entrées ; contrôle rôle/statut/propriété ; SQL paramétré et transactions ; échappement HTML et contrôle des contenus riches CMS ; secrets hors Git ; journal des actions sensibles sans données personnelles dans les logs. RGPD : consentement, politique et cycle de suppression validé D44–D50 ci-dessous, bases légales/délais à contrôler avant implémentation. SMTP local de test ; isolation de l’auth et DB des autres projets. Les exigences ne sont pas des protections déjà implémentées.

### 15.1 Conservation, purge et demande de suppression — D40, D44–D50

Candidatures non abouties : référence 2 ans depuis dernier contact significatif, couvrant données dossier/coordonnées/messages ; vérifier base légale/délai effectif, ne pas universaliser, politique actifs distincte. Détection/signalement automatique des échéances, revue des exceptions puis validation manuelle admin ; aucune rétention indéfinie sans justification. Suppression des données personnelles, candidature et messages après validation sauf obligations légales documentées ; trace minimale non identifiante. Purge légale autorisée malgré immutabilité fonctionnelle des messages.

Demande « Supprimer mon compte » confirmée, datée/statutée, contrôle légal, traitement et notification, indépendante des 2 ans. Invalider immédiatement les sessions et suspendre simulateur/projets/messagerie pendant traitement. Contact externe MOVEE, vérification d’identité puis annulation/réactivation par admin possible avant exécution seulement ; après effacement aucune restauration.

Suivre réponse en principe sous un mois ; extension jusqu’à deux mois supplémentaires seulement dans cas légalement prévus avec information dans le premier mois, traitement anticipé permis. Aucun SLA interne 7 jours ni attente obligatoire d’un mois. Jobs, stockage, modalités de signalement, contact significatif, exceptions et contrôle légal à détailler ; aucun SQL ou comportement de purge supplémentaire créé ici.

### 15.2 Suppressions des projets et historiques — Q04–Q06

Confirmation avant écrasement du travail par restauration, confirmation explicite du propriétaire avant suppression d’historique/projet, contrôle légal et audit minimal. Mettre à jour comparaisons sans altérer exports existants ni versions restantes ; copie admin indépendante jamais modifiée silencieusement, gestion RGPD séparée. Aucune rétention de données personnelles supplémentaire ni mécanisme d’archivage d’exports serveur déduit. Les purges légales et suspension de compte D44–D50 gardent leur portée ; Q05/Q06 n’accordent pas à l’admin une édition d’original membre.

### 15.3 R02 — Exécution cible de la conservation et de l’effacement

La [politique RGPD du fonctionnel §18](MOVEE_BIZ_FUNCTIONAL_REFERENCE.md#18-annexe-r02--politique-rgpd-et-conservation-par-catégorie) est l’annexe maître G01–G16 ; bases et durées non validées juridiquement ne sont pas traitées comme des valeurs par défaut légales. Formaliser RT/habilitations et prestataires selon politique approuvée, pas créer de schéma physique ici.

La mise en œuvre devra pouvoir distinguer suspension/visibilité/effacement actif/copies résiduelles/exception justifiée. Détection et revue admin avant purge D45 ; D47 déclenche suspension immédiate D48, instruction légale et suivi D50. Originaux, copies admin, exports réellement détenus, messagerie/SMTP, logs et sauvegardes sont évalués dans leur périmètre ; pas de propagation silencieuse d’une suppression Q06 vers une copie indépendante, ni de conservation perpétuelle par clonage.

Prévoir contrôle des échecs partiels, résultat exact et trace minimale sans dossier personnel recopié. Limitation pour litige/obligation ciblée, accès restreint, revue et fin identifiées. Un changement d’UI/statut ne prouve pas effacement ; pseudonyme réidentifiable reste à traiter comme donnée personnelle. Cycle des backups et purge résiduelle à faire valider avant ouverture ; après restauration d’exploitation, réappliquer effacements avant exposition, jamais réactiver un dossier effacé D49. Aucun délai universel ajouté pour logs/actifs/archives.

Ces exigences documentent R02 et les décisions existantes ; mécanismes de stockage, tâches et preuves à concevoir ultérieurement. B02 reste ouvert à validation juridique/DPO et à recette technique réelle, sans réouverture de Q01–Q08 ni des privilèges D05.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:691 -->

## 16. Tests et critères de validation

Cible : tests unitaires moteur, invariants et cas de référence F09, intégration DB/auth/permissions, migrations, navigation deux hôtes, exports et CI. Vérifier les 10 critères S08 ; chiffres exacts de F09 dans le fonctionnel, pas arrondis substitutifs. Couvrir expirations/crédits, absence de double compte, TVA/IS/capital/amortissements, courbes relatives aux ouvertures, allocation et sensibilités. Tester droits CMS, XSS, changement de langue/fallback, cohérence des domaines et montants FR/EN/ES identiques. README, exemple env, migrations et commandes de test doivent rendre le démarrage reproductible. Aucun de ces tests applicatifs n’a été exécuté : code absent. Contrôle documentaire effectué : couverture des 21 sections sources, texte des formules/tableaux et fichiers hors périmètre.

### 16.1 Recette à prévoir des 57 arbitrages

Chaque D01–D57 fait l’objet d’une traduction technique individuelle au §19.1 et d’une couverture croisée au fonctionnel §16.1. Vérifier restrictions publiques dans la sortie exposée, absence de persistance/transfert, recalcul sans reload, formats administrables et isolation des coûts/CA ; France seule active, snapshots/FX/version/export et comparaisons non destructives.

Vérifier cinq champs, email avant examen/approbation, refus interne révisable, lecture seule admin des originaux ; fil unique partagé, aucun upload/édition/badge, regroupement email sans doublons et réponse uniquement dans l’application. Vérifier purge légale malgré immutabilité, suspension immédiate, annulation avant effacement, délais suivis. Vérifier code 5 min usage unique/remplacement/limites, confiance 30 jours révocable, logout distinct de révocation, inactivité serveur 30 min/2 h sans polling. Vérifier FR/EN/ES pour tout et invariance numérique. Aucun test applicatif, fichier de test ou code n’est écrit/exécuté dans cette mission documentaire.

### 16.2 Recette cible Q01–Q08

Tester autosauvegarde debounce/états exacts/erreur/avertissement de sortie/session expirée sans perte persistée, jamais d’historique à chaque changement. Tester création explicite et actualisation centrale traçable, séquence jamais réutilisée, restauration par copie avec confirmation et origine, suppression confirmée limitée aux objets visés et comparaisons cohérentes, exports déjà produits inchangés. Tester duplication indépendant sans historique et source intacte ; quota configuré sur créations/duplications y compris concurrentes, supprimés exclus, lecture/édition conservées.

Tester refus d’accès admin à toute mutation d’original membre, CSRF, erreurs sans écriture partielle et absence de recréation par autosauvegarde tardive après suppression ; traiter quotas non configurés sans inventer de politique. Ces tests sont à écrire/exécuter lors du développement autorisé ; aucun fichier de test ou code créé dans cette mission. Audit des deux seuls blocages V1 et des éléments non bloquants au fonctionnel §15.3–§15.4.

### 16.3 R01/R02 — Recette future des annexes

- R01 : FR-T01–FR-T12 au fonctionnel §17.5 ; reprendre toutes entrées, hypothèses conditionnelles, formules et valeurs attendues, pas convertir un scénario en règle fiscale. Contrôler T02/T03 acomptes et TVA, T05/T06 assiette/clearing/éliminations, T07 capital/intérêts/amortissement et T11 vue franchiseur sans revenu de marge doublé. T12 étend invariants de langue/ville/snapshots/pays.
- R02 : RG-T01–RG-T09 au fonctionnel §18.6 ; données synthétiques seulement, échéance2 ans conditionnelle, revue admin, suspension, annulation avant exécution, messages effaçables légalement, effets Q05/Q06 et copie admin indépendante, exports réellement détenus, absence de résurrection par backup.
- Recette des déclarations : distinguer « arithmétique vérifiée », « implémenté/testé » et « qualification validée par expert ». Pas d’accord expert revendiqué par un test de calcul ni par une recherche web.
- Non-régression documentaire : comparer séparément les textes de 57 D, 8 Q, 11 F et les lignes de couverture avant/après ; contrôler liens/sections et empreintes hors périmètre. Aucun fichier de test applicatif écrit/exécuté ici.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:714 -->

## 17. Déploiement et exploitation

Cible : VPS existant, service Gunicorn/systemd et configuration dédiés, indépendants de Newapp.


Seule l’existence d’un VPS hébergeant la base dédiée est communiquée. Le système du serveur, ses versions, le chemin de déploiement, la configuration effective des domaines, TLS, le serveur HTTP, le serveur WSGI, les services, la configuration de production, la sauvegarde et les procédures de déploiement ne sont pas documentés dans les sources accessibles.

Aucun choix sur ces éléments n’est déduit des dépendances Flask. Aucun fichier ou état serveur n’a été inspecté ou modifié.


La phrase historique sur les éléments non documentés vise leur état réel et leurs paramètres : Gunicorn/systemd sont maintenant retenus comme cible S01, sans preuve d’installation. DNS/routage, TLS, reverse proxy, chemins, sauvegardes, restauration, supervision, accès et procédures de déploiement restent à vérifier/spécifier. Aucun changement serveur effectué.

R02 : la mise en service devra disposer d’une procédure validée de sauvegardes/effacement résiduel et restauration sans réintroduction des données effacées (fonctionnel G15/RG-T07). Aucune configuration de sauvegarde, purge ou serveur n’a été créée par cette intervention.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:728 -->

## 18. État réel d’implémentation

| Élément | État au 17 octobre 2026 |
| --- | --- |
| Dépôt Git et origine | Vérifiés localement |
| Python virtuel et dépendances | Présents, versions inspectées |
| Configuration locale et exemple | Présents, divergence documentée |
| Application Flask indépendante | Choix communiqué ; code absent |
| Fonctionnalités, routes et interfaces | Aucune implémentation trouvée |
| Chargement de configuration et connexion Python | Aucun code trouvé ; test non validé |
| Base, compte et droits sur le VPS | Création et vérification des droits rapportées par la source V0.2 ; non contrôlées directement ici |
| Schéma, migrations, tests et déploiement | Aucun fichier trouvé dans le dépôt |
| Référentiels | Deux documents consolidés en V1.3 (18 octobre), arbitrages spécifiés/non implémentés ; AGENTS.md présent et inchangé |


Au 18 octobre : fichiers historiques séparés des spécifications et du modèle financier absents, contenus intégrés conservés dans le fonctionnel ; instruction courante R01/R02 présente et inchangée, registre D01–D57 intégré conservé ; ancienne instruction séparée absente à l’inventaire courant. Tous les services, interfaces, moteur, CMS, exports, auth, migrations et déploiement décrits restent à développer ; aucune connexion applicative MariaDB validée.

L’inventaire du 18 octobre confirme l’absence de code applicatif. Les faits Python/dépendances/configuration restent ceux des inspections antérieures, sans nouveau test ni contrôle serveur. Les décisions D01–D57 ne sont pas une preuve d’implémentation.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:747 -->

## 19. Décisions techniques validées et traçabilité

| Repère | Décision | Source |
| --- | --- | --- |
| BIZ-T-001 | Flask indépendant, MariaDB propre, pas metadata-driven/Designer/MCP | V0.2, S01 |
| BIZ-T-002 | Routes/Blueprints → Services → db.py SQL paramétré, pas REST/Repository obligatoire | V0.2, S01 |
| BIZ-T-003 | Une application/deux fronts ; configuration hôtes locale | S01, S08 |
| BIZ-T-004 | Moteur pur et mêmes résultats écran/exports/langues | S05, F01, F11 |
| BIZ-T-005 | Versions réseau et snapshots, migrations versionnées propres | S02, S06 |
| BIZ-T-006 | member/admin, approbation distincte pipeline, sécurité dédiée | S02–S03 |
| BIZ-T-007 | CMS MariaDB et catalogues système séparés FR/EN/ES | S10, F11 |
| BIZ-T-008 | Gunicorn/systemd dédiés sur VPS ; SMTP testable | S01, S03 |
| BIZ-T-009 | Tests moteur/intégration/migrations/exports/CI | S07–S08, F09 |

Les repères sont créés pour la traçabilité documentaire ; ils ne prouvent aucune réalisation. Les règles communes AGENTS imposent vérification des sources, séparation des autorisations et absence de transfert de décisions entre projets.

### 19.1 Décisions utilisateur validées — arbitrages du 18 octobre 2026

Registre technique : 57/57 décisions **spécifiées, non implémentées**, sans duplication du registre fonctionnel complet (§14.1). La section fonctionnelle indiquée contient l’application harmonisée ; le tableau complet de couverture/statut est au fonctionnel §16.1. Les limites de stockage/tokens/schéma/jobs restent à détailler.

| Décision | Traduction technique | Section technique | Section fonctionnelle |
| --- | --- | --- | --- |
| D01 | Routage par hôte Info/Biz, codebase/DB/CMS/auth partagés, liens réciproques ; pas de socle App imposé. | §2 | §§2.1, 3 |
| D02 | Préremplissage coûts seulement ; isoler scénarios de fréquentation/CA des références géographiques et snapshot local. | §11.1 | §7.1 |
| D03 | Référentiel économique saisi admin, origine/date ou estimation/défaut national ; aucune API requise. | §9.1 | §7.1 |
| D04 | Clé fonctionnelle pays/commune, une série par commune ; aucun niveau quartier/zone/code postal. | §9.1 | §7.1 |
| D05 | Contrôle serveur lecture seule original membre pour admin ; clonage modifiable dans espace admin. | §10.1 | §5.1 |
| D06 | Catalogues et CMS FR/EN/ES couvrent tout, emails/administration/exports inclus, pays distinct de langue. | §13 | §10.1 |
| D07 | Moteur pur commun, règles pays configurables devise/taxes/social/financement/commercial ; aucune fiscalité inventée. | §11.1 | §8.1 |
| D08 | Activation contrôlée des pays, France seule V1 ; préparation admin sans activation implicite. | §11.1 | §8.1 |
| D09 | Paramètres commerciaux par pays versionnés et snapshotés ; valeurs françaises historiques inchangées. | §11.1 | §8.1 |
| D10 | Sortie locale en devise pays, consolidation en EUR ; pas de conversion France. | §11.1 | §8.1 |
| D11 | Taux manuels admin avec date/historique ; taux exact figé simulation/consolidation, aucune API imposée. | §9.2 | §8.1 |
| D12 | Aucun recalcul historique automatique ; actualisation explicite crée une version, exports projet/hypothèses versionnés. | §9.2 | §7.2 |
| D13 | Comparer versions et projets distincts en lecture seule, tableaux/graphiques 36 mois et trois scénarios. | §8.2 | §7.2 |
| D14 | Garde serveur vérification email puis approbation manuelle avant pro/projets/exports. | §10.1 | §6 / S02.3 |
| D15 | Adaptateur public sans inscription vers moteur commun, résultats strictement limités. | §11.2 | §6 / S02.2 |
| D16 | Liste de sortie publique restreinte à investissement et CA potentiel ; aucune exposition des autres métriques. | §11.2 | §6 / S02.2 |
| D17 | Scénario public fixé réaliste ; prudent/optimiste réservés au professionnel. | §11.2 | §6 / S02.2 |
| D18 | CA mensuel à maturité et annuel au rythme de croisière, jamais l’année 1. | §11.2 | §6 / S02.2 |
| D19 | Aucun stockage anonyme ni transfert/récupération à l’inscription ou après approbation. | §9.2 | §6 / S02.2 |
| D20 | Entrées finales format/ville facultative/loyer ; étape intermédiaire corrigée par D25, pas D27. | §8.1 | §6 / S02.2 |
| D21 | Simulation publique principal uniquement ; satellites réservés aux projets professionnels. | §11.2 | §6 / S02.2 |
| D22 | Sélection de formats définis, aucun champ nombre libre public ; pro personnalisable. | §8.1 | §6 / S02.2 |
| D23 | Formats admin ajout/modification/activation/désactivation/ordre/défaut ; aucune liste figée. | §9.1 | §6 / S02.2 |
| D24 | Ville facultative, défaut national si absence de donnée ; loyer toujours modifiable, pas d’effet CA. | §8.1 | §§6 / S02.2, 7.1 |
| D25 | Aucun apport demandé publiquement ; réservé au professionnel. | §8.1 | §6 / S02.2 |
| D26 | Investissement HT et TTC distincts, taxes par poste, TTC indicatif sans présumer récupération TVA. | §11.2 | §6 / S02.2 |
| D27 | CA public mensuel/annuel à maturité exclusivement HT. | §11.2 | §6 / S02.2 |
| D28 | Recalcul direct changement format/ville/loyer sans bouton/page reload, appels inutiles évités. | §8.1 | §6 / S02.2 |
| D29 | Une page : deux colonnes desktop, paramètres puis résultats mobile, pas de wizard. | §8.1 | §6 / S02.2 |
| D30 | CTA exact vers inscription/connexion puis approbation, aucun téléchargement immédiat ni transfert. | §8.1 | §6 / S02.2 |
| D31 | Validation de cinq champs obligatoires nom/prénom/email/téléphone/mot de passe, autres informations différées. | §10.1 | §6 / S02.3 |
| D32 | Lien vérification email sécurisé temporaire, renvoi ; examen et approbation bloqués avant vérification. | §10.1 | §6 / S02.3 |
| D33 | Refus conserve compte sans accès pro, réexamen/approbation sans recréation, historique préservé. | §10.1 | §6 / S02.3 |
| D34 | Refus avec date/auteur/motif interne obligatoire ; notification email sans motif automatique. | §7.1 | §6 / S02.3 |
| D35 | Compléments demandés et réponses dans le dossier avant approbation, notifications et historique. | §7.1 | §7.3 |
| D36 | Échanges texte seuls ; aucun upload candidature/messagerie, documents hors application si nécessaires. | §7.1 | §7.3 |
| D37 | Initiation des échanges des deux côtés avant/après approbation, pendant préparation, hors suspension. | §7.1 | §7.3 |
| D38 | Un fil chronologique par candidat, pas par sujet/projet/admin. | §9.1 | §7.3 |
| D39 | Boîte partagée entre administrateurs autorisés, auteur de réponse individuel identifié. | §7.1 | §7.3 |
| D40 | Aucune édition/suppression individuelle des messages envoyés, correction par nouveau message ; exception purge légale. | §15.1 | §7.3 |
| D41 | Regroupement email premier non-lu puis silence jusqu’à consultation ; cycle remis à zéro, admin partagé sans doublons. | §7.1 | §7.3 |
| D42 | Aucun badge/compteur/alerte visuelle de messagerie ni notification in-app ; email seul et fil consultable. | §8.2 | §7.3 |
| D43 | Notification avec lien sécurisé/auth ; aucune ingestion des réponses email, réponses dans Biz exclusivement. | §7.1 | §7.3 |
| D44 | Référence 2 ans dernier contact significatif, base légale à vérifier, actifs distincts, exceptions documentées. | §15.1 | §11.1 |
| D45 | Détection/signalement automatique des échéances, exceptions puis validation admin ; pas rétention indéfinie. | §15.1 | §11.1 |
| D46 | Effacement coordonnées/candidature/messages après validation hors obligations, trace minimale non identifiante. | §15.1 | §11.1 |
| D47 | Demande personnelle confirmée datée/statutée, contrôle légal et notification, indépendamment de 2 ans. | §15.1 | §11.1 |
| D48 | Invalidation immédiate sessions et suspension simulateur/projets/messagerie après demande. | §15.1 | §11.1 |
| D49 | Annulation par admin après contact et vérification d’identité avant purge ; aucune restauration après effacement. | §15.1 | §11.1 |
| D50 | Suivi un mois / extension deux mois supplémentaires sous conditions et information au premier mois ; ni SLA 7 j ni délai minimum. | §15.1 | §11.1 |
| D51 | 2FA admin requis, candidats/franchisés sans obligation ; exception navigateur valide selon D54. | §10.2 | §11.2 |
| D52 | Second facteur code email après mot de passe, adresse admin vérifiée, risque boîte email explicite, aucun TOTP imposé. | §10.2 | §11.2 |
| D53 | Code unique 5 min, remplacement invalide ancien, limites tentatives/renvois à détailler. | §10.2 | §11.2 |
| D54 | Confiance navigateur facultative 30 j après 2FA, jeton sécurisé non IP seul, mot de passe maintenu, logout ne révoque pas. | §10.2 | §11.2 |
| D55 | Inventaire appareils et dates, révocation serveur individuelle/globale ; prochain login avec 2FA. | §10.2 | §11.2 |
| D56 | Session admin serveur 30 min inactivité réelle, pas polling ni prolongation par confiance. | §10.2 | §11.2 |
| D57 | Session membre serveur 2 h inactivité réelle, déconnexion et réauthentification. | §10.2 | §11.2 |

### 19.2 Décisions validées Q01–Q08 — traçabilité technique

Registre fonctionnel complet au §14.2 ; toutes intégrées, spécifiées et non implémentées. Les textes D01–D57 ci-dessus demeurent inchangés ; leur portée historique est précisée par Q01–Q08 au §9.3 sans nouvelle règle financière.

| Décision | Traduction technique | Section fonctionnelle | Section technique | Statut |
| --- | --- | --- | --- | --- |
| Q01 | Debounce sur travail mutable, états exacts, garde de session/erreur et données persistées conservées. | §7.4 | §§8.3, 9.3 | intégré |
| Q02 | Historiques créés explicitement ou à actualisation centrale volontaire, jamais par chaque autosauvegarde. | §§7.2, 7.4 | §9.3 | intégré |
| Q03 | Séquence/date/libellé facultatif par projet, numéro attribué jamais réutilisé. | §7.4 | §9.3 | intégré |
| Q04 | Copie paramètres historique vers travail avec origine et confirmation, historiques intacts. | §7.4 | §§8.3, 9.3 | intégré |
| Q05 | Suppression historique propriétaire confirmée/légale, comparaisons actualisées, exports produits inchangés. | §§7.4, 11.3 | §§9.3, 15.2 | intégré |
| Q06 | Suppression projet/travail/historiques confirmée/légale, copies admin séparées et audit minimal. | §§7.4, 11.3 | §§9.3, 15.2 | intégré |
| Q07 | Nouveau projet/identifiant depuis travail, configurations/hypothèses copiées sans historique source. | §7.4 | §9.3 | intégré |
| Q08 | Quota admin contrôlé sur création/duplication, pas sur lecture/édition ; supprimés exclus, non configuré à préciser. | §§7.4, 9.2 | §§9.3, 10.3 | intégré |

### 19.3 R01/R02 — Traçabilité documentaire

| Décision | Mandat / traduction technique | Annexe fonctionnelle | Sections techniques | Statut |
| --- | --- | --- | --- | --- |
| R01 | Fiche France détaillée, séparation fiscalité/comptabilité/cash, matrice et cas conditionnels ; aucune qualification fiscale inventée | §17, FR-T01–FR-T12 | §§11.3, 14, 16.3 | intégré, spécifié ; validation expert/assiette requise |
| R02 | Politique par catégorie, inventaire des copies, effacement/backup/exception et recette sans données réelles | §18, G01–G16 et RG-T01–RG-T09 | §§15.3, 16.3, 17 | intégré, spécifié ; validation juridique/DPO requise |

D01–D57 et Q01–Q08 restent inchangées dans leurs registres. R01/R02 sont des mandats documentaires validés, pas des autorisations de code ni des validations externes obtenues.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:851 -->

## 20. Points ouverts, couverture et historique

### 20.1 Écarts résolus et questions ouvertes

D05 résout O01 (original membre jamais édité admin), D01 résout O02 (Info/Biz même socle et deux domaines), D06 résout O03 (tout FR/EN/ES). Public, candidature, coûts locaux et confidentialité/auth sont harmonisés dans le corps des §§2 et 7–15, pas seulement ajoutés dans un registre. D20 contenait un mauvais renvoi : D25 retire l’apport et D27 fixe le CA HT, identifiants conservés.

**Q01–Q08 validées**, voir §§8.3, 9.3, 10.3 et registre §19.2 : travail mutable autosauvegardé, historiques créés explicitement, restaurations/suppressions/duplication et quota définis ; public toujours sans stockage D19. Les O04–O08 et hypothèses financières restantes sont détaillés au fonctionnel §15.2 : aucun arbitrage sur mixes, fiscalité, RH ou budget logiciel ajouté.

Restent à détailler : schéma physique, mécanismes serveur de sessions/codes/tokens/confiance, événements de sécurité, limite des tentatives/renvois, notifications partagées/consultation, exécution/signalement de purge et vérification légale, contact significatif et conservation des actifs, taux FX manuels (cotation/source d’estimation/date), activation pays, SMTP/sécurité email ; bibliothèques frontend/graphiques/Excel/PDF/i18n, fichiers/Blueprints et exploitation serveur. Référentiel économique interne manuel validé, pas de fournisseur externe ni API géographique obligatoire.

### 20.2 Couverture, historique et limites

Les 20 sections techniques restent organisées selon les conventions documentaires précédentes. S01–S10 et F01–F11 ont été conservés à partir de V1.0 et harmonisés quand D les remplace ; voir contrôles financiers au fonctionnel §16. L’absence des sources séparées est explicitée au §1 et ne devient pas un faux constat de lecture.

| Version | Date | Changement |
| --- | --- | --- |
| 0.1 | 17 octobre 2026 | Inspection initiale |
| 0.2 | 17 octobre 2026 | Architecture simplifiée et cadrage transmis |
| 1.0 candidate | 17 octobre 2026 | Consolidation exhaustive S/F, séparation cible/existant |
| 1.1 | 18 octobre 2026 | D01–D57 intégrées ; Q01 encore ouverte à cette version |
| 1.2 | 18 octobre 2026 | Q01–Q08 intégrées, intégrité travail/historique et audit V1 |
| 1.3 | 18 octobre 2026 | Annexes R01/R02 intégrées au fonctionnel, liens et exigences de recette/conservation croisés ; validations externes en attente |

Seuls les deux référentiels modifiés. Instruction et AGENTS inchangés ; aucun autre projet modifié, aucun fichier applicatif/SQL/configuration/test créé. Aucun test DB ni contrôle serveur ; aucune installation, migration, configuration serveur, déploiement, commit ou push. Attendre relecture et validation avant tout développement.

### 20.3 Audit V1 — classement croisé

Tableau des seuls blocages essentiels au fonctionnel §15.3 : **B01 fiscal/comptable France et clearing** pour recette financière complète (F01/F03/F05–F07, D26 ; technique §§11, 14) ; **B02 politique légale de conservation/effacement** avant mise en service avec données personnelles (D40/D44–D50, Q05/Q06 ; technique §§15.1–15.2). Validations de référentiel comptable et de politique légale à obtenir ; aucune nouvelle durée, taux ou base de royalties décidé par l’audit.

Les conventions de moteur autorisées S09/F10 (allocation cohérente crédits/ventes/occupation, reconnaissance prépayée explicitée, avertissements de mix, paramètres et tests) sont NON BLOQUANTES pour construire une V1 prévisionnelle sous hypothèses documentées : pas de nouvelle question sur chaque algorithme. Leur validation fiscale/comptable conditionne les chiffres concernés de B01. Procédure pro/approbation, paramètres versionnés/publication CMS, contenu minimal Excel/PDF et authentification sont DÉJÀ TRANCHÉS (§§8–14, 19) ; bibliothèques, SMTP, schéma/stockage, détails d’exploitation et quota non configuré sont des précisions d’implémentation ordinaires, pas des arbitrages métier accessoires.

Le quota numérique reste configurable sans valeur par défaut décidée ; ne pas adopter de politique implicite pour l’absence de configuration. Les tests et vérifications effectives DB/SMTP/sécurité/déploiement sont des travaux requis avant ouverture, pas une preuve de réalisation ni de nouveaux blocages utilisateur. Deux thèmes de validation essentiels seulement ; voir fonctionnel §15.4 pour la classification exhaustive des domaines examinés.

Contrôle V1.2 : registre D01–D57 et lignes de traçabilité inchangés ; 11 blocs financiers préservés dans le fonctionnel ; Q01–Q08 intégrées individuellement et anciens points ouverts supprimés du corps courant. Seuls les deux référentiels modifiés, aucun code/SQL/configuration/dépendance, installation/migration, commit ou push. Aucun développement lancé ; attendre validation du compte rendu.

### 20.4 Réserves après préparation R01/R02

Les annexes sont prêtes pour examen documentaire et conception, **pas validées par expert** : seul le mandat de les produire est validé. B01 reste qualification/taux/calendriers France et assiette clearing à confirmer par expert-comptable et, pour options contractuelles, franchiseur/conseil ; B02 reste RT/bases/durées/événements/exceptions/copies/backups à confirmer juridiquement/DPO. Voir fonctionnel §15.5, matrice §17.6 et G01–G16. Ces validations conditionnent respectivement les chiffres concernés et l’ouverture des données personnelles, pas la réouverture de décisions déjà closes.

Aucun autre arbitrage essentiel remonté ; recette réelle DB/auth/SMTP/exports/sécurité/déploiement reste à réaliser avant exploitation. Préparation documentaire ne prouve aucune implémentation ou validation finale. D57+Q8 = **65 décisions conservées**, R01/R02 ajoutent deux mandats documentaires distincts ; F01–F11 restent inchangés. Seuls les deux documents maîtres modifiés, aucune annexe externe créée dans le dépôt, aucun code/SQL/configuration/installation/commit/push.


## Conventions du moteur financier conservées

Consolidation du2novembre2026 depuis movee-biz/ASSUMPTIONS.md (empreinte de la source enregistrée dans CLEANUP_REMAINING_RESULT.json). Les conventions détaillées ci-dessous complètent le modèle financier sans devenir des règles commerciales App ni une validation expert R01/R02.

**Précisions plus récentes déjà validées :** l’ancien résumé B07 des seules sorties publiques et l’affichage B08 au centime sont historiques. Les compléments du23octobre imposent les cinq montants publics (HT, apport indicatif, CA mensuel/annuel, bénéfice année3) et une présentation monétaire en euros entiers, arrondi au plus proche, demi-euro à l’opposé de zéro, sans double arrondi. Les valeurs Decimal enregistrées et les volumes non monétaires gardent leur précision ; Excel conserve ses valeurs numériques. Les contrats actuels PROJECTS/EXPORTS et les décisions datées correspondantes font autorité sur ces points. Aucune formule ou configuration n’est modifiée par ce transfert.

### Hypothèses du moteur financier — B06, 21 octobre 2026

Ces conventions implémentent S09/F10 sans modifier D01–D57, Q01–Q08 ou F01–F11.
Les valeurs du référentiel France ne constituent pas une validation par un expert.
Aucune projection n'est un revenu garanti. Les interfaces des simulateurs et la
persistance des projets relèvent du chantier 7 ; les exports du chantier 8.

#### Références et calcul

- France/EUR seule active. Futurs pays préparables mais inactifs, sans fiscalité
  étrangère. Taux manuels cotés en EUR pour une unité étrangère ; historique
  conservé, aucun appel externe. Aucun FX appliqué aux projets France.
- Versions réseau ajoutées, jamais modifiées par le service. Publication sous
  verrou du pays avec contrôle de la version attendue. Le snapshot résolu contient
  version, paramètres, sources de commune et format, et coûts locaux. `simulate`
  en conserve une copie indépendante ; aucun recalcul ne consulte la DB.
- Decimal en contexte fixe de 36 chiffres, indépendant de celui de l'appelant.
  Valeurs sérialisées en chaînes ; arrondi monétaire uniquement à la présentation.
  Langue absente des entrées de calcul. Aucun import Flask, DB ou réseau du moteur.
- Pas de format, commune, taux de change ou centre commercial fictif initialisé.
  Les huit machines des tests sont exclusivement une référence de recette F09.

#### Capacité, clients et produits

- Mois moyen : 52/12 semaines, capacité relative au mois d'ouverture. Interpolation
  M13–M24 par défaut, paramétrable. Réservation de toutes les machines pendant les
  24 heures collectives hebdomadaires. Autonomie à 60 minutes par défaut.
- Coach : 42 heures/semaine moins les cours. Individuel 60 minutes, Light 30 min,
  Complete 4 h, upgrade 3,5 h supplémentaires. Une machine réservée pendant ces
  activités réduit la capacité autonome ; dépassement refusé. Aucun onboarding ou
  individuel généré par défaut (zéro, calendriers locaux de 36 valeurs possibles).
  Pas de collectif, coach ou onboarding satellite.
- Une demande de crédits est dérivée des séances (2/3/6). Convention : 80 % de
  cette demande servie par abonnements, avec 80 % d'utilisation ; les poids Active
  et Premium sont normalisés entre eux. Cela ne garantit pas simultanément les
  cibles de clients 50/30/20 et de séances 80/20. Les parts réalisées et l'écart
  à la cible packs sont retournés, avec avertissement. Clients fractionnaires de
  planification, jamais présentés comme factures ou adhérents réels.
- Après abonnements, consommation FIFO des packs existants. Le solde est acheté
  en fractions de packs pour couvrir exactement la demande. Mix technique initial
  pack 10 seulement, modifiable par admin. Achats supplémentaires explicites
  possibles ; leurs crédits se reportent sans expiration arbitraire. Aucun churn,
  aucune acquisition ou rétention de clients inventée.
- Abonnements reconnus à la vente ; crédits résiduels expirent en fin de cycle
  sans revenu supplémentaire. Packs reconnus à consommation par défaut, passif
  différé distinct de l'encaissement ; variante à la vente explicite. Les séances
  n'ajoutent aucun CA aux ventes. Light + upgrade = 19 + 110 ; aucun Complete
  supplémentaire pour la même conversion. Les volumes d'upgrade sont des entrées
  de planification, sans registre opérationnel des personnes.

#### Investissement, dette et cash

- Surface arrondie au m² supérieur. Profil travaux/mobilier satellite obligatoire
  et distinct ; pas de réutilisation silencieuse du principal ni de droit d'entrée
  satellite. Coûts travaux/mobilier locaux modifiables ; machines, transport et
  droit d'entrée restent les conditions réseau.
- Commande par défaut trois mois avant livraison ; livraison à l'ouverture sauf
  dates explicites compatibles. Deux acomptes machines 50/50. Entrée payée à la
  commande, reconnue par le franchiseur à l'ouverture ; travaux et mobilier payés
  à l'ouverture. Transport payé/livré sans marge. Pas de stock spéculatif.
- Les mois négatifs et M0 sont conservés dans `prelude` ; aucune avance n'est
  perdue pour une ouverture M1. Le reporting contient exactement M1–M36.
- Financement sur base HT + réserve de trois mois de charges ; **base technique
  de financement**, sans prétendre financer exactement les besoins TTC. Tirage
  apport/prêt à la commande ; échéances dès le mois suivant. Le besoin de
  financement TTC peut être supérieur. Capital remboursé hors résultat ; intérêts
  en charges ; amortissements sans décaissement supplémentaire.
- Amortissement linéaire dès l'ouverture : machines/transport 60 mois,
  travaux/vestiaires/douches 120 mois, mobilier 60 mois ; droit d'entrée 84 mois
  comme convention technique à confirmer. Réserve de remplacement 4 000/84 par
  machine purement indicative, jamais déduite deux fois du cash ou du résultat.
- Coach exploitant : coût société explicite, défaut zéro ; aucun net assimilé
  à un coût employeur. Les coûts communaux affectent uniquement les charges.
  Un agrégat communal « autres charges » remplace énergie à marketing, hors
  loyer, maintenance et coach ; le loyer saisi au projet prime la référence.

#### Fiscalité conditionnelle

- Prix produits TTC convertis avec taux produit explicite (référence 20 %).
  Aucune TVA uniforme implicite sur CAPEX ou charges : chaque poste est inconnu
  au départ, même assurance ou taxes locales. Zéro exige une saisie explicite.
  CAPEX TTC et cash TTC sont indisponibles lorsqu'une qualification manque.
- Cash HT proxy disponible et étiqueté ; ce n'est pas un solde bancaire TTC.
  Quand les taux par poste sont explicitement renseignés : exigibilité et
  déductibilité proportionnelles aux paiements, droit à déduction intégral comme
  hypothèse conditionnelle ; report de crédit, sans remboursement automatique.
  Déduction partielle refusée, son traitement comptable n'étant pas qualifié.
- Règlement de TVA après le décalage paramétré (un mois par défaut). IS clôturé
  annuellement M12/M24/M36, pertes reportées dans le modèle ; taux standard sauf
  éligibilité réduite explicitement vraie. Seuil annuel, jamais divisé par douze.
  Paiement après clôture avec décalage paramétré (un mois), sans prétendre reproduire
  un régime réel d'acomptes. Les dettes non encore payées restent visibles à M36.
- Centre isolé : IS autonome indicatif. Réseau : entité juridique explicitement
  renseignée pour chaque centre, calcul IS et TVA regroupé par entité ; ne pas
  sommer les IS autonomes de plusieurs établissements d'une même société.
  Aucun groupe d'intégration fiscale déduit de l'arborescence principal/satellites.

#### Clearing et franchiseur

- Flux explicites uniquement, autonomie/collectif, 8/12 HT provisoires. Ils
  allouent des séances déjà prévues chez l'hôte, sans accroître leur capacité ;
  refus si volume supérieur aux séances prévues. Pas d'individuel/onboarding.
- Assiette royalties choisie pour chaque flux : origine (vente externe chez
  l'origine) ou split (ventilation de cette assiette, sans la doubler). La
  compensation ajoute revenu chez l'hôte et charge chez l'origine ; élimination
  dans le CA économique réseau et dans l'entité commune. Pas de commission centrale.
  TVA du clearing non qualifiée : cash TTC indisponible pour les entités concernées.
- Le réseau économique retourné couvre les centres ; le franchiseur est présenté
  séparément. Ce n'est pas une consolidation comptable centres + franchiseur.
- Franchiseur : ventes machines et achats fabricant entiers, pas marge ajoutée
  une seconde fois au CA ; entrée uniquement principal, formation 300/principal,
  transport refacturé au coût et royalties reçues une seule fois. Dépôts machines
  différés jusqu'à livraison dans le résultat ; coût fournisseur reconnu à livraison.
- Charges centrales de base 4 750/mois, dont juridique 250 déjà inclus ; lancement
  10 000 une fois ; IT 2/machine effectivement ouverte. Développeur dès M13,
  support dès M25 ; indexation salaires annuelle, y compris leur mois d'entrée.
  Fondateur 0/2 000/3 000 net par mois selon année, multiplicateur employeur 1,8
  **hypothèse technique modifiable**, aucun taux de charges sociales certifié.
- Réserve centrale initiale 6 × 4 750 + 10 000 = 38 500, apport/prêt 30/70 sur
  cinq ans à 4 %. Plancher glissant 3 mois de charges centrales incluant personnel
  et IT ; ce plancher n'est pas ajouté à la réserve initiale. Besoin complémentaire
  signalé, sans financement automatique. Cash central HT proxy seulement ; le TTC
  central attend la qualification détaillée des flux, jamais un taux inventé.
- Calendrier uniforme déterministe fourni pour les trajectoires de principaux
  2/3/5, 5/8/12 ou 10/15/25 ; calendrier modifiable via les projets. Aucun satellite
  créé automatiquement sans profil explicite (cibles finales 5/15/40 à construire
  dans le simulateur réseau au chantier 7).
- EV indicative sur somme EBITDA M25–M36 × 4/6/8, multiples illustratifs ; aucune
  EV mécanique si EBITDA non positif. Equity indicative sur dette moins cash HT
  proxy, donc conditionnelle. Primaire apporte du cash à la société, secondaire
  non. DSCR = EBITDA moins IS / service de dette, ROI = résultat net / investissement
  financé HT sur 36 mois, ARPU de planification à M36 ; pas d'indicateurs certifiés.
  Seuil simplifié = charges fixes M1 / (1−royalty), hors dette/IS/clearing.

#### Réserves maintenues

R01 : validation expert-comptable des natures/taux, exigences de TVA, prépayés,
amortissement d'entrée, fiscalité/éligibilité, assiettes contractuelles et cash.
R02 : conservation/suppression et validation juridique au chantier 9. Ces tests
arithmétiques ne lèvent aucune de ces réserves et ne valident pas les exports.

#### Branchement B07 — conventions locales et présentations

Le facteur local de fréquentation vaut 1 par défaut, entre 0 et 2, et multiplie
les courbes sans dépasser les plafonds 100 % collectif/70 % autonomie. Les
conditions réseau restent figées côté serveur. Les écrans utilisent les mêmes
calculs Decimal ; mise en forme localisée et dates affichées en heure de Paris
sont indépendantes des résultats. Graphiques comparatifs à échelle commune.
Public : investissement CAPEX hors BFR et CA réaliste à maturité seulement ;
aucun cash ou financement transmis. Si le mois de maturité configuré dépasse
M36, le public signale une indisponibilité au lieu de nommer M36 « maturité ».
Cycles de travail, quotas non configurés et contrôle préalable de conservation
sont décrits dans [PROJECTS.md](../movee-biz/docs/PROJECTS.md) ; ce contrôle ne lève pas les réserves R02.

#### Présentation des exports B08

Les exports reprennent les résultats Decimal et la même vue agrégée que les écrans.
La présentation monétaire est au centime ; les taux ne sont pas arrondis au centime.
Excel stocke les nombres selon sa précision native (environ 15 chiffres significatifs)
et affiche les séparateurs de l'application. Le PDF applique FR/EN/ES explicitement.
Un TTC non qualifié reste indisponible. Le classeur est un instantané de valeurs
traçables sans recalcul financier autonome. Aucune convention financière n'est
modifiée par le rendu ; R01/R02 demeurent ouvertes. Voir [EXPORTS.md](../movee-biz/docs/EXPORTS.md).

