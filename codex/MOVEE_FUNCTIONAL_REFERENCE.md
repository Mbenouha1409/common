# MOVEE — référence fonctionnelle commune

Version de consolidation : 2 novembre 2026. **Référence centralisée validée ; nettoyage des anciennes copies autorisé.**

## Lecture et portée

Ce fichier donne la vue d’ensemble du produit et le registre métier réseau Q001–Q130. Les décisions gardent leur propriétaire : App exécute le métier opérationnel ; Biz conserve ses calculs et ses décisions D/Q/S/F propres. Un Q réseau ne prouve pas une intégration Biz–App. Les détails de chaque application sont uniquement dans son couple de références du même dossier ; lire [README.md](README.md) et [AGENTS.md](AGENTS.md) d’abord.

## Ensemble des applications et responsabilités

| Projet / composant | Responsabilité | Frontière à conserver |
| --- | --- | --- |
| App — movee-app | Autorité métier réseau, identité, droits, programmes, crédits, réservations, consentements et résultats centraux | Pas de calcul physique temps réel ; Services font autorité sur les écritures |
| Admin — composant de movee-app | Administration Web native par Pages/Fields/Actions/Designer | Aucun nouveau dépôt Admin ni droit implicite ; contrats App communs |
| Mobile — movee-mobile | Client iOS/Android adhérent/coach, expérience conversationnelle cible et parcours classiques déclaratifs | Hors entraînement ; aucun accès direct SQL/Redis/OpenAI ou matériel |
| Biz / Info — movee-biz | Deux sites par hôte, candidatures, relation commerciale et simulations | Base/auth/moteur indépendants ; hypothèses de simulation ne deviennent pas politiques App |
| Pod — movee-pod | Cible d’exécution locale d’une séance autorisée, interface tactile et connecteurs | Cadrage, pas logiciel matériel livré ; pas d’éditeur de programme libre |
| MOTION — movee-motion | Analyse contextualisée des exercices connus et comparaison aux références coach/individuelles | Aide à l’observation ; ni diagnostic, ni arrêt d’urgence, ni station BODY |
| Studio / BODY | Studio : coordination locale proposée ; BODY : périmètre de bilan morphologique distinct | Aucun dépôt logiciel propre trouvé dans l’inventaire ; ne pas inventer un projet livré |

## Principes réellement partagés

Une donnée inconnue ne devient ni zéro ni résultat positif. Droits actuels, restrictions et consentements priment ; une proposition acceptée ne prouve pas son exécution. Les programmes appartiennent à App ; AR02 réserve leur création/modification à l’IA, consultation maintenue sans IA. AR01 encadre les adaptations par limites préautorisées et accord ; AR03 distingue contexte actif et rattachement contractuel ; AR04 n’outrepasse jamais les permissions OS ; AR06 distingue historique, contexte et mémoire ; AR07 sépare acquisition externe, autorité App et restitution Mobile. Les formulations complètes restent dans Q et B, pas de nouvel arbitrage ici.

La marque commune est décrite une seule fois dans [DESIGN_SYSTEM_MOVEE.md](DESIGN_SYSTEM_MOVEE.md), avec [adaptations Web](ADAPTATIONS_WEB_MOVEE.md) et [Admin](ADAPTATIONS_ADMIN_MOVEE.md). Les valeurs commerciales Biz, horaires simulés et politiques synthétiques locales ne sont pas des valeurs par défaut App.

## Dépendances fonctionnelles et travail restant

Mobile/Admin consomment les capacités autorisées d’App ; une Page n’active pas un Service absent. Pod dépend de contrats App de préparation/résultats encore à formaliser ; MOTION dépend du contexte Pod, de calibration et de références validées. Biz n’a pas de synchronisation automatique autorisée vers les offres ou comptes App. Push réel, voix, acquisition matérielle, autonomie hors ligne et mises en production gardent leurs statuts et gates propres. Aucune consolidation ne les marque livrés.

## Registre réseau conservé et convention d’autorité

Les Q ci-dessous sont issus de l’ancien référentiel App ; propriétaire du métier opérationnel : App. Q001–Q130 conservés intégralement avec leurs précisions AR. B1–B8 sont dans [MOVEE_APP_FUNCTIONAL_REFERENCE.md](MOVEE_APP_FUNCTIONAL_REFERENCE.md) ; les 78 T sont dans [MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md](MOVEE_MOBILE_FUNCTIONAL_REFERENCE.md) ; D01–D57/Q01–Q08 et S/F/R dans [MOVEE_BIZ_FUNCTIONAL_REFERENCE.md](MOVEE_BIZ_FUNCTIONAL_REFERENCE.md). Les Q01–Q08 Biz ne sont pas Q001–Q008 App.

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:139 -->

## Directive actuelle — expérience mobile et agent IA

