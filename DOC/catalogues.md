# 1. Introduction
## Rôle central des catalogues
Les catalogues constituent la mémoire organisée et vivante de l’agence. Ils centralisent la définition et la disponibilité de tous les objets du système, depuis les classes et méthodes jusqu’aux scénarios, prompts, agents ou extensions. Chaque objet est inscrit dans un catalogue correspondant à son type, garantissant qu’il soit unique, traçable et utilisable à tout moment.  
## Fonctions principales
Ils jouent un rôle de référentiel (chaque objet a une identité claire et vérifiable), d’orchestration (les scénarios et les agents résolvent leurs dépendances en s’appuyant sur les catalogues) et de gouvernance (les permissions, les statuts et l’audit se font au niveau des entrées de catalogue).  
## Génération et cohérence fractale
Les catalogues sont initialisés à partir d’une collection de catalogues de base puis générés et maintenus automatiquement par MetaMetaClass à partir des définitions d’objets.
## Utilité pratique
En pratique, les catalogues rendent le système réutilisable, auto-organisé et adaptable. Ils assurent que les objets puissent évoluer sans casser la stabilité globale, tout en permettant une traçabilité complète des changements et des exécutions.  
## Base pour MongoDB
Le but des catalogues est aussi de servir de base pour MongoDB ultérieurement, afin d’optimiser les requêtes complexes et de bénéficier des capacités d’indexation et de performance offertes par ce type de base de données.
# 2. Typologie des catalogues
## 2.1 Catalogues primaires (par type d’objet)
Chaque type d’objet (scénario, méthode, prompt, agent, ressource, extension, etc.) possède un catalogue primaire qui centralise sa définition, assure unicité et traçabilité, et sert de source de vérité pour l’exécution.
## 2.2 Catalogues de relations (un par type de relation)
Les relations sont gérées dans des catalogues dédiés, un par type de relation, conformément à la logique de triplet. Cette séparation optimise l’indexation et permet de parcourir la matrice par relations (profondeur, direction, cardinalité) de manière performante.
## 2.3 Catalogues dérivés
Construits automatiquement par MetaMetaclass à partir des catalogues primaires et de relations, ils regroupent des signatures utiles (vues, variantes de prompts, regroupements par statut/contexte). Ils simplifient les requêtes et l’exécution sans dupliquer inutilement la source.
## 2.4 Catalogues virtuels générés à la volée
Générés dynamiquement selon le besoin (requêtes ponctuelles, simulations), ils ne sont pas persistés par défaut. Ils peuvent être promus en définitions persistantes si leur usage devient récurrent.
## 2.5 Méta-catalogue transversal
Vue agrégée de tous les catalogues, construite à la volée pour l’administration et l’audit. Il n’est pas une source primaire mais un index global pour naviguer et superviser l’ensemble.
## 2.6 Modes de représentation : absolu et relatif
Indépendamment du type de catalogue, chaque entrée peut être représentée en mode absolu (fractale complète inline, autosuffisante) ou en mode relatif (références par identifiants de vecteurs vers d’autres objets). Le choix dépend du contexte (archivage, exécution, audit, optimisation) et est géré de manière uniforme par MetaMetaclass.
# 3. Structure d’une entrée de catalogue
## Vecteur primaire : Identité, Contexte, Vue 
Chaque entrée de catalogue est structurée autour d’un vecteur principal composé de trois piliers. 
- Identité (identity) décrit ce qu’est l’objet et regroupe tous ses attributs intrinsèques et métadonnées (y compris celles de traçabilité)
- Contexte (context) précise l’environnement de l’objet, ses relations et les possibilités d’action qui lui sont ouvertes
- Vue (view) spécifie la projection externe de l’objet, c’est-à-dire les modalités de rendu et d’exposition.
## Vecteur secondaire : Définition, Règle et Option
Chacun des trois piliers est enrichi par un vecteur secondaire composé de Définition, Règle et Option. 
- Définition (definition) précise les attributs attendus
- Règle (rule) impose les schémas et règles de validations
- Option (option) regroupe les variantes et paramètres ajustables, y compris les éléments dépendants de l’objet comme ses instances, afin d’étendre ou de personnaliser son comportement sans modifier sa définition de base.
## Statuts et transitions
Chaque entrée de catalogue possède un statut reflétant son état courant (par exemple registered, published, deprecated). Les transitions définissent les passages autorisés entre statuts et garantissent que les évolutions d’un objet restent cohérentes et traçables.  
Les transitions ne sont pas de simples attributs : elles existent comme des objets à part entière, définis et validés par MetaMetaClass. Chaque métaclasse référence explicitement les transitions qu’elle autorise, tandis que les instances n’expriment que leur statut courant. Lorsqu’un changement est invoqué, l’objet Transition applique ses règles, conditions et effets, et déclenche les hooks correspondants.
## Métadonnées système
En plus des vecteurs et des statuts, chaque entrée de catalogue enregistre des métadonnées techniques comme la version, le hash d’intégrité, les horodatages de c réation et de mise à jour, ainsi que l’acteur et le tenant. Ces informations assurent la traçabilité et l’auditabilité complète du système.
# 4. Génération et maintenance des catalogues
### 4.1 Génération automatique via MetaMetaclass
La génération des catalogues est entièrement prise en charge par MetaMetaclass. À partir des définitions d’objets et de leurs vecteurs, MetaMetaclass crée les entrées initiales, applique les règles de validation et inscrit les métadonnées de traçabilité. Les catalogues primaires (un par type d’objet) sont alimentés dès l’initialisation du système, tandis que les catalogues dérivés et virtuels sont générés à la volée en cas de besoin. Aucune intervention manuelle n’est nécessaire : enregistrement, mise à jour et suppression passent systématiquement par MetaMetaclass, garantissant cohérence et conformité.
### 4.2 Alimentation implicite par scénarios et méthodes
Les scénarios et méthodes alimentent implicitement les catalogues au cours de leur exécution. Chaque fonction qui manipule un objet (create, read, update, delete, execute, engage) produit automatiquement une entrée ou une mise à jour dans le catalogue correspondant. Cette alimentation est transparente pour l’utilisateur et ne nécessite aucune opération explicite. Les catalogues deviennent ainsi la mémoire vivante des activités du système.
### 4.3 Promotion de vues virtuelles en définitions persistantes
De nombreuses vues sont générées à la volée, de manière virtuelle, lors de l’exécution des scénarios. Lorsque certaines vues deviennent critiques ou récurrentes, elles peuvent être promues en définitions persistantes et inscrites comme entrées de catalogue à part entière. Ce mécanisme permet d’équilibrer flexibilité (création dynamique) et performance (stockage ciblé), tout en conservant la cohérence fractale des objets et leurs vecteurs.
### 4.4 Mise à jour et versionning des entrées
Chaque mise à jour d’un objet entraîne automatiquement la mise à jour de son entrée de catalogue et l’enregistrement des journaux associés. Les transitions de statut sont gérées par MetaMetaclass via le metaobjet transition, garantissant que toutes les évolutions suivent des règles strictes et auditées. Les catalogues intègrent un système de versionning permettant de retracer l’historique des modifications, de détecter les incohérences et de restaurer des versions précédentes si nécessaire. Des mécanismes de maintenance complètent ce dispositif : régénération automatique en cas de corruption, réplication vers des sauvegardes sécurisées et contrôle de l’intégrité par hash. Cette organisation rend les catalogues fiables, autoportants et résilients, tout en respectant la logique fractale et full dynamique du système.
# 5. Optimisation et performance
## 5.1 Vues et matérialisation
Les catalogues produisent par défaut des vues à la volée, générées uniquement au moment où elles sont sollicitées. Lorsqu’une vue est utilisée de manière récurrente ou critique, elle peut être promue en vue matérialisée et inscrite comme définition persistante dans le catalogue. Ce mécanisme équilibre flexibilité et performance, en limitant le stockage aux seules données nécessaires.
## 5.2 Caches et TTL dynamiques
Les entrées les plus sollicitées peuvent être conservées temporairement en cache. La durée de vie (TTL) n’est pas fixe mais pilotée par des métriques d’usage : plus une entrée est demandée, plus elle reste disponible en cache. Dès qu’un objet est modifié, sa version en cache est invalidée et remplacée. Cette approche permet d’accélérer les requêtes répétées sans compromettre la cohérence fractale.
## 5.3 Indexation et requêtes optimisées
Chaque catalogue est indexé sur les identifiants et les relations principales afin de réduire le temps de recherche. Les stratégies de requêtes privilégient les parcours relationnels directs, avec génération éventuelle de catalogues dérivés pour les opérations complexes. Ces catalogues dérivés sont temporaires par défaut, supprimés une fois la requête terminée, sauf promotion explicite en définitions persistantes.
## 5.4 Scalabilité et SLA
Le système est conçu pour supporter une scalabilité horizontale : les catalogues peuvent être répartis sur plusieurs nœuds ou serveurs, avec réplication et synchronisation automatiques. Cette architecture garantit la disponibilité et la continuité de service, même en cas de montée en charge soudaine. Les SLA sont pilotés par des métriques de performance intégrées : temps de réponse, taux d’erreur, cohérence entre nœuds. Le monitoring permanent permet de détecter toute anomalie et d’adapter la répartition des ressources.
# 6. Adaptation aux bases de données
## 6.1 Compatibilité multi-bases
Les catalogues sont conçus pour être indépendants de toute technologie de stockage. Ils peuvent être projetés dans n’importe quel type de base de données : SQL relationnelle, RDF natif, clé-valeur ou stockage distribué. Cette agnosticité garantit que le système reste adaptable aux besoins et contraintes de chaque projet.
## 6.2 Rôle de MetaMetaclass
MetaMetaclass agit comme couche d’abstraction : elle génère les catalogues à partir des définitions d’objets et applique les règles fractales de cohérence, quel que soit le backend choisi. Ainsi, la structure logique et la cohérence des vecteurs restent identiques, indépendamment de la technologie utilisée.
## 6.3 Optimisation des requêtes
Les catalogues sont organisés de manière à faciliter les requêtes complexes : division des relations en tables ou collections dédiées, indexation automatique des identifiants et des relations principales, et possibilité de générer des vues matérialisées. Ces optimisations s’appliquent uniformément, qu’il s’agisse d’une base SQL, RDF ou autre, afin de garantir performance et scalabilité.
# 7. Formats d’import et export
## 7.1 Option A : format fractal
Le format fractal repose sur la double fractale (identité, contexte, vue, enrichis par définition, règle et option). Il existe deux modes de représentation :  
- Absolu (inline) : l’objet est décrit en dur avec sa fractale complète. Ce mode rend l’objet autonome et archivable mais peut être lourd.  
- Relatif (référencé) : l’objet est décrit uniquement par l’identifiant de son vecteur ou des références à d’autres objets. Ce mode est léger, factorisé et dépend du catalogue parent.  
## 7.2 Option B : format simplifié
Le format simplifié est destiné aux imports manuels ou aux intégrations externes. Chaque objet est décrit par un dictionnaire clair, avec ses attributs essentiels (nom, type, valeur, règles). MetaMetaclass reconstruit ensuite la fractale complète à partir de ces définitions minimales.  
## 7.3 Cohérence et conversions
Quel que soit le format choisi, MetaMetaclass assure la cohérence fractale. Elle peut convertir automatiquement un objet relatif en représentation absolue (et inversement), selon le besoin (exécution, archivage, audit). Les conversions sont tracées et journalisées.  
## 7.4 Export et affichage
Lors d’un export, chaque catalogue peut être affiché en mode absolu (fractale complète) ou relatif (références). Le choix dépend du contexte : les exports destinés à l’archivage privilégient le mode absolu, tandis que les exports destinés à l’intégration ou à l’échange privilégient le mode relatif pour alléger les données.
# 8. Gestion des labels et du cache
Les catalogues s’appuient sur l’objet Label, qui regroupe dans son meta des paires clé/valeur et se rattache aux objets concernés via la relation label_of. Cela permet d’éviter les redondances, par exemple pour un champ identity.name réutilisé dans de multiples contextes, tout en laissant la possibilité de surcharger la valeur au niveau d’un client, d’un projet ou d’un produit.
La gestion des labels doit également intégrer la dimension linguistique : par défaut, un label est défini globalement par l’agence. Il peut être adapté au besoin par scope (client, projet, produit, utilisateur), et, le cas échéant, selon la locale de l’utilisateur. La logique reste relative par défaut, avec la possibilité d’imposer des absolus pour stabiliser un rendu ou un audit.
En parallèle, le cache joue un rôle clé dans l’efficacité du système. Chaque objet doit définir dans ses Meta.rules la fréquence de mise à jour et la stratégie de rafraîchissement (TTL, invalidation par événement, etc.). Le cache matérialise alors des vues absolues partielles ou complètes, optimisant l’accès aux données les plus utilisées. Le système doit assurer une optimisation continue du cache : rafraîchir les entrées critiques, supprimer les entrées obsolètes, et ajuster la profondeur de résolution selon les profils.
# 9. Extensions et interopérabilité
Les catalogues ne doivent pas rester confinés à l’intérieur du système. Leur rôle est aussi de servir de point d’ancrage pour interagir avec d’autres environnements, qu’il s’agisse de bases de données externes, d’outils tiers ou de services applicatifs. L’extension et l’interopérabilité garantissent que les catalogues peuvent être utilisés comme socle de référence partagé, tout en préservant leur logique relative/absolue.
Les vecteurs qui composent les catalogues intègrent déjà tout le nécessaire pour être utilisés dans différents contextes. Il n’y a pas de connecteurs additionnels à développer. Selon les méthodes centrales appliquées, un même vecteur peut être :
- exploité dans un paradigme SQL (relations tabulaires)
- manipulé comme document ou clé/valeur dans un environnement NoSQL
- parcouru comme graphe de relations
- exposé via une API interne
- rendu disponible à des partenaires via une API externe
- résolu en fonction des locales dans un contexte multilingue
# 10. Conclusion
## Rôle des catalogues comme mémoire vivante du système
## Perspectives d’évolution
# Cas d’usage
Les catalogues trouvent leur utilité dans plusieurs situations concrètes :
- Centraliser des définitions communes et éviter les redondances, par exemple un champ identity.name utilisé dans de nombreux modules et projets
- Permettre la navigation dans la matrice relationnelle, en suivant les liens label_of ou related_to
- Générer des vues adaptées selon le profil (relatif par défaut, absolu pour l’exécution ou l’audit)
- Rejouer des états passés pour l’audit ou la traçabilité
- Servir de base pour l’export et l’interopérabilité avec d’autres systèmes
En pratique, les cas d’usage illustrent pourquoi les catalogues sont un composant central du système, garantissant à la fois cohérence, performance et traçabilité.