# MOVEE — référence technique commune

Version de consolidation : 2 novembre 2026. **Référence documentaire centralisée ; aucune activation, migration ou configuration modifiée.**

## Architecture par propriétaire

| Ensemble | Architecture / transport | Stockage et limite |
| --- | --- | --- |
| App et Admin | Web/API → Services → Repositories → MariaDB ; contexte serveur et droits revalidés | État métier central ; sessions/quotas Redis distincts de l’historique durable |
| Mobile | React Native/Expo actuellement ; API native Bearer, sans identité cookie | SecureStore natif ; jeton Web en mémoire. Pas de SQL/Redis/OpenAI direct |
| Biz/Info | Flask/Blueprints/Jinja → Services → db.py paramétré → MariaDB ; moteur financier Python pur | Base/auth propres ; pas d’imposition du Designer, MCP ou Repository App |
| Pod/MOTION | Cible Linux/Python, exécution et analyse locales séparées, interfaces matérielles | SQLite/fichiers proposés ; aucun schéma ni protocole App–Pod livré par cette synthèse |

Cette table est une carte documentaire, pas un audit de code ni de production. Les versions précises, modèles physiques et contrats sont dans les spécificités.

## Contrats et dépendances à vérifier avant modification

| Interface | Fournisseur | Consommateur | Invariants |
| --- | --- | --- | --- |
| Pages natives / session / métier | App | Admin et Mobile | UID natifs, champs/actions autorisés, config_version, contexte/ligne/sujet réautorisés, pas de cible arbitraire |
| Réservation / crédit / accords / préférences | Services App | IA, Admin, Mobile selon transport | Choix, aperçu, accord, exécution et récupération distincts ; intention stable et reçus ; pas de CRUD parallèle |
| Catalogue et médias | App | Admin/Mobile ; futur Pod à qualifier | Traductions en lignes et langue explicite ; référence/media sous droits, animation explicite |
| Acquisition / résultat sportif | Pod/MOTION envisagés | App puis Mobile | Qualification, unités, version, ordre, déduplication et autorisation ; pas de contrat inventé |
| Calculs prévisionnels | Moteur Biz | Public/pro/export Biz | Même moteur, snapshots et précision ; aucune écriture des politiques App |

Un profil ou contrat historiquement décrit n’est pas forcément servi aujourd’hui. Pour les Pages Mobile, la consolidation livrée du31 octobre utilise14, conserve30 Pages et retire les anciens transports exposés ; les reconnaissances historiques et preuves restent distinctes. État daté : voir références App/Mobile et leurs rapports pointés, pas un hardcode de version applicable à tout nouveau projet.

## Moteur partagé App/Admin/Mobile

Déclarations Pages/Fields/Actions, instances et Designer sont le moteur existant à réutiliser. Front_type est une propriété physique qualifiée par contexte serveur (1Web,2Mobile dans le contrat existant), jamais une bascule de sécurité fournie par le client. Les UID ne sont ni des permissions ni des alias permanents de noms métier. Ne pas créer un parcours ou une copie de Page pour une variation cosmétique.

Les descriptions génériques reprises plus bas exposent le modèle mental. Le brief d’origine est partiellement hérité d’un autre projet : son exemple d’administrateur ou de scope propriétaire n’atteste pas les droits réseau MOVEE. Seuls les Services, affiliations datées, intersections de studios, permissions actuelles et tests du dépôt qualifient les accès ; liste, comptage, fiche et écriture doivent avoir le même périmètre. Reset, ID forgé ou changement de Page ne l’élargissent jamais.

## Exploitation et maintenance communes

Procédure officielle conservée à son emplacement réel : [environnement Mac](../docs/ENVIRONNEMENT_DEVELOPPEMENT_MAC.md), [validation locale](../dev/VALIDATION_ENVIRONNEMENT_LOCAL.md). Backend via movee-dev/Gunicorn, jamais Flask manuel5050. MariaDB partagée, Redis et Expo ne sont pas à redémarrer pour recharger Python. Aucun redémarrage n’est exécuté par la consolidation. Biz garde son lancement séparé et ses cibles propres. Ne pas prendre un port local de tunnel pour une autorisation VPS.