MOVEE App vise **deux applications mobiles iOS et Android développées et maintenues en interne**, avec une expérience principalement conversationnelle de type chatbot IA, enrichie de composants structurés (créneaux, confirmations, programmes, résultats et historique). **Expo est l’environnement initial de développement et de test**, non une exigence permanente de distribution ou d’implémentation. Les API et contrats métier doivent rester indépendants du framework client. Les parcours classiques restent accessibles lorsque l’IA est indisponible (B8.2), avec l’exception AR02 : création et modification de programmes exclusivement via IA, consultation autorisée sans IA.

L’agent IA côté serveur reçoit les messages, comprend l’intention, sélectionne des capacités natives explicitement publiées, puis délègue aux Services les autorisations, transactions, confirmations et résultats. La consultation autorisée s’exécute sans confirmation superflue ; les opérations sensibles nécessitent le consentement adapté (B8.4). Les adhérents et les coachs bénéficient d’informations proactives dans l’application et, après raccordement fournisseur, de notifications Push sur téléphone hors application, dans le respect des préférences. Le modèle ne décide jamais seul du succès d’une opération.

**Traçabilité :** Q088, Q090 et Q091 ont été réorientées après le cadrage initial ; leurs identifiants sont conservés, mais les anciennes prescriptions de transport et de génération automatique d’outils ne sont plus applicables. Les autres décisions Q001–Q130 et B1–B8 demeurent dans le périmètre cible, même si leur implémentation n’est pas terminée.

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:200 -->

## Positionnement

MOVEE App est la plateforme d’un réseau de centres de fitness franchisés et studios satellites, avec séances autonomes sur machines connectées, coaching IA adaptatif et séances encadrées par des coachs. Le siège pilote le réseau, les contrats, la sécurité, le catalogue d’équipements et les règlements interfranchises ; chaque franchisé exploite ses centres dans un périmètre de droits défini. Les adhérents disposent d’un centre de rattachement et peuvent fréquenter d’autres centres selon leur offre.

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:204 -->

## Acteurs

- Siège : gouvernance réseau, catalogue, règles, approbations sensibles, finances et go/no-go.
- Franchisé/exploitant : exploitation locale et paiements des coachs, avec historique de rattachement.
- Responsable de centre : capacité, incidents, exceptions et relation client.
- Adhérent : abonnements/packs, réservations, historique sportif, consentements et préférences IA.
- Coach salarié ou indépendant : séances accompagnées, bilans, programmes et rémunération contractuelle.
- Fournisseur/partenaire : équipements, paiement, marketplace, communications ; intégration contrôlée.
- Agent IA natif MOVEE : opérations dans les seules permissions effectives et approuvées ; aucun privilège supplémentaire par rapport à l’utilisateur.

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:214 -->

## Principes non négociables

La sécurité sportive, la confidentialité, l’audit, les limites contractuelles et les validations humaines prévalent sur toute optimisation IA. L’IA ne modifie pas seule les règles métier, ne prend pas de décision contractuelle ou disciplinaire sensible et ne contourne pas les contrôles Services. Les fonctions V1 différenciantes incluent machines connectées, coaching adaptatif, réservations optimisées et pilotage réseau (Q128), avec validation siège après pilotes (Q129).

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:218 -->

## Périmètre temporel

V1/V2/V3 sont des propositions de séquencement, non des choix validés individuellement. Les 130 exigences restent dans le périmètre produit cible.



---

AR05.10 impose le multilingue mobile dès V1. Les autres phasages V1/V2/V3 demeurent des propositions ; AR05 ne fixe pas de calendrier supplémentaire des capacités serveur. Les fonctionnalités marketplace et administration B2B restent des décisions backend, avec les exclusions mobiles AR05.7/AR05.8 ; l’export reste côté App par canal externe (AR05.9).

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:234 -->

## Portée et fiabilité

Ce registre reprend **exactement 130 décisions**, une fois chacune, sans remplacer les formulations de la source par de prétendues citations. Q001–Q097 sont des reformulations conservées dans le cadrage, Q098–Q130 ont des choix C explicitement consignés ; seules Q086, Q088, Q089 et Q091 ont un choix B conservé parmi les premières. « Non conservée » indique une lettre de réponse inconnue, **pas une décision non validée**.

**Source canonique :** le présent registre Q001–Q130 ; aucune source séparée n’est requise.

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:240 -->

## Registre intégral Q001–Q130

### Q001 — Réseau

**Choix conservé :** non conservée. **Décision validée :** Un franchisé exploite un centre à un instant donné ; conserver l’historique daté des exploitants.

### Q002 — Réseau

**Choix conservé :** non conservée. **Décision validée :** Un studio satellite dépend d’un centre principal à un instant donné ; transfert possible au sein du même franchisé avec historique.

### Q003 — Identités

**Choix conservé :** non conservée. **Décision validée :** Une personne possède une identité users unique, plusieurs rôles et rattachements à des centres ; distinguer l’entité exploitante franchisée.

### Q004 — Adhérents

**Choix conservé :** non conservée. **Décision validée :** Chaque adhérent a un centre de rattachement ; accès possible aux autres centres selon son offre, avec traçabilité de la consommation.

