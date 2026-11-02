# MOVEE Mobile — référence fonctionnelle spécifique

Version de consolidation : 2 novembre 2026. **Référence centralisée validée ; anciennes copies retirées après accord utilisateur.** Lire d’abord [README.md](README.md), [règles communes](AGENTS.md), [fonctionnel global](MOVEE_FUNCTIONAL_REFERENCE.md) et [technique globale](MOVEE_TECHNICAL_REFERENCE.md). Les sections issues des anciennes références conservent leur date/statut ; un constat historique ne décrit pas l’installation actuelle.

## État et précisions applicables à la lecture

Les78 décisions T décrivent la cible, non une liste de fonctions livrées. L’IA reste la cible principale et les écrans classiques sont indépendants de sa disponibilité, AR02 conservé. Mobile n’est pas utilisé pendant l’entraînement. Le rendu actuel réutilise le moteur commun14 et ses30Pages, pas une nouvelle version ou de nouveaux écrans par rôle. Langues initiales FR/EN/DE/ES, thème local Light/Black et charte commune.

La réalisation coach du2novembre conserve les Pages : profil propre en haut, Accueil/Planning/Adhérents en bas, sans métrique adhérent inventée pour le coach. Voir [résultat Mobile](../movee-mobile/codex/COACH_SHARED_PRESENTATION_MOBILE_RESULT.md) ; le sujet de navigation sélectionné n’est pas le propriétaire de toute fiche. Pas de sous-titre d’adhérent suggérant que Mon compte appartient à celui-ci. Les limites de recette restent celles du rapport.

Le paragraphe ancien « design system à valider » est dépassé pour la charte commune ; les autres contrats et gates restent à vérifier individuellement.

## Précisions UX communes aux parcours Mobile déjà validées

Bandeau supérieur, pied de navigation et cadre compact proviennent des métadonnées ; logo complet réservé au login, retour/titre/rafraîchissement uniques et modales sans navigation du bas. Le plafond demandé de trois clics concerne la navigation jusqu’au formulaire ou à l’action finale, hors choix métier et confirmations ; ne pas supprimer un choix de sujet ou un consentement pour le respecter. Les mesures de quelques parcours ne prouvent pas tous les parcours.

Planning coach limité aux séances qu’il encadre, pas à toutes les réservations de ses adhérents. Choix et changement d’espace explicites pour les affiliations cumulées ; anciennes lectures/sujets/aperçus invalidés au changement, journal et reçus préservés. Le sujet sélectionné reste visible hors modales quand utile, sans devenir l’identité du compte personnel.

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:423 -->

## 1. Sources et frontières entre projets

- `AGENTS.md` : règles de travail communes aux quatre projets ; ne pas le réécrire dans ce document.
- `MOVEE_APP_FUNCTIONAL_REFERENCE.md` : autorité sur les règles métier MOVEE App, notamment Q001–Q130 et B1–B8.
- `MOVEE_APP_TECHNICAL_REFERENCE.md` : autorité sur les contrats d'architecture du backend MOVEE App.
- `MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md` : autorité sur les parcours et exigences d'expérience du client MOVEE Mobile, **sans réinterpréter les règles métier serveur**.
- `MOVEE_MOBILE_TECHNICAL_REFERENCE.md` : autorité sur l'architecture du client mobile.
- MOVEE Biz : référentiels propres à consulter lorsqu'une intégration est réellement concernée ; aucun rôle, API ou contrat Biz n'est présumé.

**Principe :** une même capacité métier peut être présentée par plusieurs applications, mais la décision de réservation, les droits, le solde, le contrat et la sécurité sportive restent du ressort de MOVEE App. Toute divergence entre spécifications doit être signalée et arbitrée, jamais corrigée silencieusement dans un seul projet.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:434 -->

## 2. Vision de l'application

MOVEE Mobile est l'interface personnelle du réseau MOVEE sur iOS et Android. Elle offre une expérience **principalement conversationnelle**, enrichie de composants visuels structurés et de parcours classiques autonomes. Les deux profils prioritaires sont **adhérent** et **coach** ; une identité peut cumuler des rôles, et le contexte actif doit rester explicite (Q003, Q005).

L'assistant n'est ni le détenteur des données ni l'autorité métier. Il aide à consulter, préparer et demander des actions que le backend exécute ou refuse selon les permissions effectives. Une panne de l’IA ne doit pas rendre inutilisables les parcours classiques requis (B8.2), avec l’exception AR02 : pas de création/modification de programmes sans IA, mais consultation autorisée maintenue.


**Contrainte d'usage validée avec T7.8 : MOVEE Mobile n'est pas utilisé pendant les entraînements.** Il sert à consulter programmes, performances et historiques enregistrés, gérer réservations/plannings, échanger, utiliser l'assistant, traiter les notifications et gérer les informations personnelles autorisées. Les machines enregistrent les performances via MOVEE App indépendamment du téléphone. Aucun compteur de répétitions, suivi de séries en direct, chronomètre d'entraînement ou pilotage des machines n'est prévu ; ni continuité d'interface ni hors connexion ne sont justifiés par une reprise d'exercice physique.

### Registre des décisions validées — Thème 1

Décisions validées le 17 octobre 2026 ; leur validation ne vaut ni implémentation ni recette. Les contrats techniques restant à vérifier sont distingués dans les sections concernées.

| Référence | Décision | Statut |
| --- | --- | --- |
| T1.1 | Accueil conversationnel IA | Validée |
| T1.2 | Navigation contextuelle | Validée |
| T1.3 | Menu latéral coulissant | Validée |
| T1.4 | Affichage adaptatif | Validée |
| T1.5 | Bouton IA flottant | Validée |
| T1.6 | Conversation unique et continue | Validée |
| T1.7 | Zone d'informations prioritaires | Validée |
| T1.8 | Accueil de secours automatique | Validée |

### Registre des décisions validées — Thème 2

Décisions validées le 17 octobre 2026 ; les exigences ci-dessous ne constituent pas une preuve d'implémentation. Les contrats MOVEE App restant ouverts sont identifiés séparément.

| ID | Décision | Statut |
| --- | --- | --- |
| T2.1 | Inscription libre | Validée |
| T2.2 | Rattachement par demande ou invitation | Validée |
| T2.3 | Centre actif sélectionnable | Validée |
| T2.4 | Profil actif adhérent/coach | Validée |
| T2.5 | Session persistante et biométrie facultative | Validée |
| T2.6 | Réinitialisation par code e-mail intégré | Validée |
| T2.7 | Connexion avant vérification e-mail avec restrictions | Validée |
| T2.8 | Inscription minimale et profil progressif | Validée |
| T2.9 | Profil principalement conversationnel | Validée |
| T2.10 | Suppression autonome avec confirmation | Validée |

### Registre des décisions validées — Thème 3 : Parcours adhérent

Décisions validées le 17 octobre 2026. Leur validation décrit la cible fonctionnelle et les exigences induites ; elle ne prouve ni disponibilité des contrats backend, ni implémentation, ni recette.

| ID | Décision | Statut |
| --- | --- | --- |
| T3.1 | Consultation principalement conversationnelle de l'activité sportive | Validée |
| T3.2 | Réservation conversationnelle et calendrier classique sans IA | Validée |
| T3.3 | Déplacement d'une réservation sans annulation préalable imposée | Validée |
| T3.4 | Suivi automatique des séances par les machines | Validée |
| T3.5 | Performances expliquées et graphiques interactifs | Validée |
| T3.6 | Programme structuré et interactif dans la conversation | Validée |
| T3.7 | Adaptation distincte en entraînement libre ou suivi coach | Validée |
| T3.8 | Communication adhérent–coach via l'assistant | Validée |
| T3.9 | Coaching proactif personnalisé | Validée |
| T3.10 | Accompagnement adaptatif entre les séances | Validée |

### Registre des décisions validées — Thème 4 : Parcours coach

Décisions T4.1–T4.10 validées par l'utilisateur. Elles décrivent la cible et ses contraintes ; elles ne prouvent aucune implémentation ou disponibilité backend.

| ID | Décision | Statut |
| --- | --- | --- |
| T4.1 | Gestion conversationnelle des adhérents et répertoire interactif | Validée |
| T4.2 | Détection proactive et priorisation des adhérents | Validée |
| T4.3 | Création et modification entièrement conversationnelles des programmes — option A | Validée |
| T4.4 | Présentation proactive et validation groupée des propositions | Validée |
| T4.5 | Planning conversationnel et calendrier interactif | Validée |
| T4.6 | Configuration conversationnelle des disponibilités | Validée |
| T4.7 | Boîte de réception conversationnelle intelligente | Validée |
| T4.8 | Bilans sportifs intelligents et contextuels | Validée |
| T4.9 | Relance automatique des adhérents absents — option B | Validée |
| T4.10 | Autonomie graduée selon les conséquences | Validée |

### Registre des décisions validées — Thème 5 : Assistant IA

Décisions T5.1–T5.10 validées par l'utilisateur. Les besoins techniques et contrats ouverts restent distincts des capacités effectivement vérifiées ; aucune implémentation n'est attestée par ce registre.

| ID | Décision | Statut |
| --- | --- | --- |
| T5.1 | Mémoire sélective et contexte métier actualisé | Validée |
| T5.2 | Orchestration intelligente des demandes complexes | Validée |
| T5.3 | Recherche contextuelle et clarification minimale | Validée |
| T5.4 | Suivi contextuel avec résultats vérifiables | Validée |
| T5.5 | Récupération intelligente des erreurs et alternatives | Validée |
| T5.6 | Assistant sportif et bien-être élargi | Validée |
| T5.7 | Personnalisation adaptative avec contrôle utilisateur | Validée |
| T5.8 | Explications contextuelles et vérifiables | Validée |
| T5.9 | Conversation vocale bidirectionnelle en temps réel | Validée |
| T5.10 | Mémoire transparente et contrôlable par conversation | Validée |

### Registre des décisions validées — Thème 6 : Notifications et proactivité

Décisions T6.1–T6.10 validées par l'utilisateur. Les exigences cibles ne prouvent ni capacité backend, ni livraison push, ni intégration mobile opérationnelle.

| ID | Décision | Statut |
| --- | --- | --- |
| T6.1 | Notifications intelligentes intégrées à l'assistant | Validée |
| T6.2 | Préférences intelligentes et contextuelles | Validée |
| T6.3 | Priorisation intelligente et contextuelle | Validée |
| T6.4 | Proactivité autonome encadrée | Validée |
| T6.5 | Regroupement intelligent et synthèses personnalisées | Validée |
| T6.6 | Actions rapides et continuité conversationnelle | Validée |
| T6.7 | Messagerie intelligente et notifications contextualisées | Validée |
| T6.8 | Rappels intelligents et personnalisés | Validée |
| T6.9 | Confidentialité adaptative et configurable | Validée |
| T6.10 | Synchronisation intelligente et fiabilité renforcée | Validée |

### Registre des décisions validées — Thème 7 : Fiabilité, hors connexion et performance