Plans scellés, manifests SQL, signatures, migrations, fixtures et rapports d’installation peuvent être des dépendances exécutables. Les conserver dans les dépôts ; cette centralisation porte sur les référentiels, pas sur le déplacement des contrats/runtime. Un plan expiré ou divergent n’est pas réappliqué. DML transactionnel et DDL MariaDB à commits implicites restent distincts ; aucun rollback DDL global promis.

Langues : contenus catalogue localisés en lignes avec métadonnée de langue (FR/EN/DE/ES, FR initial et absence sans repli silencieux pour RepDB). Biz conserve FR/EN/ES et ses règles nationales distinctes. La charte reste [DESIGN_SYSTEM_MOVEE.md](DESIGN_SYSTEM_MOVEE.md), pas une seconde copie ici.

## Architecture de référence App et brief de moteur conservés

Les sections suivantes concernent le moteur App et ses consommateurs, pas l’architecture imposée à Biz ou à Pod. Elles restent des décisions/modèles datés et ne remplacent pas les contrats effectivement livrés.

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:497 -->

## Architecture obligatoire

```text
Mobile iOS / Android (Expo pour les tests initiaux) → API Flask → Services → Repositories → MariaDB
API Flask → Agent IA natif / orchestration OpenAI → Services métier → Repositories → MariaDB
Web / borne / machine → API Flask → Services métier → Repositories → MariaDB
```

L’agent IA ne requête jamais SQL ou Repository directement. L’API porte transport, authentification et contexte ; les Services portent règles métier, permissions, validations, transactions et idempotence ; les Repositories portent la persistance. Les clients connectés n’imposent pas eux-mêmes les règles métier.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:507 -->

## Framework metadata-driven conservé

Le schéma existant comporte `entities`, `fields`, `pages`, `actions`, `metadata`, `permissions`, `users`. Le CRUD générique est privilégié pour les opérations sans invariant métier spécifique. Réservation et immobilisation de crédits, démarrage/clôture de séance, compensation interfranchises, activation de contrat, affectation de machine et approbation IA nécessitent des **actions Services dédiées** ; ne pas les implémenter comme simples mises à jour CRUD non contrôlées.

Le modèle Newapp Entity 16–72 est une **référence de départ gelée**, non une preuve que les besoins MOVEE sont couverts. Toute extension doit être motivée par un gap physique démontré, sans création de table par réflexe. Users est l’identité unique ; le parcours commercial est porté par les rattachements datés aux centres ; Contacts/Trainers restent uniquement sources de migration en phase B ; pas de table `clients` ni `organizations` ; pas de `sessions_remaining` ; solde par `session_credit_transactions` ; propositions IA dans `proposals`.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:513 -->

## Périmètres et identité

Identité `users` unique, rôles multiples et rattachements datés centre/franchisé (Q001–Q006). L’autorité serveur vérifie à chaque action les droits effectifs et le périmètre temporel. Les autorisations de capacités IA sont révocables, bornées par action/scope/durée et jamais supérieures aux droits de l’utilisateur (Q088–Q092). Les tables `user_affiliations` et `user_locations` sont présentes dans la baseline V1 ; les contrats de sélection et propagation du contexte mobile restent à formaliser.

**AR03 — Centre contractuel unique, centres accessibles multiples, centre actif.** Le centre actif est un contexte opérationnel choisi, jamais une mutation contractuelle ; les droits et l'éligibilité sont revérifiés côté App à chaque action.

**Identité/centres :** centre contractuel, liste des centres accessibles, centre actif et contrôles d'éligibilité par action ; invalidation du contexte à la révocation.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:564 -->

