# MOVEE Biz — référence fonctionnelle spécifique

Version de consolidation : 2 novembre 2026. **Référence centralisée validée ; anciennes copies retirées après accord utilisateur.** Lire d’abord [README.md](README.md), [règles communes](AGENTS.md), [fonctionnel global](MOVEE_FUNCTIONAL_REFERENCE.md) et [technique globale](MOVEE_TECHNICAL_REFERENCE.md). Les sections issues des anciennes références conservent leur date/statut ; un constat historique ne décrit pas l’installation actuelle.

## Priorité des décisions et exceptions déjà validées

D01–D57 et Q01–Q08 sont des registres Biz distincts des Q001–Q130 opérationnels. Les compléments datés du23octobre et suivants précisent les formulations anciennes : entrées publiques6–10machines/codepostalfacultatif/choixcoach ; sortie apport indicatif et bénéficeannée3 remplacent le TTC/public ancien ; budgets travaux400HT/m², vestiaire2000HT/module, douche2500HT/unité, versions acquises conservées. Navigation par ancres, thèmes Light/Black du31octobre remplacent les essais de palette du25. Les tableaux historiques F/R chiffrés restent des cas datés, pas un changement rétroactif de version ou des règles App.

**Réserves maintenues :** R01 fiscal/comptable France et clearing ; R02 juridique/DPO, conservation/effacement. Leur rédaction n’est ni validation d’expert ni autorisation d’ouverture. Les références juridiques et taux cités sont ceux des sources datées du18octobre, non revérifiés aujourd’hui et non actualisés par cette consolidation.

## Décisions complémentaires datées puis registre détaillé

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:3 -->

## Design public Light / Black — 31 octobre 2026

Choix explicite des deux variantes pour Biz et Info avec bouton Light / Black en
haut, comme Mobile. Référence commune : ../codex/DESIGN_SYSTEM_MOVEE.md v1.2 depuis
la racine du projet ; adaptations validées dans ../codex/ADAPTATIONS_WEB_MOVEE.md.
Flask/Jinja et CSS/JS natifs conservés. Manrope/Sora locales et tokens partagés,
compositions Light/Black responsive, ancres et FAQ finale, champs52px, focus et
contrastes de la charte. Préférence locale par origine, système au premier usage,
aucune écriture de compte ; saisies, consentement et simulation conservés au switch.

Nouveaux libellés du thème en CMS FR/EN/ES : 3champs,18lignes insert-only par base,
204champs/site/langue et1224lignes. CTA hero standard alignés sur l'action réelle
uniquement si l'ancienne valeur standard était encore présente ; contenus
personnalisés préservés. Pas de migration ni changement économique. Suppression
des liens circulaires ; contact proposé dans la recherche vide. Images et légendes
existantes conservées. Administration et Mobile inchangés, aucun déploiement.

Recette : 13tests publics et2tests Node du thème réussis ; contrôles clavier,
persistance, stockage indisponible, écrans1440/390/320, simulation et formulaire
(non envoyé) vérifiés. Comparaisons aux quatre planches et captures dans le dossier
commun codex/design-web-2026-10-31/recette. Rapport design-qa.md : passed. Données
synthétiques des tests nettoyées. Serveur Biz local relancé séparément du pilotage
commun. Voir les limites de recette dans le rapport commun.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:28 -->

## Photographies illustratives des pods — 26 octobre 2026

Six nouveaux visuels générés via le skill ImageGen et l'outil intégré depuis les
deux références de pods fournies : collectif de six avec coach, collectif de
quatre sans coach, autonomie sur quatre/six pods, coaching individuel femme avec
coach et homme avec coach. Palette #10131A/#EFFF4F, LED jaunes, mixité, aucune
cote ou annotation. Vues inspectées ; correction ciblée de la pose sur une image.
Fichiers PNG v2 sauvegardés dans public_static/media/, originaux conservés.
Références brutes conservées dans docs/media-references, non exposées dans le site.
Galerie et prompts : MEDIA_GALLERY_2026-10-26.md, MEDIA_PROMPTS_2026-10-26.md et
MEDIA_GENERATED_2026-10-26.json dans docs/. Ces visuels sont des illustrations,
pas des photographies d'un studio réel ; mention provisoire conservée.

Intégration aux deux sites autorisée par l'utilisateur : bannières et photos
principales remplacées ; cartes pratiques Info illustrées (autonomie, collectif,
individuel) ; accompagnement Biz avec coach. Références médias et descriptions
FR/EN/ES en CMS : 8 champs supplémentaires, 48 lignes insert-only par base.
Anciennes références/descriptions standard remplacées ; éditions personnalisées
conservées. Catalogue 201 champs/site/langue, 1 206 lignes. Aucune migration.
12 tests publics réussis ; six fichiers servis en HTTP et pages Info/Biz vérifiées
au navigateur. Aucun paramètre financier, compte ou service commun modifié.
Les vidéos génériques préexistantes sont conservées avec leur signalement.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:51 -->

## Identité publique définitive — 25 octobre 2026

Palette #EFFF4F / #10131A choisie explicitement et appliquée par défaut à Info et
Biz. Sélecteur et script de mémorisation retirés ; l'ancien choix navigateur
n'a plus d'effet. Anciennes références de libellés CMS conservées sans usage,
sans effacement de données. Logo PNG fourni par l'utilisateur copié à l'identique
dans public_static/media/movee-logo.png et affiché dans l'en-tête/pied de page ;
mention BIZ et texte alternatif CMS conservés. Référence media.logo ajoutée
insert-only FR/EN/ES aux deux sites et deux bases (6 lignes/base). Catalogue
193 champs/site/langue, 1 158 lignes. Aucune migration, aucun changement métier.
12 tests publics réussis, contrôles HTTP des deux sites et vérification visuelle
Info/Biz. Données synthétiques nettoyées. Serveurs Biz relancés séparément du
pilotage commun movee-dev, resté intact.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:65 -->

## 25 octobre 2026 — sélecteur temporaire de couleurs publiques

Info et Biz proposent « Couleurs (test) » dans la barre supérieure : palette
actuelle par défaut ; 1 : #EFFF4F / #10131A ; 2 : #050505 / #D7FFE0. Variantes
sombres avec accents jaune ou menthe, adaptation des boutons, formulaires,
sections, bandeaux et pieds de page. Choix instantané et mémorisé uniquement
dans le navigateur par origine ; aucune préférence globale ni compte modifiés.
Textes du sélecteur en CMS FR/EN/ES : 2 champs, 12 ajouts insert-only par base,
192 champs par site/langue, 1 152 lignes au total. Pas de migration.
Recette des 12 tests publics réussie, contrôle syntaxique JavaScript et essais
navigateur des deux palettes, rechargement/persistance et retour à l'actuelle.
Aucun service movee-dev Backend/Redis/Expo modifié ; Biz relancé séparément
sur 127.0.0.1:5051 et 192.168.1.38:5051 selon sa procédure propre.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:79 -->

## Accès mobile Wi-Fi autorisé — 23 octobre 2026

Mode réseau local explicite BIZ_LAN_IP, réservé au lancement development. Sur ce
Mac : 192.168.1.38, serveur supplémentaire lié à cette seule IP privée:5051 ;
le serveur habituel reste sur 127.0.0.1:5051. Deux hôtes exacts sslip.io pour Info
et Biz, DNS vers l'IP privée, sans tunnel ni ouverture de port du routeur. Liste
blanche sans wildcard ; aucune modification système/pare-feu ou exposition DB.
Navigation, formulaires, sitemap et nouveaux liens des emails locaux respectent
la paire d'hôtes de la requête. Auth uniquement Biz, cookies host-only, CSRF,
approbation et MFA admin conservés. Aucun compte réel connecté par l'agent.
95 tests réussis dont 53 MariaDB, puis 4 règles CRM repassées après correction
des liens de notifications réseau. Accueils Info/Biz, connexion et simulateur
vérifiés par HTTP sur les vrais noms LAN ; hôte inconnu refusé. Pas de test
physique du téléphone. Comptes synthétiques nettoyés. Voir docs/LOCAL_NETWORK.md.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:94 -->

## Budgets d'aménagement validés — 23 octobre 2026

Demande utilisateur : travaux **400 € HT/m²**, douches **2 500 € HT/unité**,
vestiaires **2 000 € HT/module**. Les pods arrivent alignés, écran et sol intégrés ;
les travaux correspondent à l'adaptation/embellissement du local. Ces trois prix
remplacent les anciens 800/4 000/3 000 dans les nouvelles références françaises.
Le nombre de modules et la surface sont inchangés : 6 pods → 74 m², 3 modules
vestiaires et 3 douches. Nouveau total HT 92 700 € : travaux 29 600, vestiaires
6 000, douches 7 500, mobilier/IT 10 000, machines 24 000, transport 600,
droit d'entrée 15 000. Aucun changement aux autres hypothèses ni qualification TVA.

Révision économique 2 publiée dans les deux bases locales en préservant tous
les autres paramètres, anciennes versions et snapshots/travaux courants des
projets. Initialisation neuve alignée sur ces prix. Les projets existants
conservent leur référence jusqu'à l'action explicite d'actualisation, qui fige
une nouvelle version sans écraser les historiques ni leurs surcharges locales.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:111 -->

## Simulateur public : apport et bénéfice annuel — 23 octobre 2026

Demande utilisateur : remplacer le bloc TTC public par un apport personnel
indicatif et ajouter le bénéfice annuel à la fin. L'API anonyme expose désormais
exactement investissement HT, apport indicatif, CA HT mensuel/annuel à maturité et
résultat net de l'année 3 (somme des mois 25–36, pertes non masquées). Cette décision
remplace la limitation antérieure aux quatre montants et l'affichage TTC public.
Le TTC du moteur et du professionnel n'est pas remplacé par un montant d'apport.

L'apport reprend les fonds propres du plan de financement calculé : taux
configuré appliqué à l'investissement HT + réserve de démarrage du modèle.
Hypothèse actuelle 30 %, sans avance de TVA ni frais bancaires, sans garantie
d'accord de crédit. Le loyer et le choix coach agissent sur les charges, la
réserve, l'apport et le bénéfice, sans modifier automatiquement le CA. En mode
coach exploitant, aucune rémunération personnelle n'est déduite par défaut dans
ce modèle simplifié ; l'interface le précise et renvoie au professionnel.
Bénéfice distinct du revenu personnel et de la trésorerie ; fiscalité et
hypothèses toujours estimatives.

Source de cadrage financement consultée le 23 octobre 2026 : Bpifrance Création,
https://bpifrance-creation.fr/encyclopedie/financements/lemprunt/recourir-a-pret-bancaire-financer-son-projet-creation
(30 % constitue un repère de financement, dépendant du dossier et de la banque).

4 nouveaux champs CMS FR/EN/ES, 24 ajouts insert-only par base ; catalogue de
190 champs par site/langue, soit 1 140 lignes. Aides standard mises à jour si
non personnalisées, autres textes conservés. Aucun schéma ni projet existant
modifié. Montants affichés à l'euro entier avec symbole après la valeur.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:139 -->

## Simulateur public simplifié — décision du 23 octobre 2026

La demande utilisateur remplace les anciennes restrictions D22/D30 sur les
entrées publiques : curseur entier **6 à 10 machines** (8 au départ), code postal
français facultatif avec recherche de communes réelles et sélection en cas de
plusieurs correspondances, question « Êtes-vous coach ? ». Oui correspond au
mode existant coach exploitant, non au coach salarié. Le modèle exploitant
conserve son coût de rémunération paramétrable dans le complet ; aucun salaire
légal ou gratuité de travail n'est affirmé. Le public affiche toujours uniquement
investissement HT/TTC hors BFR et CA HT mensuel/annuel à maturité, sans bénéfice.
Le choix coach ne change pas ces quatre métriques avec les hypothèses actuelles ;
il définit le mode d'exploitation utilisé dans le moteur.

Les formats administrables ne bloquent plus ce parcours public. Le loyer estimé
reste ajustable dans un volet optionnel. La commune utilise sa référence économique
administrée si elle existe, sinon la référence nationale, sans effet automatique
sur le CA. Recherche via l'API officielle geo.api.gouv.fr, uniquement à partir du
code postal ; cache borné 128 recherches par tranche d'une heure, délai 4 secondes,
réponse bornée et validée. Une panne ou absence de résultat est affichée et permet
de réessayer ou de poursuivre sans code postal. Aucun appel externe requis pour
calculer sans ville, aucune simulation ni réponse coach enregistrée.

Tous les nouveaux textes sont dans le CMS FR/EN/ES (14 champs par site/langue,
84 ajouts insert-only par base, catalogue de 186 champs et 1 116 lignes). Les textes
existants sont conservés ; seule l'aide standard non personnalisée a été actualisée.
Aucune migration, aucun format commercial ni donnée de commune fictive conservés.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:166 -->

## Champs du simulateur complet — 23 octobre 2026

Hypothèses locales préremplies depuis la référence figée et les surcharges du
centre ; calcul partagé pour surface/CAPEX/loyer, coûts, financement, volumes et
calendrier. Les valeurs héritées sont affichées sans être enregistrées comme
surcharges ; l'autosauvegarde actualise leurs dépendances. Valeurs inconnues
conservées inconnues, historiques en lecture seule et références réseau inchangés.
86 tests réussis dont 50 MariaDB, contrôle du payload JavaScript avec Node et
nettoyage des données synthétiques. Aucun changement de schéma ou de projet
préexistant ; serveur local redémarré. Voir docs/PROJECTS.md.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:177 -->

## Navigation publique validée — 23 octobre 2026

Les deux sites publics sont des pages uniques par langue. Les menus défilent
vers les sections ; les anciennes URLs de rubriques redirigent vers les ancres.
Info comprend « Trouver mon studio » ; Biz « Simuler mon projet » avec le
simulateur simplifié intégré. La FAQ est le dernier bloc du contenu sur les deux
sites. Le simulateur complet conserve son accès professionnel authentifié.
Les regroupements du CMS restent des filtres éditoriaux, sans pages publiques
séparées. Aucun format commercial inventé ; le calcul public attend des formats
actifs configurés. Cette décision remplace la navigation publique par rubriques.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:188 -->

## Catalogue public complet en BDD — 22 octobre 2026

Textes publics utilisés, menus, actions, formulaires, simulateur public, messages,
descriptions et noms des fichiers médias désormais lus en MariaDB. Catalogue de
172 champs par site/langue ; 912 lignes manquantes ajoutées dans chaque base locale,
1 032 au total, avec vérification de préservation des 120 lignes préexistantes.
Aucune migration de schéma ; `cms_entries` réutilisée. Éditeur par site/langue/page/
section, brouillon ciblé, aperçu de rubrique et publication globale atomique du site
avec validation des trois langues. Révisions et contrôles de fichiers médias locaux.
Jeu JSON réservé à l'initialisation insert-only, aucun repli éditorial depuis le code.
Interface connectée/administration et secours technique hors périmètre public.
82 tests réussis dont 48 MariaDB, recette navigateur synthétique puis nettoyage.
Le compte local a été promu admin sur demande explicite avec révocation des anciens
accès et 2FA obligatoire ; aucune habilitation RGPD implicite. R01/R02 et D/Q/S/F
conservés. Voir `../docs/PUBLIC_CMS.md` et `DEVELOPMENT_PROGRESS.md`. Aucun email
externe, modification Backend/Mobile, commit/push ou déploiement.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:205 -->

## Présentation publique — 22 octobre 2026

Arborescence Info/Biz validée dans la conversation puis implémentée : accueils
visuels et pages de rubriques FR/EN/ES (dont offres/tarifs Info sans nouveaux prix).
Identité de couleurs conservée, photos générées et deux clips stock locaux
explicitement provisoires, menu responsive et navigation entre les sites.
CMS principal, demandes Info et simulateur public conservés ; nouveaux libellés et
textes complémentaires centralisés en code, sans nouveaux champs CMS.
79 tests réussis dont 45 MariaDB ; rendus des accueils et lecture vidéo Info
vérifiés au navigateur. Aucun nouveau schéma, donnée commerciale ou média réel
MOVEE présumé. Sources et remplacement : `../docs/PUBLIC_MEDIA.md`. Le compte
local demandé a été vérifié/approuvé et le quota de développement fixé à 10 sur
autorisation explicite, sans promotion admin. Chantier 9 toujours partiel,
R01/R02 inchangés ; aucun déploiement ou email externe.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:220 -->

## Avancement B09A — 22 octobre 2026

Premier lot de conservation et droits livré en local : confirmation de demande de
suppression membre, suspension immédiate et révocation sessions/jetons/confiance,
habilitation explicite du référent, instruction, exceptions à réexaminer, réponse,
prolongation motivée et annulation après vérification d'identité. Échéances de
réponse calculées en mois calendaires Paris ; revues de conservation motivées sans
initialisation implicite de durée ni contact technique réinitialisant les dates.
Inventaire limité et copies descendantes identifiées par provenance/journal minimal,
y compris source supprimée ; chaînes interrompues, textes libres et tiers restent
à examiner. Migrations 027–029 autorisées et appliquées aux deux bases locales.
77 tests réussis dont 43 MariaDB ; cycle transactionnel vérifié sur les deux bases,
recette navigateur synthétique et nettoyage ciblé, comptes préexistants préservés.
Aucun référent réel ni politique juridique initialisé. Effacement définitif et
réapplication après restauration non activés : R02 et sauvegardes restent à valider.
Aucun dump/restauration, SMTP externe, HTTPS production ou déploiement effectué.
Le chantier 9 reste partiel ; D/Q/S/F et réserves R01/R02 inchangés. Voir
`../docs/RETENTION.md`, `../docs/RELEASE_READINESS.md` et `DEVELOPMENT_PROGRESS.md`.
Les constats B01–B08 ci-dessous restent historiques.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:240 -->

## Avancement B08 — 21 octobre 2026

Exports Excel/PDF livrés en local, FR/EN/ES : 36 mois, trois scénarios, travail
enregistré ou historique figé, métadonnées et hypothèses traçables. Même moteur
et vue financière que les écrans ; classeur de valeurs sans recalcul autonome.
Droits membre/admin et hypothèses privées respectés, révision courante contrôlée,
aucune archive serveur ni création d'historique au téléchargement. 68 tests réussis
dont 37 MariaDB ; génération transactionnelle annulée sur les deux bases et
contrôle visuel des rendus synthétiques PDF/XLSX. Pas de migration supplémentaire
(001–026 inchangées), données préexistantes préservées. Voir `../docs/EXPORTS.md`
et `DEVELOPMENT_PROGRESS.md`. Chantier 9 à poursuivre ; R01/R02, recette utilisateur
et mise en service restent ouverts. D/Q/S/F inchangés ; aucun email externe ou
déploiement. Les constats B01–B07 ci-dessous restent historiques.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:254 -->

## Avancement B07 — 21 octobre 2026

Simulateurs et projets livrés en local : public limité aux quatre agrégats prévus,
professionnel approuvé, satellites explicites et réseau/franchiseur admin. Travail
autosauvegardé avec révision, historiques explicites, actualisation centrale,
restauration confirmée, copies indépendantes et comparaison sur trois scénarios.
Originaux membres en lecture seule admin, quota configurable sans valeur implicite,
contrôle de conservation avant suppression. Migrations 023–026 autorisées et
appliquées sur test et développement. 60 tests réussis dont 34 MariaDB réels ;
cycle transactionnel aussi vérifié sur les deux bases. Recette navigateur
synthétique : recalcul, persistance, états d'erreur/reprise et version volontaire.
Données de recette nettoyées, données préexistantes conservées ; ni format
commercial ni quota ajouté automatiquement. Voir `../docs/PROJECTS.md` et
`DEVELOPMENT_PROGRESS.md`. Exports au chantier 8 ; R01/R02, SMTP/HTTPS, recette
utilisateur et mise en service encore ouverts. D/Q/S/F conservés, aucun email
externe ou déploiement. Les constats B01–B06 ci-dessous restent historiques.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:271 -->

## Avancement B06 — 21 octobre 2026

Références économiques France versionnées et administration FR/EN/ES livrées en
local : paramètres, coûts communaux manuels, formats sans catalogue inventé,
pays futurs inactifs et historique FX. Migrations 017–022 autorisées et appliquées
sur les deux bases ; version France initiale conservée, aucun format/commune/FX
fictif. Moteur Decimal pur 36 mois pour centres, entités explicites, réseau
économique et franchiseur séparé ; préambule des acomptes, résultat/dette/cash,
packs reportables et élimination clearing. Snapshots indépendants et langue
absente des calculs. 52 tests réussis dont 27 MariaDB réels ; vérifications
transactionnelles supplémentaires sur les deux bases et nettoyage des seules
données synthétiques. Les données préexistantes sont préservées.
Voir `../ASSUMPTIONS.md`, `../docs/FINANCIAL_ENGINE.md` et
`DEVELOPMENT_PROGRESS.md`. Cash TTC indisponible si poste non qualifié ; cash
central/clearing HT proxy seulement. R01 reste en attente d'expertise ; aucun
taux/traitement fiscal certifié. Interfaces de simulation/projets au chantier 7,
exports au 8. D/Q/S/F, R01/R02 et constats historiques ci-dessous conservés.
Aucun email externe ni déploiement.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:290 -->

## Avancement B05 — 21 octobre 2026

Suivi commercial local livré : pipeline distinct de l'approbation, historique,
notes/contacts internes, relances datées sans email automatique et fil unique
candidat/admin avant et après approbation. Notifications email locales regroupées,
consultation admin partagée, aucun badge/compteur ou upload. Rattachements de
centres principal/satellites, propriétaire, territoire et date ajoutés.
Migrations 011–016 autorisées/appliquées sur test et développement. 41 tests
réussis dont 24 sur MariaDB réel, avec vérification des envois simultanés et des
droits. Voir `../docs/CRM.md` pour les conventions techniques et limites, et
`DEVELOPMENT_PROGRESS.md` pour les neuf chantiers. Les constats antérieurs sont
historiques ; D01–D57, Q01–Q08, S/F et réserves R01/R02 restent inchangés.
Aucun email externe, compte de démonstration conservé ou déploiement.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:305 -->