**AR03 — Centre contractuel unique, centres accessibles multiples, centre actif.** Le centre actif est un contexte opérationnel choisi, jamais une mutation contractuelle ; les droits et l'éligibilité sont revérifiés côté App à chaque action.

### Q005 — Sécurité

**Choix conservé :** non conservée. **Décision validée :** Permissions contextualisées par franchisé et centre ; aucun accès transversal implicite.

### Q006 — Réseau

**Choix conservé :** non conservée. **Décision validée :** Le siège contrôle création des centres et statuts structurels officiels ; les franchisés assurent les opérations quotidiennes.

### Q007 — Équipements

**Choix conservé :** non conservée. **Décision validée :** Le siège contrôle catalogue et affectation des machines ; le local suit disponibilité et incidents.

### Q008 — Réservations

**Choix conservé :** non conservée. **Décision validée :** Réserver un créneau de séance dans un centre, non une machine particulière.

### Q009 — Capacité

**Choix conservé :** non conservée. **Décision validée :** Calculer la capacité des séances autonomes selon machines opérationnelles, contraintes et capacité maximale du centre.

### Q010 — Crédits

**Choix conservé :** non conservée. **Décision validée :** Réserver les crédits à la réservation ; consommer à la séance réalisée ; libérer à l’annulation admissible.

### Q011 — Crédits

**Choix conservé :** non conservée. **Décision validée :** Vérifier la validité des crédits à la date de réservation et les immobiliser lors de la réservation. Une réservation confirmée reste valable si les crédits immobilisés expirent avant la séance. L'expiration ne doit pas supprimer ou rendre indisponibles les crédits déjà réservés. Les règles de restitution après annulation restent celles définies dans B3.

### Q012 — Crédits

**Choix conservé :** non conservée. **Décision validée :** Consommer prioritairement les crédits d’abonnement puis les packs prépayés ; autoriser une combinaison.

### Q013 — Annulations

**Choix conservé :** non conservée. **Décision validée :** Délai d’annulation gratuite configurable ; pénalités de retard et exceptions explicites.

### Q014 — Absences

**Choix conservé :** non conservée. **Décision validée :** Le no-show consomme les crédits selon la politique ; restauration exceptionnelle par responsable, auditée.

### Q015 — Annulations

**Choix conservé :** non conservée. **Décision validée :** Annulation par le centre : libérer les crédits et proposer des alternatives soumises à confirmation de l’adhérent.

### Q016 — Finance

**Choix conservé :** non conservée. **Décision validée :** Compensation interfranchises des séances consommées hors centre de rattachement selon tarif réseau défini par le siège.

### Q017 — Finance

**Choix conservé :** non conservée. **Décision validée :** Centraliser les règlements de compensation interfranchises au siège.

### Q018 — Finance

**Choix conservé :** non conservée. **Décision validée :** Le siège encaisse abonnements et packs puis redistribue selon les règles contractuelles.

**AR05.2 — Abonnements.** Consultation et demandes conversationnelles de souscription, renouvellement ou modification ; **accord explicite** avant engagement financier/contractuel ; exécution App.

### Q019 — Finance

**Choix conservé :** non conservée. **Décision validée :** Affecter le chiffre d’affaires selon les séances effectivement consommées ; traiter distinctement les crédits non utilisés.

### Q020 — Finance

**Choix conservé :** non conservée. **Décision validée :** Affecter les revenus des crédits d’abonnement expirés au franchisé du centre de rattachement, à l’échéance.

### Q021 — Finance

**Choix conservé :** non conservée. **Décision validée :** Constater les droits de répartition à la séance achevée ou pénalité finalisée ; consolider périodiquement.

### Q022 — Finance

**Choix conservé :** non conservée. **Décision validée :** Une période financière clôturée est immuable ; ajustements ultérieurs séparés et audités.

### Q023 — Finance

**Choix conservé :** non conservée. **Décision validée :** La cadence de clôture financière est configurable selon les contrats.

### Q024 — Finance

**Choix conservé :** non conservée. **Décision validée :** Tarif réseau défini par le siège avec dérogations par franchisé et dates d’effet.

### Q025 — Finance

**Choix conservé :** non conservée. **Décision validée :** Imputer chaque transaction au franchisé exploitant le centre à la date de l’événement.

### Q026 — Machines

**Choix conservé :** non conservée. **Décision validée :** Collecter les événements d’exercice et les résumés des machines, avec historique.

### Q027 — Machines

**Choix conservé :** non conservée. **Décision validée :** Authentifier sur machine via QR/NFC ou autre moyen autorisé, lié à l’utilisateur et à la séance.

### Q028 — Machines

**Choix conservé :** non conservée. **Décision validée :** Synchroniser programme et réglages personnalisés avec les machines ; conserver les ajustements.

### Q029 — Coaching

**Choix conservé :** non conservée. **Décision validée :** Programmes créés/adaptés par coach, IA ou adhérent selon droits ; versionner et conserver l’origine.