## IA et sécurité

Les adaptations automatiques de programme et de machine sont soumises aux limites individuelles, au consentement et aux contraintes matérielles (Q030–Q031). Les actes financiers, contractuels, disciplinaires, sensibles ou irréversibles demandent les validations humaines prévues. Le stockage vidéo est facultatif, limité et consenti (Q048–Q052). Les capacités natives de l’agent IA et les workflows conservent audit, version, idempotence, reprise et contrôle de permissions (Q089–Q096).

**AR01 — Autonomie encadrée des adaptations de programme supervisé.** L'IA peut appliquer une adaptation **dans les limites préautorisées par le coach** avec consentement de l'adhérent ; hors limites, exercices protégés, objectifs globaux ou restrictions de sécurité : validation coach selon les règles métier. Cette précision prévaut sur toute formule exigeant une approbation coach pour chaque adaptation.

**AR02 — Création et modification de programme uniquement via IA.** En cas d'indisponibilité IA, consultation autorisée mais aucune création/modification. **Exception explicite à B8.2** ; les autres parcours classiques restent requis selon leur périmètre.

**Programme/IA :** limites coach versionnées et vérifiées par Service, consentement adhérent, demandes hors cadre, refus et journal d'audit ; consultation classique indépendante de l'IA, écriture exclusivement IA.

---

<!-- provenance: movee-app/codex/MOVEE_APP_TECHNICAL_REFERENCE.md:574 -->

## Hors ligne et événements

Les équipements peuvent produire des événements en mode dégradé limité (Q034, Q086). Toute synchronisation doit distinguer identité d’événement, ordre logique, doublon, conflit, droits à l’instant d’exécution et état de séance. Les choix de protocole et de persistance ne sont pas encore décidés.

**AR07 — Mesures externes, résultats mobiles.** MOVEE Motion/dispositifs spécialisés acquièrent les mesures ; MOVEE App centralise les résultats validés et droits ; MOVEE Mobile restitue bilans et évolutions, sans connexion directe aux appareils.

**Bilans/Motion :** origine, validation, visibilité et évolution des mesures ; échange interprojet à contractualiser avec MOVEE Motion, jamais accès matériel direct depuis Mobile.

---

<!-- provenance: movee-app/codex/METADATA_ENGINE.md:28 -->

## 1. Le principe

On ne développe pas d'écran. On décrit un comportement en base, et un moteur
générique l'interprète à l'exécution.

```
métadonnées  ->  moteur  ->  écran, requête SQL, droits
```

Ajouter une entité, une page, un champ, un filtre ou une action se fait
**en décrivant**, pas en codant. Un fichier Service ou Repository ne se crée que
pour un comportement propre — une règle métier que les métadonnées ne savent pas
exprimer. Le CRUD, lui, est déjà servi pour toute entité du registre.

Corollaire : `if (entity === "...")` dans un composant générique est un signal
d'alarme. Le métier vit dans le Service de son entité.

---

---

<!-- provenance: movee-app/codex/METADATA_ENGINE.md:47 -->

## 2. Les quatre piliers

### `entities` — le registre

Une ligne par entité : son nom, sa table SQL, son alias, et les colonnes qui la
structurent (`id_field`, `label_field`, `value_field`, `order_field`).

Le moteur résout tout depuis ce registre. **Le nom d'entité ne vient jamais de
l'URL** : il vient du registre, ce qui interdit de fabriquer un chemin d'import
depuis une requête.

La résolution Service/Repository se fait **par convention** :

```
services/<entity_name>_service.py       -> utilisé s'il existe
repositories/<entity_name>_repository.py -> utilisé s'il existe
sinon                                    -> construits à la volée
```

Conséquence majeure : une règle métier ne peut pas être contournée. Il suffit
qu'un fichier existe pour qu'il gagne, y compris par la route générique.

### `fields` — le catalogue des champs