## Avancement B04 — 21 octobre 2026

Deux sites publics FR/EN/ES et CMS local livrés : contenu MariaDB, brouillon,
aperçu et publication atomique avec contrôle des trois langues et des révisions.
Migrations 008–010 autorisées/appliquées sur les deux bases ; 120 propositions
éditoriales explicitement marquées à valider. Annuaire sans centre fictif,
formulaire Info avec consentement versionné, consultation/affectation admin seules.
31 tests réussis dont 18 MariaDB réels ; contrôles navigateur desktop effectués.
Voir `../docs/PUBLIC_SITES.md` et `DEVELOPMENT_PROGRESS.md`. Les états B01–B03
ci-dessous sont historiques et complétés par ce lot ; D/Q/F et réserves R01/R02
inchangés. Pas de validation éditoriale/juridique ou ouverture publique présumée.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:318 -->

## Avancement d'implémentation locale — 21 octobre 2026, après B03

Le socle deux hôtes, les bases Biz isolées et l'authentification locale FR/EN/ES
sont maintenant implémentés et testés. B03 couvre inscription, vérification email,
approbation/refus/réexamen, reset, sessions serveur, 2FA admin et confiance navigateur.
Les emails sont capturés en boîte locale, sans transport externe. Aucun compte
administrateur de démonstration conservé. 25 tests réussis dont 12 sur MariaDB.

Les mentions d'absence de code dans la reprise initiale ci-dessous sont désormais
historiques. Elles ne décrivent pas le code courant ; les décisions D/Q/F et les
réserves R01/R02 restent inchangées. Voir `DEVELOPMENT_PROGRESS.md` pour les neuf
chantiers et `../docs/AUTHENTICATION.md` pour les conventions et limites B03.
CMS, CRM complet, moteur, projets, exports et exploitation restent à développer.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:332 -->

## Actualisation de l’état local — 21 octobre 2026

La conversation **Movee Biz Webapp** est propriétaire de `/Users/mbenmouha/Documents/Movee/movee-biz` : les fronts `movee.info` et `movee.biz`, prospects, candidatures, franchise et simulations. Il s’agit d’une application autonome ; la gestion opérationnelle des adhérents, coachs, crédits et programmes appartient à MOVEE App, leur interface téléphone à MOVEE Mobile.

L’environnement Python et les dépendances Biz sont réinstallés et vérifiés sur le nouveau Mac. **Le code applicatif et la base locale de test Biz restent à préparer** ; aucune fonctionnalité Biz n’est déclarée livrée par l’installation. D01–D57, Q01–Q08 et les blocs/annexes financiers et RGPD sont inchangés, avec leurs réserves de validation externe. Les anciennes versions et inspections restent historiques ; l’état de reprise est détaillé dans le référentiel technique de Biz.

---


**Version : 1.3 — 18 octobre 2026 (Europe/Paris).**
**Statut : D01–D57 et Q01–Q08 conservées ; R01/R02 intégrées, spécifiées mais non implémentées ; validation externe financière et juridique en attente.** Consolidation documentaire candidate à relecture finale ; aucune autorisation de développement, SQL ou déploiement. Les réserves du modèle financier demeurent provisoires quand elles ne sont pas explicitement arbitrées.

**Lecture des statuts :** Validé = cadrage explicitement transmis ; À détailler = principe acquis, spécifications incomplètes ; À arbitrer = décision non prise ou contradiction ; Implémenté = présence vérifiée dans le code ; À développer = prévu mais absent. Les réserves, valeurs indicatives et conventions techniques des sources gardent leur statut ; leur incorporation ne les transforme pas en décisions commerciales définitives.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:346 -->

## 1. Identification, sources et autorité

Sources de la V1.3 : lecture intégrale des référentiels **locaux V1.2**, de [codex/AGENTS.md](AGENTS.md) et de `codex/CODEX_MOVEE_BIZ_ANNEXES_FINANCE_RGPD_V1.md`. Les spécifications/modèle financier séparés restent absents du dépôt ; les blocs historiques intégrés S01–S10/F01–F11 sont utilisés sans remplacement par une copie externe. La précédente instruction D01–D57 séparée n’est plus présente au nouvel inventaire ; son registre intégré est préservé. Aucune décision disparue n’est reconstituée.

Les annexes R01 et R02 sont intégrées au **fonctionnel §§17 et 18**, avec renvois techniques. R01/R02 valident la préparation documentaire : elles ne valent pas approbation fiscale/juridique de leur contenu. Les recherches officielles du 18 octobre 2026 sont datées/liées dans ces annexes, distinctes du cadrage MOVEE ; pas de validation finale déclarée. Les 65 décisions D/Q et les 11 blocs F demeurent intacts.

Sources historiques de la consolidation V1.2 : lecture intégrale des deux référentiels locaux V1.1 et de [codex/AGENTS.md](AGENTS.md), ainsi que de la consigne jointe « MOVEE Biz : consolidation Q01–Q08 et audit des blocages V1 ». Les références historiques du paragraphe suivant décrivent l’intervention V1.1, pas de nouvelles lectures de fichiers absents. Les copies externes ne remplacent pas les référentiels locaux. Q01–Q08 précisent D12/D13 sans supprimer aucune décision : travail courant mutable, historique figé hors suppression explicite Q05/Q06. Aucune autre décision métier ni configuration technique n’est inventée.

Sources de l’intervention V1.1 lues le 18 octobre : [codex/AGENTS.md](AGENTS.md), `codex/CODEX_MOVEE_BIZ_MISE_A_JOUR_REFERENTIELS.md` (57 décisions D01–D57 et Q01), les deux référentiels V1.0 du 17 octobre avant édition. Inventaire du dépôt et état Git contrôlés en lecture seule.

**Sources historiques absentes du dépôt courant :** `codex/MOVEE_BIZ_SPECIFICATIONS.md` et `codex/MOVEE_BIZ_FINANCIAL_MODEL.md`. Leur contenu S01–S10 / F01–F11, intégré en V1.0, reste disponible dans le fonctionnel et sert de base conservatoire ; aucun fichier historique n’est recréé ni prétendu relu séparément aujourd’hui. Le workflow `MOVEE_PROJECTS_CODEX_WORKFLOW.md` n’a pas été retrouvé lors de la consolidation précédente. Aucun sous-dossier codex n’est présent ; les fichiers `.DS_Store` n’ont pas de valeur normative.

Consultations historiques du 17 octobre, pour les conventions seulement : en-têtes/structure des deux référentiels MOVEE App et des deux référentiels MOVEE Mobile dans leurs dépôts respectifs. Aucune règle métier importée, aucun autre projet modifié. Les anciens échanges ChatGPT complets ne sont pas accessibles ; seules les décisions transmises sont utilisées.

**Autorité : D01–D57 prévalent sur toute ancienne formulation contraire.** Les blocs historiques corrigés citent la décision applicable ; leurs chiffres, tableaux et formules restent conservés sauf changement explicitement décidé. Q01–Q08 sont désormais validées : autosauvegarde du travail mutable, création explicite et gestion des historiques (§7.4 du fonctionnel / §9.3 du technique). Les noms de pays, villes et données économiques ne créent aucun chiffre d’affaires automatique.

La séparation fonctionnel/technique, les frontières entre projets, les registres de décisions, la recette et les réserves sur l’implémentation suivent les conventions observées App/Mobile. La numérotation Biz suit la structure commune demandée, sans reproduire leurs organisations historiques à l’identique.

Les blocs S01–S10 et F01–F11 conservent le contenu historique intégré en V1.0. Les corrections de règles décidées le 18 octobre sont identifiées dans les blocs concernés ; les valeurs et formules financières historiques non contredites sont conservées. Leur titre est préfixé pour la traçabilité. Les indications techniques incluses dans le cadrage sont conservées pour ne perdre aucune exigence ; leur organisation cible est précisée dans [le référentiel technique](MOVEE_BIZ_TECHNICAL_REFERENCE.md).

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:366 -->

## 2. Présentation générale et objectifs

### S01 — Périmètre et identité


MOVEE est un concept de studios de fitness connecté, premium accessible, destiné notamment aux 40–70 ans, avec exercices de force, mobilité et cardio. La machine MOVEE à câbles motorisés, bras réglables, miroir-écran et tapis intégré adapte la résistance. L'emprise retenue **est de 2,5 m² par machine, mouvements compris** (encombrement physique annoncé 1,20 × 1,80 m).

**MOVEE BIZ** est une application autonome Python/Flask, dans un dépôt Git `movee-biz`, développée en local sur Mac puis déployée sur le VPS existant, indépendamment de Newapp. Base MariaDB, environnement Python, service Gunicorn/systemd, authentification et configuration propres. Pas de socle metadata-driven, de Designer ni de MCP. Pas d'API REST obligatoire : routes Flask + templates, Services métier, `db.py` SQL paramétré; isoler les accès SQL des vues et les calculs purs des accès DB. Prévoir migrations SQL versionnées et tests.