Décisions T7.1–T7.10 validées par l'utilisateur. La clarification T7.8 exclut l'utilisation de MOVEE Mobile pendant les entraînements. Les exigences cibles ne démontrent ni stockage local, ni synchronisation, ni reprise déjà implémentés.

| ID | Décision | Statut |
| --- | --- | --- |
| T7.1 | Mode hors connexion intelligent | Validée |
| T7.2 | Résolution intelligente des conflits selon les règles métier | Validée |
| T7.3 | Synchronisation anticipative et configurable | Validée |
| T7.4 | Sécurité adaptative selon la sensibilité des données | Validée |
| T7.5 | Mises à jour intelligentes et compatibilité contrôlée | Validée |
| T7.6 | Continuité intelligente de l'activité | Validée |
| T7.7 | Résilience intelligente et assistance contextuelle | Validée |
| T7.8 | Expérience fluide et optimisation contextuelle | Validée |
| T7.9 | Compatibilité étendue avec adaptation progressive | Validée |
| T7.10 | Observabilité proactive et respectueuse de la confidentialité | Validée |

### Registre des décisions validées — Thème 8 : Accessibilité et expérience utilisateur

Décisions T8.1–T8.10 validées par l'utilisateur. Le cadrage documentaire comprend désormais **78 décisions validées sur huit thèmes** (8 + 7 × 10). Cette clôture ne démontre ni implémentation ni recette et n'autorise aucun développement.

| ID | Décision | Statut |
| --- | --- | --- |
| T8.1 | Accessibilité universelle et adaptative | Validée |
| T8.2 | Personnalisation intelligente et contrôlable | Validée |
| T8.3 | Intégration native contextuelle et facultative | Validée |
| T8.4 | Présentation intelligente et progressive | Validée |
| T8.5 | Recherche intelligente et accès contextuel | Validée |
| T8.6 | Accompagnement conversationnel et progressif | Validée |
| T8.7 | Retours intelligents et contextuels | Validée |
| T8.8 | Paramètres intelligents, conversationnels et centralisés | Validée |
| T8.9 | Assistance intelligente et contextualisée | Validée |
| T8.10 | Amélioration continue intelligente et respectueuse de la confidentialité | Validée |

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:577 -->

## 3. Profils et contexte

### 3.1 Adhérent

- Consulter son programme, ses séances, ses réservations, son historique et les informations auxquelles il a droit.
- Rechercher des créneaux, réserver, modifier et annuler selon les règles du backend.
- Consulter ses crédits et droits contractuels sans compteur client indépendant.
- Consulter les performances enregistrées automatiquement par les machines et dialoguer sur ses objectifs et ses adaptations dans les limites autorisées ; aucune saisie manuelle des séries, répétitions et charges n’est imposée pour les séances suivies par machines (T3.4). Les actions de saisie autorisées restent soumises au périmètre précisé en section 7.
- Consulter et répondre aux propositions et demandes de consentement.
- Recevoir des informations contextuelles et notifications autorisées.

**AR05.8 — B2B.** Administration entreprises/partenaires **hors Mobile** ; les adhérents bénéficiaires voient/utilisent leurs droits dans Mobile.

### 3.2 Coach

- Consulter les séances, programmes, adhérents et demandes relevant de ses affectations et permissions.
- Être informé des changements de programme, remplacements, restrictions, douleurs, demandes de réévaluation et priorités.
- Approuver, refuser ou amender les propositions nécessitant une décision humaine, via les actions métier autorisées.
- Consulter ses informations opérationnelles pertinentes ; aucune vue transversale du réseau n'est implicite.

### 3.3 Multi-rôle et périmètre

L'identité est unique côté MOVEE App. Le mobile doit afficher clairement le profil et le centre de contexte, lorsque plusieurs contextes sont autorisés. Un changement de profil ou de centre entraîne une actualisation des données et des capacités visibles. Les droits sont toujours revérifiés côté serveur ; masquer un bouton ne constitue pas une autorisation.

### 3.4 Inscription libre et progressive (T2.1, T2.8)

Toute personne peut créer un compte MOVEE depuis l'application avec une adresse e-mail et un mot de passe. Seuls le prénom, le nom, l'adresse e-mail et le mot de passe sont demandés initialement. Le téléphone, la date de naissance et les informations sportives ne sont pas imposés à l'inscription ; les compléments sont demandés progressivement lorsqu'ils deviennent nécessaires. L'inscription n'accorde aucun accès automatique aux données d'un centre. L'existence d'une API publique d'inscription dans MOVEE App reste à vérifier.

### 3.5 Vérification e-mail et rattachement (T2.2, T2.7)

L'utilisateur peut se connecter immédiatement après inscription, avant vérification de son adresse e-mail, avec des fonctionnalités limitées : il peut compléter son profil et découvrir l'application. La vérification e-mail est obligatoire avant le rattachement effectif à un centre et certaines opérations sensibles, dont la liste reste à préciser dans les contrats métier. MOVEE App applique ces restrictions ; un contrôle uniquement visuel côté mobile ne suffit pas. Le mécanisme de vérification e-mail reste à contractualiser, sans présumer qu'il utilise le code de récupération du mot de passe.

Deux méthodes de rattachement sont autorisées : rechercher un centre et demander son rattachement, ou accepter une invitation envoyée par un centre. Le centre conserve le contrôle des rattachements et des droits. Les règles exactes d'approbation et les API de recherche, demande et invitation doivent être vérifiées avec MOVEE App ; ni demande ni inscription ne valent rattachement effectif.

### 3.6 Centre et profil actifs (T2.3–T2.4)

Un utilisateur peut être rattaché à plusieurs centres et posséder les profils adhérent et coach. Il sélectionne son centre actif et son profil actif parmi les contextes autorisés par le serveur. Le contexte actif est le couple **centre + profil** ; changer l'un ou l'autre ne nécessite ni déconnexion ni nouvelle connexion.

Les données, actions, menu, accueil, informations prioritaires et assistant s'adaptent à ce couple. Le changement invalide les données liées au contexte précédent pour empêcher leur réutilisation dans le nouveau contexte ; les affiliations, rôles et permissions restent vérifiés côté MOVEE App. T1.6 conserve un fil unique par utilisateur : changer de contexte ne crée pas de nouveau fil, mais sa restitution doit respecter les droits et la confidentialité, selon un contrat encore à vérifier.

**AR03 — Centre contractuel unique, centres accessibles multiples, centre actif.** Le centre actif est un contexte opérationnel choisi, jamais une mutation contractuelle ; les droits et l'éligibilité sont revérifiés côté App à chaque action.

### 3.7 Connexion persistante et biométrie facultative (T2.5)

La première connexion utilise l'e-mail et le mot de passe. La session est maintenue de manière sécurisée pour éviter les reconnexions inutiles ; les éléments d'authentification sont conservés dans un stockage sécurisé mobile. Face ID, Touch ID ou la biométrie Android peuvent protéger facultativement l'accès local à l'application, sans remplacer l'authentification ni les autorisations serveur. Durée, expiration, renouvellement et révocation restent à contractualiser avec MOVEE App ; aucun mécanisme de renouvellement des tokens n'est supposé existant.

### 3.8 Réinitialisation du mot de passe intégrée (T2.6)

L'utilisateur demande un code temporaire à usage unique par e-mail, le saisit dans MOVEE Mobile, puis y définit son nouveau mot de passe. MOVEE App gère génération, validation, expiration, limitation des tentatives et sécurité. Les API correspondantes doivent être vérifiées avant implémentation ; aucune durée ni procédure serveur supplémentaire n'est présumée.

### 3.9 Profil principalement conversationnel (T2.9)

L'utilisateur consulte et modifie principalement ses informations personnelles et sportives avec l'assistant, à l'aide de cartes interactives et de formulaires structurés lorsque nécessaire. Les modifications passent par les API et règles métier MOVEE App, avec confirmations proportionnées à leur sensibilité. Les contenus détaillés et opérations complexes respectent les écrans dédiés de T1.4. Les paramètres essentiels — sécurité, confidentialité, notifications et déconnexion — restent accessibles par un parcours classique sans IA, y compris dans le secours T1.8.

### 3.10 Suppression autonome du compte (T2.10)

L'utilisateur peut demander la suppression de son compte depuis un parcours mobile accessible sans assistant. Une vérification d'identité et une confirmation explicite sont nécessaires. MOVEE App exécute les opérations autorisées : suppression des données éligibles et respect des obligations légales de conservation. Aucune suppression physique immédiate ni cascade SQL n'est présumée. Les modalités, API et effets sur les affiliations restent à contractualiser avec MOVEE App.

**AR05.9 — Portabilité.** Demande et export de données personnelles **via canal externe**, non intégrés au Mobile ; IA d'orientation uniquement ; App contrôle l'exécution.

La suppression de compte T2.10 reste un parcours mobile autonome sans IA ; elle est distincte de la demande/export de portabilité réalisés par canal externe selon AR05.9.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:639 -->

## 4. Accueil et proactivité

**T1.1 — Accueil conversationnel IA :** pour les adhérents comme pour les coachs, la conversation avec l'assistant est l'écran principal à l'ouverture lorsque l'IA est disponible. L'assistant peut accueillir spontanément l'utilisateur ; les fonctionnalités classiques restent accessibles indépendamment de l'IA. Le secours automatique est défini en section 11 (T1.8).

À l'ouverture, MOVEE Mobile peut présenter une synthèse contextualisée **sans attendre une question** : prochaine séance, changement pertinent, proposition à examiner, nouvelle disponibilité compatible, échéance ou alerte utile. L'accueil varie selon le profil et les permissions. Il ne doit ni divulguer d'information d'un autre utilisateur, ni annoncer comme certaine une disponibilité non confirmée par le backend.

Exemples de formulations cibles :

- Adhérent : « Une place compatible avec ton offre s'est libérée dans ton centre. Veux-tu voir le créneau ? »
- Coach : « Une demande de réévaluation prioritaire nécessite ton attention. »

**L'information proactive n'exécute jamais d'elle-même une réservation ou une décision sensible.** Le système évite les répétitions inutiles et respecte les préférences de notification.

### 4.1 Zone d'informations prioritaires (T1.7)

Une zone compacte en haut de l'accueil conversationnel présente les informations importantes et pertinentes pour le contexte utilisateur. Ces informations peuvent être ouvertes ou masquées ; la zone reste distincte de l'historique conversationnel. Son contenu provient des données et règles métier autorisées côté serveur. Le contrat de fourniture et de priorisation reste à vérifier avec MOVEE App ; aucun nouvel endpoint ni mécanisme de priorisation n'est présumé validé.

### 4.2 Navigation contextuelle et menu latéral (T1.2–T1.3)

Aucune barre d'onglets permanente : la conversation occupe l'écran principal. Un bouton de menu ouvre un panneau latéral coulissant donnant directement accès aux écrans métier. Le menu adapte ses rubriques au profil actif, adhérent ou coach, et aux permissions et capacités déterminées par le serveur ; le mobile n'invente aucun droit. Il se referme après sélection d'une rubrique et reste accessible et utilisable sur iOS et Android, y compris lorsque l'IA est indisponible.