Une ligne par colonne réelle, avec son type et son `default_config`.

> **Une colonne ajoutée en base sans sa ligne dans `fields` est invisible du
> moteur.** Elle n'existe que pour le code qui la nomme explicitement.

C'est le point qu'on oublie en ajoutant une colonne.

### `pages` — les écrans

Une page porte son type (liste, formulaire, vue, import…), sa cible (page,
modale, panneau), et quatre configurations JSON :

| | |
|---|---|
| `page_config` | titre, icône, pagination, ce qui s'affiche |
| `config_fields` | les champs **utilisés sur cette page** |
| `config_actions` | les actions proposées |
| `config_filters` | les champs **utilisés comme filtres** |

Plusieurs pages peuvent servir la même entité avec des configurations
différentes, sans dupliquer la définition des champs. Les variantes sont liées
par `parent_id`, et la propagation ne doit jamais écraser un override d'enfant.

### `actions` — le vocabulaire des gestes

Une action déclare son `action_type`, que le moteur frontend sait exécuter :
ouvrir une page, soumettre un formulaire, supprimer, recharger, importer,
appeler une API… Elle porte aussi son emplacement (barre, menu de ligne, barre
de menu) et sa portée de données.

Une action peut en déclencher d'autres (`next_actions`), ce qui permet de
composer un enchaînement — enregistrer, fermer, recharger — **sans écrire une
ligne de JavaScript**.

### `permissions` — les droits

Une ligne par couple (rôle **ou** utilisateur, entité, action). Le brief décrit une précédence de permissions nominatives/rôle. Ne pas en déduire un accès réseau illimité : qualifications et scopes actuels des Services MOVEE font autorité, y compris pour un acteur administrateur.

> **Les permissions sont fermées par défaut.** Une entité neuve répond à
> l'administrateur et renvoie 403 à tout le monde sinon, tant que ses lignes
> n'existent pas. C'est l'étape qu'on oublie.

---

---

<!-- provenance: movee-app/codex/METADATA_ENGINE.md:116 -->

## 3. Le modèle central : `default_config` + overrides

```
fields.default_config            comportement global du champ
          +
pages.config_fields[field_uid]   uniquement les différences de CETTE page
          =
      configuration effective
```

Une entrée minimale est juste un identifiant. Avec deux personnalisations :

```json
{ "field_uid": "aaa111", "field_label": "Compte", "width": 350 }
```

Le bénéfice : changer un `default_config` change toutes les pages qui n'ont pas
d'override. Les règles qui en découlent :

1. Ne jamais stocker une valeur identique au défaut.
2. Un override qui revient au défaut se **supprime**, il ne se réécrit pas.
3. Normaliser avant de comparer : `null` et `""` sont la même absence.
4. Le **Service** décide de ce qui constitue un override ; le Repository
   persiste sans interpréter.

Et le piège qui revient : le frontend reçoit une configuration **hydratée**,
donc complète. Cela ne signifie pas qu'il possède ces overrides. Ne jamais
resauvegarder l'objet hydraté.

### ID et UID

| | |
|---|---|
| `xxx_id` | clé primaire SQL, relations. **Les entités métier utilisent leur ID.** |
| `xxx_uid` | identifiant d'une **instance de configuration** manipulée par le Designer |

Ne pas généraliser l'UID à toutes les entités. Et connaître un UID n'autorise
rien : un UID identifie, il ne donne aucun droit.

---

---

<!-- provenance: movee-app/codex/METADATA_ENGINE.md:157 -->

## 4. Ce qui se passe au chargement d'une liste

```
page_uid -> Service -> Repository
         -> hydratation des quatre configurations
         -> filtrage par permission
         -> frontend : construction de la page, filtres, actions, tableau
```

Les colonnes sélectionnées sont **celles de la page**, aliasées par leur
`field_uid`. Filtres, tri et données partagent donc le même espace de noms de
bout en bout. C'est pourquoi un filtre est indexé par `field_uid` et non par nom
de colonne.