**AR02 — Création et modification de programme uniquement via IA.** En cas d'indisponibilité IA, consultation autorisée mais aucune création/modification. **Exception explicite à B8.2** ; les autres parcours classiques restent requis selon leur périmètre.

### Q030 — IA sportive

**Choix conservé :** non conservée. **Décision validée :** L’IA adapte de manière autonome entraînements et réglages dans les permissions accordées.

**AR01 — Autonomie encadrée des adaptations de programme supervisé.** L'IA peut appliquer une adaptation **dans les limites préautorisées par le coach** avec consentement de l'adhérent ; hors limites, exercices protégés, objectifs globaux ou restrictions de sécurité : validation coach selon les règles métier. Cette précision prévaut sur toute formule exigeant une approbation coach pour chaque adaptation.

### Q031 — Sécurité sportive

**Choix conservé :** non conservée. **Décision validée :** Respecter limites individuelles, contraintes techniques des machines et escalade si risque.

### Q032 — Confidentialité

**Choix conservé :** non conservée. **Décision validée :** Performances visibles par adhérent, coachs affectés et acteurs autorisés ; accès audités.

### Q033 — Historique sportif

**Choix conservé :** non conservée. **Décision validée :** Historique sportif unifié à l’échelle du réseau.

### Q034 — Hors ligne

**Choix conservé :** non conservée. **Décision validée :** Séances machine hors ligne autorisées dans un périmètre limité ; synchronisation différée avec déduplication.

### Q035 — Intégrations

**Choix conservé :** non conservée. **Décision validée :** Connecteurs multi-constructeurs pour les équipements.

### Q036 — Machines

**Choix conservé :** non conservée. **Décision validée :** Le siège supervise firmware et mises à jour ; aucune interruption d’une séance active.

### Q037 — Maintenance

**Choix conservé :** non conservée. **Décision validée :** Détection des pannes, maintenance locale et supervision siège ; machine indisponible exclue des capacités.

### Q038 — Maintenance IA

**Choix conservé :** non conservée. **Décision validée :** L’IA anticipe et planifie les maintenances autorisées dans les limites de sécurité et des contrats.

### Q039 — Capacité

**Choix conservé :** non conservée. **Décision validée :** Incident machine : recalcul de capacité et propositions d’alternatives nécessitant confirmation de l’adhérent.

### Q040 — Accès

**Choix conservé :** non conservée. **Décision validée :** Entrée physique libre pendant les horaires d’ouverture ; vérifier les droits au démarrage de la séance.

### Q041 — Séances

**Choix conservé :** non conservée. **Décision validée :** Confirmer l’achèvement sur activité machine et seuils définis.

### Q042 — Séances

**Choix conservé :** non conservée. **Décision validée :** Crédit d’une séance interrompue traité selon progression et cause de l’interruption.

### Q043 — Adhérents

**Choix conservé :** non conservée. **Décision validée :** Tableau de bord sportif individuel et coach IA.

### Q044 — Assistant IA

**Choix conservé :** non conservée. **Décision validée :** L’assistant traite coaching, réservation, crédits, abonnements et routines ; confirmation des actions sensibles.

### Q045 — Permissions IA

**Choix conservé :** non conservée. **Décision validée :** Autoriser les actions IA selon une politique fondée sur le niveau de risque.

### Q046 — Mémoire IA

**Choix conservé :** non conservée. **Décision validée :** Mémoire IA contrôlée par l’utilisateur : préférences, objectifs, habitudes et confidentialité.

**AR06 — Historique IA durable et mémoire sélective.** Historique, contexte éphémère et mémoire personnalisée distincts ; contrôle de consultation/correction/suppression et vérification des droits à chaque accès. Les données métier officielles demeurent dans MOVEE App.

### Q047 — Multimodal

**Choix conservé :** non conservée. **Décision validée :** Assistant IA texte, voix, photo et vidéo.

### Q048 — Analyse mouvement

**Choix conservé :** non conservée. **Décision validée :** Analyse de mouvement compatible et consentie pendant la séance.

### Q049 — Vidéo

**Choix conservé :** non conservée. **Décision validée :** Stockage des vidéos d’entraînement facultatif, consenti et limité dans le temps.

### Q050 — Vidéo

**Choix conservé :** non conservée. **Décision validée :** Analyse vidéo hybride locale/cloud.

### Q051 — Vidéo

**Choix conservé :** non conservée. **Décision validée :** Durées maximales de conservation par finalité définies par le siège ; suppression automatique ou anticipée selon obligations.

### Q052 — Vidéo

**Choix conservé :** non conservée. **Décision validée :** Cadrage et zones caméra restreints ; éviter les tiers présents.

### Q053 — Bilans

**Choix conservé :** non conservée. **Décision validée :** Bilans corporels facultatifs via balances, scan 3D et capteurs compatibles.

