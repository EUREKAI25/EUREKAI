### Introduction
Les scénarios constituent l’unité fondamentale de l’exécution dans le système. Chaque fonction, chaque action, chaque transformation est représentée comme un scénario, découpé en steps normalisés et orchestrés par la fonction récursive universelle. Cette approche garantit que toutes les opérations, simples ou complexes, suivent une logique commune et peuvent être tracées, auditées et rejouées de manière cohérente.
Une fonction, une action, une méthode ou un scénario désignent la même entité. Il n’existe pas plusieurs options terminologiques : tout est objet, et toute opération est un scénario. Ainsi, chaque méthode d’objet est une fonction, qui est elle-même un scénario composé de steps. Cette unification garantit la cohérence du système et élimine toute ambiguïté.
Un scénario n’est pas seulement une suite d’instructions : c’est une structure déclarative et exécutable, définie par son vecteur (identité, contexte, vue enrichis de définition, règles et options) et pilotée par les catalogues. Il peut décrire une opération élémentaire (copier une donnée, afficher un module) comme une orchestration complexe impliquant plusieurs objets, relations et agents.
La granularité des scénarios est pensée de façon fractale : un scénario peut contenir des sous-scénarios, qui eux-mêmes suivent le même modèle. Cette récursivité garantit que le système reste extensible et homogène, sans multiplier les exceptions ni les chemins particuliers.
Des conventions de nommage et de structuration assurent que chaque scénario est identifiable, réutilisable et versionnable. L’ensemble forme une bibliothèque vivante qui alimente aussi bien l’exécution interne que les interactions avec les utilisateurs, les clients ou les agents.
### Modèle canonique des steps
Chaque scénario suit un modèle canonique composé de quatre steps, toujours exécutés dans le même ordre. Cette structure simple et universelle permet de normaliser toutes les opérations.
- get : récupération des données ou du contexte nécessaires à l’exécution.  
- execute : exécution de la logique métier. L’étape execute est toujours une boucle (loop), même si elle ne s’exécute qu’une fois. Ce choix garantit l’uniformité, facilite le batching, le streaming et la reprise après interruption.  
- validate : contrôle de la validité du résultat produit par la boucle, application des règles et vérification de la conformité au schéma. Si le résultat ne respecte pas les contraintes, le système applique les corrections nécessaires et réexécute le cycle tant que les conditions ne sont pas satisfaites, garantissant qu’aucune sortie invalide ne peut franchir cette étape.
- render : production du rendu final, qui peut être une sortie utilisateur, une mise à jour de base de données, un envoi à une API ou toute autre forme de résultat observable.  
Ce modèle garantit que toute action, quelle que soit sa complexité, peut être exprimée, validée et exécutée dans une forme universelle. Il sert de contrat commun pour toutes les fonctions, qu’elles soient élémentaires ou composées.
### Modèle de classification des scénarios
Chaque scénario a exactement un type (get, execute, validate, render) et exactement une intention (read, create, update, delete, execute, engage). Les opérateurs affinent l’intention sans changer ni le type ni l’unicité. Aucune double intention n’est autorisée.
#### Types canoniques
Chaque scénario est classé dans un type canonique unique. Ce typage décrit la fonction fondamentale du scénario et impose la structure des steps.
- get : scénarios dont la fonction est d’accéder à des données ou ressources sans produire d’effet actif direct.  
- execute : scénarios centrés sur l’action, le calcul ou l’orchestration de sous-scénarios.  
- validate : scénarios chargés de contrôler, corriger et garantir la conformité des résultats selon les règles et schémas.  
- render : scénarios dont la finalité est de produire une sortie visible, exploitable ou transmissible (interface, fichier, rapport, API).  
#### Intentions et opérateurs autorisés
##### read
fetch : récupérer une donnée passive
load : récupérer une ressource active (handle, contexte)
list : lister, paginer
find : localiser dans un flux/texte
query : requêter une base (SQL/JS/graph)
scan : parcourir exhaustivement une zone/collection
audit : lecture à des fins de contrôle
##### create
ideate : exploration d’hypothèses
generate : matérialisation initiale d’un artefact
register : inscription dans un registre ou catalogue
log : création d’une entrée de log/événement
##### update
modify : modifier des attributs
edit : édition structurée
correct : corriger des erreurs
optimize : améliorer performance/qualité
##### delete
backup : sauvegarder avant suppression
prune : suppression sélective/élagage
purge : suppression définitive
##### execute
compute : exécuter un calcul/traitement
transform : conversion de forme, langue ou langage (inclut convert)
route : aiguiller vers chemin/agent/scénario
loop : itérer, batcher, streamer
test : exécuter des tests techniques ou fonctionnels
orchestrate : enchaîner des sous-scénarios
##### engage
brief : cadrer la demande
plan : planifier jalons et ressources
assign : affecter rôles et tâches
coordinate : synchroniser acteurs/scénarios
notify : notifier et obtenir accusé
discuss : discussion interactive
negotiate : ajuster et valider les attentes
consent : solliciter et consigner un accord
#### Règles et conventions
Un scénario = un type unique
Un scénario = une intention unique
Les opérateurs sont choisis dans l’intention et ne changent jamais le type
validate est réservé au type validate et n’apparaît pas comme opérateur d’autres intentions
transform regroupe toutes les conversions (format, langue, langage) et réside dans execute
#### Filets de sécurité
Si un scénario semble hésiter entre deux intentions, on choisit l’intention par l’effet persistant principal (create si création, update si modification en place, delete si suppression, read si accès sans effet, execute si traitement sans effet persistant direct, engage si interaction)
Toute tentative de double intention est refusée à la validation
Les schémas imposent le triplet (type, intention, opérateur) et rejettent toute combinaison non autorisée
### Déclencheurs et contexte
Les scénarios ne s’exécutent jamais de façon arbitraire. Ils sont toujours déclenchés par un signal explicite et encadrés par un contexte défini. Cela garantit que chaque exécution a une cause traçable et une portée limitée.
#### Déclencheurs
Un déclencheur (trigger) est l’événement qui lance un scénario. Les déclencheurs possibles sont :  
- système : hook, cron, signal interne  
- utilisateur : action manuelle depuis une interface  
- agent IA : appel spécifique lié à une mission affectée  
- API : requête externe ou intégration tierce  
Chaque déclencheur est enregistré avec son ident, sa source, et son horodatage. Aucun scénario ne peut démarrer sans déclencheur valide.
#### Contexte
Le contexte décrit l’environnement d’exécution du scénario. Il comprend :  
- les relations actives (objets reliés, parents, enfants, connexions transversales)  
- les permissions et rôles en vigueur  
- les paramètres de session (locale, canal, environnement)  
- les options héritées du vecteur secondaire (definition, rule, option)  
Le contexte est injecté automatiquement dans le vecteur du scénario. Il fixe ce à quoi le scénario a accès, quelles actions sont autorisées, et quelles contraintes s’appliquent. En l’absence de contexte valide, l’exécution est refusée par validate.
### Entrées et sorties
Chaque scénario dispose d’entrées et de sorties clairement définies. Elles assurent l’interopérabilité, la traçabilité et la cohérence de l’ensemble du système.
#### Entrées
Les entrées d’un scénario sont toujours exprimées sous forme de vecteur. Un vecteur se compose du vecteur principal et de son vecteur secondaire. Chaque élément du vecteur est obligatoire dans la structure, même s’il peut être vide selon le contexte.
##### Vecteur principal  
- identité : identifiant unique de l’objet, type, classe, héritage  
- contexte : relations de l’objet avec d’autres objets, permissions actives, état courant  
- vue : gabarit ou template de rendu, options i18n, formats d’affichage
##### Vecteur secondaire (lié à chaque élément du vecteur principal)  
- définition : attributs détaillés, métadonnées propres à l’élément  
- règle : contraintes, validations et conditions de conformité applicables  
- option : variantes, paramètres ajustables, configurations spécifiques
##### Exemple : pour un scénario de type render appliqué à une page web, le vecteur peut inclure :  
- identité → ident:page_123, type:page, classe:Page  
- contexte → relations:{site:site_1, parent:section_5}, permissions:{read:true, write:false}  
- vue → template:landing_page, i18n:{lang:fr}, format:html  
Chacun de ces éléments est enrichi de son vecteur secondaire, par exemple :  
- identité.définition → titre, description, tags  
- contexte.règle → interdiction d’accès en dehors du rôle admin  
- vue.option → choix entre plusieurs layouts disponibles  
Ce découpage garantit que l’ensemble des informations nécessaires au scénario est présent dès l’entrée, sans ambiguïté, et que chaque champ peut être validé ou corrigé en phase validate.
#### Sorties
Les sorties sont normalisées pour être directement réutilisables par d’autres scénarios. Elles incluent le résultat produit, enrichi de son identité, des règles appliquées et du contexte de validation. Toute sortie est sérialisée dans un format commun (JSON structuré) et horodatée, avec possibilité d’inclure les logs associés.
#### Objet opération et objet sortie
##### Principe  
Chaque exécution crée deux objets :  
- opération : représente l’exécution elle-même (qui, quand, pourquoi, comment).  
- sortie : représente le résultat produit (données, artefacts, rendus).
##### Opération  
Contient un snapshot d’entrée (vecteur complet), un journal des steps (get, execute(loop), validate, render), les validations effectuées et leurs corrections, les métriques (latence, ressources), les événements de hooks, le statut final, les erreurs, l’agent/l’utilisateur à l’origine et un hash de reproductibilité.
##### Sortie  
Contient le résultat structuré, les métadonnées de provenance (opération_id, horodatage, version), l’empreinte d’intégrité, et les pointeurs vers les artefacts (fichiers, pages, API).
##### Rétention et archivage  
- rétention courte par défaut pour opération et sortie (configurable), puis archivage compressé ou purge.  
- épinglage possible par règle (compliance, preuve, incidents, analytics) pour prolonger la conservation.  
- anonymisation/minimisation avant archivage si nécessaire.  
- export et réhydratation possibles à partir d’un bundle signé (entrée + graine + version des catalogues).
##### Sécurité et intégrité  
- signatures/hashes, horodatage, journal append-only.  
- séparation des domaines de stockage (opérations, sorties, artefacts) avec permissions dédiées.  
- indexation par ident, opération_id, scénario, type, intention et période.
##### Bénéfices  
- audit complet, reproduction à l’identique, preuves d’intégrité, mesure de qualité, et coût de stockage maîtrisé grâce aux politiques de rétention/archivage.
#### Contrat
Le couple entrée/sortie constitue un contrat. Toute entrée incomplète ou non conforme est rejetée en phase de validate, et toute sortie est vérifiée avant d’être rendue disponible. Ce mécanisme garantit qu’aucun scénario ne peut produire un état incohérent ni transmettre des données inutilisables.
### Orchestration récursive
L’orchestration récursive applique la fonction récursive universelle à tout objet du graphe en se déplaçant exclusivement via les relations. À chaque nœud, le scénario canonique est exécuté (get → execute(loop) → validate → render), avec sélection déterministe des méthodes par héritage et métamétaclasse, sans recherche heuristique.
#### Parcours par relations
Le déplacement entre objets se fait par les relations typées (plusieurs tables selon le type de relation). Le contexte référence les relations actives et, le cas échéant, les éléments imbriqués via context.option.elements. Le parcours respecte direction, cardinalités et priorités, et s’arrête selon des bornes explicites.
#### Profondeur et prévention de cycles
La profondeur maximale est bornée par règle. Les cycles sont détectés par empreintes de chemin et ident déjà visités, avec stratégie stop ou skip configurable. Toute récursion qui dépasserait les limites ou reviendrait sur un même nœud est bloquée et journalisée.
#### Sélection déterministe des méthodes
L’objet transporte son vecteur complet. L’héritage, les règles et les options imposent la méthode applicable, de sorte qu’il n’existe qu’un seul chemin valide. Aucune recherche ou résolution ambiguë n’est autorisée : en cas de conflit, validate échoue et propose une correction conforme au schéma.
#### Loop universelle et agrégation
L’étape execute est toujours une loop, même à une itération. Les itérations d’un nœud agrègent leurs résultats selon les règles de l’objet (réduction, concaténation, fusion, transformation). Cette uniformité rend possible le batching, le streaming, la pause/reprise et la distribution de charge sans divergence de logique.
#### Référence au status universel
Toute transition de cycle de vie s’exprime par un changement de status tel que défini au niveau des classes d’objets et validé par la MetaMetaclass; les scénarios de transition restent soumis au modèle canonique et à validate
### Boucle et contrôle de flux
Chaque scénario repose sur une boucle unique et universelle. Même lorsqu’une seule itération suffit, l’exécution passe par la loop pour garantir l’uniformité et permettre batching, streaming et reprise contrôlée.
#### Batching
La boucle regroupe plusieurs éléments similaires dans une même itération pour optimiser l’usage des ressources. Le batch est configuré par taille, durée ou condition logique. Chaque élément du batch conserve néanmoins son ident et son vecteur pour validation indépendante.
#### Streaming
La boucle peut fonctionner en mode flux continu. Les résultats partiels sont validés et rendus au fil de l’eau, sans attendre la fin du traitement complet. Ce mode permet d’exploiter des sorties en temps réel et de maintenir une latence minimale.
#### Pause et reprise
Toute boucle peut être interrompue de manière contrôlée. L’état courant (vecteur, position, résultats intermédiaires) est sauvegardé comme objet opération. La reprise reprend au point exact de l’arrêt, garantissant l’idempotence et évitant la perte de progression.
#### Contrôle d’ordonnancement
Les itérations sont ordonnancées selon priorité, dépendances et règles du scénario. Les conflits de ressources déclenchent un backoff ou une mise en file d’attente. Les boucles concurrentes s’exécutent en isolation logique, avec verrouillage ou sandbox selon les besoins.
### Validations et schémas
La validation garantit que toute exécution respecte un contrat formel. Elle s’appuie sur des schémas déclaratifs et des règles catégorisées, appliqués avant, pendant et après l’exécution, avec corrections automatiques si nécessaire.
#### Objectif
Empêcher toute entrée invalide, corriger les écarts tolérables, refuser les cas non réparables, produire des sorties sûres, cohérentes et traçables.
#### Portée
Les entrées et sorties générées par des agents (IA ou utilisateurs) sont traitées exactement comme celles issues des scripts. Elles passent par les mêmes règles et schémas, sans exception.### Schéma des vecteurs
Chaque partie du vecteur possède un schéma dédié, versionné et compatible ascendante: identity.schema, identity.rule, identity.option; context.schema, context.rule, context.option; view.schema, view.rule, view.option. Les schémas décrivent types, contraintes, dépendances inter-champs, cardinalités de relations, formats et normalisations.
#### Catégories de règles
Règles de validation de données: types, formats, required, ranges, enum, unicité, cohérence inter-champs, référentiels.  
Règles de conformité et sécurité: charte, PII/PHI, chiffrement, redaction, politiques d’accès, politiques d’exposition.  
Règles d’exécution et de flux: batching, streaming, timeouts, retries/backoff, budgets temps/mémoire, limites de profondeur, prévention des cycles.  
Règles de permissions et de portée: rôles, scopes, multitenant, contextes d’exécution, politiques de délégation.  
Règles de relations et d’intégrité: cardinalités, directions, contraintes d’existence, cascade autorisée/interdite, invariants.  
Règles de version et compatibilité: versions de schéma, migrations, dépréciations, contrats E/S stables.
#### Processus de validation
Chaque scénario contient son step validate, et chaque sous-scénario possède également le sien. La validation est donc systématique, fractale et récursive. À chaque exécution, le cycle get → execute(loop) → validate → render impose un point de contrôle obligatoire avant de poursuivre.
Dans un scénario simple, le validate contrôle la sortie de l’execute et applique corrections ou rejets. Dans un scénario complexe, composé de plusieurs sous-scénarios, chaque sous-scénario effectue son validate localement. Les résultats validés seulement sont propagés vers le scénario parent. Cela évite l’accumulation d’erreurs et garantit que chaque niveau de l’orchestration reste cohérent.
Les validations s’exécutent toujours au plus près du résultat produit. Elles appliquent les règles déclarées dans le vecteur secondaire (rule), effectuent des corrections déterministes si prévu, et journalisent chaque action. En cas d’échec, l’exécution est interrompue au niveau local et le scénario parent reçoit un statut d’erreur explicite.
Lorsqu’un agent intervient (IA ou humain), son résultat est injecté dans le cycle et validé localement par le step validate avant d’être propagé.
#### Corrections automatiques
Les règles peuvent porter des actions de réparation déterministes: compléter des valeurs par défaut, recalculer des dérivés, arrondir, tronquer, re-mapper un ident, retenter avec paramètres sûrs. Les corrections sont traçées, limitées par budget et soumises à seuil d’acceptation; au-delà, l’exécution échoue.
#### Contrat E/S et idempotence
Chaque scénario déclare un contrat E/S signé par version. Les opérations répétées doivent être idempotentes par design (clés d’empreinte, séquences contrôlées, verrous logiques) afin d’autoriser retries et reprises.
#### Refus, compensation et rollback
Si la validation échoue, l’opération est refusée avant effets persistants. Si des effets ont eu lieu, des scénarios de compensation/rollback sont déclenchés selon les règles d’intégrité et de sécurité.
#### Journalisation et audit
Chaque validation, correction et décision est journalisée via hooks. Les objets opération et sortie portent les preuves: schémas utilisés, règles appliquées, corrections, métriques, empreintes et signatures.
#### Rétention et archivage
Politiques par catégorie d’objet: opération (court terme par défaut), sortie (moyen terme), artefacts (selon criticité). Épinglage pour conformité ou preuve, anonymisation/minimisation avant archivage, export bundle signé.
#### Gouvernance des schémas
Schémas et règles sont gérés par catalogues, versionnés, testés en sandbox, publiés avec validations obligatoires et possibilité de rollback. Une matrice de compatibilité décrit quelles versions de scénarios acceptent quelles versions de schémas.
#### Désambiguïsation et interdictions
Les mots réservés des types canoniques (get, execute, validate, render) ne sont pas réutilisés comme opérateurs. Les scénarios portent un type et une intention uniques; toute double intention est rejetée à la validation.
### Permissions et sécurité
La sécurité repose sur une gestion stricte des permissions et un contrôle systématique à chaque étape du cycle. Les droits ne sont jamais implicites : ils doivent être explicitement définis et validés par le vecteur context.rule.
#### Permissions
Les permissions déterminent ce qu’un objet, un utilisateur ou un agent peut faire. Elles s’appliquent toujours à un couple (sujet, action) et sont stockées dans les règles du contexte. Les principaux niveaux sont :  
- lecture (read)  
- écriture (create, update, delete)  
- exécution (execute)  
- engagement (engage, interaction avec d’autres agents ou utilisateurs)  
Les permissions peuvent être héritées (classe, rôle, relation) ou définies localement sur l’instance. Toute absence de permission explicite équivaut à un refus.
#### Règles de sécurité
Les règles de sécurité sont inscrites dans le vecteur secondaire (rule) et appliquées automatiquement en phase validate. Elles incluent :  
- contrôle d’accès (rôle, scope, tenant, session)  
- contraintes d’exposition (données sensibles, anonymisation, redaction)  
- contraintes de conformité (charte centrale, lois applicables, GDPR, etc.)  
- contraintes de flux (budgets temps/mémoire, limites d’appels, quotas)  
#### Intégration dans le cycle
À chaque scénario, le contexte injecte les permissions actives. L’étape validate vérifie que l’action est autorisée. En cas d’infraction, l’exécution est bloquée et le log enregistre le refus. Les agents IA ne peuvent pas contourner ces règles : leurs sorties passent elles aussi par validate.
#### Journalisation
Chaque décision de permission (acceptée ou refusée) est tracée via hooks. Cela permet d’auditer les accès, de détecter les abus et d’appliquer une politique de sécurité proactive.
#### Principe général
La règle est simple : tout est interdit par défaut, sauf ce qui est explicitement autorisé et validé par schéma**.
### Hooks, logs et traçabilité
#### Hooks
Les hooks sont les points d’ancrage qui déclenchent des actions automatiques à chaque étape du cycle (before, onsuccess, onfailure). Ils permettent d’injecter de la surveillance, de la correction ou de la veille sans modifier la logique principale.
#### Triggers
Un trigger est un alias d’un hook affecté à une mission spécifique. Les triggers n’existent pas de façon autonome : ils sont toujours rattachés à un hook du cycle (before, onSuccess, onFailure). Ils servent à déclencher des scénarios ou actions prédéfinis en réponse à un événement précis (signal système, action utilisateur, requête API, intervention d’un agent). Cette unification garantit que tout déclenchement reste traçable et validé dans le cadre unique des hooks.
##### Trigger de fin de scénario
Un trigger de fin de scénario est un alias branché sur les hooks terminaux du scénario racine. Il se déclenche uniquement au moment où le scénario racine se termine, via onSuccess ou onFailure. Aucun hook after n’est nécessaire.
###### Nom et liaison
- Nom : trigger.end_of_scenario  
- Liaison : déclenché sur onSuccess ou onFailure du scénario racine (jamais sur les sous-scénarios)  
- Fréquence : tir unique, idempotent (clé = operation_id)  
###### Actions exécutées
1. **Calcule et fige les temps**  
   - wall_time_ms = now - created_at  
   - active_time_ms = somme des tranches d’exécution (hors pauses)  
   - ended_at = now  