Domaines : `movee.info` pour le site grand public; `movee.biz` pour la franchise et les espaces sécurisés, **une seule application** avec routage par hôte, un seul codebase et une seule base MariaDB, CMS/auth/backend partagés sans dupliquer les services (D01); `movee.app` est réservé à MOVEE App (Newapp aujourd'hui), application de gestion opérationnelle des adhérents, coachs, crédits et séances, **hors périmètre MOVEE BIZ**. En local, fournir une configuration permettant de tester les deux sites sans DNS réel.

### 2.1 Deux sites et un socle partagé — D01

MOVEE Info désigne le site grand public `movee.info`, MOVEE Biz le site franchise `movee.biz` : deux pages publiques distinctes sur deux domaines, au sein d’une seule application Flask. Pied de page Info : « Devenir franchisé » vers Biz ; pied de page Biz : « Voir le site public » vers Info. Aucun troisième site public n’est déduit. Le dépôt `movee-biz` et la base existante `movee_biz` peuvent être réutilisés ; aucun renommage ni décision supplémentaire sur leur naming n’est imposé.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:381 -->

## 3. Positionnement dans l’écosystème MOVEE

MOVEE Info (`movee.info`) et MOVEE Biz (`movee.biz`) sont les deux sites d’une même application, codebase, base MariaDB et backend partagés (D01). Leur séparation est fonctionnelle et par hôte, pas une séparation d’applications ou de bases.

L’ensemble reste indépendant de MOVEE App (gestion opérationnelle), MOVEE Mobile (application mobile IA), MOVEE Motion (mesures posturales/corporelles) et Newapp. Leurs contraintes metadata-driven, SQL et Services ne s’appliquent pas par défaut. Toute intégration future exige spécification et validation explicites. Le domaine public précédent a été remplacé dans tout ce référentiel : seul `movee.info` est retenu.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:387 -->

## 4. Périmètre et exclusions

Promotion, franchise, candidatures, CRM, centres côté développement réseau, projets financiers et CMS. Aucune gestion opérationnelle des adhérents, crédits, séances, coachs, équipements ou programmes. Les prix/crédits et capacités décrits servent à la simulation, sans créer une application de gestion de séances. Aucun paiement en ligne V1 ni module documentaire général.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:391 -->

## 5. Profils, rôles et permissions

### S03 — Autorisations et périmètre


Deux rôles seulement : `member` et `admin`. Statut de compte distinct `pending/approved/rejected` (plus désactivation si nécessaire). Statut commercial indépendant du rôle. L'admin seul gère les hypothèses réseau, les candidatures, les demandes grand public, les centres et le simulateur réseau. Le membre approuvé gère uniquement ses propres projets et ses paramètres **locaux** : nombre de MOVEE, loyer, travaux/charges locales, coach salarié ou exploitant, fréquentation, calendrier des satellites, apport/financement, etc. Il ne modifie pas les prix réseau, redevances, prix des machines ni règles centrales. Les paramètres éditables sont affichés clairement; toute modification du réseau crée une nouvelle version de paramètres.

Authentification : mots de passe hachés robustement (Werkzeug/Argon2 si dépendance), CSRF, cookies sécurisés HttpOnly/SameSite, limitation tentatives, protection des accès par rôle/statut, réinitialisation mot de passe par token expirant, validation des entrées, secrets hors Git, journalisation des actions sensibles. Email via SMTP configurable, avec backend de test en local. RGPD : consentement et politique de confidentialité ; conservation et suppression selon D44–D50 (§11.1), avec vérification juridique avant implémentation. Les sessions et le second facteur admin suivent D51–D57 (§11.2). Ne pas envoyer de données personnelles dans les logs.

### 5.1 Propriété, administration et accès — D05, D14, D31–D39

Le membre gère ses propres projets et versions. L’admin ne peut jamais éditer l’original d’un membre : lecture seule et clonage dans son espace d’analyse, modifications uniquement sur cette copie (D05). Le rôle member couvre candidat/franchisé ; rôle, vérification email, approbation et pipeline commercial sont des notions distinctes.

L’espace de candidature et la messagerie sont accessibles avant approbation selon D35–D37 ; cela n’ouvre ni simulateur professionnel, ni projets, ni exports. Accès professionnel seulement après vérification email puis approbation manuelle. Le refus conserve le compte et peut être réexaminé ; toute demande de suppression suspend immédiatement les accès selon D48, y compris la messagerie. Les administrateurs autorisés partagent le fil candidat, chaque auteur restant identifié.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:406 -->

## 6. Interfaces, pages et parcours

### S02 — Quatre interfaces


#### 2.1 Grand public — `movee.info`
Landing page responsive : proposition de valeur, équipement, bénéfices, parcours, CTA; recherche de centres par ville/code postal et liste des centres publiés (avec adresse, contact et état d'ouverture); formulaire de demande d'information avec identité, coordonnées, ville/centre éventuel, message et consentement. **Toutes les demandes sont centralisées chez le franchiseur**, enregistrées et consultables/affectables par l'administrateur; aucun accès direct du franchisé aux demandes en V1 sauf décision ultérieure. Pour centre inexistant : permettre demande générale. Ne pas inventer de centres; utiliser des données de démonstration explicitement marquées en environnement de développement.

#### 2.2 Franchise — `movee.biz` public — D15–D30

Landing page franchise : concept, modèle Principal/Satellite, avantages, fonctionnement, coûts et conditions estimatifs, CTA de candidature. Le simulateur public gratuit sans inscription utilise le même moteur que le professionnel, avec un périmètre de restitution limité.

- **Entrées finales :** format de machines administrable, ville facultative, loyer estimé modifiable. Centre principal uniquement ; aucun satellite, apport personnel ou nombre libre de machines. L’ancien choix public coach oui/non n’appartient pas à la liste finale des entrées ; le mode d’exploitation reste configurable dans le professionnel.
- **Formats :** ajout/modification, activation/désactivation, ordre et défaut gérés par l’admin ; aucune liste ni configuration de 8 machines n’est figée pour le public. Les exemples de formats ne sont pas validés comme catalogue. Les calculs suivent la configuration active.
- **Ville :** références internes communales si disponibles, sinon défauts nationaux ; jamais d’effet automatique sur fréquentation ou CA. Le loyer reste modifiable.
- **Scénario :** réaliste uniquement. Sorties exclusivement investissement initial estimé distinctement HT et TTC, CA potentiel mensuel HT à maturité et annuel HT à maturité (12 mois au rythme de croisière, pas l’année 1). Taxes appropriées par poste pour l’investissement, sans taux uniforme supposé ; TTC = décaissement indicatif sans préjuger de récupération de TVA.
- **Aucune restitution publique** de charges, marge/EBITDA/rentabilité, trésorerie, financement, seuil de rentabilité, scénarios prudent/optimiste ou projection 36 mois. Le moteur conserve ces capacités pour les espaces autorisés ; elles ne sont pas exposées au visiteur.
- **Interaction :** recalcul automatique dès modification du format, de la ville ou du loyer ; aucun bouton « Calculer », aucun rechargement, appels inutiles évités. Une page responsive : paramètres/résultats en deux colonnes sur desktop, paramètres puis résultats sur mobile ; pas d’étapes.
- **Aucune persistance anonyme**, ni rattachement à l’inscription ni récupération après approbation. Le candidat approuvé recrée son projet professionnel. CTA exact : « Obtenir mon business plan complet » vers inscription/connexion puis approbation ; aucune promesse de téléchargement immédiat.

Cette rédaction remplace les anciennes entrées satellites/nombre libre, restitution CA/marge et transmission du scénario à l’inscription. D20 décrit une étape intermédiaire : le retrait effectif de l’apport est D25 (le renvoi à D27 dans D20 est une erreur matérielle) ; D27 impose le CA HT.

#### 2.3 Espace candidat / franchisé — D05, D12–D14, D31–D43

Inscription courte : **nom, prénom, email, téléphone, mot de passe**, cinq champs obligatoires seulement. Ville et statut coach pourront être demandés ultérieurement ; aucun apport à l’inscription. Lien email sécurisé temporaire avec renvoi possible ; candidature examinable et approbation uniquement après vérification de l’adresse. Notification admin, compte `pending`, décision manuelle `approved`/`rejected`, emails correspondants. Aucun accès aux simulations privées avant approbation.

Refus révisable : compte conservé sans accès professionnel, réouverture/réexamen et approbation possibles sans recréer le compte. Date, auteur et motif de refus obligatoire/interne historisés ; email de refus sans communication automatique du motif. Messagerie accessible avant et après approbation (§7.3), sauf désactivation/suppression ; candidat peut répondre aux compléments dans son dossier.

Un seul rôle `member` pour candidat et franchisé ; étapes commerciales séparées. Après approbation : projets détaillés sur 36 mois, scénarios prudent/réaliste/optimiste, sauvegarde, duplication et comparaison de versions et de projets distincts, centre principal et satellites avec nombre, ouverture et financement propres, paramètres locaux éditables, Excel BP et PDF explicatif (~10 pages selon contenu). Admin : lecture seule de l’original et clonage modifiable, jamais édition de l’original (D05).

La version de travail courante est mutable et autosauvegardée après debounce (Q01) ; les versions historiques sont figées, créées explicitement via « Créer une version » ou lors d’une actualisation volontaire des hypothèses centrales (Q02). Aucune actualisation centrale rétroactive automatique. Les changements du travail ne réécrivent pas l’historique ; restauration par copie, suppression confirmée et duplication indépendante sont définies au §7.4 (Q03–Q08). Exports identifiant projet/version/hypothèses ; aucune promesse de conservation serveur des exports.

#### 2.4 Administration franchiseur
Tableau de bord candidatures, approbation/rejet, notification email, notes internes et historique des contacts, relances datées (aujourd'hui/en retard/à venir) sans email automatique en V1. Pipeline commercial distinct de l'approbation : `à contacter`, `contacté`, `en discussion`, `projet validé`, `contrat signé`, `franchise ouverte`. Gestion des centres et leur publication sur la recherche publique; rattachement des satellites à un principal/franchisé, ville/territoire, dates d'ouverture. Hypothèses réseau contrôlées par l'admin (tarifs, redevances, prix machines, autres paramètres commerciaux); simulateur franchiseur 36 mois, déploiement réseau, cash, financement, valorisation, levées de fonds/dilution, exports Excel/PDF banque/investisseurs. Les paramètres globaux versionnés doivent être figés/snapshotés dans chaque projet afin de rendre les résultats reproductibles.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:441 -->

## 7. Domaines fonctionnels détaillés

Les quatre interfaces S02 couvrent acquisition, candidature, CRM, centres et projets. Le simulateur simple, le simulateur professionnel membre et le simulateur réseau admin partagent le moteur. Création et sauvegarde d’un projet, duplication, comparaison, principal et satellites, ouvertures et financements propres sont acquis. Aucun inventaire d’URL, maquette ou texte commercial final n’est fourni.

### S04 — Modèle métier


- Un franchisé exploite **un centre principal** et peut ouvrir plusieurs **satellites** dans son territoire. Franchise initiale : 7 ans renouvelables, exclusivité territoriale à contractualiser, droit d'entrée principal 15 000 € HT, **aucun nouveau droit d'entrée pour satellite**.
- Principal : typiquement 6–10 machines (exemple 8), coach salarié ou exploitant, séances collectives, autonomes et individuelles; ouvert 8 h–21 h tous les jours. Coach prévu lundi–samedi 11–14 h et 17–21 h (42 h/semaine); 4 cours collectifs/jour, 6 jours/semaine, d'une heure, occupant toutes les machines; les 18 h restantes servent à l'accompagnement. Attention : durée légale/majorations/remplacements à valider, ne pas présenter 4 200 €/mois comme conformité RH acquise.
- Satellite : sans coach et sans cours collectifs, **autonomie uniquement**; nombre de machines et mois d'ouverture variables, financement et charges propres; dépend d'un principal, pas de frais d'entrée additionnels.
- Onboarding client : Start Light 19 € TTC, 30 min; Start Complete 129 € TTC, 4 h de coach au total (1 h bilan, 2 × 1 h guidées, 2 × 30 min suivis); upgrade Light→Complete 110 € TTC; découverte gratuite promotionnelle possible. Coaching individuel uniquement au centre principal d'origine.
- Tarifs sans engagement : Active 69 € TTC/mois/8 crédits, Premium 119 € TTC/mois/16 crédits. Crédits mensuels expirant à l'anniversaire de facturation, consommation de référence 80 %, crédits abonnement consommés avant packs. Packs : 2 crédits 19 € TTC, 10 crédits 89 € TTC, 20 crédits 169 € TTC, valables jusqu'à consommation sous réserve CGV. Coût crédits : autonome 2, collectif 3, individuel 6. Hypothèses de mix de référence : 50 % Active, 30 % Premium, 20 % packs, et 80 % des séances via abonnement / 20 % via packs. **Ces deux mixes ne sont pas nécessairement mathématiquement compatibles** : le moteur doit signaler les écarts et utiliser une méthode de réconciliation documentée, sans double compter les revenus.
- Usage interfranchise : autonome et collectif uniquement; compensation à l'hôte provisoire 8 € HT/autonome, 12 € HT/collectif; pas de commission centrale supplémentaire au-delà des 5 % de royalties. Flux intercentres à traiter en compensation/clearing et à ne pas compter deux fois dans le CA consolidé. Les modalités exactes comptables et fiscales sont à confirmer.

### 7.1 Référentiel économique communal — D02–D04, D24

Pays et commune identifient chaque ville sans homonymie internationale ; une série de références par commune, aucun découpage économique par quartier, zone ou code postal. Le code postal reste utilisable pour la recherche publique de centres historiques, sans devenir une granularité du référentiel de coûts.

Admin saisit et maintient manuellement loyers au m², charges et contexte local. Origine/date renseignées si disponibles ; sinon « estimation interne » ou « valeur nationale par défaut ». Aucune API INSEE, géocodage ou fournisseur externe obligatoire. Les références locales préremplissent uniquement les hypothèses économiques, modifiables dans le professionnel et conservées en snapshot. Repli national sans ville ou sans donnée locale ; jamais de fréquentation, occupation, nombre de clients ou CA calculés automatiquement depuis la ville.

### 7.2 Historique et comparaison — D12–D13, Q01–Q08

Tout changement central/local/fiscal/commercial/FX laisse les historiques antérieurs intacts. L’autosauvegarde porte seulement sur le travail courant mutable. Actualiser volontairement les hypothèses centrales crée une nouvelle version traçable ; « Créer une version » fige explicitement un historique. Comparer historiques d’un projet et projets distincts (villes, formats/machines différents) sans les modifier : tableaux/graphiques côte à côte, hypothèses, résultats mensuels 36 mois et trois scénarios. Exports avec version du projet et des hypothèses. L’immutabilité interdit la modification de l’historique, pas sa suppression explicite confirmée Q05/Q06. Une comparaison référençant une version supprimée doit être actualisée ; aucun export déjà produit n’est réécrit.

### 7.3 Dossier et messagerie — D35–D43

Admin et candidat peuvent initier en permanence des échanges textuels, avant et après approbation, pendant la préparation du projet. Les demandes de compléments et réponses sont dans le dossier. **Un seul fil chronologique par candidat**, aucun fil par sujet/projet/admin ; tous les administrateurs autorisés peuvent consulter et répondre, auteur précis identifié.

Aucune pièce jointe ni upload candidature/messagerie en V1 ; documents éventuels transmis hors application par email. Messages envoyés immuables : ni édition ni suppression individuelle, correction par nouveau message ; exception d’effacement légal lors des purges RGPD (D40, D44–D50).

Premier nouveau message non lu : notification email ; suivants regroupés sans répétition jusqu’à consultation, puis nouveau cycle. Gérer le partage admin sans doublons, tous les messages restant visibles dans le fil. Le suivi technique de consultation ne crée aucun badge, compteur non lu, notification in-app ni alerte visuelle. Consultation manuelle possible ; cette absence d’alerte de messagerie n’annule pas le signalement administratif des échéances de purge.

Email localisé avec lien sécurisé vers la conversation après authentification ; réponse exclusivement dans MOVEE Biz, jamais ingestion d’une réponse directe à l’email. Aucun lien de notification ne contourne rôle, statut ou suspension. Les notifications transactionnelles de candidature restent distinctes des relances commerciales sans email automatique en V1.

### 7.4 Cycle des projets professionnels — Q01–Q08

**Deux objets fonctionnels distincts :** une version de travail courante mutable et des versions historiques figées. Les hypothèses centrales d’un travail ne sont pas remplacées silencieusement ; actualisation volontaire et traçable selon D12/Q02. Ce cycle concerne les projets professionnels, jamais le public sans persistance (D19).

| Décision | Comportement utilisateur et règle d’intégrité |
| --- | --- |
| Q01 | Modifications enregistrées automatiquement après un bref debounce dans le travail courant ; aucun bouton Enregistrer requis. États « Enregistrement… », « Enregistré », « Erreur de sauvegarde ». Avertir avant sortie si changements non persistés ; ne jamais annoncer Enregistré avant persistance effective. Expiration de session ne supprime pas ce qui est déjà enregistré ; aucune garantie inventée de sauvegarde de changements encore non persistés. |
| Q02 | « Créer une version » fige volontairement un historique. Autosauvegarde sans historique à chaque modification. Actualisation volontaire des hypothèses centrales créant aussi une nouvelle version traçable ; anciens historiques intacts, comparables entre projets et versions. |
| Q03 | Numéro séquentiel automatique par projet, date de création, libellé personnalisé facultatif (exemple « Hypothèses bancaires »). Numéro attribué jamais réutilisé après suppression d’intermédiaires ; identification stable. |
| Q04 | Restaurer = copier les paramètres d’un historique sélectionné vers le travail courant après confirmation d’écrasement ; conserver l’origine, aucun historique modifié. Les modifications ultérieures suivent Q01. |
| Q05 | Propriétaire : suppression d’un historique après confirmation explicite, travail et autres historiques intacts. Actualiser les comparaisons qui le référencent, exports Excel/PDF déjà produits inchangés. Obligations de conservation/effacement respectées ; aucun archivage serveur des exports promis. |
| Q06 | Propriétaire : suppression confirmée du projet, travail et historiques, sous obligations de conservation. Copies indépendantes admin gérées séparément conformément au RGPD, jamais modifiées silencieusement ; audit minimal sans conservation indue de données personnelles. |
| Q07 | Dupliquer le travail courant crée un projet indépendant avec nouvel identifiant, copie de ses paramètres/configurations/hypothèses, **aucun historique copié**, source intacte, historique propre et évolution indépendante. |
| Q08 | Admin configure/modifie le maximum de projets actifs par candidat approuvé/franchisé. À quota atteint, création et duplication bloquées ; consultation et modification de l’existant possibles. Projets supprimés exclus du décompte. Aucune valeur par défaut, aucun statut d’archivage inventé ; valeur non configurée = comportement technique à préciser, sans politique commerciale présumée. |

**Droits :** ces opérations sur un projet membre appartiennent au propriétaire approuvé. D05 reste intégral : l’admin lit l’original, ne l’autosauvegarde/restaure/supprime pas à la place du membre ; son analyse modifiable porte uniquement sur sa copie indépendante. Les actions de purge légale D44–D50 demeurent distinctes. Configurer un quota ne donne aucun droit d’édition du projet membre.

**Erreurs et sécurité :** sauvegarde refusée/échouée ou session expirée ne doivent pas être affichées comme un succès. Après réauthentification, les données déjà persistées restent disponibles ; prévenir la perte du travail non persisté par les états et l’avertissement Q01 sans promettre une récupération non spécifiée. Une action annulée, refusée faute de droit ou soumise à une obligation légale ne modifie pas silencieusement la source. Contrôler côté serveur propriété, approbation, session et confirmations des actions concernées ; protéger la cohérence du quota et des identifiants même avec opérations concurrentes. Les mécanismes techniques de conflit/reprise restent à définir, sans nouveau parcours métier imposé.

**Renvois techniques :** §8.3 pour l’interface, §9.3 pour persistance/intégrité et §10.3 pour les autorisations. Les suppressions explicites ne sont pas une édition d’un historique figé. La demande de suppression du compte D47–D50 conserve son traitement légal et suspension immédiate propres.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:496 -->

## 8. Règles métier et modèle financier intégral

Source historique de calcul : blocs financiers V1 intégrés F01–F11, complétés par D07–D12. Les montants en EUR sont les références françaises initiales, non des règles universelles ; HT/TTC, comptabilité, trésorerie et hypothèses distincts. Prévisions illustratives non contractuelles. Les conventions signalées comme modifiables ou à confirmer ne sont pas des règles commerciales définitives.

### S05 — Calculs, investissements et financement


Le modèle historique intégré F01–F11 conserve les formules, valeurs par défaut, limites, contrôles, scénarios et exports ; D01–D57 prévalent sur les formulations explicitement contredites. Le fichier historique séparé est absent du dépôt courant. Le moteur est une bibliothèque Python pure et testable; les routes et les exports consomment **exactement les mêmes résultats**. Projections mensuelles 36 mois par centre et réseau, HT/TTC explicites, trésorerie et compte de résultat séparés. Les coûts machines (4 000 € HT facturés, 3 500 € HT fabrication), transport/installation 100 € HT au coût, frais de franchise, travaux, BFR, amortissements, emprunts, IS, TVA, royalties, charges, réserves et marges sont configurables selon rôle.

Fabrication machines à la commande, délai 3 mois; franchisee verse 50 % à la commande et 50 % avant livraison; franchiseur paie fabricant 50 % puis 50 %; pas de stock. Garantie fabricant 2 ans, **pas de provision forfaitaire de garantie**. Maintenance 25 €/machine/mois distincte des réparations sous garantie. Renouvellement économique machine à 7 ans; réserve économique séparée des amortissements comptables.

### F01 — Principes de calcul


Entrée : `NetworkAssumptions` (version administrateur), `ProjectAssumptions` (hypothèses locales), scénario, calendrier d'ouvertures. Sortie : 36 lignes mensuelles par centre et consolidé, détail sources et avertissements. Séparer les modules : capacités → fréquentation → demande crédits → vente d'abonnements/packs → revenus HT → charges → résultat/IS → amortissements → emprunts → cash/TVA → indicateurs. Ne jamais calculer le CA comme `nombre_de_séances × prix` **en plus** des ventes d'abonnements/packs.

**Points à résoudre de manière visible** : le mix 50 % Active/30 % Premium/20 % packs décrit des types de clients, tandis que 80 % abonnement/20 % packs décrit des séances. Il peut être impossible de satisfaire les deux avec 80 % d'utilisation des crédits. Implémenter une stratégie cohérente de conversion de demande en ventes, afficher les écarts aux objectifs de mix et ne jamais générer de ventes fictives silencieusement. Les revenus récurrents sont reconnus selon abonnement vendu; les packs doivent avoir une convention explicite de reconnaissance (vente versus consommation, avec passif de revenu différé si retenu), distincte de l'encaissement. Prendre en compte expiration des crédits abonnements; ne pas faire passer des crédits non utilisés en revenu supplémentaire.

### F02 — Capacité et scénarios d'un principal


Principal ouvert 13 h/jour × 7 jours = **91 h/machine/semaine**. Quatre cours d'une heure du lundi au samedi = **24 h/machine/semaine**, toutes machines réservées aux cours; autonomie brute **67 h/machine/semaine** (avant créneaux 1:1, indisponibilités, maintenance et temps de rotation). À 8 machines : 192 places de cours/semaine et 536 créneaux-machine d'une heure autonomes théoriques; à 70 % cela fait **375,2 séances/semaine**. Ne pas confondre 91 h hebdomadaires avec une surface en m². La durée d'une séance autonome et l'occupation 1:1 doivent être des paramètres explicites (défaut de simulation 60 min à confirmer). Satellite : pas de cours ni coaching, capacité selon horaires paramétrables; défaut 13 h/jour × 7 jours, à confirmer.

| Mois | Prudent cours | Prudent auto | Réaliste cours | Réaliste auto | Optimiste cours | Optimiste auto |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 10% | 5% | 15% | 10% | 20% | 15% |
| 2 | 15% | 10% | 20% | 15% | 25% | 20% |
| 3 | 20% | 15% | 25% | 20% | 30% | 25% |
| 4 | 25% | 20% | 30% | 25% | 40% | 30% |
| 5 | 30% | 25% | 35% | 30% | 45% | 35% |
| 6 | 35% | 30% | 40% | 35% | 55% | 40% |
| 7 | 40% | 35% | 45% | 40% | 60% | 45% |
| 8 | 45% | 40% | 50% | 45% | 70% | 50% |
| 9 | 50% | 45% | 55% | 50% | 75% | 55% |
| 10 | 55% | 50% | 60% | 55% | 85% | 60% |
| 11 | 60% | 55% | 65% | 60% | 90% | 65% |
| 12 | 65% | 60% | 70% | 65% | 100% | 70% |

**Décision validée** : après M12, continuer à progresser jusqu'à maturité **100 % cours / 70 % autonomie**, puis stabiliser. La vitesse de convergence M13–M36 n'a pas été définie : retenir par défaut une interpolation linéaire vers les cibles à M24, **étiquetée convention technique modifiable par l'admin**. Pour le scénario optimiste, maturité atteinte dès M12. Saturer à 100/70; ne pas dépasser les capacités. La courbe est relative à chaque ouverture de centre, non au calendrier global.

### F03 — Crédits et revenus clients


| Produit | Prix TTC | Crédits | Règle |
|---|---:|---:|---|
| Active | 69 € / mois | 8 | Sans engagement, crédits expirent au cycle anniversaire |
| Premium | 119 € / mois | 16 | Sans engagement, crédits expirent au cycle anniversaire |
| Pack 2 | 19 € | 2 | Prépayé |
| Pack 10 | 89 € | 10 | Prépayé |
| Pack 20 | 169 € | 20 | Prépayé |
| Start Light | 19 € | — | 30 min de coach |
| Start Complete | 129 € | — | 4 h de coach |
| Upgrade Light→Complete | 110 € | — | Conversion |

Crédits par séance : autonome **2**, collectif **3**, individuel **6**. Consommation cible des crédits abonnement **80 %**, abonnements consommés avant packs. Mix de référence **50 % Active / 30 % Premium / 20 % packs** par clients; **80 % abonnement / 20 % packs** par séances; les deux sont des **cibles**, pas des égalités garanties. Paramètres d'onboarding et coaching individuel à afficher séparément, avec capacités du coach et conversion commerciale configurables (valeurs par défaut prudentes explicitement indiquées). Gratuité découverte optionnelle.

Formules : `demande_credits = 2 * sessions_autonomes + 3 * sessions_collectives + 6 * sessions_individuelles`. `ca_ht = somme_des_ventes_ttc / (1 + taux_tva)` pour produits taxables à TVA standard (20 % par défaut, configurable). Déterminer nombre de membres actifs et packs par modèle de cohortes ou allocation optimisée, **sans arrondis qui créent des revenus non justifiés**; documenter le choix et tester crédits fournis/consommés/expirés/reportés. Pour les packs, pas d'expiration arbitraire. La répartition des packs 2/10/20 n'est pas figée : choix paramétrable et documenté.

### F04 — Investissement d'un centre


Par MOVEE : **4 000 € HT facturés** au franchisé, **3 500 € HT coût fabricant**, **500 € HT marge brute franchiseur**. Transport + installation **100 € HT/machine** refacturés au coût. Achat ferme sans leasing. Fabrication sur commande **3 mois**; 50 % payé à la commande et 50 % avant livraison, même phasage fabricant. Pas de stock. Garantie fabricant 2 ans, **pas de provision de garantie 70 €/machine**. Maintenance **25 €/machine/mois**.

Surface indicative : `surface_m2 = ceil((2.5*n + 8*ceil(n/2) + 25) * 1.15)` avec 1 vestiaire de 5 m² et 1 douche séparée de 3 m² pour 2 machines, salon 15 m², accueil/stockage/tech 10 m², circulation 15 %. **Pour n=8 : ceil((20+32+25)*1.15) = ceil(88.55) = 89 m²**, et non 91 m² (valeur provisoire utilisée précédemment). Prévoir possibilité de surface réelle saisie, en affichant la recommandation calculée.

Travaux généraux : **800 €/m² HT**; vestiaire **3 000 € HT par module 2 personnes**, douche **4 000 € HT par unité**, mobilier/déco/enseigne/accès/IT **10 000 € HT**. Éviter tout double compte travaux/équipements. Droit d'entrée **15 000 € HT pour le principal uniquement**, 0 pour satellite. **Exemple 8 machines** : surface 89 m², travaux 71 200 €, vestiaires 12 000 €, douches 16 000 €, mobilier 10 000 €, machines 32 000 €, livraison 800 €, entrée 15 000 € = **157 000 € HT** hors lancement, TVA, fonds de roulement et frais financiers. Ne pas ajouter de marge de 20 % sur travaux turnkey; seuls 500 €/machine constituent la marge explicite sur vente d'équipement.

Pour satellites, ne pas appliquer automatiquement toutes les surfaces/équipements du principal : permettre un profil d'aménagement satellite spécifique **à confirmer**, avec détail éditable et sans double compte. Coûts d'installation et équipements propres par site.

### F05 — Charges et financement franchisé


Loyer référence **200 € HT/m²/an** (8 MOVEE/89 m² → **1 483,33 €/mois**, et non 1 517 € issu de 91 m²). Autres charges mensuelles principales de référence avant correction de la maintenance : énergie 350, eau 120, ménage 450, assurance 120, internet/sécurité 70, comptabilité/paie/banque 180, taxes locales 150, marketing/divers 200, maintenance `25*n` (200 pour n=8), soit **1 840 €/mois à n=8**. Pas de frais logiciel distincts (inclus dans redevance). Redevance franchiseur **5 % du CA HT**. Pas de fonds marketing additionnel.

Coach salarié coût chargé **4 200 €/mois** par défaut, hausse 2 %/an, ou coach franchisé exploitant coût salarié = 0 avec **rémunération souhaitée optionnelle**, défaut 0 et coût social à calculer selon statut juridique paramétré (ne pas assimiler net et coût entreprise). Charges fixes principales pour 8 MOVEE avec surface corrigée : **1 483,33 + 1 840 + 4 200 = 7 523,33 €/mois** avec salarié; **3 323,33 €/mois** avec exploitant non rémunéré. Trésorerie de sécurité initiale = **3 mois de charges fixes** (22 570 € ou 9 970 € respectivement, hors autres charges variables et échéances de prêt).

Financement par site : **30 % apport / 70 % emprunt**, durée **7 ans**, taux nominal **4 % annuel** indicatif, échéances mensuelles amortissables; montant financé = investissement + BFR initial et frais pertinents selon configuration. Chaque satellite : apport, prêt, ouverture, machines propres. Ne pas comptabiliser le remboursement du capital en charge du résultat; intérêts en charge financière, capital en trésorerie. Loyer et charges indexés **2 %/an** par défaut, salaires 2 %, tarifs **0 %/an** par défaut. IS : **15 % jusqu'à 42 500 € de bénéfice éligible puis 25 %**, **sous condition d'éligibilité légale** et avec report des pertes simplifié documenté; taux personnalisables. TVA standard **20 %** configurable; gérer TVA collectée/déductible et calendrier de décaissement de façon explicite. Amortissements comptables : machines 5 ans, travaux 10 ans, mobilier/IT 5 ans. Réserve de remplacement économique **4 000/(7×12) = 47,619 €/machine/mois**, **ne pas la déduire deux fois** en charge comptable et en cash si simple mise en réserve interne.

### F06 — Redevances et flux intercentres


Redevance 5 % du CA HT franchisé, avec logiciel/support inclus. Interfranchise : centre d'origine conserve la relation client; centre hôte reçoit **8 € HT/autonome**, **12 € HT/collectif** (montants provisoires). Aucun prélèvement central supplémentaire. Présenter séparément ventes clients, flux de clearing, CA par centre et éliminations intragroupe/entre centres pour les vues consolidées; expliciter la base de royalties sur ces flux pour éviter double perception. Individuel et onboarding uniquement au principal d'origine.

### F07 — Franchisor — revenus, charges, déploiement


Revenus : **15 000 € HT** par franchise principale signée/ouverte selon convention de reconnaissance documentée; **500 € HT de marge machine** sur chaque vente; **5 % royalties** sur CA HT franchisés. Coût de formation initiale **300 € HT/franchise**, 1 journée de 7 h incluse dans droit d'entrée. Transport/installation 100 €/machine au coût, marge nulle. Budget de lancement **10 000 € HT** juridique/commercial (DIP, contrats, marque, docs), sans nouvel investissement logiciel (déjà développé). Légal récurrent **3 000 €/an**, **attention** à la ligne mensuelle juridique de 250 € ci-dessous : il s'agit du même budget, **ne pas additionner deux fois**.

Charges centrales mensuelles hors salaires : hébergement/sauvegardes 500, marketing national 2 000, acquisition franchisés 500, administratif 1 000, déplacements 500, juridique 250 = **4 750 €/mois**; variable IT **2 €/machine active/mois**. Année 1 : fondateur seul, pas de salarié permanent; année 2 (à partir M13) responsable développement **4 500 €/mois coût chargé**; année 3 (à partir M25) technicien/support/formation **3 500 €/mois coût chargé**; salaires +2 %/an. Fondateur en SAS assimilé salarié : salaire net M1–12 = 0, M13–24 = **2 000 €/mois**, M25–36 = **3 000 €/mois**, **calculer le coût chargé à partir d'une hypothèse de cotisations configurable, non inventer un taux légal exact**. Dividendes 0 % par défaut, distribution optionnelle de profits distribuables; commission apporteur franchise 0 € par défaut.

| Scénario | Nouvelles franchises année 1 / 2 / 3 | Principaux M36 | Satellites M36 | Centres totaux M36 |
|---|---|---:|---:|---:|
| Prudent | 2 / 3 / 5 | 10 | 5 | 15 |
| Réaliste | 5 / 8 / 12 | 25 | 15 | 40 |
| Optimiste | 10 / 15 / 25 | 50 | 40 | 90 |

Calendrier mensuel d'ouvertures **éditable**, nombre de machines/centre et satellites distincts; si absent, distribution mensuelle uniforme déterministe et signalée comme hypothèse. Distinguer date signature, commande, livraison et ouverture, en intégrant **3 mois de fabrication**. Royalties uniquement sur centres ouverts et chiffre d'affaires réellement projeté. Pas de royalties fictives sur un centre non ouvert.

Trésorerie initiale centrale de référence : **6 mois × 4 750 = 28 500 €** + **10 000 €** lancement = **38 500 €**, hors payroll fondateur, IT variable, besoins additionnels et TVA. Minimum de cash roulant **3 mois de charges fixes** : initialement 14 250 € (non additionné automatiquement aux 6 mois de réserve). Financement de départ indicatif 30 % equity (**11 550 €**) et 70 % dette (**26 950 €**) sur **5 ans à 4 %**; recalculer selon besoin réel, financement gap quand cash sous minimum. Les salaires et expansion peuvent accroître le besoin. Scénarios investisseurs : montant levé, valorisation pré-money, post-money = pré-money + investissement primaire, dilution = investissement/post-money, distinguer primaire/cession secondaire et cash entrant société.

### F08 — Valorisation et indicateurs


À M36, EV indicative = EBITDA annuel de référence × **4 / 6 / 8** (multiples **illustratifs**, non attestés marché). Valeur des capitaux propres = EV − dette financière nette (dette moins trésorerie, convention explicite). EBITDA négatif : éviter une valorisation mécanique trompeuse, afficher avertissement et méthode alternative éventuelle. Indicateurs : CA, EBITDA, EBIT, résultat net, cash-flow opérationnel, cash après dette, trésorerie, seuil de rentabilité, ROI, DSCR indicatif, dette, nombre de centres/franchisés/machines, taux d'occupation, ARPU/clients nécessaires, royalties, marge machines. Proposer analyse de sensibilité.

### 8.1 Pays, devise et consolidation — D07–D11

Un moteur commun extensible avec paramètres/règles par pays : devise, TVA/taxes, fiscalité, charges sociales, financement et conditions commerciales. **France seule active en V1** ; l’admin peut préparer de futurs pays sans les activer, aucune règle fiscale étrangère inventée. La langue d’interface est indépendante du pays projet.

Prix machines, droit d’entrée, royalties, abonnements, packs et autres conditions commerciales sont configurables par pays, versionnés et figés dans chaque simulation. Les valeurs françaises historiques restent exactement celles de S04/F03–F07 (notamment 4 000 € HT machine, 15 000 € HT entrée, 5 % CA HT, Active/Premium 69/119 € TTC et packs 19/89/169 € TTC), sans portée universelle.

Simulation locale dans la devise du pays ; consolidation franchiseur/réseau en EUR. France : aucune conversion. Admin renseigne manuellement les taux par devise, date de référence et historique, sans API obligatoire ; taux exact utilisé figé dans chaque snapshot de simulation/consolidation, sans actualisation rétroactive. Convention de cotation/arrondis et contrôles d’une future devise à détailler sans inventer de taux.

Les sorties professionnelles conservent tout le modèle 36 mois ; le public ne reçoit que les agrégats autorisés au §6.2. Les règles HT/TTC d’investissement public s’appliquent par poste, distinctes de la formule historique de CA taxable standard F03.

### 8.2 Fiche France et validation R01

Voir [l’annexe R01 — fiche France](#17-annexe-r01--fiche-financière-france-et-recette-conditionnelle) pour catalogue FL01–FL15, qualification TVA, assiettes/clearing, identités cash/résultat et 12 cas FR-T01–FR-T12. Les formules F01–F11 restent textuellement conservées ; l’annexe explicite seulement leurs hypothèses et points de validation. Exemple : CA taxable standard F03 n’est pas un taux universel sur investissements, prépayés ou clearing ; séparer taux, exigibilité et paiement. Les résultats conditionnels n’accordent ni fiscalité validée ni revenu supplémentaire. Mise en œuvre cible : technique §11.3.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:615 -->

## 9. Données fonctionnelles, paramètres et persistance

### S06 — Données et persistance


Créer un **schéma MariaDB propre à MOVEE BIZ**, sans réutiliser ni modifier les tables Newapp. Codex doit concevoir des migrations explicites et un schéma minimal couvrant comptes/approbations, candidatures, pipeline/historique/relances, demandes d'information, centres/territoires et rattachements, projets de simulation et snapshots d'hypothèses, versions des paramètres réseau, éventuellement audit et tokens de réinitialisation. **Ne pas créer de tables de gestion opérationnelle des abonnements, crédits, séances ou dossiers clients** : elles appartiennent à MOVEE App. Aucun centre fictif en production. Index/contraintes FK/unique nécessaires, transactions sur écritures multi-tables. Ne pas créer une table par calcul financier dérivé si le calcul peut être reproduit depuis les hypothèses enregistrées.

Paramètres réseau réservés à l’admin, locaux au membre approuvé ; versions et snapshots par projet selon S02–S03. Les noms NetworkAssumptions et ProjectAssumptions désignent des entrées cibles du moteur, pas des classes existantes.

### 9.1 Données cibles supplémentaires — D02–D13, D31–D57

Références économiques pays/commune (origine/date), configurations publiques ordonnées/activables et défaut, paramètres commerciaux/fiscaux par pays avec activation contrôlée, taux FX historiques et snapshots. Projets/version/hypothèses/FX et comparaisons reproductibles ; aucun stockage de simulation anonyme publique.

Vérification email et approbations/refus historisés (motif interne), fil textuel unique avec auteur/consultation pour regroupement des emails, demandes de suppression datées/statutées, échéances et exceptions légales, trace de purge minimale non identifiante, appareils de confiance/révocations et sessions. Ce sont des besoins fonctionnels de persistance ; aucun nom de table, colonne, schéma physique, token ou job n’est créé ou inventé ici.

### 9.2 Travail, historiques et quota — Q01–Q08

Représenter fonctionnellement travail mutable, historiques figés, identifiant projet indépendant, séquence non réutilisable, date, libellé facultatif et origine de restauration. Les copies Q07 n’emportent pas d’historique. Décompte des projets actifs et maximum configuré admin, exclusion des projets supprimés, contrôle à création/duplication seulement. Comparaisons à actualiser après suppression et audit minimal de projet ; aucune conservation d’export serveur déduite. Aucun schéma SQL définitif ni nom physique décidé.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:634 -->

## 10. Internationalisation et CMS

### S10 — Internationalisation et CMS des deux landing pages — exigence V1


Tout le périmètre fonctionne en **français, anglais et espagnol** dès la V1 (D06), notamment les deux fronts publics (`movee.info` et `movee.biz`), avec ajout ultérieur de langues sans modification du schéma. Les contenus éditoriaux des one-pagers (titres, paragraphes, CTA, FAQ, textes des sections, métadonnées SEO, textes alternatifs des médias) sont stockés en **MariaDB**, et **non codés en dur dans les templates**. Utiliser une structure normalisée avec une entrée par clé stable, langue et site/page (par exemple `public.hero.title` / `franchise.hero.title`), contrainte d'unicité appropriée, publication et repli documentés; les noms physiques des tables sont à définir dans les migrations de ce dépôt neuf.

**Éditeur de contenu intégré à l'administration V1** : l'administrateur peut consulter et modifier les traductions FR/EN/ES pour chaque landing page, avec aperçu, validation, statut de publication et protection contre les traductions manquantes. L'édition est strictement réservée au rôle `admin`, avec protections CSRF, échappement HTML et contrôle des contenus riches; conserver au minimum la date et l'auteur de modification. Les traductions sont des contenus gérés, pas une fonction de traduction automatique obligatoire. Prévoir des données initiales traduites explicitement et ne jamais afficher une traduction fictive comme validée.

Les templates sont communs à toutes les langues. Détection initiale de langue par préférences du navigateur, **sélecteur manuel prioritaire** conservé entre les visites et **repli français** si une traduction manque. Définir des URLs publiques indexables et cohérentes par langue (par exemple `/fr/`, `/en/`, `/es/` sur chaque domaine), balises `hreflang`, titre et description SEO localisés, canonical et sitemap appropriés. La recherche de centres et les formulaires fonctionnent quelle que soit la langue; enregistrer la langue de la demande quand utile.

Les messages techniques (formulaires, validation, erreurs, authentification, simulateurs) utilisent un système i18n dédié avec catalogues de traduction versionnés, séparé du contenu éditorial MariaDB. Ne pas mélanger les contenus publics et les libellés système dans des templates codés en dur. Tester changement de langue, fallback, permissions d'édition, protection XSS et cohérence des deux domaines.

### F11 — Présentation multilingue des résultats


Le moteur financier conserve des identifiants de métriques et des résultats numériques indépendants de la langue. Les libellés, descriptions, avertissements, formats de nombres, devises et dates affichés dans les simulateurs et exports sont localisés via les catalogues i18n. **La langue ne doit jamais modifier les calculs ni les hypothèses**. Les textes éditoriaux des deux landing pages relèvent du CMS MariaDB décrit dans le bloc S10 intégré (source historique séparée absente), pas du moteur financier. Tester qu'une simulation donne les mêmes montants en FR, EN et ES.

### 10.1 Multilingue intégral — D06–D08

FR/EN/ES couvrent deux sites publics, compte, candidature, messagerie, professionnel, administration/CRM, simulateur franchiseur, emails, erreurs et exports PDF/Excel dès V1. CMS MariaDB pour éditorial public, catalogues i18n pour système ; langue d’interface distincte du pays du projet, mêmes hypothèses et chiffres quelle que soit la langue. Trois langues n’activent pas trois pays : France seule active financièrement. Aucun texte traduit non fourni n’est présenté comme validé.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:656 -->

## 11. Sécurité et confidentialité fonctionnelles

Les exigences S03 et S10 demeurent : consentement, politique de confidentialité, cloisonnement des projets, édition CMS admin, absence de données personnelles dans les logs. Demandes grand public centralisées franchiseur sans accès direct franchisé en V1. Les décisions ci-dessous précisent conservation, suppression et authentification ; elles ne valent pas validation juridique externe.

### 11.1 Conservation et suppression — D44–D50

Candidatures non abouties : référence **2 ans après dernier contact significatif**, couvrant dossier, coordonnées, messages et données personnelles. Vérifier base juridique et délai applicable avant implémentation ; aucune règle RGPD universelle de 2 ans. Politique distincte pour franchisés actifs. À échéance : détection et signalement automatiques, revue des exceptions/fondements documentés puis validation administrative manuelle ; aucune rétention indéfinie sans justification.

Après validation : **suppression plutôt qu’anonymisation** des coordonnées, données de candidature et messages, sauf obligation légale documentée ; trace minimale non identifiante. L’immutabilité des messages ne s’oppose pas à l’effacement légal.

Fonction personnelle « Supprimer mon compte » : confirmation explicite, demande datée/statutée, contrôle légal, traitement et notification, indépendamment des 2 ans. Dès demande : fermer les sessions et suspendre immédiatement simulateur, projets et messagerie pendant traitement. Annulation possible avant effacement définitif : candidat contacte MOVEE, vérification d’identité puis annulation/réactivation par admin ; après effacement aucune restauration. Ce contact ne suppose pas de messagerie utilisable pendant la suspension.

Suivi des échéances de réponse : en principe **un mois**, extension jusqu’à **deux mois supplémentaires** dans les cas légalement prévus avec information dans le premier mois ; traitement plus tôt possible, aucun SLA interne de 7 jours ni attente imposée d’un mois. Les détails de base légale, contact significatif et conservation des actifs restent à préciser avant implémentation.

### 11.2 Second facteur et sessions — D51–D57

Admin : 2FA obligatoire pour accéder à l’administration, après mot de passe par code email à l’adresse vérifiée, usage unique et **5 minutes**. Nouveau code invalide l’ancien ; tentatives et renvois limités. Aucun TOTP imposé, aucune obligation de 2FA pour candidat/franchisé. Dépendance à la sécurité de la boîte email : compromission de celle-ci compromet le second facteur ; modalités de protection/récupération à détailler.

Après 2FA, choix de confiance navigateur **30 jours**, jeton sécurisé spécifique au navigateur, pas seulement IP. Connexions suivantes exigent mot de passe, sans nouveau code si confiance valide et sans événement de sécurité ; la déconnexion ne révoque pas automatiquement cette confiance. Liste des appareils : type/navigateur, dates d’autorisation, dernière utilisation, expiration ; révocation individuelle/globale côté serveur, 2FA à la prochaine connexion après révocation.

Sessions expirant **côté serveur** après inactivité réelle : admin **30 minutes**, candidat/franchisé **2 heures**, déconnexion/réauthentification. Polling automatique ne prolonge pas les sessions ; confiance appareil ne prolonge pas une session. Les choix de jetons, stockage et mécanismes de contrôle restent techniques à détailler.

### 11.3 Protection des projets et opérations destructives — Q01, Q04–Q08

Autosauvegarde uniquement sur travail autorisé, jamais sur original membre par admin ; session expirée/refus de droit bloque les nouvelles écritures sans effacer les sauvegardes acquises. Restaurer exige confirmation d’écrasement ; supprimer historique/projet exige confirmation explicite et contrôle des obligations légales. Une suppression de projet n’efface pas silencieusement les copies indépendantes admin, qui restent soumises à leur propre gestion RGPD. Trace minimale, sans rétention personnelle injustifiée. Q05/Q06 ne contournent pas les obligations d’effacement D44–D50 et ne promettent pas de conservation documentaire supplémentaire.

### 11.4 Politique détaillée R02

Voir [l’annexe R02 — conservation par catégorie](#18-annexe-r02--politique-rgpd-et-conservation-par-catégorie) : matrices G01–G16, traitements par état du dossier et effets Q05/Q06/D47 sur originaux, copies admin, exports, logs et sauvegardes. Deux ans reste la référence conditionnelle D44, pas une durée universelle pour actifs/projets/archives. L’immuabilité numérique ne contourne pas l’effacement légal ; une sauvegarde n’autorise pas à restaurer un dossier effacé. Mise en œuvre cible : technique §15.3, sans SQL ni nouveau privilège d’édition admin.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:686 -->

## 12. Cas particuliers, exceptions et conventions

### S09 — Points non figés — décisions d'implémentation documentées


Méthode exacte de déduction des abonnements/packs à partir de la demande en crédits; répartition de la fréquentation entre individuel et collectif; rythme de convergence vers maturité après M12; détail charges satellites; ventilation mensuelle des ouvertures du réseau; coûts salariaux complets du fondateur; TVA sur flux de compensation; dates précises de reconnaissance comptable des revenus et commissions; modalités d'email et géocodage. Codex doit **choisir des conventions explicites, paramétrables et testées**, les signaler dans `ASSUMPTIONS.md` et ne pas les présenter comme validées commercialement. Pas de services tiers payants requis pour démarrer.

### F10 — Hypothèses non arrêtées


Les données commerciales ne permettent pas encore de fixer de manière unique : acquisition/rétention membres, churn, répartition des packs, 1:1, onboards, reconnaissance revenus prépayés, répartition intra-mois, profil travaux satellites, rythme M13–M24, coût employeur exact du fondateur, taxes locales détaillées, fiscalité des transferts intercentres. Codex doit écrire **`ASSUMPTIONS.md`** pour ses conventions, utiliser des valeurs par défaut modifiables plutôt que les déguiser en décisions validées, et tester la sensibilité des résultats. Aucun chiffre d'affaires garanti.

### 12.1 Priorité des décisions du 18 octobre

Les réserves financières S09/F10 sont conservées ; la liberté de conventions techniques ne peut contredire D01–D57 ou Q01–Q08, désormais toutes validées. Pour email et géocodage : réponses dans l’application, notifications regroupées, 2FA email et référentiel économique communal interne sont désormais décidés ; transport, stockage et contrôles restent à détailler. Les sessions, suppressions et délais suivent §11 ; les formulations historiques génériques « à valider » ne les rouvrent pas.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:702 -->

## 13. Critères d’acceptation fonctionnels et financiers

### S07 — Exports, qualité et UX


Excel : hypothèses, CAPEX, financement, compte de résultat mensuel 36 mois, cash-flow, indicateurs, scénarios et tableaux synthétiques; feuilles avec formules ou valeurs traçables et unités. PDF : business plan clair (~10 pages cible, longueur adaptée aux données), contexte, hypothèses, rentabilité, trésorerie, risques et avertissements. Chaque export mentionne scénario, date, version des paramètres et distinction prévision/non garantie.

UI responsive FR/EN/ES sur tout le périmètre (D06), formulaires accessibles, montants HT/TTC avec devise du pays visibles selon les limites publiques D16–D27, tableaux lisibles sur mobile, graphiques utiles, validation et messages d'erreur, données de démonstration identifiables. Tests unitaires du moteur, intégration DB/auth/permissions, navigation multi-domaines, tests exports, migrations et CI. Aucun paiement en ligne V1; aucun module documentaire général; aucune réservation ou gestion des adhérents.

### S08 — Critères d'acceptation V1


1. Démarrage local reproductible via README + `.env.example`, migrations et commandes de test.
2. Les deux domaines (ou hôtes locaux) rendent les deux landing pages de la **même application**.
3. Recherche centres et formulaire d'information fonctionnent, demande visible à l'admin uniquement.
4. Inscription, email, approbation manuelle et droits d'accès sécurisés fonctionnent.
5. Simulations sauvegardées/dupliquées/comparées; paramètres réseau verrouillés pour membres; satellites configurables.
6. Résultats financiers cohérents sur 36 mois, scénarios et contrôle explicite des incompatibilités de mix; tests d'invariants financiers.
7. Admin : pipeline, notes, relances, centres, simulateur réseau et versions de paramètres.
8. Excel et PDF exportent les mêmes chiffres que l'écran.
9. Aucun lien DB ou authentification avec Newapp; aucun MCP; secrets exclus du dépôt.
10. Aucune hypothèse ambiguë n'est masquée : les approximations sont étiquetées et testées.

### F09 — Invariants de test et cas de référence


- `surface(8)=89`; `investissement_principal(8, défauts)=157000` € HT **avant BFR**.
- `charges_hors_loyer_coach(8)=1840 €/mois`; loyer 89×200/12 = 1483,333… €/mois.
- `charges_fixes(8, salarié)=7523,333… €/mois`; coach exploitant non rémunéré = 3323,333… €/mois.
- Capacité cours 8×24=192 places/semaine; autonomie brute 8×67=536; à 70 % =375,2 séances/semaine (avant 1:1).
- 500 €/machine de marge fabricant franchiseur; 100 €/machine transport marge zéro; aucun stock et aucun droit d'entrée satellite.
- Royalties = 5 % CA HT, jamais 5 % TTC; aucun revenu doublé entre séances et abonnements.
- Crédit packs non expiré par défaut; crédits abonnements expirés en fin de cycle; pas de solde négatif.
- IS seulement sur bénéfice imposable, seuil réduit conditionnel; remboursement capital hors résultat; amortissements non décaissés.
- Résultat d'une simulation identique entre écran, Excel et PDF; projections M1–M36 cohérentes même pour ouvertures différées.
- Lignes juridiques centrales 250 €/mois = 3 000 €/an, pas 6 000 €.
- Comparer scénarios prudent/réaliste/optimiste et mode coach; tests de sensibilité TVA, taux prêt, machine count, lancement satellites.

Ces critères sont à réaliser et à tester, aucun résultat de recette n’est revendiqué.

### 13.1 Recette documentaire des décisions D01–D57

- Deux hôtes Info/Biz pour la même application/base, liens de pied de page réciproques, aucune dépendance DB/auth avec les autres projets.
- Ville : défauts nationaux/locaux manuels par commune, origine/date ; changer ville/loyer n’altère jamais fréquentation/CA à configuration/scénario identiques. France seule active, catalogues pays préparables, EUR en consolidation et taux FX figés.
- Public : formats admin, principal uniquement, ville facultative/loyer modifiable, réaliste seul, investissement HT+TTC par poste et CA HT mensuel/annuel à maturité ; aucun autre indicateur/projection/satellite/apport, aucun stockage/transfert, recalcul direct responsive une page et CTA sans téléchargement immédiat.
- Candidature : cinq champs, vérification email préalable à examen/approbation, professionnel bloqué avant approbation mais messagerie autorisée ; refus motivé interne/révisable et historique.
- Projets : admin ne modifie jamais un original membre ; copie et versions comparables sans réécriture, aucune actualisation automatique, export versionné ; autosauvegarde du seul travail courant selon Q01, historiques explicites selon Q02 et suppressions confirmées Q05/Q06.
- Messagerie : fil unique partagé, texte seul, auteur identifié, messages immuables hors purge, regroupement email réinitialisé par consultation sans doublons, aucun badge/alerte in-app, réponse uniquement après authentification dans l’application.
- RGPD : échéances/exception/revue/purge avec validation, suppression et trace minimale, demande personnelle avec suspension immédiate, annulation avant purge seulement, suivi des délais réglementaires sans SLA 7 jours.
- Sécurité : code email admin unique 5 min, remplacement/limites ; confiance navigateur 30 jours révocable sans révocation par simple logout ; sessions serveur 30 min/2 h sans prolongation par polling.
- Tout le périmètre, emails/exports inclus, est FR/EN/ES ; résultats numériques identiques selon langue. Chaque D01–D57 est couvert individuellement dans le tableau du §16.1.

Ces critères sont **spécifiés et non exécutés** ; aucune recette applicative ni conformité légale n’est attestée.

### 13.2 Critères d’acceptation Q01–Q08

- Modifier un travail : autosauvegarde après debounce et trois états exacts ; erreur visible, avertissement si sortie non persistée, persistance acquise conservée après expiration de session. Aucun historique créé à chaque frappe.
- « Créer une version » et actualisation volontaire des paramètres centraux produisent un historique traçable sans mutation des précédents. Numéro séquentiel/date/libellé facultatif ; supprimer un intermédiaire ne permet jamais de réutiliser son numéro.
- Restaurer après confirmation copie vers travail et garde l’origine ; annuler ne remplace rien, original et autres historiques intacts.
- Supprimer historique/projet exige propriétaire, confirmation et contrôle légal ; comparaisons actualisées, exports déjà produits inchangés, copies admin indépendantes et audit minimal. Pas d’archivage d’exports serveur promis.
- Dupliquer : nouvel identifiant, paramètres/configurations/hypothèses du travail copiés sans historique ; source intacte. Quota configuré contrôlé pour création/duplication, exclut supprimés et ne bloque ni lecture ni édition de l’existant. Cas non configuré à préciser techniquement sans défaut inventé.
- Refuser côté serveur toute édition/suppression du projet membre par admin hors traitement légal distinct, toute action non autorisée/session expirée ; absence d’écriture partielle en cas d’erreur/concurrence. D05 et D14 restent acquis.

Critères à implémenter et tester ultérieurement ; aucun test applicatif effectué par cette consolidation.

### 13.3 Recette des annexes R01/R02

R01 : utiliser les entrées/hypothèses/formules et attentes FR-T01–FR-T12 du §17.5, en conservant les réserves fiscales et d’assiette. R02 : cas synthétiques RG-T01–RG-T09 du §18.6, en contrôlant effacement réel, exceptions et sauvegardes. Résultats numériques arithmétiques contrôlables ne signifient ni test de l’application ni validation par expert. Technique §16.3 pour les contrôles cibles, aucune fixture ni donnée personnelle créée.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:771 -->

## 14. Décisions validées et traçabilité

| Repère documentaire | Décision | Source |
| --- | --- | --- |
| BIZ-F-001 | Cible franchisés et futurs franchisés, élargie au périmètre commercial et grand public en V0.2 | Cadrages V0.1 et V0.2 |
| BIZ-F-002 | Indépendance des autres produits MOVEE | V0.1, confirmée V0.2 |
| BIZ-F-003 | Pas de contraintes MOVEE App imposées par défaut | V0.1, confirmée V0.2 |
| BIZ-F-004 | Intégrations futures spécifiées et validées explicitement | V0.1, conservée |
| BIZ-F-005 | Quatre interfaces et cadrage des domaines | V0.2 |
| BIZ-F-006 | FR/EN/ES, interfaces et contenus commerciaux | V0.2 |
| BIZ-F-007 | Candidatures, CRM, centres côté réseau et CMS MariaDB | V0.2 |
| BIZ-F-008 | Moteur financier commun, deux perspectives sur 36 mois, graphiques et exports Excel/PDF | V0.2 |
| BIZ-F-009 | Authentification et séparation des autorisations | V0.2 |

Ces repères sont documentaires, sans prétendre reproduire des identifiants historiques ChatGPT. Les arbitrages D01–D57 ci-dessous précisent ou remplacent les règles historiques ; Q01–Q08 sont désormais validées au §14.2.

Les S01–S10 et F01–F11 constituent les identifiants stables de consolidation des décisions et réserves nouvelles. Chaque bloc conserve sa source ; le traitement actualisé des écarts O01–O08 et les questions restantes figurent au §15.

### 14.1 Décisions utilisateur validées — arbitrages du 18 octobre 2026

Registre exhaustif : **57 décisions**, toutes spécifiées, non implémentées. Les renvois concernent le corps harmonisé ; voir §16.1 pour la couverture technique individuelle. La formulation de D20 corrige seulement le renvoi matériel D27 → D25 pour le retrait de l’apport, sans changer les identifiants.

#### D01 — Deux sites, une application.

`movee.info` = site grand public / concept / clients potentiels ; `movee.biz` = site franchise, simulateur public, candidatures, simulateur professionnel et administration. Deux pages publiques distinctes, sur deux domaines distincts, avec liens réciproques en pied de page : « Devenir franchisé » depuis Info vers Biz ; « Voir le site public » depuis Biz vers Info. Le domaine public antérieur indisponible est remplacé par `movee.info` dans tous les référentiels. Une seule application Flask, un seul codebase, une seule base MariaDB, CMS/auth/backend partagés et routage par hôte. L'application reste indépendante de MOVEE App, MOVEE Mobile, MOVEE Motion et Newapp ; aucun metadata-driven, MCP, API REST ou Repository imposé. Architecture Flask/Blueprints → Services → accès SQL paramétré centralisé `db.py` → MariaDB ; moteur financier Python pur. Ne pas prétendre qu'une implémentation existe. Le dépôt `movee-biz` et la base existante `movee_biz` peuvent être réutilisés, mais ne pas présenter leur réutilisation/naming comme une décision supplémentaire non validée.

**Application :** fonctionnel §§2.1, 3 ; technique §2.

#### D02 — Ville : impact économique uniquement.

Pays/ville peuvent préremplir loyers au m², charges et contexte local, mais ne modifient **jamais automatiquement** fréquentation, occupation, nombre de clients ou chiffre d'affaires. Ces derniers dépendent des scénarios financiers. Les hypothèses locales sont modifiables dans le simulateur professionnel et conservées dans le snapshot. Valeurs nationales par défaut si pas de référence locale.

**Application :** fonctionnel §7.1 ; technique §11.1.

#### D03 — Référentiel de villes interne.

Données économiques locales saisies et maintenues manuellement par l'administrateur ; aucune API INSEE, géocodage ou fournisseur externe obligatoire. Identifier origine/date si disponibles, sinon marquer « estimation interne » ou « valeur nationale par défaut ».

**Application :** fonctionnel §7.1 ; technique §9.1.

#### D04 — Granularité communale.

Une série de références par ville/commune, pas par quartier, zone ou code postal ; identifier les villes par pays et commune afin d'éviter les homonymies à l'international.

**Application :** fonctionnel §7.1 ; technique §9.1.

#### D05 — Projets : admin lecture seule.

L'administrateur peut consulter les projets originaux des membres en lecture seule ; il peut cloner un projet dans son espace d'analyse et modifier uniquement cette copie. Il ne peut jamais éditer l'original du membre. Les membres gèrent leurs propres projets et versions.

**Application :** fonctionnel §5.1 ; technique §10.1.

#### D06 — Multilingue intégral FR/EN/ES dès V1.

Traduire les deux sites publics, le compte, les candidatures, la messagerie, les simulations professionnelles, l'administration/CRM, le simulateur franchiseur, les emails, les erreurs, les exports PDF/Excel. CMS MariaDB pour contenu éditorial public ; catalogues i18n pour libellés système. Langue de l'interface distincte du pays du projet ; résultats numériques invariants selon langue.

**Application :** fonctionnel §10.1 ; technique §13.

#### D07 — Moteur international extensible.

Moteur financier commun avec paramètres/règles spécifiques par pays : devise, TVA/taxes, fiscalité, charges sociales, financement et conditions commerciales. Ne pas inventer de règles fiscales étrangères.

**Application :** fonctionnel §8.1 ; technique §11.1.

#### D08 — France seule active en V1.

Architecture préparée pour l'ajout de pays, activation contrôlée ; l'admin peut préparer des configurations futures sans activer de pays ni inventer des règles fiscales.

**Application :** fonctionnel §8.1 ; technique §11.1.

#### D09 — Conditions commerciales par pays.

Prix des machines, droit d'entrée, redevances, abonnements, packs et autres paramètres commerciaux configurables par pays, versionnés et figés dans chaque simulation. Conserver les valeurs françaises initiales documentées (machine 4 000 € HT, droit d'entrée 15 000 € HT, redevance 5 % du CA HT, Active 69 € TTC, Premium 119 € TTC, packs 2/10/20 à 19/89/169 €) comme références initiales, pas comme règles universelles.

**Application :** fonctionnel §8.1 ; technique §11.1.

#### D10 — Consolidation du franchiseur en euros.

Simulations locales dans la devise du pays ; consolidation réseau/franchiseur en EUR. France : aucune conversion.

**Application :** fonctionnel §8.1 ; technique §11.1.

#### D11 — Taux de change manuels.

L'administrateur renseigne les taux par devise avec date de référence et historique ; aucune API de change obligatoire. Taux exact utilisé conservé dans le snapshot de simulation et de consolidation pour reproductibilité.

**Application :** fonctionnel §8.1 ; technique §9.2.

#### D12 — Historique financier figé.

Aucune actualisation rétroactive automatique après changement des paramètres centraux, locaux, fiscaux, commerciaux ou des taux. Le membre peut demander une actualisation, créant une **nouvelle version**, sans écraser les précédentes. Comparaison des versions ; exports indiquant version du projet et des hypothèses.

**Application :** fonctionnel §7.2 ; technique §9.2.

#### D13 — Comparaisons étendues.

Comparer des versions d'un même projet **et** des projets distincts (ex. villes et nombres de machines différents), avec tableaux/graphiques côte à côte, hypothèses et résultats sur 36 mois, scénarios prudent/réaliste/optimiste. Ne jamais modifier les versions comparées.

**Application :** fonctionnel §7.2 ; technique §8.2.

#### D14 — Accès professionnel après approbation manuelle.

Inscription → vérification email → examen/approbation par administrateur → simulateur professionnel, projets, exports. Aucun accès professionnel avant approbation.

**Application :** fonctionnel §6 / S02.3 ; technique §10.1.

#### D15 — Simulateur simplifié public.

Disponible sur `movee.biz` sans inscription ; utilise le même moteur financier que le professionnel, mais une interface et des résultats limités.

**Application :** fonctionnel §6 / S02.2 ; technique §11.2.

#### D16 — Résultats publics minimaux.

Afficher seulement l'investissement initial estimé et le chiffre d'affaires potentiel (détaillé ci-dessous) ; ne pas afficher charges, EBITDA/rentabilité, trésorerie, financement, seuil de rentabilité ou prévisions 36 mois.

**Application :** fonctionnel §6 / S02.2 ; technique §11.2.

#### D17 — Scénario réaliste uniquement

pour le simulateur public ; ne pas montrer les scénarios prudent/optimiste.

**Application :** fonctionnel §6 / S02.2 ; technique §11.2.

#### D18 — CA à maturité sur deux périodes.

Afficher CA mensuel à maturité et CA annuel à maturité (12 mois au rythme de croisière, **pas** CA de la première année).

**Application :** fonctionnel §6 / S02.2 ; technique §11.2.

#### D19 — Aucune persistance anonyme.

Simulations publiques non sauvegardées, non rattachées à l'inscription, non récupérables après approbation. Le candidat approuvé recrée son projet professionnel.

**Application :** fonctionnel §6 / S02.2 ; technique §9.2.

#### D20 — Paramètres publics initiaux enrichis.

Ville, configuration de machines, loyer estimé, apport personnel avaient été initialement retenus ; **D25 retire ensuite l'apport personnel**. La liste finale est donc : configuration de machines, ville facultative, loyer estimé modifiable.

**Application :** fonctionnel §6 / S02.2 ; technique §8.1.

#### D21 — Centre principal uniquement

dans le simulateur public ; satellites réservés au simulateur professionnel.

**Application :** fonctionnel §6 / S02.2 ; technique §11.2.

#### D22 — Formats de machines prédéfinis

côté public ; pas de nombre libre saisi par le visiteur. Le simulateur professionnel reste personnalisable.

**Application :** fonctionnel §6 / S02.2 ; technique §8.1.

#### D23 — Formats entièrement administrables.

L'administrateur peut ajouter, modifier, activer, désactiver, ordonner les configurations et choisir celle par défaut ; **ne figer aucune liste** (6/8/10 ou 4/6/8/10/12 ne sont que des exemples non validés). Les calculs dérivent de la configuration active.

**Application :** fonctionnel §6 / S02.2 ; technique §9.1.

#### D24 — Ville facultative.

Sans ville, références économiques nationales ; avec ville, préremplissage local disponible, sans modifier le CA/occupation ; absence de données locales → repli national. Loyer toujours modifiable.

**Application :** fonctionnel §§6 / S02.2, 7.1 ; technique §8.1.

#### D25 — Apport personnel retiré du public.

Paramètre réservé au simulateur professionnel. Aucune donnée d'apport personnel demandée au visiteur public ; cette décision prévaut sur D20.

**Application :** fonctionnel §6 / S02.2 ; technique §8.1.

#### D26 — Investissement public HT et TTC.

Afficher distinctement les deux ; appliquer les taxes appropriées aux postes, sans taux uniforme supposé. Le TTC est un décaissement indicatif, sans préjuger du remboursement ultérieur de TVA.

**Application :** fonctionnel §6 / S02.2 ; technique §11.2.

#### D27 — CA public HT uniquement.

CA mensuel et annuel potentiel à maturité affichés en HT ; pas de CA TTC.

**Application :** fonctionnel §6 / S02.2 ; technique §11.2.

#### D28 — Recalcul automatique en direct.

Recalcul dès changement de configuration, ville ou loyer, sans bouton « Calculer » et sans rechargement de page ; éviter les appels inutiles. Pas de sauvegarde publique.

**Application :** fonctionnel §6 / S02.2 ; technique §8.1.

#### D29 — Interface responsive sur une page.

Desktop : paramètres et résultats en deux colonnes ; mobile : paramètres au-dessus, résultats au-dessous. Pas de parcours multi-étapes.

**Application :** fonctionnel §6 / S02.2 ; technique §8.1.

#### D30 — CTA « Obtenir mon business plan complet ».

Après résultats publics, lien vers inscription/connexion puis approbation administrative ; ne pas promettre de téléchargement immédiat ni transférer la simulation publique.

**Application :** fonctionnel §6 / S02.2 ; technique §8.1.

#### D31 — Inscription courte.

Cinq champs obligatoires seulement : nom, prénom, email, téléphone, mot de passe. Les autres informations peuvent être demandées ultérieurement.

**Application :** fonctionnel §6 / S02.3 ; technique §10.1.

#### D32 — Email vérifié obligatoire.

Lien sécurisé temporaire envoyé à l'inscription, renvoi possible ; candidature examinable et approbation possibles uniquement après vérification de l'adresse.

**Application :** fonctionnel §6 / S02.3 ; technique §10.1.

#### D33 — Refus révisable.

Compte conservé sans accès professionnel ; admin peut rouvrir/réexaminer puis approuver sans recréer de compte ; conserver historique des décisions.

**Application :** fonctionnel §6 / S02.3 ; technique §10.1.

#### D34 — Motif de refus obligatoire et interne.

Date, auteur, motif conservés ; motif non automatiquement communiqué au candidat ; notification du refus par email.

**Application :** fonctionnel §6 / S02.3 ; technique §7.1.

#### D35 — Demandes d'informations intégrées.

Admin demande des compléments dans le dossier ; candidat peut répondre dans son espace même avant approbation ; email de notification et historique questions/réponses.

**Application :** fonctionnel §7.3 ; technique §7.1.

#### D36 — Aucune pièce jointe en V1.

Échanges textuels uniquement ; documents éventuels transmis hors application par email ; pas d'upload dans le module candidature ou messagerie.

**Application :** fonctionnel §7.3 ; technique §7.1.

#### D37 — Messagerie bidirectionnelle permanente.

Candidat et administrateur peuvent initier des échanges textuels avant et après approbation ; conversation et historique continu pendant la préparation du projet.

**Application :** fonctionnel §7.3 ; technique §7.1.

#### D38 — Un seul fil par candidat.

Pas de fils par sujet, par projet ou par administrateur ; tous les messages dans un fil chronologique.

**Application :** fonctionnel §7.3 ; technique §9.1.

#### D39 — Messagerie administrative partagée.

Tous les administrateurs autorisés consultent et répondent ; auteur précis de chaque réponse identifié ; permissions respectées.

**Application :** fonctionnel §7.3 ; technique §7.1.

#### D40 — Messages immuables.

Aucune édition ni suppression individuelle des messages envoyés par candidat/admin ; correction par nouveau message. **Exception nécessaire : effacement légal des données personnelles lors des purges RGPD** ; l'immutabilité fonctionnelle ne bloque pas les obligations d'effacement.

**Application :** fonctionnel §7.3 ; technique §15.1.

#### D41 — Notifications email regroupées.

Premier nouveau message non lu → notification ; messages suivants sans emails répétés jusqu'à consultation, puis cycle réinitialisé. Gérer la messagerie admin partagée sans doublons. Tous les messages restent visibles dans l'application.

**Application :** fonctionnel §7.3 ; technique §7.1.

#### D42 — Pas de compteur ni notification in-app.

Uniquement notification par email ; pas de badge non lu ni alerte visuelle dans l'interface. La messagerie reste consultable manuellement.

**Application :** fonctionnel §7.3 ; technique §8.2.

#### D43 — Réponse exclusivement dans MOVEE Biz.

Email de notification avec lien sécurisé vers conversation après authentification ; réponses directes à l'email non ingérées dans l'application.

**Application :** fonctionnel §7.3 ; technique §7.1.

#### D44 — Conservation des candidatures non abouties.

Référence de 2 ans après dernier contact significatif ; dossier, coordonnées, messages, données personnelles. Suppression/anonymisation à échéance sauf fondement légal documenté ; politique différente pour franchisés actifs. Vérifier la base juridique et le délai applicable avant implémentation, ne pas présenter 2 ans comme règle RGPD universelle.

**Application :** fonctionnel §11.1 ; technique §15.1.

#### D45 — Purge à validation administrative.

Détection et signalement automatiques des dossiers arrivés à échéance ; contrôle des exceptions, puis validation manuelle ; ne pas permettre une rétention indéfinie sans justification.

**Application :** fonctionnel §11.1 ; technique §15.1.

#### D46 — Suppression plutôt qu'anonymisation à l'échéance.

Après validation, effacer coordonnées, données de candidature et messages, sauf obligations légales documentées ; trace minimale non identifiante de l'opération.

**Application :** fonctionnel §11.1 ; technique §15.1.

#### D47 — Suppression volontaire depuis l'espace personnel.

Fonction « Supprimer mon compte », confirmation explicite, demande datée/statutée, contrôle légal, traitement et notification ; possible indépendamment de l'échéance des 2 ans.

**Application :** fonctionnel §11.1 ; technique §15.1.

#### D48 — Désactivation immédiate après demande.

Fermer les sessions et suspendre immédiatement simulateur, projets, messagerie pendant traitement administratif.

**Application :** fonctionnel §11.1 ; technique §15.1.

#### D49 — Annulation avant effacement définitif.

Candidat contacte MOVEE ; vérification d'identité ; admin peut annuler et réactiver avant exécution ; après effacement, aucune restauration.

**Application :** fonctionnel §11.1 ; technique §15.1.

#### D50 — Délais réglementaires, sans SLA interne 7 jours.

En principe réponse sous un mois ; extension jusqu'à deux mois supplémentaires dans les cas légalement prévus, avec information dans le premier mois. Suivi des échéances ; ne pas imposer d'attente d'un mois si traitement possible plus tôt.

**Application :** fonctionnel §11.1 ; technique §15.1.

#### D51 — 2FA obligatoire pour administrateurs.

Aucun accès admin sans vérification requise ; pas de 2FA obligatoire pour candidats/franchisés.

**Application :** fonctionnel §11.2 ; technique §10.2.

#### D52 — Second facteur par email.

Après mot de passe, code à usage unique envoyé à l'adresse email vérifiée de l'administrateur ; pas de TOTP imposé. Documenter le risque de dépendance à la sécurité de la boîte email.

**Application :** fonctionnel §11.2 ; technique §10.2.

#### D53 — Code valide 5 minutes.

Usage unique ; expiration ; nouveau code invalide l'ancien ; limiter tentatives et renvois.

**Application :** fonctionnel §11.2 ; technique §10.2.

#### D54 — Appareils de confiance 30 jours.

Après 2FA, admin peut choisir de faire confiance au navigateur pendant 30 jours ; connexions suivantes avec mot de passe mais sans nouveau code tant que confiance valide, sauf événement de sécurité. Jeton sécurisé spécifique au navigateur, non basé seulement sur IP. Déconnexion ≠ révocation automatique de confiance.

**Application :** fonctionnel §11.2 ; technique §10.2.

#### D55 — Gestion des appareils.

Liste des appareils autorisés (type/navigateur, dates d'autorisation, dernière utilisation, expiration), révocation individuelle ou globale ; révocation appliquée côté serveur ; 2FA requis à prochaine connexion après révocation.

**Application :** fonctionnel §11.2 ; technique §10.2.

#### D56 — Session admin : 30 minutes d'inactivité.

Expiration côté serveur, basée sur activité réelle de l'utilisateur, non sur polling automatique. La confiance appareil ne prolonge pas la session.

**Application :** fonctionnel §11.2 ; technique §10.2.

#### D57 — Session candidat/franchisé : 2 heures d'inactivité.

Même exigence d'expiration côté serveur, déconnexion et réauthentification.

**Application :** fonctionnel §11.2 ; technique §10.2.

### 14.2 Décisions utilisateur validées — Q01–Q08 (18 octobre 2026)

Ces huit décisions remplacent le seul point Q01 anciennement ouvert et précisent D12/D13. D01–D57 restent intégralement conservées au §14.1. Travail mutable et historiques immuables sont distincts ; supprimer selon Q05/Q06 n’est pas modifier un historique.

#### Q01 — Sauvegarde automatique

modifications de la simulation professionnelle enregistrées automatiquement après un bref délai (debounce) dans la version de travail courante. Aucun bouton Enregistrer requis. États d'interface « Enregistrement… », « Enregistré », « Erreur de sauvegarde ». Avertissement si sortie avec changements non persistés. Expiration de session ne doit pas supprimer les données déjà enregistrées. Ne jamais écraser les versions historiques.

**Application :** fonctionnel §7.4 ; technique §§8.3, 9.3.

#### Q02 — Versionnement explicite

l'utilisateur crée volontairement une version historique figée via « Créer une version ». La sauvegarde automatique ne crée pas de version historique à chaque modification. Une actualisation volontaire des hypothèses centrales crée également une nouvelle version traçable. Versions historiques immuables, comparables entre elles et entre projets.

**Application :** fonctionnel §§7.2, 7.4 ; technique §9.3.

#### Q03 — Nommage

numéro séquentiel automatique par projet, date de création, libellé personnalisé facultatif (ex. « Hypothèses bancaires »). L'identification reste stable même si des versions intermédiaires sont supprimées : ne pas réutiliser un numéro attribué.

**Application :** fonctionnel §7.4 ; technique §9.3.

#### Q04 — Restaurer par copie

sélection d'une version historique, copie de ses paramètres vers la version de travail courante ; l'original et les autres versions restent intacts. Conserver l'origine de la restauration. Confirmer avant d'écraser un travail courant ; les changements ultérieurs suivent Q01.

**Application :** fonctionnel §7.4 ; technique §§8.3, 9.3.

#### Q05 — Suppression d'une version historique

le propriétaire peut supprimer une version après confirmation explicite, sans toucher à la version de travail ni aux autres versions. Actualiser les comparaisons qui la référencent ; les PDF/Excel déjà exportés ne sont pas modifiés rétroactivement. Respecter les obligations légales de conservation/effacement ; ne pas promettre une conservation d'exports côté serveur non spécifiée.

**Application :** fonctionnel §§7.4, 11.3 ; technique §§9.3, 15.2.

#### Q06 — Suppression d'un projet complet

le propriétaire peut supprimer un projet, sa version de travail et ses versions historiques après confirmation explicite, sous réserve d'obligations légales de conservation. Les copies indépendantes créées par l'administration sont gérées séparément dans le respect du RGPD ; ne pas les modifier silencieusement. Audit minimal de l'opération, sans conservation indue de données personnelles.

**Application :** fonctionnel §§7.4, 11.3 ; technique §§9.3, 15.2.

#### Q07 — Duplication d'un projet

création d'un nouveau projet indépendant avec nouvel identifiant et copie des paramètres/configurations/hypothèses de la version de travail courante, **sans** copier l'historique. Le projet source reste intact. Le nouveau projet a son propre historique et peut évoluer librement.

**Application :** fonctionnel §7.4 ; technique §9.3.

#### Q08 — Quota configurable de projets actifs

un administrateur peut configurer et modifier le nombre maximal de projets actifs par candidat approuvé/franchisé. La création et la duplication sont bloquées lorsque le quota est atteint ; consultation et modification des projets existants restent possibles. Les projets supprimés ne comptent plus dans le quota. Ne pas inventer de valeur par défaut ni de notion d'archivage non décidée ; expliciter le cas « valeur non configurée » comme point technique à préciser, sans inventer de politique commerciale.

**Application :** fonctionnel §§7.4, 9.2 ; technique §§9.3, 10.3.

### 14.3 R01/R02 — arbitrages documentaires validés du 18 octobre 2026

| Décision | Mandat validé | Application et statut |
| --- | --- | --- |
| R01 | Établir une fiche financière France détaillée : fiscalité, TVA, royalties, clearing, formules, cas chiffrés et points à confirmer par un expert-comptable | Fonctionnel §17 ; technique §11.3 ; annexe intégrée, réserves expert/contractuelles maintenues |
| R02 | Établir une politique RGPD détaillée par catégories de données : finalités, bases légales, durées, points de départ, effacement, exceptions, copies administrateur et points à valider juridiquement | Fonctionnel §18 ; technique §15.3 ; annexe intégrée, validation juridique/DPO requise |

Les 65 décisions D/Q restent conservées dans leurs registres ; ces deux mandats ajoutent des annexes, pas des taux, durées ou contrats supposés validés.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:1196 -->

## 15. Contradictions et arbitrages restants

### 15.1 Contradictions résolues par les décisions validées

| Repère | Traitement au 18 octobre |
| --- | --- |
| O01 | Résolu D05 : admin lecture seule sur original membre, clone modifiable uniquement. S02.3 et synthèses corrigés. |
| O02 | Résolu D01 : MOVEE Info est le site public movee.info et Biz le site franchise, même application/base ; routage par hôte et liens réciproques. |
| O03 | Résolu D06 : tout FR/EN/ES dès V1, y compris privé/admin/emails/exports. La mention française seule S07 est harmonisée. |
| Public | D15–D30 remplacent entrées libres/coach/satellite, estimation marge et transfert anonyme par format admin/principal/ville/loyer, investissement HT+TTC et CA HT à maturité, aucun stockage. |
| Candidature | D14 et D31–D34 remplacent ville/coach obligatoires par cinq champs, vérification email puis approbation, refus révisable et motif interne. |
| Ville | D02–D04 fixent référentiel manuel par pays/commune, préremplissage des coûts et repli national ; aucun impact automatique sur occupation/CA. |
| Conservation | D44–D50 remplacent l’alternative générique suppression/anonymisation : suppression validée, exceptions légales, suspension et délais réglementaires. |
| Authentification | D51–D57 fixent 2FA email admin, confiance révocable et inactivité serveur distincte des deux profils. |
| Renvoi D20 | Correction matérielle : apport retiré par D25, D27 concerne le CA HT ; aucune décision supprimée ni renumérotée. |

### 15.2 Précisions restantes après Q01–Q08

**Q01–Q08 : DÉJÀ TRANCHÉ.** Aucune question ouverte sur autosauvegarde, historiques explicites, nommage, restauration par copie, suppressions, duplication sans historique ou quota configurable ; voir §7.4 et registre §14.2. La valeur numérique du quota n’est pas fixée et son état non configuré reste une précision technique, sans plafond commercial inventé.

O04 reste une convention technique documentable : interpolation vers M24 modifiable. O05 : allocation ventes/crédits et écarts de mix doivent être explicités/testés selon F01/F03, pas transformés en égalités garanties. O06 : corrections financières historiques inchangées. O07 : exemple env non aligné avec le local, correction technique future. O08 : hypothèse de logiciel déjà développé, code absent, à signaler dans le budget sans inventer de coût. Les réserves S09/F10 restent conservées.

### 15.3 Audit de préparation V1 — seuls blocages essentiels

Audit **documentaire**, pas un audit juridique/fiscal externe ni une recette de production. Deux thèmes restent bloquants pour la validation financière/conforme de la V1 concernée ; ils n’interdisent pas de construire les composants déjà spécifiés après autorisation. Le caractère prévisionnel autorise des hypothèses visibles, pas la présentation d’une règle fiscale ou contractuelle inconnue comme acquise. Les propositions ci-dessous ne sont pas adoptées par cet audit.

| Priorité / thème | Classe | Sources exactes | Manque réellement bloquant et portée | Proposition à valider, non décidée |
| --- | --- | --- | --- | --- |
| P1 — B01 : cadre fiscal/comptable français et clearing intercentres | BLOQUANT pour recette financière complète | F01/F03, F05–F07 ; D26, D07–D09 ; §§8, 12 / S09, F10 | Les références de TVA/IS existent mais ne fixent pas toutes les taxes par poste, dates d’encaissement/décaissement/récupération et règles d’éligibilité ; TVA/qualification et base de royalties du clearing restent explicitement à confirmer. Le TTC public par poste, la trésorerie et la redevance consolidée ne peuvent être validés comme financièrement exacts sur ces flux à partir des seules sources. Il ne s’agit pas de reposer les taux français déjà documentés ni d’inventer de fiscalité étrangère. | Faire valider une fiche France : régimes/éligibilité et taxation par poste, traitement/calendrier des prépayés et droits d’entrée, clearing et base de royalties sans double perception. Codex peut préparer les conventions et cas chiffrés ; validation comptable/fiscale nécessaire avant recette des chiffres concernés, sans nouveau taux inventé ici. |
| P1 — B02 : politique légale de conservation/effacement | BLOQUANT avant mise en service avec données personnelles | D44–D50, D40 ; §§11.1, 11.3 ; Q05–Q06 | Les actions/délais de traitement sont décidés, mais base légale du délai de référence, définition opérationnelle du dernier contact significatif, politique des franchisés actifs et exceptions obligatoires (dont copies admin/audit) restent non validées. Une purge ou une rétention ne peut être déclarée conforme en laissant ces fondements indéfinis. | Valider une politique par catégorie de données et état du dossier, exceptions justifiées et circuit de revue ; conserver le principe de suppression confirmé et les délais D50, sans inventer de durée supplémentaire ni transformer les deux ans en règle universelle. |

Aucun autre arbitrage utilisateur bloquant identifié dans les sources accessibles ; ces deux thèmes regroupent les validations métier/juridiques indispensables, pas une liste de nouvelles fonctionnalités. La publication de chiffres définitifs et l’ouverture à de vraies données exigent la résolution des gates concernés ; aucun développement n’est lancé ici.

### 15.4 Revue croisée : décisions acquises et éléments non bloquants

| Domaine examiné | Classe | Référence et raison |
| --- | --- | --- |
| CA/crédits/occupation et absence de double compte | NON BLOQUANT pour commencer le moteur sous conventions explicites | F01–F03, F09/F10 et S09 autorisent Codex à choisir/documenter/tester cohortes ou allocation, priorité crédits, arrondis, packs et reconnaissance prépayée. Aucun chiffre unique ne découle des deux mixes ; produire une stratégie cohérente, avertissements et sensibilités avant recette, sans demander une nouvelle décision sur chaque algorithme. Sa conformité comptable relève de B01. |
| Capacité, scénarios, hypothèses locales, rémunérations et satellites | NON BLOQUANT sous hypothèses visibles | F02/F04/F05/F07/F10 : valeurs modifiables, conventions autorisées, RH/statut non certifiés. Ne pas inventer une conformité ni un paramètre caché. Le rythme M13–M24 possède déjà sa convention ; surface, marges et chiffres historiques restent inchangés. |
| Simulation pro, propriété et cycle de projets | DÉJÀ TRANCHÉ | D05/D12/D13, §§5.1, 7.2, 7.4 et Q01–Q08 : admin lecture seule, travail autosauvegardé, historiques explicites, copie/restauration/suppressions et quota. |
| Approbation et compte | DÉJÀ TRANCHÉ | D14/D31–D34, S02.3 : cinq champs, email vérifié avant examen/approbation, refus motivé interne/révisable ; messagerie avant approbation, pro interdit. |
| Paramètres financiers et publication/versionnement | DÉJÀ TRANCHÉ pour les droits et le figement | S02.4, S03, D09/D11/D12, Q01/Q02 : admin seul pour paramètres centraux versionnés, France seule active, snapshots et actualisation volontaire sans modification rétroactive. Aucun workflow d’approbation supplémentaire requis. |
| CMS, contenu minimal PDF/Excel et langues | DÉJÀ TRANCHÉ pour le périmètre ; NON BLOQUANT pour les moyens | S07/S10/F11, D06/D12 et technique §14 : contenu minimal et mêmes chiffres versionnés/localisés déjà fixés, publication/aperçu CMS déjà requis ; bibliothèque, mise en page et textes de traduction sont des travaux d’implémentation/contenu, pas de nouveaux arbitrages métier. |
| Quota non configuré, débit d’autosauvegarde et concurrence | NON BLOQUANT pour le cadrage | Q01/Q08, technique §9.3 : délai exact, contrôles/reprise et signalement technique de configuration à préciser ; aucune valeur de quota ni notion d’archivage choisie. Configuration du quota nécessaire pour recetter création/duplication ; pas d’autodéfaut commercial. |
| Exploitation et authentification | DÉJÀ TRANCHÉ pour les règles ; NON BLOQUANT comme choix techniques restants | D01/D51–D57, S01/S03, technique §§6, 10.2, 17 : sessions, second facteur et hôtes acquis ; SMTP, tokens, TLS/service/DB et bibliothèques à réaliser/vérifier avant mise en service. Absence d’implémentation ou de connexion testée ne constitue pas un nouvel arbitrage utilisateur. |

Les recettes de sécurité, disponibilité SMTP, connexion DB, sauvegarde/restauration d’exploitation et déploiement devront réussir : elles sont à faire, pas des questions métier rouvertes. Aucune décision nouvelle n’est imposée par ce classement.

### 15.5 État des deux validations externes après préparation des annexes

| Point essentiel | Travail documentaire disponible | Validation restante / conséquence réelle |
| --- | --- | --- |
| B01 — France fiscale/comptable et assiette clearing | Annexe R01 §17, matrice §17.6, cas FR-T01–FR-T12 ; aucune formule historique changée | Expert-comptable : nature/taux par poste, exigibilité/déduction/paiement TVA, reconnaissance et régime/éligibilité ; franchiseur/contrat avec expert : base clearing/royalties et éventuels avoirs. Recette finale des chiffres/TTC/cash concernés non certifiable tant que non confirmé. Les valeurs existantes ne sont pas rouvertes. |
| B02 — conservation/effacement | Annexe R02 §18, G01–G16 et RG-T01–RG-T09 | Juriste/DPO : RT et responsabilités, bases/finalités, durées/événements et exceptions par catégorie, actifs/anciens, copies/sauvegardes ; mise en service des données personnelles concernées conditionnée à cette validation et à exécution effective des protections. |

Ces deux points restent les seuls thèmes externes essentiels identifiés ; la rédaction des fiches ne les marque pas résolus. Les choix ordinaires d’implémentation du §15.4 ne sont pas remontés comme nouveaux arbitrages. Aucun expert n’a encore validé les annexes dans les sources accessibles.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:1379 -->

## 17. Annexe R01 — Fiche financière France et recette conditionnelle

### 17.1 Portée, sources et statuts

Annexe documentaire du 18 octobre 2026, fondée sur S04/S05/S07/S09, F01–F11, D02/D06–D13/D26–D27 et Q01–Q08. Les blocs historiques demeurent intacts. **R01 valide la préparation de cette fiche, pas une qualification fiscale, un contrat ni l’approbation d’un expert-comptable.** Aucun traitement non documenté n’est adopté silencieusement. Tous les cas sont fictifs ; aucune donnée réelle n’est requise.

Statuts de la matrice : `validé` = décision MOVEE ; `hypothèse de simulation` = convention explicitement conditionnelle ; `validation expert-comptable requise` = règle/applicabilité non attestée ; `arbitrage métier requis` = option contractuelle non arrêtée. « Validé » ne signifie ni fiscalité certifiée ni code implémenté. France seule active, montants historiques en EUR. Les taux 20 %, 15 % et 25 % ci-dessous proviennent du modèle historique ; leur applicabilité aux entités et postes n’est pas certifiée.

**Recherche externe consultée le 18 octobre 2026**, distincte des décisions MOVEE : [DGFiP — régimes de TVA, page modifiée le 21 mai 2026](https://www.impots.gouv.fr/professionnel/les-regimes-dimposition-la-tva) : régime et obligations déclaratives doivent être identifiés, pas déduits du seul statut de franchisé. [BOFiP — actualité du 21 décembre 2022 sur les acomptes de biens](https://bofip.impots.gouv.fr/bofip/13758-PGP.html/ACTU-2022-00148) : les acomptes sur biens peuvent déclencher une exigibilité avant livraison ; vérifier le régime et les conditions applicables au cas MOVEE. Ce contrôle documentaire ne constitue ni rescrit ni validation comptable. Aucun seuil ou nouveau taux légal issu de ces recherches n’est activé dans le modèle.

### 17.2 Catalogue des flux, TVA et calendriers à qualifier

Notation : **C** = TVA collectée chez le vendeur lorsqu’exigible ; **D** = TVA déductible chez l’acheteur seulement si ses conditions sont réunies. Une facture, un encaissement et une reconnaissance de CA sont trois événements distincts. Une charge HT ou un coût chargé ne fournit pas son taux de TVA. « À confirmer » signifie absence de qualification suffisante dans les sources, jamais taux zéro implicite.

| Flux / source | Comptabilité et montant documentés | TVA par poste et contrepartie | Trésorerie / calendrier et réserve |
| --- | --- | --- | --- |
| FL01 — droit d’entrée, S04/F04/F07 | 15 000 € HT principal, aucun droit satellite ; franchiseur produit, franchisé traitement charge/immobilisation à confirmer | C franchiseur / D franchisé si taxable/déductible ; nature du droit, taux et éventuelle ventilation formation à confirmer | Paiement et reconnaissance signature/ouverture non arrêtés ; ne pas assimiler encaissement, CA et amortissement |
| FL02 — achat fabricant et vente machine, F04/F07 | Fabricant 3 500 HT, vente 4 000 HT ; marge brute 500 par machine ; pas leasing/stock | TVA distincte facture fournisseur et facture franchisé, C/D de chaque entité ; taux/conditions à confirmer, 20 % uniquement hypothèse du cas T02 | Fabrication 3 mois, 50 % commande / 50 % avant livraison de chaque côté ; exigibilité des acomptes à qualifier, pas tout décaler à livraison |
| FL03 — transport/installation, F04/F07 | 100 HT/machine refacturé au coût, marge zéro | C sur refacturation et D sur achat sous qualification/taux à confirmer ; pas de remboursement supposé net de TVA | Ventilation des paiements non spécifiée ; pas de revenu de marge ajouté au coût refacturé |
| FL04 — travaux, vestiaires, douches, mobilier/IT, F04/F05 | 800 HT/m², 3 000 HT/module, 4 000 HT/douche, 10 000 HT mobilier/IT ; immobilisations/ventilation à confirmer | Chaque poste a sa propre qualification/taux/déductibilité à confirmer ; **aucun TTC = CAPEX total × 1,20 automatique** | Dates facturation/acomptes/règlement paramétrables à documenter ; pas de double compte travaux/équipements ; cas T09 |
| FL05 — abonnements Active/Premium, F01/F03 | 69/119 TTC mensuels, 8/16 crédits ; CA reconnu selon abonnements vendus ; crédits non utilisés sans revenu additionnel | F03 autorise conversion taxable standard avec taux configuré, 20 % hypothèse France initiale ; C et exigibilité effective à confirmer | Encaissement au cycle de facturation selon convention ; expiration à anniversaire, pas conversion de crédits en une seconde vente |
| FL06 — packs 2/10/20, F01/F03 | 19/89/169 TTC ; vente ou consommation avec passif différé : convention à documenter | Qualification prépaiement/produit et événement de TVA à confirmer ; pas de TVA redéclenchée automatiquement par chaque séance | Encaissement distinct de CA reconnu ; pas d’expiration arbitraire du pack ; cas T04 conditionnel |
| FL07 — autonome/collectif/individuel, S04/F02/F03 | Demande 2/3/6 crédits ; ni prix de séance autonome supplémentaire ni vente fictive | Conversion crédits n’est pas un taux TVA ; rattacher aux ventes correspondantes, nature prestation à confirmer | Décompte de capacité/consommation distinct d’un nouveau flux monétaire ; individuel seulement principal d’origine |
| FL08 — onboarding, S04/F03 | Light 19 TTC/30 min, Complete 129 TTC/4 h, upgrade 110 TTC ; découverte gratuite possible | C selon traitement taxable validé ; gratuité/upgrade/ventilation à confirmer, pas taux universel | Conversion commerciale et consommation temps coach explicites ; pas ajouter Complete entier à Light + upgrade |
| FL09 — loyer, F05 | Référence 200 HT/m²/an ; 89 m² → 1 483,333… HT/mois | Option/qualification du bail et TVA déductible à confirmer ; loyer exprimé HT ne prouve pas que TVA facturée | Règlement/charges et éventuelle franchise de loyer non définis ; ne pas inventer un avantage local |
| FL10 — personnel et exploitant, S04/F05/F07 | Coach salarié 4 200 chargé/mois ; exploitant salaire 0 et rémunération optionnelle ; fondateur net selon F07 | Coût salarial chargé séparé des factures de prestations ; aucune TVA extraite automatiquement d’un coût chargé ; statut social et composition à confirmer | Décaissement salaires/cotisations distinct, net ≠ coût entreprise ; 42 h et coût non certifiés RH |
| FL11 — maintenance/charges centrales et locales, F04/F05/F07 | 25/machine/mois ; 1 840 hors loyer/coach à 8 machines ; central 4 750/mois et IT 2/machine active | Qualifier séparément énergie/eau/assurance/banque/taxes/marketing/etc. ; aucun taux appliqué à l’agrégat de charges | Réparation sous garantie distincte de maintenance ; juridique 250/mois = 3 000/an, pas deux budgets ; TVA/dates par poste à confirmer |
| FL12 — financement, F05/F07 | Apport/dette 30/70 de référence ; centre 7 ans 4 %, central 5 ans 4 % ; capital hors résultat | Apport/principal ne sont pas CA ; pas de TVA calculée par défaut sur leur montant ; régime intérêts/frais annexes à confirmer | Entrée dette/equity, intérêts et principal selon échéancier ; BFR et frais selon périmètre documenté |
| FL13 — redevance, F05/F06/F07 | 5 % CA HT franchisé, logiciel/support inclus ; pas fonds marketing additionnel | Assiette HT ≠ TVA de facture de redevance ; taux/exigibilité de celle-ci à confirmer | Périodicité d’appel/paiement et avoirs non fixés ; conditions §17.3 ; cas T05 |
| FL14 — clearing, S04/F06 | Hôte 8 HT/autonome ou 12 HT/collectif **provisoires**, aucun prélèvement central supplémentaire | Prestation interfranchisés, réallocation ou mouvement interne : alternatives §17.3 ; TVA non résolue | Encaissement client chez origine, règlement à exécutant distinct ; ne pas supprimer un virement réel au prétexte d’élimination de présentation |
| FL15 — IS, taxes et TVA, F05/F07 | IS historique conditionnel 15 % jusqu’à 42 500 éligibles puis 25 % ; taxes locales référence 150/mois | TVA collectée/déductible distincte des taxes/coûts/IS ; éligibilité et retraitements fiscaux à confirmer | TVA à payer/crédit, IS dû/acompte/solde et taxes ont calendriers distincts ; remboursement crédit TVA jamais instantané supposé |

### 17.3 Assiettes, clearing et périmètres de consolidation

**Redevance acquise :** `royalties_ht = 0.05 * assiette_ca_ht_franchise`. CA TTC, apport, principal de prêt et TVA ne sont pas l’assiette CA HT. Source F06 : logiciel/support inclus, pas de supplément central sur interfranchise. Aucun barème d’avoir, réduction, exonération de lancement ou intégration des ventes de machines dans l’assiette franchisé n’est décidé. Les hypothèses de test d’avoir sont conditionnelles, sans nouvelle règle commerciale.

**Clearing :** distinguer le payeur client, le centre d’origine titulaire de la relation, l’hôte exécutant (satellite du même franchisé ou tiers juridiquement distinct), l’émetteur d’une éventuelle facture et le destinataire du paiement. Individuel/onboarding exclus du séjour interfranchise selon F06. Les alternatives suivantes restent non arbitrées :

| Option non validée | Conséquence à faire qualifier | Contrôle |
| --- | --- | --- |
| A — prestation exécutée par un franchisé tiers facturée à l’origine | Origine garde vente client, hôte constate prestation interentreprises ; TVA, traitement et assiette royalties à confirmer | Ne pas taxer automatiquement deux assiettes qui répliquent la même vente ; T06-A |
| B — réattribution d’une part de revenu entre entités | Ventilation commerciale/comptable/fiscale et supports d’ajustement à confirmer, pas de netting arbitraire | Somme des assiettes approuvées non dupliquée ; T06-B |
| C — deux centres d’une même personne morale | Ventilation analytique interne plutôt qu’une vente entre personnes distinctes ; vérifier statut réel, pas simple rattachement UI | Transfert interne jamais nouveau CA externe ni royalty doublée |

**Trois vues différentes :** (1) comptes de chaque entité légale, (2) présentation économique de tous les centres, après élimination explicite des flux croisés selon périmètre, (3) compte du franchiseur (droits, ventes machines, royalties, charges). Un réseau de franchisés indépendants n’est pas automatiquement un groupe légalement consolidé. La vue économique réseau ne remplace ni livres fiscaux ni déclarations. Ne pas additionner marge machine et vente intégrale comme deux revenus ; ne pas afficher 100 € de vente client comme CA du franchiseur. Périmètre et éliminations sont visibles et snapshotés.

### 17.4 Formules de rapprochement et financement

Ces identités sont des contrôles arithmétiques ou conventions de test, pas une réécriture des formules F01–F11 :

- Poste taxable `TVA_i = base_ht_i * taux_i`, `TTC_i = HT_i + TVA_i` ; total TTC = somme des postes qualifiés. Poste non qualifié : résultat conditionnel/avertissement, jamais taux universel ajouté silencieusement.
- Période `solde_tva = TVA_collectee_exigible - TVA_deductible_ouverte + reports_et_regularisations_valides`. Si positif, dette à décaisser au calendrier retenu ; si négatif, crédit à suivre, pas cash remboursé de plein droit. Conditions de déduction/régime/calendrier à confirmer par expert.
- `tresorerie_fin = debut + encaissements_clients + apports + tirages_dette + remboursements_tva_effectifs - paiements_fournisseurs_TTC - salaires_cotisations - principal - interets - tva_versee - is_verse - autres_decaissements`. Ne pas additionner une dette à l’EBITDA ; ne pas déduire les amortissements une seconde fois du cash.
- Sous test linéaire, machine `amortissement_mensuel = 4000/60`, travaux 10 ans et mobilier/IT 5 ans selon F05 ; base/amortissement/date de mise en service à confirmer. Réserve économique `4000/(7*12)` non assimilée à une dotation fiscale ou un deuxième décaissement interne.
- Prêt amortissable de test : `r=taux_annuel/12`, `N=12*annees`, `A=P*r/(1-(1+r)**(-N))`, `interet_m=P_restant*r`, `principal_m=A-interet_m`. Si `r=0`, `A=P/N`. Sans différé/assurance/frais, hypothèses à afficher ; aucun échéancier bancaire contractuel promis.
- `EBIT = EBITDA - dotations_amortissements` dans un cas sans autres ajustements ; `resultat_avant_impot = EBIT - interets + autres_resultats_documentes`. Bénéfice imposable dépend des retraitements/éligibilité, pas automatiquement égal au cash. Formule d’IS du cas T08 strictement conditionnelle, jamais taux réduit garanti ou plafond proratisé mensuellement sans validation.

### 17.5 Cas chiffrés de recette reproductibles

Les résultats ci-dessous sont attendus **si** les hypothèses d’entrée sont expressément retenues. Arrondis au centime pour présentation, précision intermédiaire conservée ; règle exacte d’arrondi fiscal à valider. Aucune fixture ni test applicatif n’est créé ici.

| Cas / flux | Entrées et hypothèses explicites | Formule / résultat attendu | Invariant / réserve |
| --- | --- | --- | --- |
| FR-T01 — HT/TTC abonnement | 1 Active vendu 69 TTC, taxable au taux de simulation 20 %, consommation crédits 80 % | HT = 69/1,20 = **57,50** ; C = **11,50** ; cash si payé = **69** | 6,4 crédits consommés théoriques n’ajoutent aucun CA ; F03 ne fixe pas un arrondi commercial de clients |
| FR-T02 — machine, acompte et marge | 1 machine vendue 4 000 HT, achat 3 500 HT, TVA 20 % des deux côtés sous droit à déduction intégral ; 50/50 commande/livraison 3 mois ; paiements aux mêmes jalons | Vente TTC **4 800**, deux paiements **2 400** ; achat TTC **4 200**, deux paiements **2 100** ; marge brute **500 HT**, différentiel cash cumulé avant TVA **600** | Sur chaque acompte, sous exigibilité proportionnelle retenue, C **400**, D **350** ; 100 TVA nette au total, après règlement net cash **500** ; achat HT pas amorti intégralement une seconde fois |
| FR-T03 — TVA et décalage cash | Seconde échéance T02 : client paie2 400 TTC, fournisseur2 100 TTC ; C400/D350 ouverts sur période M, TVA nette réglée M+1 ; pas autres flux | M : cash net **+300**, dette TVA **50** ; M+1 : cash net **−50**, cumul **+250** sur cette échéance | Même structure au premier acompte → différentiel final **500** après TVA sur les deux échéances. La trésorerie M n’est pas la marge HT ; échéance M+1 est hypothèse de test, pas régime MOVEE validé |
| FR-T04 — prépayé pack | Pack 10 vendu 89 TTC, TVA de simulation 20 % ; **hypothèse conditionnelle CA reconnu à consommation**, 5 crédits sur 10 consommés ; pas de remboursement | Vente HT **74,166666…**, C **14,833333…** si exigible à vente ; cash **89** ; CA reconnu **37,083333…**, passif différé **37,083333…** | CA + passif = HT initial ; crédits restants 5 sans expiration arbitraire. Variante CA reconnu à vente : **74,166666…** une seule fois, consommation ensuite sans revenu supplémentaire. Choix comptable/TVA à confirmer |
| FR-T05 — royalties et avoir | Assiette approuvée 10 000 HT ; aucun clearing ; 5 % ; taxe de facture non encore qualifiée | Royalty HT **500**, jamais 600 sur 12 000 TTC. Si taux de facture hypothétique 20 %, TTC **600**, TVA **100** | Variante **uniquement si** avoir client 1 000 HT admis contractuellement dans l’assiette : (10 000−1 000)*5 % = **450 HT** ; cette réduction n’est pas décidée |
| FR-T06 — clearing origine A / hôte B | Vente client externe A 100 HT déjà reconnue ; 1 autonome chez B, compensation provisoire 8 HT ; hors TVA de compensation tant que non qualifiée ; période identique | A : vente **100**, coût compensation **8** ; B : revenu compensation **8** ; A+B avant élimination revenus **108**, coûts croisés **8** ; présentation réseau après élimination : CA externe **100**, flux croisés **0** | Paiements HT analytiques client→A **100**, A→B **8** ; pas 108 encaissés depuis clients. Option A assiettes royalties A100/B0→**5** ; option B A92/B8→**4,60+0,40=5**. Aucun choix adopté ; A100/B8→**5,40** signale duplication. Si la compensation est taxable hypothétique 20 %, facture B **9,60 TTC**, C B/D A **1,60** sous conditions ; aucun traitement juridiquement acquis |
| FR-T07 — prêt et amortissement | P=10 000, 7 ans, 4 % nominal, mensualités constantes, aucun frais/différé ; machine 4 000 amortie linéaire 60 mois complets | A **136,68806336** ; intérêts M1 **33,33333333**, principal **103,35473003**, dette fin **9 896,64526997** ; dotation machine **66,66666667/mois** | Cash prêt M1 **−136,68806336**, charge intérêt seulement **33,33333333** ; principal jamais charge. Dotation non décaissée ; réserve interne **47,61904762** non déduite deux fois |
| FR-T08 — IS conditionnel annuel | Bénéfice imposable annuel après retraitements =50 000 ; éligibilité au taux réduit et tranche entière historique supposées ; aucune perte reportée | 42 500*15 % + 7 500*25 % = **8 250** ; résultat après IS, si résultat comptable avant IS=50 000, **41 750** | Sans éligibilité sous hypothèse de taux 25 % : **12 500** ; calendrier des acomptes indépendant, pas cash mensuel automatique 8 250/12 |
| FR-T09 — investissement corrigé et TTC par poste | Principal 8 machines aux défauts F04 ; aucun BFR/financement/lancement ; qualification TVA par poste encore absente | Surface **89**, total HT **157 000** =71 200+12 000+16 000+10 000+32 000+800+15 000 ; `TTC = somme(HT_i + TVA_i)` une fois chaque qualification validée | Ne pas annoncer **188 400 TTC** sans hypothèse poste par poste ; pas d’erreur silencieuse taux unique. Surface réelle saisie distincte de recommandation |
| FR-T10 — transport et onboarding | Transport 100 HT refacturé 100 HT, TVA symétrique hypothétique 20 % ; Light 19 TTC puis upgrade110 TTC | Transport facture **120 TTC**, coût **120 TTC**, marge **0** ; Light+upgrade=**129 TTC**, pas 19+129+110 | Au taux hypothétique 20 %, total onboarding HT **107,50**, TVA **21,50**, aucun doublon ; gratuité sans vente fictive |
| FR-T11 — vue franchiseur et non-double-compte | 1 principal ouvert, 8 machines livrées ; reconnaissance droits/vente sur ce mois explicitement supposée ; CA HT franchisé10 000 ; coûts centraux4 750 ; formation300 ; hors taxes/paie/IT variable/amortissement/intérêts | Ventes HT franchiseur :15 000+32 000+800+500=**48 300** ; achats/coûts :28 000+800+300+4 750=**33 850** ; EBITDA partiel de test **14 450** | Marge machines **4 000** déjà incluse, ne pas ajouter à 48 300 ; 500 royalties déjà comptées ; pas confondre CA clients10 000 et CA franchiseur. Délai fabrication3 mois respecté en amont, aucun revenu centre fermé ; exemple exclut explicitement IT variable, donc ne prétend pas total complet |
| FR-T12 — invariants transversaux | Même projet/version/hypothèses en FR/EN/ES ; ville A/B à format/scénario identiques ; changement central ou FX ultérieur ; France active seulement | Mêmes nombres ; changement ville = coûts seuls ; historique/taux figés identiques ; travail peut évoluer, actualisation centrale nouvelle version ; aucun FX France | Pays futur local/devise et consolidation EUR sans fiscalité étrangère activée ; écrans/graphiques/PDF/Excel mêmes résultats autorisés ; export public limité selon D16–D27 |

### 17.6 Matrice de validation R01 et conditions de mise en production

| Règle | Source précise | Statut | Impact développement / recette et test |
| --- | --- | --- | --- |
| Produits, prix français, capacités et surface | S04, F02–F04, D09 | validé (référence initiale) | Conserver valeurs, pas de fiscalité universelle ; T01/T09/T10 |
| Allocation crédits/ventes et mix | F01/F03/F10, S09 | hypothèse de simulation | Convention cohérente documentée et testée, jamais double CA ; T01/T04 et F09 |
| Taxes par poste, exigibilité acomptes, déduction et calendrier | F03/F05, D26 ; recherche §17.1 | validation expert-comptable requise | B01 : qualifier FL01–FL15 avant certifier TTC/cash concernés ; T02/T03/T09 |
| Traitement des packs/droits d’entrée et prépayés | F01/F03/F07/F10 | validation expert-comptable requise | Convention simulation visible en attendant, pas vérité fiscale ; T04/T11 |
| Royalties 5 % CA HT, pas supplément central | F05/F06/F07 | validé | Calcul HT séparé de facture taxable ; T05/T06 |
| Assiette clearing, avoirs/réductions, faits déclencheurs contractuels | F06, S04 ; §17.3 | arbitrage métier requis | Valider seulement les options indispensables avec contrat/expert, aucun nouveau barème ; T05/T06 |
| Qualification clearing et périmètre des vues | F06/F10 ; §17.3 | validation expert-comptable requise | B01 : pas de consolidation légale supposée, éliminations explicites ; T06/T11 |
| Machines et transport marges | F04/F07 | validé | 500 HT et zéro, pas de revenu de marge ajouté à la vente ; T02/T10/T11 |
| Prêts, amortissements et réserve économique | F05/F07 | hypothèse de simulation | Échéancier/math conditionnels aux entrées, bases/dates comptables à confirmer ; T07 |
| IS, fiscalité/social et coût chargé | F05/F07/F10 | validation expert-comptable requise | Vérifier régime/éligibilité/retraitements/statut, pas net=coût ; T08, contrôle FL10 |
| Pays/langue/snapshots/exports | D02/D06–D13, Q01–Q08, F11 | validé | Pas de requalification fiscale par traduction ou ville ; T12 |
| Arrondis et dates de recettes ci-dessus | F09/F10, §17.5 | hypothèse de simulation | Valeurs intermédiaires conservées, conventions explicites sans toucher F01–F11 |

Le blocage financier **B01 n’est pas levé par la seule rédaction** : validation de l’applicabilité fiscale/comptable et de l’assiette contractuelle clearing avant recette finale/publication des chiffres concernés. Aucun besoin de rouvrir prix, taux de royalties, langues ou workflow déjà validés. Les autres paramètres indicatifs restent configurables/documentés selon S09/F10. Mise en production générale également soumise à la recette technique réelle ; aucun code n’est présent ni certifié.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_FUNCTIONAL_REFERENCE.md:1474 -->

## 18. Annexe R02 — Politique RGPD et conservation par catégorie

### 18.1 Portée, responsabilité et validation

Version documentaire du 18 octobre 2026 : **projet de politique, validation juridique/DPO requise**, non une conformité certifiée ni une fonction implémentée. R02 valide sa préparation ; D40/D44–D57 et Q05/Q06 gardent exactement leurs décisions. Aucune nouvelle durée universelle ni collecte de pièces d’identité réelle n’est demandée.

L’entité juridique exploitant Info/Biz et déterminant les traitements doit être identifiée comme responsable (ci-dessous **RT**, identité à confirmer). Un administrateur applicatif n’est pas automatiquement le responsable légal ni le DPO. Le franchiseur est le destinataire commercial désigné ; déterminer les personnes morales et leurs responsabilités, y compris hébergeur/SMTP et éventuels sous-traitants. D05 reste acquis : lecture admin des originaux, analyse sur copie distincte ; une habilitation large à la messagerie ne dispense pas de nécessité d’accès. Aucun accès de franchisé tiers aux demandes publiques, aucun partage avec MOVEE App/Mobile/Motion/Newapp déduit.

**Recherche externe consultée le 18 octobre 2026** : [CNIL — RGPD, chapitre II, articles 5–6](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre2) pour minimisation, finalité et choix du fondement ; [CNIL — chapitre III, articles 12, 17 et 19](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre3) pour traitement des droits et exceptions ; [CNIL — durées de conservation, 2 avril 2026](https://www.cnil.fr/fr/passer-laction/les-durees-de-conservation-des-donnees) pour distinguer activité, archivage justifié et effacement. Ces sources guident une analyse, ne valident ni l’entité MOVEE ni son délai de deux ans. L’exemple RH de la CNIL n’est pas transposé aux candidats franchisés. Aucune durée comptable citée dans cette source n’est appliquée à tous les projets de simulation : ce ne sont pas automatiquement des factures/pièces comptables.

### 18.2 Légende des bases, états et effets des suppressions

Les codes ci-dessous sont **des pistes à vérifier juridiquement pour chaque catégorie**, pas des bases MOVEE déjà approuvées : **B** = nécessité contractuelle/précontractuelle lorsque pertinente pour la personne ; **F** = intérêt légitime à justifier et mettre en balance ; **C** = obligation légale précisément identifiée ; **A** = consentement spécifique lorsque réellement approprié. Pour les représentants de personnes morales, ne pas présumer que tout traitement repose sur B ; faire vérifier le fondement. Pas de consentement global par défaut.

États **N** : candidat non abouti (dont rejeté, compte non vérifié/pending ou approuvé sans franchise conclue selon qualification à valider), **V** : compte approuvé et relation de candidature toujours en cours, **A** : franchisé actif, **X** : ancien franchisé. L’approbation seule ne prouve ni conclusion de contrat ni durée de conservation illimitée ; le refus reste révisable selon D33 dans la durée justifiée.

**C2**, seulement là où D44 couvre la candidature non aboutie : référence de **2 ans après dernier contact significatif**, soumise à validation de fondement/portée/exceptions. La notion de contact significatif reste à confirmer : ne pas la réinitialiser tacitement par polling, autosauvegarde, email automatique ou notification technique. **LA** : durée de relation active strictement nécessaire puis règle de clôture à faire valider. **DX** : durée post-clôture/exception à déterminer par obligation/finalité, aucun chiffre adopté ici. Durée non définie ≠ permission de conserver indéfiniment ; B02 reste une condition de mise en service concernée.

Les colonnes des deux matrices suivantes se complètent **ligne par ligne** : finalité/accès/base puis durée/états/effacement/validation. **VJ** = validation juridique/DPO requise, même lorsqu’une opération MOVEE est déjà validée. Les bases candidates sont les seules pistes de fondement, non des décisions commerciales nouvelles.

### 18.3 Matrice des finalités, responsables, accès et bases à vérifier

Pour chaque ligne, RT est l’entité à identifier au §18.1. Accès techniques prestataires uniquement dans leur mission et après qualification contractuelle ; pas de droit commercial supplémentaire déduit.

| Catégorie | Finalité / responsable opérationnel | Destinataires et accès cibles | Base candidate / justification à vérifier |
| --- | --- | --- | --- |
| G01 — compte/identité | Accès et relation candidat/franchisé ; RT, admins habilités | Titulaire et admins nécessaires, pas autres membres ; secrets jamais exposés | B/F : relation demandée et identité nécessaire |
| G02 — coordonnées/contact | Réponses, notifications et suivi commercial ; RT | Candidat et équipe admin, SMTP pour envoi nécessaire, pas centre tiers automatiquement | B/F : échanges nécessaires ; A si prospection optionnelle distincte effectivement décidée |
| G03 — preuve de vérification email | Contrôle email obligatoire D32 ; RT, sécurité | Service d’authentification/admin habilité, preuve minimale sans conserver jeton brut inutile | B/F : sécuriser l’adresse et le parcours |
| G04 — candidature, statuts, motif de refus | Examen/approbation/réexamen, pipeline ; RT, commerciaux habilités | Admins autorisés ; motif interne non envoyé automatiquement, exposition des droits légaux à vérifier | B/F : instruction demandée et traçabilité proportionnée |
| G05 — fil candidat–administration | Compléments et suivi continu D35–D43 ; RT | Candidat et admins autorisés, auteur identifié ; SMTP notification sans copie systématique intégrale du dossier | B/F : échanges nécessaires |
| G06 — compte franchisé actif/ancien | Gestion de la relation franchise, accès autorisés ; RT | Titulaire/admins nécessaires, conseils si habilitation justifiée | B/F, C si obligation identifiée ; pas de conservation universelle |
| G07 — projets/travail/historiques | Prévisions et comparaison reproductible, Q01–Q08 ; RT | Propriétaire approuvé, admin lecture seule ; données financières identifiantes protégées | B/F : service demandé et analyse nécessaire |
| G08 — PDF/Excel exports | Business plan livré au titulaire ; RT pour copie détenue | Propriétaire et destinataires choisis hors app sous leur responsabilité ; accès admin limité au besoin | B/F : restitution demandée ; C seulement pour vraie pièce soumise à obligation |
| G09 — copies d’analyse admin | Analyse indépendante D05/Q06 ; RT | Admins autorisés dans espace d’analyse, pas autres candidats | F/B à vérifier selon nécessité ; copie ne soustrait pas au droit d’effacement |
| G10 — demandes d’effacement et instruction | Exercice des droits, suivi des délais, contrôle identité proportionné ; RT/référent droits | Personnel habilité au traitement de demande, pas tout utilisateur admin par défaut | C/F : réponse aux droits et preuve proportionnée |
| G11 — preuve minimale d’exécution | Attester opération sans garder dossier supprimé ; RT | Référent droits/auditeurs habilités uniquement | C/F si justification ; preuve non identifiante privilégiée D46 |
| G12 — journaux sécurité/audit | Prévenir/diagnostiquer abus, tracer actions sensibles ; RT/sécurité | Exploitants sécurité habilités, accès contrôlé ; jamais message, mot de passe ou dossier en clair dans logs | F/C à vérifier, minimisation ; pas de données personnelles indues |
| G13 — sessions/appareils de confiance/codes | Authentification et révocation D51–D57 ; RT/sécurité | Titulaire voit ses appareils selon droits, services de sécurité ; codes/secrets non publiés | B/F : accès sécurisé ; preuve/rétention distincte à justifier |
| G14 — consentements éventuels | Prouver choix spécifique réellement requis et permettre retrait ; RT | Titulaire et référents habilités, pas réutilisation commerciale globale | A pour finalité concernée ; C/F pour preuve si nécessaire à vérifier |
| G15 — sauvegardes | Reprise après incident, continuité ; RT/exploitation | Exploitants strictement habilités et prestataires qualifiés, jamais consultation commerciale normale | Même fondement justifié que données sources, nécessité sécurité à vérifier |
| G16 — demandes grand public Info | Répondre au formulaire et affecter admin ; RT/franchiseur | Admins centraux seulement D01/S02.1, pas accès direct franchisé V1 | B/F selon demande ; portée du consentement historique du formulaire à vérifier, pas consentement par défaut pour tout |

### 18.4 Matrice de conservation, états, suppressions et avis requis

Toute exception doit avoir fondement, périmètre minimal, accès restreint, événement de sortie et revue ; aucun archivage systématique nouveau. **Q05** supprime un historique ciblé, **Q06** un projet avec travail/historiques ; ni l’un ni l’autre ne supprime automatiquement le compte ou le fil. Demande compte **D47** distincte, suspension immédiate **D48**, revue de toutes les données personnelles et copies. L’immuabilité des historiques/messages n’empêche pas l’effacement légal.

| Catégorie | Durée, point de départ et traitement N/V/A/X | Q05 / Q06 / compte / copies et effacement | Exception, sauvegarde et avis VJ |
| --- | --- | --- | --- |
| G01 — compte/identité | N : portée C2 sur données du dossier à confirmer ; V : relation suivie sans effacer contrôle d’échéance ; A : LA ; X : DX à définir depuis fin de relation | Q05/Q06 sans suppression automatique compte ; D47 ferme accès/sessions immédiatement puis instruction et suppression validée | VJ : portée C2, fin de relation et obligations ; sauvegardes G15, pas refus révisable éternel |
| G02 — coordonnées | N : C2 D44 ; V : contact significatif réel ; A : LA ; X : DX à définir | Q05/Q06 ne suppriment pas coordonnées hors projet ; demande compte/purge efface sauf exception justifiée, examiner aussi copies/prestataires | VJ : dernier contact et finalités séparées, pas relance automatique prolongeant sans justification |
| G03 — preuve email | Validité du lien temporaire non chiffrée ; preuve minimale pendant nécessité du compte, point départ vérification/clôture ; N/A/X selon finalité justifiée | Révoquer/invalider secrets lors suppression compte ; preuve identifiante effacée sauf nécessité distincte ; Q05/Q06 sans incidence directe | VJ : durée de preuve et logs, ne pas confondre token de vérification avec code admin 5 min |
| G04 — candidature/refus | N : C2 depuis contact significatif, pas forcément date refus ; V : suivi et revue ; A/X : seules pièces nécessaires à relation/obligation selon LA/DX validées | Q05/Q06 sans suppression dossier ; purge validée et D47 incluent statuts/motifs perso ; historique refus n’autorise pas rétention sans limite | VJ : base C2, obligations/gel éventuel et durée ; accès motif interne n’écarte pas droits légaux |
| G05 — échanges | N : C2 D44 ; V : nécessité du suivi ; A/X : portée LA/DX à confirmer depuis fin de finalité/contact | Messages immuables en usage normal ; effacement légal permis D40/D46. Q05/Q06 n’effacent pas le fil ; compte/purge examinent le fil et notifications détenues | VJ : contact significatif, données tierces, emails SMTP et gel éventuel ; aucun upload ajouté |
| G06 — franchisé actif/ancien | A : LA avec minimisation ; X : DX à fixer par pièce/obligation à partir de fin de contrat ou événement légal approprié ; pas C2 universel | Q05/Q06 limités au projet ; D47 déclenche instruction légale sans promettre disparition d’obligations contractuelles documentées | VJ : catégories réellement obligatoires et échéances ; archives restreintes si justifiées, pas compte opérationnel maintenu à titre d’archive |
| G07 — projets/versions | Travail mutable et historiques conservés pour finalité simulation ; N : portée C2 à confirmer si attaché au dossier ; A/X : LA/DX à valider, pas délai comptable automatique | Q05 historique seul ; Q06 travail+historiques ; comparaisons actualisées ; D47/purge couvrent données personnelles et liens ; copies G09 à revue séparée | VJ : nécessité/durée et exceptions légales ; séquence stable Q03 ne justifie pas conserver contenu supprimé ; G15 sans résurrection |
| G08 — exports | Aucune conservation serveur acquise ; si temporaires, durée technique minimisée à définir dès génération ; si détenus, base/durée par finalité et nature réelle, N/A/X à qualifier | Q05/Q06 ne modifient pas les fichiers déjà remis ; pour copies serveur réellement détenues, revue d’effacement légal, pas exemption automatique ; destinataires externes à traiter selon obligations applicables | VJ : copie livrée versus temporaire versus archive légalement nécessaire ; ne pas promettre serveur d’archives ni effacement chez tout tiers autonome |
| G09 — copies admin | Finalité/date de création/source identifiables ; N/V/A/X ne donnent aucun droit perpétuel, durée liée à analyse ou obligation documentée à valider | Q06 source ne modifie pas silencieusement la copie ; contrôle séparé et tracé de nécessité/effacement lors D47/purge. Pas contournement d’une demande par clonage | VJ : base/durée et éventuel gel ciblé ; informer le référent de toutes copies, G15 également |
| G10 — demandes d’effacement | Dès réception : réponse sous délai D50 (1 mois, extension motivée jusqu’à 2 mois de plus si applicable) ; conservation de l’instruction après clôture à fixer | Q05/Q06 peuvent produire un événement ciblé sans devenir une suppression compte ; D47 instruction/suspension, annulation D49 avant effacement irréversible, notification de résultat | VJ : preuves d’identité strictement nécessaires, exception, durée de dossier de droits et accès ; pas garder pièce d’identité par défaut |
| G11 — trace d’exécution | Départ opération réalisée ; contenu minimal et durée nécessaire à définir, aucune conservation infinie ; N/A/X même exigence de nécessité | Trace non identifiante D46 ; si une référence permet de réidentifier, donnée personnelle à soumettre à base/durée contrôlée, pas « anonyme » par simple pseudonyme | VJ : contenu/durée de preuve et rapprochement éventuel ; pas copie des projets/messages effacés en journal |
| G12 — logs/audit | Depuis événement ; horizon proportionné à justifier, aucun chiffre universel ; N/A/X pas motif d’allongement silencieux | Q05/Q06 audit minimal ; suppression compte exige évaluer logs identifiants, effacer ou limiter si obligation/finalité indépendante documentée | VJ : finalités/durée/gel ; aucun mot de passe, code OTP, texte des messages ou dossier en clair conservé dans logs |
| G13 — sessions/confiance | Inactivité admin30 min, membre2 h ; code admin5 min unique ; confiance navigateur30 j maximum D53–D57. Ce sont validités d’accès, pas durées universelles de logs | D48 invalide sessions et suspend accès immédiatement ; révocation confiance serveur selon D55. Q05/Q06 n’effacent pas tout compte ; données d’auth devenues inutiles éliminées selon politique validée | VJ : conservation métadonnées après invalidation, séparation preuve/audit et jeton actif ; aucun prolongement par polling |
| G14 — consentements | Durée liée à finalité et besoin de preuve ; départ octroi/retrait/clôture selon cas à valider ; N/A/X aucune durée automatique | Retrait pour finalité concernée et demande de compte traités sans convertir toute donnée en consentement révoqué ; preuve minimale/exception évaluées séparément | VJ : texte/versions/portée preuve et conservation ; pas nouvelle prospection ou cookie marketing ajouté |
| G15 — sauvegardes | Cycle/rotation/horizon d’effacement à définir avant production ; départ date sauvegarde + échéance approuvée, pas nouveaux délais C2 à chaque copie | Suppression visible/active ne prouve pas purge de backup. Après restauration technique, réappliquer effacements avant réouverture ; aucune réactivation des données effacées D49 | VJ : délai résiduel, accès, sous-traitants, exceptions ; ne pas annoncer effacement total tant que copies résiduelles non traitées ou légalement justifiées |
| G16 — demandes Info | D44 ne fixe pas automatiquement délai de tout prospect grand public ; besoin de réponse, clôture puis horizon à valider ; si rattaché à candidature, qualifier portée C2 explicitement | Q05/Q06 ne suppriment pas la demande ; D47/exercice des droits évalue les contacts détenus y compris hors compte | VJ : base/durée/finalité prospection éventuelle ; pas transformer accès admin central en droit illimité |

### 18.5 Processus opérationnel, exceptions et sauvegardes

Processus **spécifié**, non réalisé :

1. Établir la fiche de traitement : RT, catégories G01–G16, finalités, destinataires/sous-traitants, fondements vérifiés, événements/durées validés et notices FR/EN/ES. Les zones VJ doivent être résolues pour les traitements réellement ouverts à des personnes.
2. Détecter les échéances des candidatures selon C2 une fois sa portée validée, signaler à l’admin, revoir les exceptions et obtenir validation manuelle D45. Une notification automatique ou un statut approuvé n’autorise pas à repousser indéfiniment l’échéance.
3. Demande volontaire : confirmation explicite, date/statut, suspension immédiate et sessions fermées ; instruction avec vérification d’identité proportionnée, inventaire originaux/copies admin/exports détenus/sous-traitants/sauvegardes. Respecter D50 sans délai minimum imposé ; extension seulement si fondée et annoncée dans le premier mois.
4. Décider l’effacement ou la limitation ciblée justifiée. Obligation légale/litige : identifier texte ou motif, pièces strictement nécessaires, habilitations, événement de fin et revue. Une exception à une pièce ne gèle pas tout le dossier sans motif ; aucune nouvelle archive générale ajoutée à MOVEE Biz.
5. Exécuter Q05/Q06 dans leur périmètre ou la purge/D47 dans le périmètre personnel validé. Distinguer compte désactivé (accès coupé), retrait de visibilité (UI), suppression des bases actives, traitement des copies/sauvegardes et exceptions légales. Aucune simple désactivation présentée comme effacement effectif.
6. Tracer minimalement résultat, catégories, dates, éventuelles exceptions et traitement résiduel ; ne pas recopier contenus personnels dans l’audit. Contrôler l’exécution, informer la personne et les destinataires concernés selon obligations applicables. En cas d’échec partiel : conserver état exact, reprendre sous contrôle, ne pas notifier « tout effacé » fictivement.
7. Annulation après vérification d’identité possible uniquement avant exécution irréversible D49 ; après effacement aucune restauration du compte/dossier. Une restauration technique d’exploitation ne doit pas restaurer ces données personnelles ; neutraliser les éléments effacés avant réouverture. Cycle des sauvegardes et procédure de reprise à valider, pas d’effacement instantané de toutes copies promis.

Ces déclinaisons servent R02 et les décisions existantes ; modalités d’implémentation sans nouveaux privilèges admin ni durées implicites. La conservation financière des snapshots ne justifie jamais de contourner un effacement légal ; les hypothèses numériques réellement non identifiantes peuvent être distinguées du dossier personnel seulement après analyse de réidentification, sans anonymisation analytique décidée par défaut.

### 18.6 Recette documentaire et technique future R02

| Cas | Situation synthétique / entrée | Résultat attendu et réserve |
| --- | --- | --- |
| RG-T01 — échéance candidature | Dossier non abouti dont dernier contact significatif qualifié date t ; date de revue t+2 ans sous portée C2 validée | Signalement puis validation manuelle, exceptions revues ; pas suppression silencieuse ni échéance repoussée par notification/polling ; pas durée 2 ans appliquée à tous les contrats actifs |
| RG-T02 — refus révisable | Refus avec date/auteur/motif interne, dans durée de conservation justifiée | Réexamen possible sans compte neuf, pas pro avant approbation ; email refus sans motif automatique ; maintien historique sous durée validée |
| RG-T03 — demande et annulation | Demande confirmée à t, identité vérifiée, puis annulation avant effacement | Sessions immédiatement invalidées, pro/projets/messagerie suspendus ; traitement D50, admin peut annuler/réactiver avant purge ; aucun retour possible après effacement |
| RG-T04 — suppression version/projet | Q05 cible version V ; Q06 cible projet P ; copie admin C séparée | Q05 ne touche pas travail/autres versions ; Q06 retire travail/historiques, comparaisons actualisées ; exports déjà remis inchangés. C non modifiée silencieusement mais inscrite à revue légale si données personnelles concernées |
| RG-T05 — purge légale de messages | Dossier à effacer après validation, messages normalement immuables | Effacement légal malgré D40, fil et données perso traités ; pas texte copié dans logs, trace minimale non identifiante |
| RG-T06 — exception ciblée | Pièce effectivement nécessaire au litige, justification et échéance de revue validées | Restriction ciblée et accès habilités, autres données effaçables traitées ; pas gel intégral/illimité par simple mention « litige » |
| RG-T07 — sauvegarde restaurée | Backup antérieur à effacement, reprise d’exploitation | Accès contrôlé, réapplication des effacements avant ouverture ; dossier effacé ne réapparaît pas. Horizon réel de résidu connu/validé, aucune promesse de purge physique instantanée |
| RG-T08 — logs et preuves | Code OTP/texte message transmis par tentative d’erreur ; action de purge réalisée | Aucun secret/contenu personnel indu dans logs ; preuve minimale contrôlée ; durée des preuves non dérivée automatiquement du 5 min/30 j d’auth |
| RG-T09 — exports et données Info | Export déjà livré hors serveur ; demande publique non rattachée à compte | Ne pas promettre effacement d’un fichier externe autonome ni conservation serveur inexistante ; inventaire copies réellement détenues et politique du prospect à valider |

**B02 reste ouvert à validation juridique/DPO** : identifier RT/destinataires, bases et durées/événements par catégorie, exceptions/copies/sauvegardes et notices. Les règles décidées (C2 conditionnel, revue admin, suppression, suspension, annulation et délais D50) ne sont pas rouvertes. Une approbation de ce document par l’utilisateur ne constitue pas à elle seule l’avis juridique manquant.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:290 -->

## Avancement B05 — 21 octobre 2026

Suivi commercial local livré : pipeline distinct de l'approbation, historique,
notes/contacts privés, relances datées sans email automatique et fil unique
candidat/admin avant et après approbation. Emails locaux regroupés, consultation
admin partagée, aucun badge/compteur ou upload. Rattachements de centres
principal/satellites, propriétaire, territoire et date ajoutés.
Migrations 011–016 autorisées/appliquées sur test et développement ; 41 tests
réussis dont 24 MariaDB réels, envois simultanés et droits compris.
Voir `../docs/CRM.md` pour les conventions techniques, verrous et limites, et
`DEVELOPMENT_PROGRESS.md` pour les neuf chantiers. Les états B01–B04 ci-dessous
sont historiques. D/Q/S/F et réserves R01/R02 inchangés. Aucun email externe,
compte de démonstration conservé ou déploiement.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:318 -->

## Avancement local — B01, B02 et B03, 21 octobre 2026

B01 est présent : fabrique Flask, routage `movee.info.localhost:5051` /
`movee.biz.localhost:5051`, écran technique partagé, lancement sans dotenv,
tests sans DB. L'utilisateur a confirmé le parcours navigateur.

B02 comprend `movee_biz/db.py`, le runner `movee_biz/migrate.py`, les migrations
`001_accounts.sql` / `002_approval_events.sql` et le journal `schema_migrations`.
Les cibles provisionnées après autorisation SQL explicite sont `movee_biz_local` / `movee_biz_test` sur 3306 avec
comptes Biz distincts. Configurations privées en `instance/`, permissions 600,
ignorées par Git. Migrations 001/002 appliquées sur test puis développement ;
rejeu sans réapplication. 16 tests réussis dont trois tests MariaDB réels :
contraintes, rollback des données synthétiques et isolation des droits. Comptes
et événements vides dans les deux bases. Voir [docs/DATABASE.md](../movee-biz/docs/DATABASE.md). Aucun accès VPS,
aucun changement Backend ni `.env` historique. Ce constat B02 précède la livraison B03 décrite ci-dessous.

B03 est livré en mode local : routes auth, services et SQL séparés, catalogues
FR/EN/ES, sessions serveur, liens à usage unique, approbation/réexamen, code admin
email et confiance navigateur. Migrations 003–007 autorisées et appliquées sur
les deux bases Biz. Boîte email DB locale uniquement, aucun envoi externe.
Clé auth privée persistante ; aucun admin de démonstration créé. 25 tests réussis,
dont 12 MariaDB réels, et formulaires FR/EN/ES vérifiés dans le navigateur.
Voir [docs/AUTHENTICATION.md](../movee-biz/docs/AUTHENTICATION.md) pour les conventions, commandes et limites ; SMTP
réel, HTTPS, recette utilisateur et audit final restent à qualifier. Le suivi des
neuf chantiers est dans [Suivi consolidé dans la référence technique Biz](MOVEE_BIZ_TECHNICAL_REFERENCE.md).

Ces constats complètent les états historiques ci-dessous sans modifier les
décisions D/Q, les formules F ou les réserves R01/R02. L'absence de code décrite
dans l'inventaire de reprise est désormais historique, pas l'état courant.

---

<!-- provenance: movee-biz/codex/MOVEE_BIZ_TECHNICAL_REFERENCE.md:348 -->

## Reprise sur le nouveau Mac — état vérifié le 21 octobre 2026

**Outils Apple : correction vérifiée le 21 octobre.** Command Line Tools sélectionnés ; Git et Homebrew fonctionnent normalement. Le blocage de licence signalé lors de l’installation de Xcode est résolu pour le développement courant. Xcode reste facultatif pour le parcours EAS cloud.

### Couche propriétaire et emplacement

- Dépôt : `/Users/mbenmouha/Documents/Movee/movee-biz`.
- Conversation propriétaire : **Movee Biz Webapp**. Une application Flask indépendante, deux fronts `movee.info` / `movee.biz` avec routage par hôte ; prospects, candidatures, franchise et simulation financière. Aucun traitement des réservations, adhérents, crédits ou coachs opérationnels d’App.
- Python Homebrew **3.13.16**, environnement **`.venv/` recréé sur ce Mac** ; les neuf dépendances épinglées de `requirements.txt` ont été réinstallées. `pip check` et imports Flask/PyMySQL/python-dotenv réussis. La mention historique Python 3.13.2 ci-dessous décrit l’ancien Mac.
- Inventaire courant : **pas de code applicatif Python, route, template, schéma ou migration propre à Biz constaté**. L’environnement est prêt pour commencer le développement ; il n’existe pas encore d’application Biz lancée ou de connexion applicative validée.

### Configuration et base : distinction locale/VPS

- Configuration privée de Biz : **`movee-biz/.env`**, indépendante du `.env` parent propriétaire du Backend.
- Le fichier transféré indique **127.0.0.1:3307**, base **`movee_biz`**, et prévoit donc le tunnel SSH historique vers le VPS. Une adresse loopback ne signifie pas nécessairement une base de test sur le Mac : le port et le tunnel doivent être vérifiés.
- **Aucune base locale `movee_biz` n’est présente sur le serveur MariaDB du Mac au contrôle du 21 octobre**. Aucune base Biz locale, compte Biz local, migration ou tunnel n’a été créé dans cette session. Les comptes et droits du VPS restent des éléments historiques non contrôlés ici.
- Ne pas tester une écriture sur la cible du tunnel en la supposant locale. Préparer une cible de développement/test Biz indépendante et obtenir l’autorisation SQL correspondante avant sa création/import. Ne jamais utiliser `movee_app_local` ou le compte `movee_local` de MOVEE App pour Biz.
- **Port HTTP 5051 proposé/réservé par convention de reprise**, pas un service existant : 5050 appartient au Backend, 8081 à Metro/Expo Mobile. Tester les deux hôtes publics localement lors du développement du routage ; aucune modification DNS ou `/etc/hosts` n’a été faite.

### Statut des exigences et reprise

D01–D57, Q01–Q08, S01–S10/F01–F11 et les annexes financières/RGPD restent conservés. L’installation de Python ne vaut ni implémentation du moteur, ni validation fiscale/juridique, ni recette des calculs ou exports. Les sources annexes absentes de l’inventaire courant ne sont pas recréées ; utiliser les annexes déjà intégrées aux deux référentiels canoniques.

La prochaine conversation Biz doit lire les deux référentiels, vérifier l’état Git, puis proposer le premier lot de développement conforme au cadre validé, en incluant une stratégie de base locale/test isolée. Aucune reprise automatique du framework metadata-driven, Designer, MCP, Repositories ou SQL d’App.

Commandes d’environnement, séparation des bases et limites du Mac : [environnement du Mac](../docs/ENVIRONNEMENT_DEVELOPPEMENT_MAC.md).

### Règle de séparation des conversations

Cette conversation travaille exclusivement dans le dépôt indiqué ci-dessous. Les deux référentiels de ce même dépôt et [codex/AGENTS.md](AGENTS.md) font autorité dans leur périmètre. Les autres dépôts peuvent être consultés en lecture seule pour vérifier un contrat ; une évolution nécessaire dans une autre couche doit être décrite comme demande d’intégration à transmettre à sa conversation, sans y modifier du code, de configuration ou de SQL. Ne pas copier une règle, un schéma ou un Service d’une application à l’autre. Le compte administrateur de test ne valide pas les parcours adhérent/coach.

Les anciens chemins `/Users/mehdi.benmouha/Documents/Projects/newapp/...` désignent l’ancien Mac ; les chemins de travail actuels sont sous `/Users/mbenmouha/Documents/Movee`. Les sections historiques et résultats antérieurs restent datés ; l’état local ci-dessous ne prouve aucun déploiement sur le VPS.

---


**Version : 1.3 — 18 octobre 2026 (Europe/Paris).**
**Statut : D01–D57 et Q01–Q08 conservées ; R01/R02 intégrées, spécifiées mais non implémentées ; validation externe financière et juridique en attente.** Consolidation documentaire candidate à relecture finale ; aucune autorisation de développement, SQL ou déploiement. Les réserves du modèle financier demeurent provisoires quand elles ne sont pas explicitement arbitrées.

**Lecture des statuts :** Validé = cadrage explicitement transmis ; À détailler = principe acquis, spécifications incomplètes ; À arbitrer = décision non prise ou contradiction ; Implémenté = présence vérifiée dans le code ; À développer = prévu mais absent. Les réserves, valeurs indicatives et conventions techniques des sources gardent leur statut ; leur incorporation ne les transforme pas en décisions commerciales définitives.