**AR07 — Mesures externes, résultats mobiles.** MOVEE Motion/dispositifs spécialisés acquièrent les mesures ; MOVEE App centralise les résultats validés et droits ; MOVEE Mobile restitue bilans et évolutions, sans connexion directe aux appareils.

### Q054 — Bilans

**Choix conservé :** non conservée. **Décision validée :** Mesures de composition corporelle exclusivement accompagnées par un coach.

### Q055 — Bilans

**Choix conservé :** non conservée. **Décision validée :** Réservation dédiée d’un bilan avec coach et équipement.

### Q056 — Bilans

**Choix conservé :** non conservée. **Décision validée :** Inclusion, supplément, quota ou pack de bilans selon l’offre commerciale.

### Q057 — IA sportive

**Choix conservé :** non conservée. **Décision validée :** Utiliser les bilans pour objectifs et programmes sous restrictions fixées par le coach.

**AR05.1 — Bilans sportifs.** Adhérent : consultation, évolution, explications IA ; coach autorisé : création, complément, modification et validation **conversationnels** via Services App. Acquisition des mesures externe.

### Q058 — Coachs

**Choix conservé :** non conservée. **Décision validée :** Choix du coach par l’adhérent ou affectation automatique compatible.

### Q059 — Planning

**Choix conservé :** non conservée. **Décision validée :** Calendrier coach multi-centres avec prévention des conflits et prise en compte des déplacements.

### Q060 — Rémunération

**Choix conservé :** non conservée. **Décision validée :** Rémunération coach selon statut, contrat et prestation ; paiement effectué par le franchisé concerné.

**AR05.3 — Rémunération coach.** Consultation des contrats, commissions, rémunérations, factures et paiements autorisés ; explication IA et signalement d'anomalies ; pas de gestion comptable complète dans Mobile.

### Q061 — Contrats coach

**Choix conservé :** non conservée. **Décision validée :** Contrats multiples simultanés ou successifs avec siège/franchisés, datés et historisés.

### Q062 — Facturation coach

**Choix conservé :** non conservée. **Décision validée :** Pour les indépendants : relevés de prestations, rapprochement facture, approbation des écarts et paiement par franchisé.

### Q063 — Annulations coach

**Choix conservé :** non conservée. **Décision validée :** Pénalités d’annulation paramétrées par siège ; rémunération selon contrat ; exceptions auditées.

### Q064 — Remplacement

**Choix conservé :** non conservée. **Décision validée :** Indisponibilité coach : rechercher remplaçant qualifié ; l’adhérent confirme, reporte ou annule sans frais.

### Q065 — Qualité coach

**Choix conservé :** non conservée. **Décision validée :** Évaluations, KPI objectifs et analyse IA des tendances ; supervision humaine.

### Q066 — Réclamations

**Choix conservé :** non conservée. **Décision validée :** Traitement local des réclamations avec escalade siège ; triage assisté par IA.

**AR05.4 — Réclamations.** Dépôt, justificatifs, suivi, échanges et décision restitués via IA ; décisions de remboursement/litige réservées aux personnes/Services habilités.

### Q067 — Réclamations IA

**Choix conservé :** non conservée. **Décision validée :** Résolution automatique des cas simples ; escalade des cas financiers ou graves.

### Q068 — Communication

**Choix conservé :** non conservée. **Décision validée :** Messagerie et notifications omnicanales, canaux externes et assistance IA.

**AR04 — Push immédiat pour alerte de sécurité Élevé.** Exception aux heures de tranquillité configurées dans MOVEE, mais **jamais** aux refus/autorisations/restrictions iOS/Android ; émission ≠ livraison garantie. Les autres notifications respectent les préférences.

### Q069 — Marketing IA

**Choix conservé :** non conservée. **Décision validée :** Création de campagnes, segmentation et optimisation de canaux par IA, selon budgets et consentements.

### Q070 — Fidélisation IA

**Choix conservé :** non conservée. **Décision validée :** Actions individualisées de rétention et récompenses pilotées par IA dans les budgets autorisés.

### Q071 — Parrainage IA

**Choix conservé :** non conservée. **Décision validée :** Parrainage et incitations à l’acquisition optimisés par IA sous règles autorisées.

**AR05.6 — Parrainage.** Lien/code partageable, invitations, suivi et avantages via IA ; éligibilité et récompenses exclusivement calculées/attribuées par App.

### Q072 — Pilotage IA

**Choix conservé :** non conservée. **Décision validée :** Tableaux de bord prédictifs et actions opérationnelles automatiques autorisées.

### Q073 — Objectifs réseau

**Choix conservé :** non conservée. **Décision validée :** Objectifs de performance proposés dynamiquement par IA ; validation humaine des engagements contractuels.

### Q074 — Ouverture centre

**Choix conservé :** non conservée. **Décision validée :** Suivi complet des projets d’ouverture ; IA aide au choix d’implantation et à la rentabilité ; investissement décidé par humain.

### Q075 — Franchises