2. **Fige l’état final**  
   - status = succeeded | failed | compensated  
   - last_event_at = now  
   - error_summary (si échec)  
3. **Fige l’intégrité et le contexte**  
   - integrity_hash final, catalog_version, code_version, seed  
   - snapshot minimal des vecteurs utilisés (références ou pointeurs)  
4. **Journalise l’issue**  
   - entrée de log terminale “end” (append-only) avec métriques et tags  
5. **Déclenche les suites éventuelles**  
   - notifications et analytics (asynchrones)  
   - remédiations ou compensations si onFailure l’exige  
   - purge des verrous temporaires, fermeture des files internes  
6. **Émet un event externe optionnel**  
   - scénario.ended pour les consommateurs (dashboard, SLA, billing)  
###### Contraintes
- Pas de hook after distinct : l’alias se branche uniquement sur onSuccess/onFailure.  
- Racine uniquement : le trigger ignore les fins de sous-scénarios.  
- Idempotence : un seul tir possible par operation_id.  
- Reprises : si reprise ou crash, le premier onSuccess/onFailure validé gagne; les suivants sont ignorés.  
###### Schéma minimal logué
- operation_id  
- scenario_id  
- ended_at  
- wall_time_ms  
- active_time_ms  
- status  
- metrics_finales  
- error_summary (si applicable)  
- integrity_hash_final  
- catalog_version  
- code_version  
- seed  
- tags complets (type, intention, operators, tenant, role, trigger.kind, etc.)  
#### Logs
Les logs sont produits exclusivement par les hooks. Chaque fonction, chaque scénario, chaque validate génère un log structuré décrivant entrées, sorties, règles appliquées, corrections et statut. Les logs sont horodatés, signés et stockés de façon immuable.
#### Traçabilité
La traçabilité est assurée par la combinaison des logs et des ident d’objets. Tout résultat peut être relié à son scénario, ses entrées, son contexte et ses validations. Cela garantit la possibilité d’audit complet, de reproduction et de responsabilité sans perte d’information.
### Gestion des erreurs
#### Détection
Toute erreur est détectée soit par un step validate qui échoue, soit par un hook onfailure déclenché automatiquement. Aucune erreur ne peut passer silencieusement.
#### Catégorisation
Les erreurs sont classées en catégories : données invalides, permissions refusées, ressources manquantes, dépassements de quotas, conflits de règles, erreurs système.
#### Traitement
Chaque erreur déclenche un scénario de traitement. Selon le type, le système peut corriger automatiquement (valeur par défaut, retry, fallback), compenser (rollback d’opération), ou bloquer définitivement avec log d’incident.
#### Journalisation
Toutes les erreurs sont loguées via hooks avec leur contexte complet (vecteurs, relations, règles actives, déclencheur). Les corrections appliquées sont également tracées pour garantir audit et transparence.
#### Principe
Une erreur non réparable bloque le scénario localement mais ne compromet pas le reste du système. Le statut est remonté au parent avec indication explicite de l’échec.
### Transactions et remédiations
#### Modèle transactionnel
Toute opération déclare son périmètre transactionnel et ses effets persistants. Par défaut, les effets ne sont engagés qu’après validate réussi. Les opérations multi-ressources utilisent des transactions locales + orchestration de compensations (saga) pour garantir un état cohérent en cas d’échec partiel.
#### Idempotence et verrous
Chaque action expose une clé d’idempotence pour autoriser retries sans effets doublons. Des verrous logiques à granularité d’objet (ident, relation, ressource) évitent les conflits. Les verrous expirent automatiquement et sont journalisés.
#### Compensation et rollback
Si un effet persistant a été appliqué avant l’échec, une action de compensation dédiée est exécutée (annulation inverse, réécriture, neutralisation). Si aucune compensation sûre n’existe, l’opération est mise en quarantaine et un scénario de remédiation est ouvert.
#### Cohérence et invariants
Des invariants déclaratifs (intégrité de relations, budgets, états autorisés) sont vérifiés avant et après les effets. En cas de violation, l’opération est stoppée et une compensation est tentée. Les invariants sont versionnés et référencés par validate.
#### Stratégies de remédiation
##### Retries contrôlés
Les réexécutions sont limitées par règles de flux (compteur, fenêtre temporelle, backoff exponentiel, jitter). Chaque tentative porte un ident d’idempotence pour éviter les effets doublons. Les causes réputées permanentes entraînent l’arrêt immédiat.
##### Délestage en file différée
Les opérations non urgentes sont placées en file d’attente avec reprise planifiée. Les métadonnées enregistrent priorité, dépendances, fenêtre d’exécution et budget. La file applique une politique FIFO avec sauts de priorité autorisés par règles.
##### Quarantaine et analyse assistée
Les cas ambigus ou non réparables automatiquement sont isolés en quarantaine. Un scénario d’analyse assiste l’agent (IA ou humain) avec le contexte complet, propose des hypothèses et des corrections candidates, sans jamais exécuter hors des règles.
##### Escalade graduée
Selon criticité et SLA, l’incident est escaladé vers un rôle ou une équipe. Les niveaux définissent délais d’intervention, canaux de notification et pouvoirs de décision. Les escalades sont tracées et réversibles.
##### Kill switch ciblé
Une capacité fautive peut être désactivée instantanément par règles. Le kill switch est contextualisé (tenant, environnement, route, opérateur) et réversible. Son activation génère un log d’incident et un plan de reprise.
##### Dégradation gracieuse
Quand l’objectif principal est indisponible, un mode dégradé fournit un résultat partiel mais sûr. Les invariants sont préservés, les limites annoncées, et un ticket de remédiation est ouvert pour rétablir la qualité nominale.
##### Circuit breaker
Les appels vers une ressource défaillante sont coupés au-delà d’un seuil d’erreurs. Le disjoncteur passe en état ouvert, puis demi-ouvert pour tests périodiques de reprise. Les états et seuils sont pilotés par règles.
##### Compensation ciblée
Si des effets persistants ont été appliqués avant l’échec, des actions inverses spécifiques sont exécutées pour revenir à un état cohérent. Chaque compensation est atomique, traçable et idempotente.
##### Rétablissement automatique
À la résolution d’une cause racine, les opérations en attente sont relancées automatiquement selon ordre, dépendances et budgets. Les verrous obsolètes sont purgés, les compteurs de retry remis à zéro selon politique.
##### Communication et notification
Les parties prenantes reçoivent des notifications adaptées au rôle et au canal. Les messages incluent ident d’opération, statut, impact, prochaine action et ETA indicatif. La communication est journalisée pour audit.
#### Politique de reprise
Toute boucle sauvegarde un snapshot minimal (position, vecteur, résultats intermédiaires). La reprise reprend exactement au dernier point validé. Les effets déjà commis sont reconnus via idempotence; les compensations déjà tentées sont marquées pour éviter re-jeu.
### Logs exhaustifs et audit
#### Couverture
Les logs capturent chaque exécution via les hooks (before, onSuccess, onFailure). Ils sont append-only, horodatés, signés et immuables. Toute entrée, sortie, décision et correction est tracée.
#### Champs obligatoires
operation_id, scenario_id, type (get|execute|validate|render), intention (read|create|update|delete|execute|engage), operators, step, trigger (source, ident), actor (user_id, agent_id, role, tenant), environment (env, locale, channel), goal (mission_id, description), resources_provided (liste), input_snapshot (vecteur ou diff), output_ref (hash, taille, pointeurs), validations_appliquees (règles, statuts, corrections), permissions_eval (décisions et motifs), metrics (durée, cpu, mem), status (succeeded|failed|compensated), error (categorie, code, message), rationale (raison fournie par l’agent le cas échéant), catalog_version, code_version, seed, integrity_hash
#### Tagging et facettes
Tags obligatoires: type, intention, operators, object.class, relation.type, error.categorie, permission.decision, tenant, environment, locale, trigger.kind, agent.kind, step. Les vecteurs alimentent aussi les tags (identity.type, context.permissions, view.template). Ces tags permettent des filtres et agrégations rapides.
#### Indexation et requêtes
Index temporel (created_at, ended_at) et facettes sur tags. Requêtes supportées: par type/intention/opérateur, par acteur/tenant, par classe d’objet/relation, par catégorie d’erreur, par décision de permission, par template de vue, par règle appliquée, par scénario. Exemples: erreurs create sur 24h; validations échouées par règle; actions execute.route par tenant; décisions refusées de permission.read.
#### Rationale et justification
Lorsque l’agent intervient, le log enregistre la justification courte (rationale) et, si prévu, un résumé de critères utilisés. La rationale est limitée, normalisée et soumise à validate; aucune donnée sensible non prévue ne peut y figurer.
#### Intégrité et conformité
Chaque entrée porte un hash et une signature. Redaction automatique des champs sensibles selon context.rule. Journal séparé pour PII si nécessaire, avec accès restreint. Politique de rétention configurable, épinglage possible pour conformité et enquête.
#### Rejeu et reproduction
Pour tout log, le bundle de reproduction référence input_snapshot, catalog_version, code_version et seed. Le système permet un dry-run contrôlé pour rejouer un scénario à l’identique ou comparer avec la version courante.
#### Export et analyse
Exports par fenêtre temporelle et facettes en formats structurés. Connecteurs d’analyse prêts (tableau de bord, requêtes d’audit). Les rapports incluent métriques, distributions d’erreurs, taux de succès et pistes de remédiation.
### Planification et scheduling
La planification est déclarative, déterministe et auditée. Tout scénario planifié expose un contrat horaire, des priorités et des garde-fous. Le cron central évalue toutes les secondes les échéances et déclenche les exécutions autorisées.
#### Définition de planning
Le planning est défini dans le vecteur context.rule (RRULE-like) avec rrule, start_at, end_at, timezone, exceptions, blackout_windows, maintenance_windows, max_concurrency, rate_limits, quotas, retry_policy, jitter. Les overrides par tenant, rôle ou environnement sont autorisés et versionnés.
#### Horloge et fuseaux
Le système opère en UTC et traduit en timezone locale au moment de l’évaluation. Correction d’horloge et de dérive incluse. Changement d’heure géré (DST): exécutions “skippées” ou “doublées” sont résolues par règle explicite.
#### Cron central par seconde
Un cron unique, déclenché chaque seconde, calcule les échéances, résout les priorités et émet des triggers. Aucune logique de scheduling hors de ce point. Le cron écrit un log de décision signé à chaque tick.
#### Priorités, fenêtres et fairness
Chaque job porte priority, deadline, time_window. L’ordonnanceur applique un algorithme fair-share par tenant et rôle, avec limites globales et locales. Les jobs hors fenêtre sont déclassés ou refusés selon règle.
#### Files d’attente et leasing
Les jobs éligibles entrent en file. Attribution via leasing avec lock à TTL pour éviter les doublons. Les workers renouvellent le lease jusqu’à fin d’exécution; à expiration, la reprise est orchestrée de manière idempotente.
#### Déduplication et idempotence
Un key_idempotence par job garantit qu’une même échéance ne s’exécute qu’une fois, même en cas de retries, partitions réseau ou redéploiements.
#### Retries, backoff et jitter
Les échecs déclenchent retries selon retry_policy (max_attempts, backoff, jitter). Les causes permanentes sont court-circuitées. Les retries respectent quotas et fenêtres.
#### Quotas et rate limits
Limites par scénario, opérateur, tenant, rôle et environnement. Le dépassement retarde ou refuse l’exécution selon politique, avec log explicite et métriques.
#### Dépendances et graphes
Un scénario peut dépendre d’autres scénarios via relations typées. L’ordonnanceur vérifie les prérequis, états autorisés et invariants. Les cycles sont interdits; toute dépendance non satisfaite reporte l’échéance.
#### Pause, reprise et expirations
Pause manuelle ou automatique par règle. Reprise au dernier snapshot validé. Jobs expirés (au-delà de deadline) sont marqués missed, avec remédiation éventuelle (rattrapage, compensation ou abandon documenté).
#### Événementiel vs horaire
Deux modes coexistent: time-driven (RRULE) et event-driven (trigger). Les triggers peuvent promouvoir un job dans la file s’ils respectent limites et priorités. L’unification se fait dans le cron central.
#### SLA et métriques
Chaque job peut déclarer un SLA (latence cible, taux de succès). L’ordonnanceur mesure temps d’attente, temps actif, respect de fenêtre, taux de réussite et alimente les tableaux de bord.
#### Sécurité et permissions
Avant déclenchement, le cron évalue permissions et contexte. Aucune exécution planifiée n’a lieu si les droits ou le contexte sont invalides; un log de refus est émis.
#### Gouvernance et audit
Toute décision de scheduling est loguée: horodatage, raison, priorités, files, verrous, déclencheur. Les configurations sont versionnées, testées en sandbox et déployées avec rollback possible.
### Parallélisation
La parallélisation répartit l’exécution d’un scénario ou d’un lot d’objets sur plusieurs workers en garantissant isolation, idempotence et ordre logique lorsque requis.
#### Modèle de concurrence
Concurrence contrôlée par worker pools. Unité de travail = item de loop. Concurrency par scénario et par tenant paramétrable. Backpressure appliquée dès que les files ou budgets sont saturés.
#### Isolation et idempotence
Chaque item porte une clé d’idempotence. Les effets persistants sont atomiques et vérifiés par validate. Les workers opèrent en sandbox logique; aucune donnée partagée mutable sans verrou déclaré.
#### Répartition de charge
Stratégies: round-robin, least-loaded, hash-based (affinité), size-aware (poids). Rebalancing à chaud autorisé. Les décisions de placement sont tracées.
#### Affinités et épingles
Affinité par ident, relation, tenant ou ressource externe pour maximiser le cache et limiter les verrous. Épingle possible d’un groupe d’items sur un worker jusqu’à complétion.
#### Limites et budgets
Budgets temps/mémoire/IO par worker et par job. Limites de concurrence par opérateur et par ressource externe. Dépassement → throttling, report ou refus selon règle.
#### Contention et verrous
Verrous logiques à granularité fine (objet, relation, ressource). TTL obligatoire, renouvellement par lease. Deadlock évité par ordre global de verrouillage; détection et résolution par abandon contrôlé.
#### Ordonnancement intra-job
Ordre partiel garanti par dépendances déclaratives. Les items indépendants s’exécutent en parallèle; les dépendants sont sérialisés. Les violations d’ordre déclenchent retry séquencé.
#### Fan-out et fan-in
Fan-out: partition d’un lot en sous-lots parallèles avec clés d’affinité. Fan-in: agrégation déterministe (réduction, merge, concat) validée avant render. États partiels journalisés pour reprise.
#### Map/Reduce et sharding
Map: transformation par item. Reduce: agrégation sous règles. Sharding par hash d’ident ou par relation; re-sharding possible entre étapes si la charge dérive.
#### Timeouts, retries, cancellations
Timeouts par item et par lot. Retries avec backoff et jitter, bornés par règles. Cancellation coopérative avec snapshot de progression pour reprise ultérieure.
#### Déduplication et anti-répétition
Clés d’empreinte sur items et sous-lots pour éviter re-jeu. Les reprises vérifient l’état via logs et idempotence; seuls les items incomplets repartent.
#### Interactions externes
Accès aux APIs/services soumis à rate limits et circuit breakers. Les appels sont regroupés (batch) quand autorisé; sinon, file dédiée par domaine pour lisser la charge.
#### Observabilité
Métriques par worker et par lot: throughput, latence p50/p95, taux d’erreur, saturation, temps d’attente. Traçage distribué corrélant items, locks et effets persistants.
#### Sécurité
Permissions évaluées par item. Aucune élévation de privilège en parallèle. Les secrets sont scellés par worker et non partagés entre items.
### Versionning et compatibilité
#### Versionnement global
Chaque scénario, objet et catalogue est versionné. Les versions incluent un ident unique, un numéro sémantique, un horodatage et un hash d’intégrité. Tout changement significatif crée une nouvelle version figée, jamais une modification en place.
#### Compatibilité ascendante
Les schémas et vecteurs sont conçus pour rester compatibles avec les versions antérieures. Les attributs nouveaux sont optionnels, les règles s’appliquent de façon cumulative. Aucun champ existant n’est supprimé sans plan de dépréciation.
#### Dépréciation contrôlée
Les versions obsolètes sont marquées deprecated avec date d’expiration, scénario de migration et documentation. Les hooks de compatibilité assurent la traduction vers le format actuel jusqu’à suppression effective.
#### Catalogues versionnés
Chaque catalogue JSON (objets, méthodes, relations, prompts) est conservé par version. Les agents et scénarios indiquent explicitement sur quelle version ils s’exécutent. Les comparaisons inter-versions sont possibles via diff structuré.
#### Basculement et rollback
Toute mise à jour majeure est déployée en parallèle avec version précédente. Les scénarios critiques testent les deux versions (A/B). En cas d’échec, rollback instantané à la version stable, journalisé et idempotent.
#### Compatibilité multi-langages
Les métaclasses assurent la traduction des objets vers différents langages (Python, JS, SQL, etc.) en conservant une signature identique. Le versionnement inclut ces générateurs, garantissant cohérence entre backends.
#### Gouvernance des versions
Les règles de versionning sont centralisées: version_minimale_supportée, politique de rétention, cadence de release, SLA. Chaque upgrade déclenche validate sur cohérence, intégrité et compatibilité ascendante.## Tests et sandbox
tests unitaires et scénarios
aperçus et dry-run
environnements isolés
### Mesures et SLA
#### Métriques collectées
Chaque scénario, step et objet produit des métriques standardisées: temps de traitement (latence wall_time et active_time), throughput (items/s), taux de succès, taux d’erreurs par catégorie, utilisation CPU/mémoire/IO, consommation réseau, taille des entrées et sorties, profondeur de file d’attente, nombre de retries et corrections appliquées.
#### Points de mesure
Les métriques sont capturées par hooks au niveau get, execute, validate et render. Les métriques agrégées sont calculées par scénario, par tenant, par rôle et par environnement. Les mesures de bout en bout incluent déclencheur → résultat.
#### SLA déclaratifs
Chaque scénario peut définir un SLA: latence maximale, taux de disponibilité, taux de réussite minimal, délais de reprise après incident. Les SLA sont stockés dans le vecteur context.rule et validés automatiquement.
#### Surveillance et alertes
Les métriques sont comparées aux SLA en temps réel. Dépassement → déclenchement d’alerte (hook onFailure dédié). Les alertes peuvent être locales (scénario, tenant) ou globales (système). Les escalades sont tracées.
#### Rapports et audits
Les SLA et métriques sont historisés. Rapports périodiques incluent taux de conformité, pannes, temps moyen de reprise, distribution des latences et erreurs. Les rapports sont consultables par tenant et consolidés globalement.
#### Auto-ajustement
Le système peut adapter dynamiquement ses ressources (parallélisation, throttling, scheduling) pour rester conforme aux SLA. Les décisions d’ajustement sont loguées et validées comme toute exécution.## Internationalisation et rendu
i18n dans render
accessibilité
formats cibles
### Réutilisation par catalogue
#### Principe
Tout objet, scénario, méthode ou vecteur est inscrit dans un catalogue. Le catalogue sert de registre central, garantissant qu’un élément défini une fois peut être réutilisé partout sans duplication ni divergence.
#### Catalogues disponibles
Les catalogues couvrent les objets, classes, méthodes, relations, prompts, scénarios, templates, règles, schémas, agents et extensions. Chaque entrée est versionnée, signée et validée. Les catalogues sont eux-mêmes des objets et suivent les mêmes règles fractales.
#### Accès et injection
Lorsqu’un scénario requiert un objet, il l’importe depuis le catalogue par ident. Le vecteur complet est injecté automatiquement. Les options locales (override) sont fusionnées avec la définition de base. Aucun chargement direct hors catalogue n’est autorisé.
#### Mutualisation et cohérence
Un objet partagé par plusieurs projets ne vit qu’une fois dans le catalogue. Les scénarios le référencent par ident. Les mises à jour sont propagées à tous les consommateurs selon règles de compatibilité et politique de version.
#### Catalogues dynamiques
Les catalogues peuvent être enrichis à la volée par création d’objets (create). Toute nouvelle entrée passe par validate et reçoit ident, hash et signature. Les catalogues sont mis à jour en temps réel avec backup immédiat.
#### Audit et gouvernance
Chaque appel à un catalogue est logué. Les diff entre versions sont historisés. Les règles d’accès aux catalogues suivent context.rule (permissions, rôles, tenants). La gouvernance définit les catalogues globaux (système) et locaux (tenant, projet).## Métaméthode et gabarits
méthode unique d’orchestration
spécialisation par paramètres
contrats de composition
### Schéma de règle dans les méta-objets (extrait)
{
  "object": {
    "identity": {
      "ident": "string",
      "type": "string",
      "class": "string",
      "inheritance": ["string"],
      "definition": {
        "attributes": {},
        "metadata": {}
      },
      "rule": {
        "status": {
          "families": ["lifecycle","execution","availability","compliance"],
          "allowed": ["string"],
          "initial": "string",
          "transitions": [
            {"from":"string","to":"string","conditions":{"permissions":["string"],"rules":["string"],"invariants":["string"]},"effects":{"notify":["role|user"],"hooks":["onSuccess","onFailure"]}}
          ],
          "invariants": [{"name":"string","check":"expr|ref","severity":"error|warn|info"}]
        },
        "versioning": {
          "compat_min": "semver",
          "deprecated_after": "iso8601",
          "migration": {"scenario":"ident","params":{}}
        },
        "i18n": {
          "labels": {"code":"Label"},
          "required_locales": ["fr","en"],
          "fallback": "en"
        }
      },
      "option": {
        "parameters": {},
        "variants": ["string"]
      }
    },

    "context": {
      "relations": [
        {"type":"string","target":"ident|class","direction":"in|out|both","cardinality":"one|many","cascade":"none|update|delete"}
      ],
      "permissions": {"read":["role"],"write":["role"],"execute":["role"],"engage":["role"]},
      "state": "string",
      "definition": {
        "attributes": {}
      },
      "rule": {
        "security": {
          "access": {"roles":["string"],"scopes":["read","create","update","delete","execute","engage"]},
          "redaction": ["jsonptr"],
          "sensitive": ["jsonptr"]
        },
        "execution": {
          "flow": {
            "batch": {"size":0,"max_ms":0},
            "stream": {"enabled":false,"chunk":0},
            "retries": {"max":0,"backoff_ms":0,"jitter_ms":0},
            "timeouts_ms": {"get":0,"execute":0,"validate":0,"render":0}
          },
          "budgets": {"time_ms":{"max":0},"cpu_pct":{"max":0},"mem_mb":{"max":0},"io_ops":{"max":0}}
        },
        "schedule": {
          "rrule":"string","start_at":"iso8601","end_at":"iso8601","timezone":"IANA",
          "blackout":["iso8601-range"],"maintenance":["iso8601-range"],
          "max_concurrency":0,"rate_limits":{"per_sec":0,"per_min":0,"per_hour":0},"quota":{"period":"day|week|month","max":0}
        },
        "logging": {
          "level":"debug|info|warn|error|audit",
          "fields_required":["operation_id","scenario_id","actor","metrics"],
          "integrity":{"sign":true,"hash":"sha256"}
        },
        "triggers": [
          {"alias":"string","on":"before|onSuccess|onFailure","mission":"ident","params":{}}
        ],
        "audit": {"pin":false,"retention_days":30,"exportable":true},
        "remediation": {
          "on_error":["retry","quarantine","compensate","escalate","degrade","kill_switch"],
          "retry":{"max":3,"backoff_ms":200,"jitter_ms":50},
          "compensations":["ident_scenario"],
          "escalation":{"to":["role"],"sla_ms":60000}
        }
      },
      "option": {
        "elements": ["ident"],
        "overrides": {}
      }
    },

    "view": {
      "template": "string",
      "format": "json|html|bin",
      "i18n": {"lang":"fr"},
      "definition": {
        "attributes": {},
        "ui_meta": {"layout":"string","theme":"string","a11y_min":"AA|AAA"}
      },
      "rule": {
        "render_policy": {"allowed_formats":["json","html","bin"],"max_payload_kb":0},
        "visibility": {"roles":["string"],"channels":["web","api","cli"]}
      },
      "option": {
        "layout": "string",
        "theme": "string",
        "placeholders": {}
      }
    }
  }
}
### Exemple JSON minimal
{
  "meta": {
    "id": "page-001",
    "name": "Landing Page",
    "class": "Page",
    "version": "1.0.0"
  },
  "status": {
    "families": ["lifecycle"],
    "allowed": ["draft", "active", "archived"],
    "initial": "draft",
    "transitions": [
      {"from": "draft", "to": "active"},
      {"from": "active", "to": "archived"}
    ]
  },
  "permissions": {
    "read": ["user", "admin"],
    "write": ["admin"]
  },
  "definition": {
    "attributes": {
      "title": "string",
      "slug": "string"
    }
  },
  "view": {
    "template": "landing_default",
    "format": "html"
  }
}
insights agrégés
traçabilité complète
export et analyses