### 4.3 Recherche et accès contextuel (T8.5)

Combiner recherche conversationnelle, recherche textuelle classique, menu latéral et raccourcis contextuels. Adapter les suggestions au rôle et au centre actifs, avec résultats issus exclusivement des données accessibles et alternative fonctionnelle sans IA. Recherche d'adhérent autorisé, dernières performances et accès à une fonctionnalité sont des exemples, sans API de recherche globale présumée. Aucune recherche locale ne contourne les permissions serveur.

### 4.4 Découverte progressive et facultative (T8.6)

Accueillir selon rôle actif et contexte disponible, présenter les principales possibilités de l'assistant, proposer de premières actions concrètes et des conseils au moment pertinent. La découverte reste progressive, sans tutoriel obligatoire : l'utilisateur peut l'ignorer puis la reprendre. Alternative classique sans IA, respect des affiliations/permissions, aucun blocage de fonction autorisée ni annonce de capacité non activée ou interdite. Aucun système persistant de progression d'onboarding n'est présumé.

### 4.5 Parrainage

**AR05.6 — Parrainage.** Lien/code partageable, invitations, suivi et avantages via IA ; éligibilité et récompenses exclusivement calculées/attribuées par App.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:672 -->

## 5. Conversation et composants visuels

L'interface principale associe messages utilisateur/assistant et cartes structurées :

- Créneaux, disponibilités et alternatives.
- Réservations, conséquences d'annulation, confirmations et reçus.
- Programmes, exercices, séries, performances et historique.
- Propositions de modification, périmètre ponctuel/durable, protections et demandes d'accord.
- Alertes, demandes au coach, états de traitement et priorités.

Les informations chiffrées et statuts doivent provenir des résultats métier vérifiés. L'assistant peut poser une **question ciblée** en cas d'ambiguïté déterminante, mais n'exige pas une confirmation systématique pour les consultations autorisées (B8.4, B8.6, B8.8).

**T1.4 — Affichage adaptatif :** les informations simples s'affichent directement dans le fil, éventuellement sous forme de cartes interactives. Les contenus détaillés et les opérations complexes utilisent des écrans dédiés, ouverts directement depuis le menu ou les cartes de l'assistant. Les composants métier sont réutilisables entre conversation et écrans classiques ; les validations et confirmations métier de MOVEE App restent applicables.

**T1.5 — Retour à l'assistant :** les écrans métier disposent d'un bouton IA flottant, discret et identifiable, qui ramène directement à la conversation en conservant l'historique et le contexte disponibles. La navigation arrière classique reste utilisable ; l'indisponibilité IA suit le comportement de secours défini en section 11.

**T1.6 — Conversation unique et continue :** chaque utilisateur dispose d'un seul fil, sans liste de conversations multiples ni création manuelle de nouveaux fils. Il retrouve les échanges précédents en remontant dans le fil. Un changement d'écran ne réinitialise pas la conversation. La persistance et la récupération de l'historique doivent être vérifiées et contractualisées avec MOVEE App avant implémentation ; les API actuelles ne sont pas présumées les permettre. Les règles de confidentialité et de changement de contexte restent applicables.

### 5.1 Confirmation proportionnée

- **Consultation :** exécution directe si l'utilisateur est autorisé.
- **Action ordinaire :** respecter les validations et consentements métier nécessaires, sans étape redondante.
- **Action sensible ou irréversible :** présenter conséquences exactes, destinataire, périmètre et demander un accord explicite.
- **Proposition en attente :** distinguer « proposée », « acceptée », « appliquée » et « échouée ». Un accord ne vaut jamais succès backend.

### 5.2 Reprise et erreurs

Après timeout, fermeture, perte réseau ou indisponibilité IA, afficher l'état connu, récupérer le résultat confirmé et proposer une reprise sûre. Ne jamais réémettre aveuglément une commande qui pourrait débiter, réserver ou modifier deux fois. En cas de conflit, montrer le nouvel état et demander une nouvelle validation si les conséquences changent (B8.1, B8.9–B8.10).

### 5.3 Mémoire sélective et personnalisation (T5.1, T5.7)

L'assistant personnalise durablement ses échanges à partir des messages récents, des informations durables pertinentes — objectifs, préférences et contraintes exprimées — et des données métier actualisées de MOVEE App. L'historique complet du fil unique T1.6 reste consultable sans devoir être envoyé intégralement au modèle à chaque interaction. Aucun stockage de mémoire, résumé ou système de récupération existant n'est présumé.

La mémoire ne détermine jamais permissions, centre ou rôle actifs : ils proviennent du contexte authentifié et des contrôles MOVEE App (T2.3/T2.4). L'assistant adapte vocabulaire, ton, niveau technique, longueur et détail des réponses au rôle autorisé, à l'expérience sportive, aux préférences exprimées et au contexte. L'utilisateur peut demander explicitement « Sois plus concis » ou « Explique-moi cet exercice comme à un débutant ». Cette personnalisation ne modifie ni droits, ni règles métier, ni validations obligatoires ; le contrôle des informations durables est décrit en section 12.1.

**AR06 — Historique IA durable et mémoire sélective.** Historique, contexte éphémère et mémoire personnalisée distincts ; contrôle de consultation/correction/suppression et vérification des droits à chaque accès. Les données métier officielles demeurent dans MOVEE App.

### 5.4 Demandes complexes et clarification minimale (T5.2–T5.3)

Une demande peut contenir plusieurs intentions, par exemple consulter les progrès de Sophie sur trois mois, adapter son programme si nécessaire et la prévenir. L'assistant identifie les opérations et leurs dépendances, exécute les consultations et actions autorisées, demande une validation uniquement si nécessaire, puis poursuit selon les résultats précédents. Le bilan distingue ce qui est réalisé, en attente ou en échec. MOVEE App conserve permissions, validations et opérations métier ; aucun moteur multi-actions existant n'est présumé.

T4.10 reste applicable : pas de confirmation systématique, relances autorisées T4.9 possibles sans accord systématique du coach, mais une adaptation d’un programme supervisé dans les limites préautorisées par le coach peut être appliquée avec consentement de l’adhérent ; hors cadre, exercice protégé, objectif global ou restriction de sécurité, la validation coach reste requise (AR01, T3.7/T4.4). L'envoi d'une information sur une modification ne doit pas présumer son application ; l'origine des messages humains et IA reste distinguée selon T3.8/T4.7.

Face à une demande incomplète, exploiter d'abord conversation, préférences disponibles, données métier, disponibilités réelles et possibilités autorisées. Proposer des options pertinentes ; demander seulement une précision indispensable impossible à déterminer fiablement. Ne jamais inventer disponibilité, préférence ou donnée manquante, ni présenter une hypothèse comme confirmée.

### 5.5 Avancement, résultats et récupération (T5.4–T5.5)

Adapter le suivi à la complexité : indicateur discret pour une opération simple ; étapes importantes pour une demande complexe avec présentation « En cours », « Terminée », « En attente de validation » ou « En échec ». Ce sont des besoins de présentation, pas un protocole d'exécution ni des statuts backend inventés. Une proposition ou action en attente n'est jamais présentée comme exécutée ; seul un résultat effectif MOVEE App autorise à annoncer sa réalisation.

En cas d'échec, identifier sa nature à partir des informations disponibles, expliquer simplement, rechercher des alternatives et proposer correction ou nouvelle tentative sécurisée si approprié. Un créneau devenu indisponible peut ainsi conduire à rechercher d'autres créneaux. Ne jamais rejouer aveuglément une opération pouvant produire un doublon ; si son résultat est incertain, le vérifier côté App avant toute nouvelle tentative. Les contrats d'idempotence, reprise et vérification d'état restent à vérifier, sans présumer leur disponibilité.

### 5.6 Expertise sportive et explications vérifiables (T5.6, T5.8)

L'assistant est spécialisé sport et bien-être : entraînement, nutrition, récupération, habitudes de vie et connaissances utiles à la pratique sportive. Il peut répondre à ces questions générales même sans fonctionnalité métier correspondante, sans devenir un assistant généraliste tous domaines. Distinguer ces réponses informatives des actions modifiant les données métier. Les conseils santé restent prudents, sans remplacer diagnostic ou avis médical ; le circuit de sécurité existant reste applicable.

Une recommandation peut être accompagnée d'une justification courte, avec davantage de détails ou les indicateurs utilisés sur demande. Distinguer explicitement faits vérifiés, hypothèses et recommandations. Affirmer une stagnation, par exemple, exige des données qui la justifient réellement ; aucune mesure, résultat, critère métier ou justification n'est inventé. Les explications restent compréhensibles, sans données non autorisées ni détails techniques internes inutiles.

### 5.7 Conversation vocale temps réel (T5.9)

Adhérents et coachs disposent d'une cible de conversation vocale naturelle bidirectionnelle en temps réel : réponses orales, interruption de l'assistant pendant sa réponse et passage libre texte/voix. Le contexte et la continuité des échanges du fil unique sont conservés lors de cette bascule. Les fonctionnalités métier autorisées restent accessibles avec les mêmes permissions et validations quel que soit le mode d'interaction.

Reconnaissance et synthèse vocales, transport temps réel, latence, interruptions, permissions natives et microphone, capture/restitution audio, confidentialité, interruptions système/réseau et repli vers le texte doivent être étudiés pour iOS/Android. Aucune technologie, bibliothèque, fournisseur, SDK, API de streaming ou connexion directe mobile-service IA n'est sélectionné ou présumé. Le mode vocal ne modifie ni les frontières d'architecture ni le secours sans IA T1.8.

### 5.8 Présentation progressive et retours accessibles (T8.4, T8.7)

Présenter l'essentiel en priorité : cartes et composants interactifs, graphiques compréhensibles, détails développables et écrans dédiés aux contenus complexes. Conserver le contexte du fil lors de la navigation et la consultation détaillée sans IA. Respecter l'accessibilité (section 12.2), sans masquer ni déformer les données métier, toujours cohérentes avec App.

Adapter les retours aux conséquences : discret pour une opération simple, traitement en cours, confirmation effective, refus ou attente locale ; progression contextualisée et prochaines étapes pour le complexe. Les retours sont accessibles aux technologies d'assistance et respectent la réduction des animations. Confirmations explicites seulement lorsque justifiées. Une opération métier n'est réussie qu'après confirmation App ; une action locale en attente ou une proposition approuvée ne prouvent pas l'application effective (T5.4/T7.1/T7.7).

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:741 -->

## 6. Parcours adhérent : réservation et crédits

**T3.1 — Consultation de l'activité sportive :** l'adhérent demande principalement à l'assistant ses prochaines séances, son programme, son historique ou ses performances, avec des composants interactifs dans la conversation. Aucun tableau de bord général supplémentaire « Mon activité » n'est prévu. Les parcours classiques nécessaires restent accessibles sans IA, selon T1.2–T1.4 et T1.8.

### 6.1 Recherche et réservation