**Choix conservé :** non conservée. **Décision validée :** Contrats, redevances et conformité suivis avec IA proactive ; sanctions humaines.

### Q076 — Audits

**Choix conservé :** non conservée. **Décision validée :** Audits structurés et détection continue IA des non-conformités ; mesures disciplinaires humaines.

### Q077 — Formation

**Choix conservé :** non conservée. **Décision validée :** Formation/LMS personnalisée par IA ; certification officielle validée humainement.

### Q078 — Recrutement

**Choix conservé :** non conservée. **Décision validée :** IA assiste recrutement et onboarding ; décision humaine et prévention des biais.

### Q079 — Effectifs

**Choix conservé :** non conservée. **Décision validée :** Prévision IA des besoins et plannings, sous droit du travail et contrats.

### Q080 — Achats

**Choix conservé :** non conservée. **Décision validée :** Prévisions IA des stocks/achats et commandes automatiques préautorisées.

### Q081 — Énergie

**Choix conservé :** non conservée. **Décision validée :** Optimisation prédictive IA des consommations énergétiques et commandes d’équipements dans les limites de sécurité.

### Q082 — Bâtiments

**Choix conservé :** non conservée. **Décision validée :** Maintenance prédictive des bâtiments et interventions préautorisées.

### Q083 — Incidents

**Choix conservé :** non conservée. **Décision validée :** Détection IA d’incidents de sécurité, alertes et gestes prédéfinis sûrs ; gestion humaine des urgences.

### Q084 — RGPD

**Choix conservé :** non conservée. **Décision validée :** Gouvernance proactive des données et confidentialité par IA ; corrections autorisées, décisions sensibles humaines.

### Q085 — Cybersécurité

**Choix conservé :** non conservée. **Décision validée :** Détection IA des menaces, protections autorisées ; actions critiques et remise en service sous contrôle humain.

### Q086 — Disponibilité

**Choix conservé :** B. **Décision validée :** Haute disponibilité et mode dégradé hors ligne, avec resynchronisation sécurisée ; pas de basculement IA autonome généralisé.

### Q087 — Écosystème

**Choix conservé :** non conservée. **Décision validée :** Écosystème ouvert d’intégrations, partenaires approuvés, API et workflows orchestrés par IA.

### Q088 — Agent IA natif et capacités métier

**Choix historique :** B (remplacé par la réorientation validée). **Décision actuelle :** Agent IA MOVEE orchestré côté serveur, disposant d’un registre fermé de capacités métier contrôlées ; les Services appliquent les permissions et les règles métier.

### Q089 — Délégation

**Choix conservé :** B. **Décision validée :** Permissions explicites et révocables par outil, action, périmètre et durée ; jamais au-delà des droits de l’utilisateur.

### Q090 — Publication contrôlée des capacités IA

**Choix historique :** non conservé (réorienté). **Décision actuelle :** Capacités de l’agent IA explicitement enregistrées et validées ; les métadonnées peuvent informer les contrats, mais ne publient jamais automatiquement toutes les actions métier au modèle.

### Q091 — Activation des capacités IA

**Choix historique :** B (réorienté). **Décision actuelle :** Activation des capacités IA par le siège après vérification contrats et permissions ; désactivation immédiate possible.

### Q092 — Audit de l’agent IA

**Choix conservé :** non conservée. **Décision validée :** Audit de bout en bout, détection IA d’anomalies et suspension autorisée d’accès.

### Q093 — Versionnement des contrats IA

**Choix historique :** non conservé. **Décision actuelle :** Versionner les contrats des capacités IA ; IA détecte incompatibilités et propose migrations ; approbation des modifications sensibles.

### Q094 — Workflows orchestrés par l’agent IA

**Choix conservé :** non conservée. **Décision validée :** Orchestration asynchrone avec reprise, idempotence, dépendances et approbations humaines.

### Q095 — Création workflow

**Choix conservé :** non conservée. **Décision validée :** Construction de workflows en langage naturel, avec validation, simulation et approbation selon le risque.

### Q096 — Déploiement workflow

**Choix conservé :** non conservée. **Décision validée :** Workflows versionnés ; IA simule impacts, déploie progressivement et peut revenir en arrière selon seuils d’anomalie.

### Q097 — Modèles IA

**Choix conservé :** non conservée. **Décision validée :** Orchestration dynamique des modèles selon qualité, coût, latence et confidentialité ; évaluations et basculement contrôlé.

### Q098 — Coûts IA

**Choix conservé :** C. **Décision validée :** Optimiser dynamiquement coûts IA, anticiper dépenses, adapter ressources et modèles aux budgets ; facturation contractuelle.

### Q099 — Qualité IA

**Choix conservé :** C. **Décision validée :** Évaluations continues, garde-fous Services, surveillance des dérives, suspension de modèles défaillants et basculement vers modèles validés ; aucune modification autonome des règles métier.

### Q100 — Données IA

**Choix conservé :** C. **Décision validée :** Apprentissage continu encadré des modèles spécialisés ; données individuelles seulement si légalement autorisé, consentement si requis, minimisation et protection renforcée des données sensibles.