---

---

<!-- provenance: movee-app/codex/METADATA_ENGINE.md:279 -->

## 7. Réflexes

Avant d'écrire du code, se demander dans l'ordre :

1. Est-ce que les métadonnées savent déjà le décrire ?
2. Quelle couche est responsable — HTTP, métier, SQL ?
3. Ai-je lu la classe concernée **et** sa classe abstraite ?
4. La valeur vient-elle d'un défaut global ou d'un override de page ?
5. Quel identifiant : clé SQL ou UID de configuration ?
6. Les permissions sont-elles déclarées ? Et leur périmètre ?
7. Quel impact sur le Designer et sur les pages clonées ?

En cas de doute entre deux approches, préférer celle qui réduit le code
spécifique, garde les métadonnées comme source de vérité, et permet d'ajouter
une entité sans écrire de fichier.

### Complément Admin — préparation du 28 octobre 2026

Les consultations supplémentaires utilisent les mêmes Pages/Fields/Actions et conservent les UID installés. Les liens vers une autre entité déclarent `record_id` par UID de champ de la Page source ; les sous-listes déclarent les filtres par UID d’instance de la Page cible. L’historique navigateur conserve filtres, tri et pagination, puis recharge configuration et données sous droits actuels ; aucun enregistrement métier n’est mis en cache dans cet historique.

Les actions Booking livrées disposent d’un adaptateur de présentation comme les réglages existants : Page HTML native (type7, entité44), propriété `page_config.booking_actions` = `create`, `cancel` ou `confirmations`, et garde serveur existante `admin_booking_actions=1`. Le menu et les liens restent des instances `open_page` natives. Les choix, versions, aperçus, droits et conséquences viennent exclusivement de `/api/admin-booking/*` sous session web. Aucune nouvelle définition d’action, règle métier ou route ajoutée. Ce composant n’est activé que par les Pages explicitement configurées ; le candidat nécessite encore examen et installation Backend autorisée.

Une écriture conserve une clé de récupération dans sessionStorage (opération + command_id uniquement, sans arguments, noms, secrets ou jeton d’aperçu). Après interruption, seul le reçu est interrogé volontairement ; aucune écriture automatique ni nouvelle clé sur résultat inconnu. Le Backend revalide l’acteur. Une confirmation ne clôt jamais par déduction une autre intention en attente.

### Raccordement des lecteurs et commandes livrés — 28 octobre 2026

- Une variante native de ListPage peut définir `page_config.read_query` pour un lecteur dont la query est fermée : les templates sont résolus avec le contexte de l’enregistrement sélectionné, limit/offset sont ajoutés, aucun filtre/tri/page_uid générique supplémentaire n’est envoyé. Exemple : adhérents du coach choisi ; le prédicat d’affectation reste entièrement serveur. Le bouton open_page indique l’endpoint dédié, la Page porte population=member ; elle n’est pas une nouvelle entrée de menu.
- `page_config.catalogue_command=create/update/set_active` raccorde les formulaires natifs à l’adaptateur CatalogueCommand et au DTO web livré. Les champs restent ceux du registre et du formulaire ; aucun alias de nom métier. Pour set_active, `catalogue_active_field_uid` désigne le booléen enregistré. Anciennes Pages sans cette configuration : comportement hérité conservé, sans prétendre à la fiabilité du nouveau transport.
- `page_config.credit_summary={location_entity_id:17}` ajoute le lecteur calculé par Service à la fiche engagement siège, avec sélecteur LinkedHelper natif sous droits courants. Les montants/quantités ne sont pas recalculés par le frontend.

Le candidat d’intégration distinct et les limites figurent dans ADMIN_COMPLETION_INTEGRATION_HANDOFF.md ; rien de ce raccordement n’est installé tant qu’un nouveau plan Backend n’a pas été autorisé et appliqué.