- Réserver **un créneau de séance dans un centre**, non une machine individuelle (B1).
- Présenter uniquement des alternatives compatibles avec offre, droits intercentres, capacité, horaires, coach et contraintes métier.
- Permettre la recherche de créneaux proches ; les alternatives suivent les règles B4 (jusqu'à trois options proches dans un horizon de sept jours pour le scénario concerné).
- Afficher les conditions et conséquences avant l'engagement, puis le résultat confirmé par MOVEE App.

**T3.2 — Réservation principalement conversationnelle :** une demande telle que « Trouve-moi une séance demain soir » conduit à des disponibilités présentées en cartes ou calendrier interactif dans la conversation. Un calendrier classique reste accessible sans IA. MOVEE App détermine les disponibilités, crédits, autorisations et règles de réservation ; le rendu mobile ne les recalcule pas.

### 6.2 Crédits

- Solde et mouvements fournis par MOVEE App ; source métier : ledger `session_credit_transactions`.
- Allocation selon les règles B2 : abonnement, pack, unitaire ; expiration la plus proche puis ancienneté à priorité égale.
- Crédits immobilisés lors de la réservation, consommés à la séance réalisée, restitués selon les règles d'annulation.
- **Règle essentielle Q011/B2 :** validité vérifiée **au moment de la réservation**. Une réservation confirmée reste valable si les crédits immobilisés expirent avant la séance.
- Le mobile ne calcule jamais seul un solde opposable ni ne déduit l'éligibilité d'une simple date affichée.

**AR05.2 — Abonnements.** Consultation et demandes conversationnelles de souscription, renouvellement ou modification ; **accord explicite** avant engagement financier/contractuel ; exécution App.

### 6.3 Modification, annulation, absence

- Présenter délais, pénalités et restitution tels que calculés par le Service métier (B3).
- Une séance commencée ne peut être annulée ou déplacée par l'adhérent.
- Une annulation par centre/coach suit les règles de restitution et d'alternatives ; pas de substitution imposée.
- No-show distinct d'une annulation, avec traitement contractuel et exceptions auditées.

**T3.3 — Déplacement d'une réservation :** l'adhérent peut demander « Décale ma séance de mardi à jeudi ». L'assistant recherche les alternatives et accompagne la modification sans imposer d'annulation préalable. MOVEE App garantit la cohérence des disponibilités, crédits et règles métier. Le contrat backend de déplacement, notamment ses garanties de cohérence et d'atomicité, reste à vérifier avant développement ; aucune API atomique n'est présumée. Le client ne simule pas le déplacement par une annulation suivie d'une nouvelle réservation.

### 6.4 Remplacement du coach

Une proposition active à la fois, créneau temporairement retenu selon la politique, information claire, accord explicite de l'adhérent et expiration non réactivable automatiquement (B5). Le refus ouvre les suites métier prévues, sans remplacement automatique.

### 6.5 Orientation vers le canal marketplace

**AR05.7 — Marketplace.** **Hors Mobile** : ni boutique, panier ni achat ; l'IA peut orienter vers le canal commercial distinct, sans transaction.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:781 -->

## 7. Parcours sportif : programme, séance, performances

- Consulter le programme applicable, ses objectifs, exercices, séries, repos et éventuelles restrictions, sous réserve des données disponibles.
- Pour les séances suivies par machines, consulter les informations d’entraînement et performances enregistrées automatiquement dans MOVEE App, sans imposer de saisie manuelle des séries, répétitions et charges (T3.4). Les actions de saisie autorisées déjà documentées ne constituent pas une obligation de saisie mobile ; leur périmètre éventuel hors suivi machine reste à vérifier. Afficher les valeurs réellement enregistrées.
- Consulter l'historique sportif réseau dans le périmètre permis (Q032–Q033).
- Proposer des changements compatibles d'exercice, charge, répétitions, séries, repos et organisation, avec contrôle backend (Q029–Q031, B6–B7).
- Distinguer les périmètres métier de modification ponctuelle d’une séance et de modification durable des prochaines séances ; demander une clarification si nécessaire (B7.2). Ces règles MOVEE App ne décrivent pas un usage mobile pendant l’entraînement (T7.8).
- Règle métier MOVEE App conservée : pour une séance en cours, seuls les exercices non commencés peuvent être modifiés dans le cadre autorisé ; protéger les décisions verrouillées par le coach. Elle ne crée aucun parcours mobile en direct pendant la séance (T7.8).
- Conserver l'historique et afficher l'origine et la portée des versions ; ne pas écraser une modification concurrente (B7.5–B7.7).
- Les parcours machines connectées, QR/NFC, réglages, bilans et analyse multimodale relèvent de la cible produit Q026–Q057, **sans présumer leur disponibilité dans les API actuelles**. Les bilans corporels et de mobilité peuvent impliquer MOVEE Motion, projet matériel distinct : la restitution mobile de ces bilans est validée par AR07 ; son contrat d’échange, l’origine et la validation des mesures restent à vérifier avant réalisation.

### 7.1 Suivi automatique et présentation des performances (T3.4–T3.5)

Pendant une séance suivie par machines, les machines enregistrent automatiquement les informations d'entraînement et les performances dans MOVEE App : c'est une cible validée, sans attestation d'intégration machine opérationnelle. MOVEE Mobile consulte les informations enregistrées et centralisées par MOVEE App en dehors de l'entraînement ; l'enregistrement machine est indépendant de son utilisation. Aucun protocole machine, interface de communication ou contrat de synchronisation n'est défini ici.

L'assistant explique les performances à partir des données et calculs métier de MOVEE App. La présentation mobile comprend des graphiques interactifs pouvant montrer évolution, comparaison entre séances et indicateurs adaptés aux exercices et objectifs. Les calculs métier restent côté App ; le mobile est responsable de la présentation et n'invente ni mesure ni indicateur absent.

**AR07 — Mesures externes, résultats mobiles.** MOVEE Motion/dispositifs spécialisés acquièrent les mesures ; MOVEE App centralise les résultats validés et droits ; MOVEE Mobile restitue bilans et évolutions, sans connexion directe aux appareils.

### 7.2 Programme conversationnel structuré (T3.6)

Le programme est présenté de façon structurée et interactive dans la conversation : séances, exercices, objectifs et consignes, détails développables et accès aux démonstrations disponibles. L'adhérent peut interroger l'assistant sur un exercice. MOVEE App reste responsable des programmes et prescriptions ; la disponibilité des démonstrations et des données doit être vérifiée. Les écrans détaillés et les accès classiques sans IA définis au thème 1 sont conservés.

### 7.3 Modification selon le mode d'entraînement (T3.7)

Les deux comportements suivants sont distincts :

- **Entraînement libre :** l’assistant peut adapter directement le programme selon les objectifs et demandes de l’adhérent, avec son consentement et dans les limites de sécurité et des protections B6–B7. Le coach est notifié de la modification.
- **Programme suivi par un coach :** l’assistant peut appliquer une adaptation dans les limites préautorisées par le coach avec consentement de l’adhérent. Hors limites, exercices protégés, objectifs globaux ou restrictions de sécurité, il prépare la demande soumise à validation coach selon les règles métier (AR01).

Le mode d'entraînement, les autorisations, validations et l'application effective relèvent de MOVEE App, jamais d'un choix libre du frontend ou du modèle IA. Les protections, restrictions de douleur, concurrence et limites de modification en cours de séance déjà documentées restent applicables. Aucun nouveau statut, table ou contrat de proposition n'est créé ici : la compatibilité des mécanismes backend avec ces deux cas reste à vérifier avec MOVEE App.

**AR01 — Autonomie encadrée des adaptations de programme supervisé.** L'IA peut appliquer une adaptation **dans les limites préautorisées par le coach** avec consentement de l'adhérent ; hors limites, exercices protégés, objectifs globaux ou restrictions de sécurité : validation coach selon les règles métier. Cette précision prévaut sur toute formule exigeant une approbation coach pour chaque adaptation.

### 7.4 Communication adhérent–coach via l'assistant (T3.8)

La communication passe principalement par l'assistant : par exemple « Dis à mon coach que je souhaite augmenter la fréquence de mes entraînements ». L'assistant transmet la demande et restitue la réponse du coach dans la conversation de l'adhérent. Distinguer clairement une réponse produite par l'IA, un message effectivement envoyé au coach et une réponse provenant du coach. Ne pas annoncer une transmission à partir du seul texte généré.

MOVEE App gère les autorisations, la transmission et l'historisation des échanges. Envoyer au nom de l'utilisateur exige de respecter les autorisations et confirmations applicables, proportionnées selon la section 5.1 ; aucun droit d'envoi implicite ni mécanisme existant n'est présumé.

### 7.5 Coaching proactif et accompagnement entre séances (T3.9–T3.10)

L'assistant suit les objectifs et performances enregistrées automatiquement. Un événement pertinent — objectif atteint, stagnation, progression remarquable ou baisse de régularité — peut déclencher une intervention dans la conversation et, selon les préférences applicables, une notification. Les critères de détection et règles métier relèvent de MOVEE App ; aucun seuil ni moteur de détection n'est inventé côté mobile.

L'accompagnement s'adapte notamment à une reprise après absence, une baisse de régularité, des entraînements rapprochés, un besoin de récupération ou un signalement de fatigue. L'assistant peut poser des questions ciblées et proposer des conseils personnalisés, sans questionnaire systématique ni intervention intrusive. Respecter les préférences de notification ; les conseils ne remplacent pas un avis médical et ne contournent pas le circuit de sécurité de la section 8.

### 7.6 Communauté et événements

**AR05.5 — Communauté.** Groupes, échanges et événements autorisés, avec recherche IA, confidentialité et modération App ; pas de réseau social généraliste.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:831 -->

## 8. Douleur, restrictions et réévaluation

Le circuit de sécurité MOVEE App ci-dessous reste applicable lorsqu'une douleur survient pendant un exercice ; il ne suppose pas l'utilisation du mobile pendant l'entraînement. MOVEE Mobile peut restituer les informations autorisées et les suites du signalement hors entraînement, sans inventer un parcours temps réel (T7.8).

En cas de douleur signalée pendant un exercice :

- Le circuit métier impose l'interruption de l'exercice concerné et les consignes de sécurité prévues ; leur restitution mobile ne constitue pas un pilotage de machine ni un écran d'entraînement en direct. Ne pas proposer automatiquement un remplacement de cet exercice.
- Transmettre l'événement au circuit métier, informer le coach et maintenir la restriction jusqu'à décision autorisée.
- Ne pas produire de diagnostic médical ni réintroduire l'exercice sans réévaluation.
- Afficher état, priorité, historique et échéance des demandes dans les limites de confidentialité.
- Priorités validées : **Normal, Prioritaire, Élevé** ; un passage à Élevé doit entraîner le push immédiat au coach lorsque le transport est disponible (B6.64–B6.68).
- Permettre la contestation sans effacer l'historique ni suspendre la restriction ; une nouvelle douleur est toujours un nouvel événement de sécurité.
- Les signes d'alerte graves relèvent d'une orientation urgente, sans prétention de prise en charge médicale automatisée.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:845 -->

## 9. Parcours coach

Le coach doit pouvoir, dans son périmètre autorisé :

- Consulter ses rendez-vous et informations de séance pertinentes.
- Lire les demandes de modification, réévaluation, remplacement, contestation et restrictions.
- Répondre aux propositions qui nécessitent son approbation, avec justification lorsque requise.
- Voir rapidement les changements effectués par l'IA et recevoir les synthèses prévues (B7.8).
- Définir ou ajuster des protections, plafonds et critères de progression via les actions métier prévues, lorsque l'API les expose.
- Être alerté des situations urgentes sans multiplication de notifications non nécessaires.

**Limite :** la disponibilité de chaque action coach sur API mobile doit être auditée ; une exigence fonctionnelle n'est pas la preuve d'un endpoint existant.

### 9.1 Adhérents et priorités (T4.1–T4.2)

Le coach consulte et gère principalement ses adhérents par conversation : « Montre-moi mes adhérents », « Affiche le programme de Sophie » ou « Quels adhérents ne sont pas venus depuis deux semaines ? ». L'assistant présente listes, fiches et indicateurs interactifs. Un répertoire dédié reste accessible pour les recherches complexes, les filtres et les consultations sans IA. Les données dépendent des permissions du coach et du contexte actif centre + rôle, correspondant au centre + profil du thème 2.

L'assistant identifie spontanément les situations nécessitant son attention : absences prolongées, stagnation, progression remarquable, demandes en attente et échéances importantes. Il les présente par priorité avec des cartes interactives, notamment à l'ouverture, en cohérence avec la zone prioritaire T1.7. Données, critères de détection et autorisations relèvent de MOVEE App ; aucun mécanisme opérationnel de détection n'est présumé.

### 9.2 Création et modification des programmes (T4.3 — option A)

Le coach conçoit et modifie entièrement les programmes en langage naturel, par exemple : « Prépare un programme de renforcement pour Sophie, trois séances par semaine, avec un accent sur le haut du corps ». L'assistant prépare une proposition dans la conversation et accepte les demandes successives d'ajustement. Le coach peut consulter le programme proposé avant application. Les composants interactifs servent à la présentation ; aucun éditeur de programme obligatoire ne remplace ce parcours conversationnel.

MOVEE App assure validation métier, autorisation, application et enregistrement. La proposition reste distincte du programme effectivement appliqué. AR02 clôt l’alternative d’écriture sans IA : création et modification de programmes exclusivement via IA ; en cas d’indisponibilité IA, seule leur consultation autorisée reste disponible. C’est l’exception explicite à B8.2 ; aucun éditeur classique de création/modification n’est prévu. Les autres parcours classiques requis restent conservés.

**AR02 — Création et modification de programme uniquement via IA.** En cas d'indisponibilité IA, consultation autorisée mais aucune création/modification. **Exception explicite à B8.2** ; les autres parcours classiques restent requis selon leur périmètre.

### 9.3 Propositions et validation groupée (T4.4)

L'assistant signale proactivement les propositions de modification de programme en attente. Les cartes permettent d'accepter, refuser, demander des ajustements ou sélectionner plusieurs propositions pour les valider ensemble. **Chaque proposition sélectionnée doit être explicitement validée avant son application.** La validation groupée facilite l'interface sans supprimer aucun contrôle individuel.

MOVEE App vérifie les permissions, l'état de chaque proposition et ses conditions d'application, et historise les décisions. Une sélection ne vaut ni validation ni succès backend ; aucun mécanisme de validation groupée existant n'est présumé. Conformément à AR01/T3.7, seules les adaptations hors limites préautorisées, les exercices protégés, les objectifs globaux ou restrictions de sécurité suivent la validation coach requise. Une adaptation dans le cadre préautorisé conserve le consentement adhérent. Le circuit distinct d'entraînement libre avec notification coach reste conservé.

### 9.4 Planning et disponibilités (T4.5–T4.6)

Le coach consulte et organise principalement son planning en langage naturel : planning de demain, créneaux disponibles vendredi ou déplacement du rendez-vous avec Sophie. L'assistant affiche cartes et calendriers interactifs ; un calendrier classique reste disponible pour les vues globales et sans IA. MOVEE App gère disponibilités, conflits, réservations et règles de modification.

Le coach définit aussi ses horaires habituels, exceptions, indisponibilités et congés par conversation, par exemple « Je travaille du lundi au vendredi de 9 h à 18 h » ou « Je suis absent du 12 au 16 novembre ». Avant application, l'assistant présente le calendrier résultant et les éventuels conflits pour permettre au coach de vérifier les changements. Un écran classique reste accessible sans IA. MOVEE App contrôle les autorisations, conflits horaires et conséquences sur les séances existantes ; aucune replanification ni annulation automatique n'est présumée.

### 9.5 Boîte de réception conversationnelle (T4.7)

L'assistant présente spontanément les messages importants des adhérents. Il peut regrouper les demandes par adhérent, prioriser les messages, résumer les échanges, aider à répondre en langage naturel et accompagner le traitement successif de plusieurs demandes. La conversation IA reste l'interface principale ; une consultation classique des échanges est disponible sans IA.

Distinguer les messages des adhérents, les messages réellement envoyés par le coach et les contenus/suggestions générés par l'assistant. MOVEE App assure transmission, permissions et historisation. Les actions ayant des conséquences respectent les confirmations contextuelles applicables (section 5.1, T4.10), sans assimiler suggestion ou texte généré à un envoi effectif ; cette exigence complète T3.8.

### 9.6 Bilans sportifs contextuels (T4.8)

L'assistant prépare un bilan lorsque pertinent : fin de cycle, objectif atteint, stagnation ou demande explicite du coach. Il peut présenter synthèse des résultats, graphiques d'évolution, comparaisons entre périodes et pistes d'adaptation du programme. Le coach peut commenter, ajuster et valider le bilan avant de le partager avec l'adhérent.

Les performances machine sont centralisées dans MOVEE App, qui reste responsable des données, indicateurs et règles de déclenchement. Aucun moteur opérationnel de génération ou de partage n'est présumé. Ces bilans sportifs ne présument aucun contrat matériel MOVEE Motion.

**AR05.1 — Bilans sportifs.** Adhérent : consultation, évolution, explications IA ; coach autorisé : création, complément, modification et validation **conversationnels** via Services App. Acquisition des mesures externe.

### 9.7 Relance automatique et autonomie graduée (T4.9 — option B ; T4.10)

Lorsqu'un adhérent est absent ou annule tardivement, l'assistant peut intervenir automatiquement pour comprendre la situation, proposer une nouvelle séance et accompagner une nouvelle réservation selon les règles applicables. Le coach n'est pas sollicité systématiquement avant chaque relance. Respecter les préférences de notification et les règles métier ; MOVEE App détermine absences, annulations tardives, droits, réservations et éventuelles conséquences sur les crédits. **Une absence ne se déduit jamais de la seule absence de données machine.** Aucun seuil, délai de relance ou canal obligatoire n'est défini ici.

L'autonomie dépend des conséquences : consultations directement exécutées si autorisées, sans confirmation inutile ; actions courantes explicitement autorisées pouvant s'exécuter automatiquement, notamment les relances T4.9 ; actions sensibles ou à conséquences importantes soumises à validation contextuelle avant exécution. Les adaptations IA de programmes supervisés suivent AR01 : consentement de l’adhérent dans les limites préautorisées par le coach ; validation coach requise hors cadre et pour protections, objectifs globaux ou restrictions de sécurité.

Classification des actions, permissions, validations et exécution effective relèvent de MOVEE App. Cette autonomie ne vaut ni autorisation générale de l'IA, ni confirmation systématique de toute action, ni réservation sans les accords métier requis. La proactivité informative de la section 4 reste sans effet métier par elle-même ; seules les actions automatiques explicitement autorisées par le serveur peuvent produire leurs effets.

### 9.8 Contrats et rémunération coach

**AR05.3 — Rémunération coach.** Consultation des contrats, commissions, rémunérations, factures et paiements autorisés ; explication IA et signalement d'anomalies ; pas de gestion comptable complète dans Mobile.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:910 -->

## 10. Notifications et préférences

Deux canaux complémentaires, précisés par les trois moyens d’accès T6.1 ci-dessous :

1. **Dans l'application :** informations contextuelles et notifications consultables selon les droits.
2. **Push hors application :** notifications aux appareils autorisés, même lorsque MOVEE Mobile est fermé, après raccordement d'un fournisseur réel et selon les préférences/consentements.

Cas prioritaires : place libérée, réservation modifiée, proposition de remplacement, décision sur programme, alerte de sécurité ou demande coach prioritaire. La présence d'une notification en outbox ne prouve pas sa réception sur téléphone. Éviter les données sensibles dans l'aperçu de l'écran verrouillé.

### 10.1 Trois accès complémentaires (T6.1)

Pour adhérents et coachs : push sur téléphone y compris application fermée, centre de notifications classique dans l'application, informations proactives dans la conversation IA. Une notification peut ouvrir son contexte et permettre de demander une action. Le centre et la conversation peuvent représenter le même événement de différentes façons sans créer plusieurs événements métier indépendants. Notifications consultables et utilisables sans assistant IA, via les accès classiques autorisés ; l'indisponibilité du backend reste distincte du secours IA T1.8.

Le push informe : il n'est ni preuve d'exécution ni source de vérité. Sa non-réception n'efface pas les événements consultables centralisés par MOVEE App. La zone prioritaire T1.7 et le fil unique T1.6 restent conservés.

### 10.2 Préférences, priorités et proactivité (T6.2–T6.4)

L'utilisateur personnalise catégories d'événements, canaux, périodes de tranquillité, fréquence et pertinence ; un réglage classique reste disponible sans IA. L'assistant peut adapter fréquence et pertinence aux préférences exprimées, habitudes fiables et contexte sportif, mais **les préférences explicites priment sur toute adaptation automatique**, sous réserve de l’exception de sécurité Élevé validée par AR04 aux heures de tranquillité MOVEE, sans contournement des autorisations OS. Catégories, canaux et paramètres précis restent à contractualiser avec App, sans nomenclature technique présumée.

La priorité dépend de la nature de l'événement, de son urgence réelle, du contexte, des préférences et des règles métier App : une urgence peut être transmise rapidement, une information secondaire différée ou regroupée. Une place pour une séance imminente peut être plus prioritaire qu'une place la semaine suivante ; cet exemple ne fixe pas de règle. Priorités, exceptions et éventuels contournements des périodes de tranquillité sont définis et contrôlés par App, jamais librement par l'IA. Aucune catégorie d'urgence réglementaire ni exception nouvelle n'est inventée.

L'assistant peut détecter des événements pertinents et déclencher automatiquement des notifications personnalisées autorisées : objectif atteint, stagnation fondée sur des données fiables, irrégularité, opportunité de réservation ou situation coach. Aucune validation humaine systématique n'est requise pour chaque notification autorisée ; permissions, préférences, fréquence, priorité et règles App restent obligatoires. Aucun moteur existant n'est présumé. L'absence ne se déduit pas du seul manque de données machine.

Notifier ne donne pas implicitement le droit d'agir : adaptations de programmes supervisés soumises à AR01 et aux validations requises selon leur cadre (T3.7/T4.4), relances automatiques autorisées (T4.9), autonomie graduée et confirmations contextuelles (T4.10/T5.2) restent inchangés. Les niveaux de sécurité et le push immédiat au passage Élevé de la section 8 restent conservés ; AR04 valide l’exception aux périodes de tranquillité MOVEE pour le passage Élevé, sous les autorisations et restrictions iOS/Android et sans garantie de réception. Les modalités techniques restent à vérifier avec App.

**AR04 — Push immédiat pour alerte de sécurité Élevé.** Exception aux heures de tranquillité configurées dans MOVEE, mais **jamais** aux refus/autorisations/restrictions iOS/Android ; émission ≠ livraison garantie. Les autres notifications respectent les préférences.

### 10.3 Regroupement et synthèses (T6.5)

Les notifications non urgentes peuvent être regroupées par catégorie, pertinence, proximité temporelle et contexte métier. L'assistant peut produire une synthèse personnalisée : progression adhérent, demandes/événements coach ou conseils sportifs non urgents. Les urgentes restent individualisées et transmises rapidement, sous réserve des règles de livraison et confidentialité. Les événements originaux qui doivent rester consultables ne disparaissent pas dans le regroupement. Distinguer informations vérifiées, interprétations et recommandations (T5.8) ; respecter préférences et priorités T6.2–T6.3.

### 10.4 Actions rapides et contexte (T6.6)

Selon les possibilités OS et contrats backend, une notification peut permettre de voir une réservation, consulter un message, examiner une disponibilité, répondre à une demande ou ouvrir le fil unique avec le contexte de l'événement. L'utilisateur peut poursuivre par « Réserve cette place », « Propose-moi un autre horaire » ou « Préviens mon coach ».

Préserver le contexte pertinent sans transmettre d'informations devenues non autorisées. App revérifie au moment de l'action droits, disponibilités, crédits et conditions métier ; une place libérée lors de l'envoi peut avoir été prise depuis. Un bouton de notification n'est pas une autorisation métier. Les confirmations sensibles restent contextuelles ; le résultat effectif et les reprises sûres suivent T5.4–T5.5.

### 10.5 Messagerie contextualisée (T6.7)

Les notifications coach–adhérent peuvent être analysées et priorisées : demandes importantes, résumés de plusieurs échanges, besoin d'intervention, réponses suggérées et accès aux messages originaux selon permissions. La provenance reste explicite : message réellement envoyé par une personne, résumé IA, réponse/formulation suggérée par l'IA, demande nécessitant une intervention humaine. Aucun contenu généré ne vaut message humain effectivement envoyé. Préserver la communication principalement conversationnelle T3.8/T4.7 et les relances automatiques autorisées T4.9.

### 10.6 Rappels personnalisés (T6.8)

Les rappels s'adaptent aux préférences, type de séance, habitudes observées fiablement, contexte temporel/sportif et changements effectifs de planning. Ils peuvent inclure conseils de préparation, information de changement, proposition de report ou suggestion d'action. Les préférences explicites restent prioritaires ; proposer un report ne modifie pas la réservation. Toute modification passe par App et ses règles. Aucun délai obligatoire, calcul prédictif d'absence ou reprogrammation automatique n'est défini.

### 10.7 Confidentialité des notifications (T6.9)

Masquer par défaut les informations personnelles sensibles dans les aperçus, notamment sur écran verrouillé. Le niveau d'aperçu est configurable dans les limites des règles de protection ; les contenus particulièrement sensibles restent protégés même si les aperçus ordinaires sont permis. Mesures corporelles, performances individualisées sensibles, santé, messages confidentiels et recommandations personnelles nécessitent une attention particulière, sans constituer ici une classification technique exhaustive.

Tenir compte des possibilités et réglages de confidentialité iOS/Android. Les textes IA ne peuvent contourner ces protections ; une préférence d'affichage n'accorde aucun droit d'accès. Critères exacts de classification et politiques de divulgation restent à définir et vérifier côté App. Les contrôles de mémoire T5.10 restent distincts des préférences, événements et historique de notification.

### 10.8 Synchronisation et fiabilité (T6.10)

App centralise les événements et leurs états ; mobile, centre classique et assistant présentent des informations cohérentes : lu/non lu, actions déjà réalisées, limitation des doublons, actualisation des événements obsolètes et cohérence multi-appareils. Conserver les événements consultables même sans réception push et vérifier l'état réel avant toute action. Une place déjà réservée ne doit plus être présentée comme disponible ; une demande traitée sur un appareil doit être reflétée ailleurs selon le contrat de synchronisation.

App reste source de vérité. Aucune livraison push garantie, aucun traitement exactement une fois et aucune synchronisation instantanée ne sont promis sans contrat démontré. La notification ou son cache ne remplacent jamais l'état métier actuel.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:967 -->

## 11. Continuité sans IA et connectivité

**B8.2 est obligatoire, avec l’exception AR02 :** le mobile conserve les parcours classiques nécessaires ; création et modification de programmes sont exclusivement via IA, tandis que leur consultation autorisée reste accessible sans IA. Les vues classiques ne doivent pas dépendre de la génération OpenAI.

**T1.8 — Accueil de secours automatique :** si l'assistant devient indisponible, MOVEE Mobile présente automatiquement un accueil simplifié donnant accès aux réservations, programmes, planning ou fonctionnalités coach selon les permissions. Cet accueil et le menu ne dépendent pas du service IA. La conversation redevient accessible lorsque l'assistant est rétabli, selon les règles de continuité T1.6. Une indisponibilité IA doit être distinguée d'une perte de réseau ou d'une indisponibilité complète du backend : le secours ne garantit pas l'accès à un service métier lui-même indisponible.

**Écart actuellement identifié :** `get_bookings`, `get_program` et `get_performance_history` ne disposent pas nécessairement d'équivalents mobiles classiques sous authentification Bearer ; la disponibilité de ces endpoints doit être confirmée ou traitée côté MOVEE App. Les consultations ne doivent pas être présentées comme réalisées tant que cette couverture n'est pas vérifiée.

En cas de réseau indisponible, conserver une expérience de lecture limitée et clairement signalée **uniquement si elle est sûre**. Ne jamais confirmer localement une réservation, un paiement, une modification de programme ou un débit de crédits non validé par le serveur. Les principes hors connexion sont validés par T7.1–T7.4 ; les données précisément éligibles, durées, opérations différées et mécanismes restent à contractualiser.

Les paramètres essentiels de sécurité, confidentialité, notifications et déconnexion (T2.9), ainsi que la demande de suppression de compte avec vérification d'identité et confirmation (T2.10), disposent de parcours classiques indépendants de l'IA. Leur accès reste soumis à l'identité et aux permissions applicables, sans garantir leur fonctionnement si le backend requis est indisponible.

### 11.1 Consultation hors connexion et opérations locales (T7.1)

Sans Internet, certaines informations autorisées déjà synchronisées restent consultables ; les parcours classiques restent accessibles dans les limites des données locales autorisées. Certaines interactions locales compatibles peuvent être conservées en attente de synchronisation, sous réserve d'un périmètre à contractualiser. Au retour réseau, App vérifie leur validité avant toute application effective. Une action locale ou en attente n'est jamais une action métier confirmée : aucune réservation validée hors connexion, aucun crédit/solde modifié localement comme faisant autorité, aucun contournement des permissions et accords sensibles.

Les fonctions IA dépendant d'un service distant, y compris la voix T5.9, peuvent être indisponibles. Le mode concerne principalement consultation et interactions locales compatibles, jamais suivi d'un entraînement en cours. Aucune file persistante ni synchronisation déjà implémentée n'est présumée.

### 11.2 Conflits et source de vérité (T7.2)

À la reconnexion, App vérifie les opérations en attente ; seules celles toujours valides peuvent être appliquées selon contrat. En cas de conflit significatif, informer simplement l'utilisateur, expliquer sa nature et présenter les résolutions autorisées, avec intervention du coach lorsque pertinente. App reste source de vérité : aucune règle universelle de dernière modification gagnante, aucune fusion présumée, aucun écrasement local d'une décision protégée ou d'un programme coaché. L'assistant peut expliquer, jamais contourner permissions/validations T3.7/T4.4.

### 11.3 Préparation configurable des données et sécurité (T7.3–T7.4)

Préparer automatiquement les données autorisées utiles aux prochaines consultations : programme actif, prochaines réservations, planning, dernières performances et informations utiles au coach pour préparer ses prochaines séances lorsque la conservation locale est autorisée. Ces exemples ne décident pas l'éligibilité de chaque donnée. L'utilisateur peut choisir certaines informations à conserver ou supprimer localement. Stockage limité au nécessaire, protégé, associé au compte et au contexte centre + rôle applicable, soumis aux permissions App ; les droits modifiés entraînent invalidation selon les mécanismes disponibles.

Chiffrer les données sensibles locales, protéger les informations personnelles, isoler comptes/contextes et prévoir invalidation ou purge adaptée à la déconnexion, révocation ou changement de contexte. Certains accès peuvent bénéficier d'un déverrouillage biométrique ou système, et les données particulièrement sensibles être exclues du hors connexion lorsque nécessaire. La biométrie reste optionnelle T2.5, complémentaire aux autorisations serveur. Ni stockage ni chiffrement ne sont sélectionnés.

Un téléphone déconnecté ne connaît pas immédiatement une révocation distante : validité, expiration et revalidation doivent être contractualisées, sans promesse de révocation instantanée. La préparation des données ne prépare aucun suivi d'exercice en direct ; le cache ne devient jamais la source métier ni une donnée confirmée en temps réel.

### 11.4 Continuité et résilience des interactions (T7.6–T7.7)

Après appel, verrouillage, changement d'application, coupure réseau, fermeture inattendue ou redémarrage, préserver et proposer une reprise contextualisée des états récupérables : navigation, formulaires, consultations, conversation unique, opérations locales autorisées en attente et actions dont le résultat doit être vérifié avec App. La reprise concerne l'interaction, jamais un exercice ou une séance physique ; aucune répétition, série ou performance n'est inventée. L'enregistrement machine demeure indépendant, côté App. Ne pas garantir toute restauration d'état volatile sans mécanisme vérifié.

Distinguer perte réseau, API indisponible, timeout, session expirée, erreur de synchronisation, refus métier explicite et résultat incertain. Récupération automatique seulement si sûre, préservation des données locales autorisées et messages compréhensibles sans détails sensibles ; l'assistant peut aider s'il est disponible, avec parcours classique sans IA. Un résultat incertain doit être vérifié côté App avant retry ; aucune idempotence ou reprise existante n'est supposée.

### 11.5 Mises à jour, fluidité et appareils (T7.5, T7.8–T7.9)

Combiner mises à jour distantes compatibles si contraintes techniques et plateformes le permettent, versions stores pour changements natifs et contrôle de compatibilité Mobile/App. Prévoir possibilité de mises à jour critiques obligatoires et déploiement progressif des non critiques. Ne perdre silencieusement aucune action locale en attente ; migrations locales et compatibilité des opérations doivent être étudiées. Aucun mécanisme OTA ni versionnement définitif n'est choisi, et une mise à jour distante ne modifie pas arbitrairement le natif.

Favoriser anticipation pertinente, navigation réactive, chargement progressif des contenus volumineux/graphiques/historiques, cache raisonné, adaptation au réseau et aux capacités du téléphone, identification des données non actualisées. Cela sert consultations de programmes, réservations, performances, adhérents autorisés et reprise de conversation, sans usage pendant les exercices ni seuil de performance ou stratégie technique imposé.

Viser une large gamme de smartphones iOS/Android effectivement compatibles avec React Native/Expo. Maintenir les parcours essentiels — programmes, réservations, performances, messagerie et informations personnelles autorisées — sur les appareils compatibles ; prévoir alternatives pour les fonctions exigeantes, notamment voix temps réel selon appareil/réseau. Versions minimales et capacités doivent être vérifiées avant définition : aucune liste d'appareils ni version minimale n'est inventée.

### 11.6 Diagnostic et signalement (T7.10)

Prévoir détection des plantages, erreurs applicatives/réseau, ralentissements et problèmes de synchronisation, corrélation possible Mobile/App et signalement d'un problème depuis l'application. La collecte reste proportionnée au diagnostic, avec protection des informations personnelles, données sensibles et échanges IA. Ne pas collecter inutilement conversations, données personnelles d'adhérents, identifiants d'authentification, secrets ou payloads métier sensibles. Outils, fournisseur, collecte et conservation restent à définir.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:1015 -->

## 12. Confidentialité, accessibilité et confiance

- Afficher uniquement les données autorisées pour l'utilisateur, son rôle et son centre ; revalider à chaque action.
- Minimiser les données transmises à l'IA et éviter les conversations complètes dans les journaux métier (B8.5, B8.11).
- Préférences et mémoire IA contrôlées par l'utilisateur (Q046).
- Vidéo/photo/voix : fonctionnalités cibles Q047–Q052, consentement et conservation limitée ; **aucune permission système demandée avant usage nécessaire** (principe validé T8.3).
- Prévoir accessibilité, lecture d'écran, contraste, tailles de police, retours d'erreur compréhensibles et internationalisation selon Q103–Q104.
- Ne jamais promettre qu'une opération a réussi avant réception d'un résultat backend fiable.

### 12.1 Mémoire transparente et contrôlable (T5.10)

L'utilisateur consulte et contrôle les informations durables mémorisées par conversation : « Que sais-tu de mes objectifs sportifs ? », « Corrige mon objectif de poids » ou « Ne retiens plus cette préférence ». L'assistant accompagne consultation, correction et suppression lorsque autorisées. Un accès classique aux mêmes contrôles reste disponible sans IA, conformément au repli T1.8 et aux paramètres essentiels T2.9.

Une modification ou suppression n'est annoncée comme réalisée qu'après confirmation effective de MOVEE App. Distinguer mémoire conversationnelle sélective, historique de conversation, données métier et données soumises à conservation légale. Retirer une préférence mémorisée ne supprime pas automatiquement ses occurrences dans l'historique ou les données métier ; corriger un objectif exige d'identifier le périmètre concerné. Confidentialité, autorisation, traçabilité, conservation et cycle de vie restent à contractualiser sans inventer de stockage existant ni contourner T2.10.

### 12.2 Accessibilité et personnalisation contrôlable (T8.1–T8.2)

Prévoir les besoins visuels, auditifs et moteurs : compatibilité VoiceOver iOS et TalkBack Android, tailles de texte système, contrastes/lisibilité, réduction des animations, alternatives aux gestes complexes et à la voix, navigation/interactions accessibles. Cartes, graphiques et composants conversationnels respectent les mêmes exigences que les parcours classiques accessibles sans IA. **Aucune fonctionnalité métier essentielle ne dépend exclusivement de la voix, d'un geste complexe ou d'une animation.** Ces exigences ne prouvent pas une accessibilité déjà implémentée.

Respecter thème clair/sombre et préférences d'accessibilité système, avec réglages manuels de présentation. L'adaptation au rôle adhérent/coach et aux usages pertinents peut prioriser l'information utile ; elle reste modifiable et désactivable, avec priorité aux choix explicites. Aucun changement de permissions/règles ni masquage de fonction autorisée. Aucun moteur de personnalisation existant n'est présumé ; l'articulation détaillée des choix système/applicatifs reste à vérifier sans affaiblir l'accessibilité.

### 12.3 Intégrations natives facultatives (T8.3)

Possibilités envisagées : ajout de réservation au calendrier personnel, partage de documents, caméra contextuelle, raccourcis, biométrie optionnelle et voix. Vérifier les capacités réelles par appareil/plateforme ; demander les autorisations seulement lorsque nécessaires, respecter refus et indisponibilité, prévoir alternatives lorsque possible, sans accès permanent injustifié ni activation facultative imposée. Aucune bibliothèque native choisie sans vérification.

Un événement du calendrier personnel ne vaut pas réservation confirmée dans App ; aucune permission OS ne donne de droit métier supplémentaire. La voix T5.9 reste une cible avec alternatives d'interaction ; la biométrie reste optionnelle T2.5. Aucune intégration ne crée de suivi d'exercice en direct ou d'utilisation pendant l'entraînement (T7.8).

### 12.4 Paramètres centralisés et maîtrisés (T8.8)

Prévoir un espace classique complet utilisable sans IA et la gestion conversationnelle autorisée : consultation des préférences actuelles, modification, suggestions contextuelles, priorité aux choix explicites, confidentialité, permissions et validations pertinentes. Distinguer paramètres de compte potentiellement synchronisés selon contrat App et réglages propres à l'appareil conservés localement. L'assistant ne force pas de changement contraire aux choix explicites.

Thème, notifications, préférences assistant et désactivation d'adaptation sont des exemples ; aucune API générique ni synchronisation universelle des paramètres n'est supposée. Les contrôles de mémoire, sécurité et confidentialité déjà définis restent applicables.

### 12.5 Aide et support contextualisés (T8.9)

Proposer aide conversationnelle d'utilisation, explications des fonctions, aide adaptée à la navigation, erreurs métier connues et solutions adaptées, avec centre d'aide classique sans IA. Séparer cause vérifiée, hypothèse, solution proposée et action réellement effectuée. Ne pas inventer une cause d'incident ou de refus de réservation sans résultat métier disponible la justifiant.

Permettre une demande au support humain avec accord préalable sur la transmission des informations nécessaires, minimisation et protection des données personnelles/conversations. Aucun système de tickets, fournisseur, base de connaissances ou API de support n'est présumé opérationnel.

**AR05.4 — Réclamations.** Dépôt, justificatifs, suivi, échanges et décision restitués via IA ; décisions de remboursement/litige réservées aux personnes/Services habilités.

### 12.6 Retours volontaires et amélioration continue (T8.10)

Recueillir volontairement les avis ; l'assistant peut solliciter un retour contextualisé. Étudier difficultés récurrentes, parcours abandonnés seulement lorsque leur mesure est autorisée, indicateurs d'usage autorisés et données agrégées adaptées. Définir règles de collecte, consentement, préférences de confidentialité, conservation et suppression avant toute collecte concernée.

Ne pas exploiter automatiquement les conversations privées pour l'analyse produit. Distinguer diagnostics techniques T7.10 et mesures d'expérience T8.10, avec finalités et règles propres. Aucun fournisseur analytics, consentement acquis ou mécanisme opérationnel de collecte n'est supposé.

### 12.7 Multilingue dès V1

**AR05.10 — Langues.** **Mobile entièrement multilingue dès V1** : interface, IA, notifications et contenus disponibles localisés ; documents contractuels uniquement en versions officiellement validées. Langues initiales et politique de repli à définir.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:1066 -->

## 13. Catalogue de parcours et maturité

| Parcours | Décision produit | État d'intégration mobile attesté |
| --- | --- | --- |
| Connexion / identité mobile | Architecture MOVEE App | Auth serveur codée selon audit ; client mobile non recetté |
| Consultation réservations / programme / historique | IA2A, Q043–Q044 | Capacités IA codées ; équivalents classiques incomplets |
| Recherche / réservation / annulation | B1–B5 | Services IA2B codés ; recette MariaDB et client non faites |
| Crédits / engagement | B2, Q010–Q012 | Lot initial D2/D5/IA2B corrigé côté backend ; intégration réelle à vérifier |
| Saisie des séries | IA2A, Q029–Q033 ; périmètre précisé par T3.4 | Action backend codée ; client non recetté ; aucune saisie manuelle imposée pour le suivi machine |
| Adaptation / douleur / demandes coach | B6–B7 | Partie backend codée ; parcours complet non attesté |
| Accueil proactif | Directive mobile validée | Expérience client non attestée |
| Push hors application | B5, B6, Q068 | Outbox/worker codés ; fournisseur et terminal non raccordés |
| Multimodal, machines, bilans | Q026–Q057 | Cible produit ; disponibilité non vérifiée |

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:1080 -->

## 14. Critères de recette fonctionnelle

- L'adhérent et le coach voient seulement leurs données et actions autorisées.
- Une consultation simple fonctionne sans confirmation inutile.
- Les confirmations sensibles reprennent les conséquences métier exactes.
- Une double demande ou un retry ne produit pas de double réservation, débit ou application.
- Une réservation confirmée avec crédits immobilisés demeure valable malgré expiration ultérieure de ces crédits.
- Une modification concurrente de programme déclenche revalidation, pas écrasement silencieux.
- Une douleur ouvre le circuit de sécurité sans suggestion médicale ou levée autonome de restriction.
- Une panne IA déclenche automatiquement l'accueil simplifié et laisse accessibles le menu et les parcours classiques effectivement supportés ; le rétablissement rend la conversation à nouveau accessible (T1.8).
- Sur iOS et Android, le menu latéral sans onglets permanents respecte le profil actif et se referme après sélection ; menu et cartes ouvrent les écrans métier (T1.2–T1.4).
- Le bouton IA et la navigation arrière fonctionnent sans réinitialiser le fil unique ; les échanges précédents et le contexte disponibles sont conservés selon le contrat vérifié (T1.5–T1.6).
- La zone prioritaire est compacte, distincte du fil, consultable ou masquable et alimentée uniquement par les données autorisées (T1.7).
- Une notification push n'est annoncée comme livrée qu'après preuve de livraison disponible.
- Les scénarios sont vérifiés sur iOS et Android, avec backend réel de recette et données synthétiques.

### Recette identité, comptes et profils — Thème 2

- T2.1/T2.8 : inscription libre limitée aux quatre informations initiales, sans accès automatique aux données d'un centre ni collecte initiale obligatoire des autres informations.
- T2.2/T2.7 : connexion immédiate non vérifiée avec restrictions serveur, vérification e-mail avant rattachement effectif et opérations sensibles contractualisées ; demande et invitation respectent le contrôle du centre.
- T2.3/T2.4 : changement de centre ou de profil sans reconnexion, adaptation au couple actif et absence de réutilisation des données d'un contexte précédent.
- T2.5 : maintien sécurisé de session dans les limites serveur, biométrie facultative locale, expiration et révocation effectives.
- T2.6 : code e-mail à usage unique saisi dans l'application, nouveau mot de passe intégré, refus des codes expirés ou réutilisés et limitation des tentatives côté serveur selon contrat.
- T2.9/T2.10 : profil conversationnel via API, confirmations proportionnées, paramètres essentiels et suppression accessibles sans IA ; vérification d'identité et confirmation avant traitement autorisé, avec respect des conservations requises.

### Recette parcours adhérent — Thème 3

- T3.1/T3.2 : activité et réservation principalement conversationnelles avec cartes et calendrier interactif, sans tableau de bord général « Mon activité » ; consultations classiques nécessaires et calendrier accessibles sans IA.
- T3.3 : alternatives et déplacement sans annulation préalable imposée, résultat et cohérence crédit/disponibilité confirmés par le backend, y compris en cas de conflit ou timeout.
- T3.4–T3.6 : restitution des données machine sans saisie manuelle imposée, performances expliquées et graphiques interactifs fondés sur les données/calculs App, programme structuré avec détails et démonstrations disponibles.
- T3.7 : entraînement libre appliqué dans les limites de sécurité avec notification coach ; programme suivi adapté avec consentement adhérent dans les limites coach préautorisées ; validation coach requise hors cadre, pour protections, objectifs globaux ou restrictions de sécurité (AR01). Le mode et les permissions sont déterminés par App.
- T3.8 : origine IA/coach et transmission effective distinguées, autorisations et confirmations respectées, réponse coach restituée dans le fil.
- T3.9/T3.10 : interventions fondées sur les événements et règles App, préférences respectées, accompagnement contextuel avec questions ciblées sans questionnaire systématique ni conseils présentés comme avis médical.

Ces critères décrivent la recette à réaliser après contractualisation ; aucun résultat de test ni disponibilité d'API n'est acquis par leur inscription.

### Recette parcours coach — Thème 4

- T4.1/T4.2 : listes/fiches conversationnelles, répertoire classique avec recherche et filtres, priorités fondées sur les données et règles App dans le contexte centre + rôle autorisé.
- T4.3 : création/modification entièrement conversationnelles, ajustements successifs et consultation avant application, sans éditeur obligatoire.
- T4.4 : acceptation/refus/ajustements et sélection groupée ; aucune proposition appliquée sans sa validation explicite et les contrôles individuels serveur, résultat distingué de la sélection.
- T4.5/T4.6 : planning et disponibilités conversationnels, calendrier résultant et conflits visibles avant application ; calendrier et écran de disponibilités classiques sans IA ; aucune annulation/replanification automatique présumée.
- T4.7/T4.8 : origine et envoi réel des messages distingués, consultation des échanges sans IA ; bilans commentables, ajustables et validables avant partage, avec données/indicateurs App.
- T4.9/T4.10 : relances automatiques autorisées sans validation systématique coach, préférences respectées, absence jamais inférée du seul manque de données machine ; confirmations contextuelles pour actions sensibles et application d’AR01 aux adaptations supervisées, avec consentement adhérent dans le cadre préautorisé et validation coach lorsque requise.

Ces critères restent à recetter après vérification des contrats ; aucun test ni fonctionnement backend du thème 4 n'est attesté par cette mise à jour.

### Recette assistant IA — Thème 5

- T5.1/T5.7 : fil unique et historique consultable, contexte sélectif sans envoi systématique de tout l'historique, préférences de communication modifiables ; aucun droit, rôle ou centre déduit de la mémoire.
- T5.2/T5.3 : intentions et dépendances respectées, opérations conditionnées aux résultats et validations nécessaires, clarification minimale sur données réelles sans hypothèse présentée comme confirmée.
- T5.4/T5.5 : suivi proportionné, attente distincte d'exécution, bilan des résultats App ; alternatives et vérification d'un résultat incertain avant reprise, sans doublon.
- T5.6/T5.8 : réponses sport/bien-être distinctes des actions, conseils santé prudents, justifications fondées et faits/hypothèses/recommandations identifiables sans divulgation non autorisée.
- T5.9 : voix bidirectionnelle temps réel iOS/Android, interruption, bascule texte/voix et continuité du fil, permissions/confidentialité, interruptions système/réseau et repli texte ; mêmes contrôles métier que le texte.
- T5.10 : consultation/correction/suppression autorisée de la mémoire par conversation et sans IA, résultat confirmé par App, distinction avec historique, données métier et conservation légale.

Ces critères restent à recetter après contractualisation ; aucune capacité vocale, mémoire ou orchestration backend n'est attestée ici.

### Recette notifications et proactivité — Thème 6

- T6.1/T6.10 : trois présentations cohérentes d'un même événement, centre classique utilisable sans IA, événements récupérables sans push reçu ; états lu/non lu, traités/obsolètes et multi-appareils réconciliés selon contrat.
- T6.2/T6.3 : préférences explicites et tranquillité prioritaires sur l'IA, priorités/exceptions contrôlées par App ; aucune dérogation libre ni catégorie technique inventée.
- T6.4/T6.5 : notifications automatiques autorisées sans validation systématique, pas d'action métier implicite ; regroupement non urgent sans perte d'originaux consultables, urgences individualisées et synthèses justifiables.
- T6.6/T6.7 : actions rapides et continuité du fil avec revalidation actuelle des droits et conditions, opportunité expirée gérée ; origine humain/résumé/suggestion/besoin humain explicite et messages originaux accessibles selon droits.
- T6.8/T6.9 : rappels sur contexte fiable sans report automatique, aperçus sensibles masqués par défaut et protection renforcée maintenue malgré personnalisation ; refus OS et changement de contexte/permissions respectés.

Critères à recetter après contractualisation, sans résultat acquis ni promesse de livraison, d'exactement une fois ou de synchronisation instantanée.

### Recette fiabilité, hors connexion et performance — Thème 7

- T7.1/T7.2 : lecture autorisée hors connexion, attente distincte du succès, revalidation serveur au retour réseau ; conflits expliqués sans écrasement protégé ni fusion universelle.
- T7.3/T7.4 : choix des informations locales, fraîcheur/expiration, chiffrement sensible, isolation compte/contexte, invalidation/purge et biométrie optionnelle ; aucune révocation instantanée promise hors réseau.
- T7.5/T7.6 : mises à jour compatibles et reprise d'interaction après interruptions sans perte silencieuse des opérations en attente, dans les capacités techniques vérifiées ; aucune reprise physique d'exercice.
- T7.7/T7.8 : distinction des incidents et refus métier, reprise sûre après contrôle d'un résultat incertain, navigation fluide/chargement progressif et cache signalé comme non actualisé.
- T7.9/T7.10 : parcours essentiels sur appareils compatibles et alternatives adaptées, diagnostics minimisés/corrélables et signalement utilisateur sans divulgation sensible.
- Clarification T7.8 : aucune utilisation pendant l'entraînement, compteur de répétitions, suivi de séries en direct, chronomètre ou pilotage ; capacités métier machine et saisie antérieure conservées sans en faire un suivi mobile.

Critères à vérifier après contractualisation et recette autorisée, sans preuve de capacité livrée.

### Recette accessibilité et expérience utilisateur — Thème 8

- T8.1/T8.2 : VoiceOver/TalkBack, texte système, contraste, focus/navigation, réduction des animations, alternatives sans voix/gestes complexes et parcours classiques sans IA ; adaptations modifiables/désactivables sans masquer les droits, choix explicites prioritaires.
- T8.3/T8.4 : intégrations natives facultatives et refus respectés, aucun droit/réservation déduit d'une action OS ; présentation progressive accessible, détails sans IA, continuité du fil et données non déformées.
- T8.5/T8.6 : recherches sous permissions et centre actif, repli sans IA ; découverte ignorable/reprenable sans blocage ni annonce de capacité indisponible.
- T8.7/T8.8 : retours accessibles séparant attente locale, proposition approuvée et résultat appliqué ; paramètres complets classiques et conversationnels autorisés, compte/appareil distincts, synchronisation seulement contractualisée.
- T8.9/T8.10 : aide classique, faits/hypothèses/solutions/actions distingués, accord avant transmission support ; avis volontaires et mesures autorisées minimisées, consentement/conservation définis, aucune exploitation automatique des conversations privées pour analyse produit.

Critères à recetter après étude et contractualisation ; aucune conformité, intégration native ou collecte opérationnelle n'est attestée ici.

### Recette des arbitrages AR01–AR07 et des périmètres AR05

- AR01 : adaptation supervisée dans les limites coach avec consentement adhérent ; demande hors cadre/protections/objectif global/restriction soumise à validation coach, sans levée autonome de sécurité.
- AR02 : panne IA autorisant la consultation du programme mais aucune création/modification ; autres parcours classiques requis maintenus.
- AR03 : centre actif distinct du centre contractuel unique ; changement de contexte sans mutation de contrat et revalidation des droits.
- AR04 : passage Élevé déclenchant immédiatement le push malgré heures calmes MOVEE, sans contournement des refus/restrictions OS ni livraison garantie.
- AR05.1–AR05.6 : bilans, abonnements avec accord financier/contractuel explicite, rémunération coach en lecture, réclamations sous habilitations, communauté modérée et parrainage calculé par App.
- AR05.7–AR05.9 : aucune transaction marketplace ni administration B2B ni demande/export de portabilité intégrés au Mobile ; droits bénéficiaires B2B accessibles ; orientation vers canaux externes seulement. Suppression T2.10 conservée dans Mobile.
- AR05.10 : interface, IA, notifications et contenus disponibles localisés dès V1 ; documents contractuels en versions officielles ; langues initiales et repli à définir.
- AR06 : historique durable distinct du contexte éphémère et de la mémoire sélective, contrôle utilisateur et droits courants à chaque accès.
- AR07 : acquisition externe, résultats validés et droits dans App, restitution des bilans/évolutions sur Mobile sans accès direct aux appareils.

Critères cibles après contractualisation ; aucun test ni service réel vérifié par cette consolidation.

---

<!-- provenance: movee-mobile/codex/MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md:1205 -->

## 16. Règle de mise à jour

À chaque décision mobile validée : mettre à jour ce référentiel, puis le référentiel technique si un contrat change ; notifier le projet MOVEE App des dépendances backend. Toute modification d'une règle Q/B doit être arbitrée et intégrée **d'abord dans MOVEE App**, puis répercutée ici avec référence. Conserver le statut « décidé / codé / testé isolément / recetté réel / déployé ».