### Q101 — Omnicanal

**Choix conservé :** C. **Décision validée :** Interfaces web, applications mobiles iOS/Android, bornes, machines et voix partageant API, Services et permissions métier ; l’agent IA MOVEE est natif côté serveur.

### Q102 — UI metadata IA

**Choix conservé :** C. **Décision validée :** Framework metadata-driven et interfaces adaptatives IA ; changements structurels contrôlés par siège et permissions.

### Q103 — International

**Choix conservé :** C. **Décision validée :** Traductions et adaptation IA en temps réel ; traductions officielles et contractuelles validées humainement ; formats et réglementations locales.

**AR05.10 — Langues.** **Mobile entièrement multilingue dès V1** : interface, IA, notifications et contenus disponibles localisés ; documents contractuels uniquement en versions officiellement validées. Langues initiales et politique de repli à définir.

### Q104 — Accessibilité

**Choix conservé :** C. **Décision validée :** Accessibilité avancée et adaptation IA des interfaces, communications et consignes sportives ; sécurité et validation professionnelle.

### Q105 — Onboarding

**Choix conservé :** C. **Décision validée :** Intégration progressive pilotée IA dès inscription, adaptée aux premières séances ; validations professionnelles conservées.

### Q106 — Parcours centre

**Choix conservé :** C. **Décision validée :** Guidage intelligent entre machines, réorganisation des exercices et alternatives selon affluence, disponibilité et performances ; sécurité.

### Q107 — Affluence

**Choix conservé :** C. **Décision validée :** Prévoir congestions, coordonner flux et parcours, adapter recommandations ; respecter réservations, capacités et sécurité.

### Q108 — Motivation

**Choix conservé :** C. **Décision validée :** Détecter démotivation, adapter objectifs et défis, intervenir sans sollicitations excessives ni culpabilisantes.

### Q109 — Communauté

**Choix conservé :** C. **Décision validée :** Réseau social sportif volontaire ; IA recommande partenaires, groupes, défis et événements ; confidentialité, modération, signalements.

**AR05.5 — Communauté.** Groupes, échanges et événements autorisés, avec recherche IA, confidentialité et modération App ; pas de réseau social généraliste.

### Q110 — Événements

**Choix conservé :** C. **Décision validée :** IA recommande événements, prévoit affluence, optimise calendriers et automatise tâches autorisées ; validations financières/sensibles.

### Q111 — Fidélité

**Choix conservé :** C. **Décision validée :** Programme réseau de récompenses personnalisées et dynamiques par IA ; budgets, contrats, équité et confidentialité.

### Q112 — Partenaires

**Choix conservé :** C. **Décision validée :** Marketplace de partenaires ; IA recommande offres, détecte opportunités, optimise campagnes ; contrôle siège des partenaires et contrats.

**AR05.7 — Marketplace.** **Hors Mobile** : ni boutique, panier ni achat ; l'IA peut orienter vers le canal commercial distinct, sans transaction.

### Q113 — Marketplace

**Choix conservé :** C. **Décision validée :** Achats/paiements via prestataire agréé, commandes, remboursements, commissions ; IA optimise ventes et détecte anomalies ; contrôles financiers.

### Q114 — SAV

**Choix conservé :** C. **Décision validée :** SAV marketplace IA : réclamations, retours et remboursements préautorisés, détection problèmes récurrents ; escalade humaine.

### Q115 — Qualité partenaires

**Choix conservé :** C. **Décision validée :** IA prévoit défaillances, propose corrections, suspend temporairement offres selon règles ; sanctions contractuelles humaines.

### Q116 — B2B

**Choix conservé :** C. **Décision validée :** Contrats entreprises, éligibilité, quotas, cofinancement, facturation et portail RH agrégé ; IA optimise offres, budgets et programmes ; confidentialité individuelle.

**AR05.8 — B2B.** Administration entreprises/partenaires **hors Mobile** ; les adhérents bénéficiaires voient/utilisent leurs droits dans Mobile.

### Q117 — Déploiement

**Choix conservé :** C. **Décision validée :** Déploiement progressif piloté siège et IA, groupes pilotes, ajustements préautorisés, arrêt/rollback sur anomalies ; changements majeurs validés.

### Q118 — Décisionnel

**Choix conservé :** C. **Décision validée :** IA détecte tendances et anomalies, explique variations, simule scénarios, recommande et exécute actions préautorisées ; décisions sensibles humaines.

### Q119 — Réversibilité

**Choix conservé :** C. **Décision validée :** Sauvegardes/restaurations testées, exports et portabilité ; IA contrôle intégrité, risques et vérification, assiste migrations ; opérations majeures validées.

**AR05.9 — Portabilité.** Demande et export de données personnelles **via canal externe**, non intégrés au Mobile ; IA d'orientation uniquement ; App contrôle l'exécution.

### Q120 — Observabilité

**Choix conservé :** C. **Décision validée :** Métriques, logs, traces ; IA prédit incidents, recherche causes et exécute corrections préautorisées ; actions critiques humaines, audit.

### Q121 — Évolutions

**Choix conservé :** C. **Décision validée :** Collecte et priorisation des demandes ; IA analyse retours/usages, propose roadmap, spécifications et tests ; siège valide.

### Q122 — Migration

**Choix conservé :** C. **Décision validée :** IA analyse sources et mappings, détecte incohérences, propose transformations validées ; rapport, traçabilité, reprise, protection des données sensibles.

### Q123 — Qualité logicielle

**Choix conservé :** C. **Décision validée :** Tests unitaires, intégration, API et parcours ; IA génère tests, détecte régressions, reproduit incidents et contrôle déploiements ; critique validé humainement.

### Q124 — Stratégie versions

**Choix conservé :** C. **Décision validée :** Développement modulaire et lancement progressif ; IA priorise valeur/coût/dépendances ; modules activables ; siège valide feuille de route.

### Q125 — Pilotes

**Choix conservé :** C. **Décision validée :** Centres pilotes représentatifs, mesures de réussite ; IA analyse incidents et retours, propose corrections et généralisation ; siège décide.

### Q126 — Support

**Choix conservé :** C. **Décision validée :** Support multi-niveaux avec base documentaire et tickets ; IA assiste, diagnostique, corrige si autorisé, détecte répétitions et escalade avec trace.

### Q127 — Catalogue modules

**Choix conservé :** C. **Décision validée :** Modules activables par contrats/offres/centres ; IA recommande, estime rentabilité et active si préautorisé ; modifications facturables validées.

### Q128 — V1

**Choix conservé :** C. **Décision validée :** V1 commerciale inclut socle métier, machines connectées, coaching IA adaptatif, optimisation des séances et pilotage réseau ; pilotes et sécurité obligatoires.

### Q129 — Go-live

**Choix conservé :** C. **Décision validée :** Critères métier, opérationnels et sécurité mesurables ; IA analyse pilotes/risques ; décision siège, sans dérogation automatique aux blocages.

### Q130 — Livrables

**Choix conservé :** C. **Décision validée :** Dossier complet : registre 130 décisions, cahier des charges, modules, V1/V2/V3, roadmap, écarts avec architecture et SQL ; distinguer décisions et hypothèses.

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:794 -->

## Contrôle de couverture

- Q001–Q130 : **130 / 130**, sans trou ni doublon.
- Les choix non conservés ne sont pas reconstitués arbitrairement.
- La décision validée n’équivaut pas à une fonctionnalité déjà développée.

---

<!-- provenance: movee-app/codex/MOVEE_APP_FUNCTIONAL_REFERENCE.md:800 -->

## Index thématique (chevauchements volontaires)

- **Réseau / franchises :** Q001, Q002, Q003, Q004, Q005, Q006, Q007, Q024, Q025, Q073, Q074, Q075, Q076, Q127
- **Adhérents / réservations / crédits :** Q004, Q008, Q009, Q010, Q011, Q012, Q013, Q014, Q015, Q039, Q040, Q041, Q042, Q105, Q106, Q107, Q108
- **Finances / contrats / rémunérations :** Q016, Q017, Q018, Q019, Q020, Q021, Q022, Q023, Q024, Q025, Q060, Q061, Q062, Q063, Q113, Q114, Q116
- **Machines / séances / maintenance :** Q007, Q008, Q009, Q026, Q027, Q028, Q029, Q030, Q031, Q032, Q033, Q034, Q035, Q036, Q037, Q038, Q039, Q040, Q041, Q042, Q080, Q081, Q082, Q083, Q106, Q107
- **Coaching / bilans / santé :** Q029, Q030, Q031, Q032, Q033, Q043, Q044, Q045, Q046, Q047, Q048, Q049, Q050, Q051, Q052, Q053, Q054, Q055, Q056, Q057, Q058, Q059, Q060, Q061, Q062, Q063, Q064, Q065, Q104, Q105
- **CRM / communauté / marketing :** Q066, Q067, Q068, Q069, Q070, Q071, Q108, Q109, Q110, Q111, Q112, Q113, Q114, Q115, Q126
- **IA / sécurité / données :** Q030, Q031, Q044, Q045, Q046, Q047, Q048, Q049, Q050, Q051, Q052, Q084, Q085, Q086, Q087, Q088, Q089, Q090, Q091, Q092, Q093, Q094, Q095, Q096, Q097, Q098, Q099, Q100, Q101, Q102, Q103, Q118, Q119, Q120, Q121, Q122, Q123
- **Pilotage / livraison / exploitation :** Q072, Q073, Q074, Q075, Q076, Q077, Q078, Q079, Q080, Q081, Q082, Q083, Q084, Q085, Q117, Q118, Q119, Q120, Q121, Q122, Q123, Q124, Q125, Q126, Q127, Q128, Q129



---
