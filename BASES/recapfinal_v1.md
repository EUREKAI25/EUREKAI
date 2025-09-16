<!-- on installe les objets (notamment les relations inheritance avantr la génération autonome pr ue les objets à exception soient là avant le déploiement) -->
# OBJET 
## RULE
### DEFINITION 
Tout est objet
### AUTOMATION
#### CREATE
Tout création d'objet déclenche automatiquement la création de son vecteur
Tout création d'objet déclenche automatiquement l'ajout de cet objet dans le catalogue de son type
# FUNCTION | [ SYSTEM ]
# METHOD | [ SYSTEM ]
## DESCRIPTION
## RULE
Toute méthode importe pour son exécution un objet de type [STEP].
# [METHOD]CENTRALMETHOD 
# [METHOD]SECONDARYMETHOD
## RULE
Toute méthode d'objet peut être lié par la relation [DEPENDS_ON] à un ou plusieurs objets de type  [STEP] en tant que [TARGET]. Il sera donc par ailleurs lié à un objet [TRIPLET] parallèlement à cet objet par la relation [RELATED_TO].
# [TYPE]METHODTYPE 
# [METHODTYPE]TRANSVERSAL | 
## IDENTITY.DESCRIPTION
﻿
# SCOPE
## RULE
# [INHERITANCERELATION]SCOPE_OF
﻿
# SCENARIO | [ SYSTEM ]
## RULE
Tout scenario est obligatoirement composé de 4 objets [STEP] pour son exécution, auxquels il sera lié par [DEPENDS_ON] en tant que [TARGET].
Il sera donc par ailleurs lié à un objet [TRIPLET] par la relation [RELATED_TO] dans tous les cas.
### SCHEMA
required_attributes : steps_bundle, goal
# GOAL | [METRICS]
# [TRANSVERSAL]METRICS | [BOOLEAN]
## IDENTITY.DESCRIPTION
## RULE
# STEP 
## RULE  
Tout objet [STEP] doit :  
- être obligatoirement lié en tant que **src** par [DEPENDS_ON] à un seul objet [SCENARIO] ;  
- être obligatoirement lié par [RELATED_TO] à l’objet [TRIPLET] impliqué ;  
- posséder obligatoirement un attribut d’ordre (position) unique dans le périmètre du [SCENARIO] parent.  
# LOOP | [ SYSTEM ]
﻿
# SCHEMA
# ELEMENT
required_attributes : definition_vector, rule_vector, option_vector
optional_attributes
required_methods
optional_methods
# rule_vector
## RULE
### SCHEMA
required_attributes : [SHEMA], [EXAMPLE], [PATH], [STAMP], [FRACTAL], [DOCUMENTATION]
required_methods : [CENTRAL_METHODS], [SECONDARY_METHODS], [TRANSVERSAL_METHODS]
# EXAMPLE
# DESCRIPTION
# TRIPLET
## RULE
Dans la bdd, on enregistre tout sous forme de triplet (<object_src>)
Tout objet de type triplet est forcément lié par depends_on à un objet de type Database
# DATABASE
## RULE
### AUTOMATION 
Tout projet généré génère automatiquement un objet de type Database, lié à cet objet par related_to 
# TYPE | [ABSTRACT]
## IDENTITY.DESCRIPTION
Un type est un objet qui définit la nature et les règles communes d’une famille d’objets, sans être instancié lui-même.
## EXAMPLE
RelationType est un type abstrait dont les enfants définissent chacun une forme précise de relation (héritage, dépendance, association, etc.).
## RULE
Les objets de type Type définissent les règles et paramètres qui lui sont applicables, qu'ils soient obliugatoires ou optionnels
### AUTOMATION 
Tout objet génère automatiquement le tag <object.type>Type (ex: Rule génère RuleType) et la relation <object.
Tout création d'un type d'objet déclenche automatiquement la création d'un catalogue
Tout objet doit impérativement posséder un schéma qui doit être respecté, des attributs et, en des méthodes 
# [CATEGORY]AUTOMATION 
## RULE
### VALIDATION 
Tout objet de la catégorie AUTOMATION est forcément lié par bundle_of à un objet comportant des objets de type RULE taggés "automation"
# STRUCTURE | [ABSTRACT]
## DEFINITION
L’objet Structure est un objet qui définit un cadre d’organisation pour d’autres objets, en fixant les règles de hiérarchie, de composition et de relations possibles.
## EXAMPLE
Catalogue est une Structure qui organise des catégories et des objets associés.
## [STRUCTURE]CATALOG | [SYSTEM]
## [STRUCTURE]CATALOG | 
## [STRUCTURE]CATALOG
# [STRUCTURE]LAYER | [ABSTRACT]
### IDENTITY.DESCRIPTION
Un layer est une couche structurelle qui permet de moduler l’organisation afin de s’adapter à différents publics et besoins.
### RULE
Chaue layer implique des permissions diférentes et impacte les méthodes et attributs en fonction de leur catégorie de type [PERMISSION] et selon ses règles propres
### EXAMPLE
Commercial Layer ajuste la présentation d’un même contenu pour un client, un investisseur ou un développeur.
## [LAYER]COMMERCIALLAYER
## [LAYER]TECHNICALLAYER
## [LAYER]ORGANICLAYER
## [LAYER]EDUCATIONALLAYER
## [LAYER]STRATEGICLAYER
# [STRUCTURE] | MATRIX
# [MATRIX] | FRACTAL
# [FRACTAL] | VECTOR
## [VECTOR] | IVCVECTOR
## [VECTOR] | DROVECTOR
# INSTANCE
## RULE
Toute instance a automatiquement la relation inherits_from avec l'objet dont elle est l'instance
Tout instance hérite automatiquement de toutes les règles et tous les attributs de ses ancêtred
# ALIAS
## RULE
Tout type d'objet peut potentiellement avoir un alias sous forme **<object.type>_of**. Ce dernier sera lié par la relation [RELATED_TO] à l'objet target, mais comme tout objet lié par une relation de type related_to ou depends_on, un alias "alias_of" sera automatiquement généré à sa création.
### SCHEMA
Un alias peut avoir exceptionellement des méthodes ou attributs spécifiques définis dans les règles du type d'objet, auquel cas la relation **<object.type>_of** doit préexister dans le catalogue.
Un alias est forcément associé à un [LAYER] 
# RELATION
## IDENTITY.DESCRIPTION
Une relation est un objet qui définit le lien entre deux autres objets à travers un [TRIPLET], en précisant sa nature (dépendance, association, héritage, etc.) sans exister par lui-même.
## [RELATION]DEPENDS_ON | [DEPENDENCYRELATION]
### DESCRIIPTION
Relation asymétrique (A dépend de B, mais B ne dépend pas forcément de A).
### RULE
#### AUTOMATION 
Tout objet possédant une relation de. type DEPENDS_ON a automatiquement aussi l'alias <object.type>_of de depends_on le liant à cet objet target
## [RELATION]INHERITS_FROM | [INHERITANCERELATION]
### DESCRIPITION
Relation hiérarchique dans laquelle l'objet enfant hérite des attributs et objets du parent
## [RELATION]RELATED_TO | [ASSOCIATIONRELATION]
### IDENTITY.DESCRIPTION
Relation symétrique (si A est lié à B, on peut dire aussi que B est lié à A).
### RULE
#### AUTOMATION 
Tout objet de type RELATED_TO a automatiquementaussi l'alias <object.type>_of de depends_on le liant à cet objet target
## [RELATIONTYPE]INHERITANCERELATION  
## IDENTITY.DESCRIPTION  
Lien où un objet hérite des attributs et règles d’un autre objet.  
## [RELATIONTYPE]DEPENDENCYRELATION  
## IDENTITY.DESCRIPTION  
Lien où un objet dépend d’un autre pour exister ou fonctionner.  
## [RELATIONTYPE]ASSOCIATIONRELATION  
## IDENTITY.DESCRIPTION  
Lien contextuel ou collaboratif entre deux objets indépendants.  
## EXAMPLE
## [RELATIONTYPE]COMPOSITIONRELATION  
## IDENTITY.DESCRIPTION  
Lien où un objet est constitué d’un ou plusieurs sous-objets.  
## [RELATIONTYPE]TAGGINGRELATION  
### IDENTITY.DESCRIPTION  
Lien qui associe un objet à un ou plusieurs tags.  
## [RELATIONTYPE]REFERENCERELATION  
### IDENTITY.DESCRIPTION  
Lien où un objet pointe vers un autre comme source d’information.  
### RULE
#### OPTION
Toute relation est forcément depends_on, related_to ou inherits_from.
# TAG
## RULE
Un tag peut faire partie d'une catégorie mais pas être taggé ni avoir d'enfant ([ABSTRACT])
## [TAG]SRC 
### RULE
Tout objet taggé src doit lié à un objet TRIPLET (depends_on) 
## [TAG]TARGET 
### RULE
Tout objet taggé target doit lié à un objet TRIPLET (depends_on) 
## [TAG]ABSTRACT
### IDENTITY.DESCRIPTION
Un objet abstrait est un objet qui sert uniquement de modèle ou de référence.
### EXAMPLE 
Un tag comme #AI est un objet abstrait : il définit une étiquette, mais n’existe jamais comme instance autonome.
## [TAG]CONCRETE
### IDENTITY.DESCRIPTION
Un objet concrete sert principalement à accueillir directement des instances 
### EXAMPLE 
La catégorie Livre qui contient des objets concrets de type Livre
### RULE
## [TAG]COMPOSITE
### IDENTITY.DESCRIPTION
Un objet composite sert à structurer d’autres catégories
### EXAMPLE 
La catégorie Produit contient les catégries Livre, Application, Formation
### USECASE
Site e-commerce, Blog
# [TAG]CATEGORY 
### IDENTITY.DESCRIPTION
Une catégorie est un tag qui a pour particularité de pouvoir ordonner, classifier
### RULE
Une catégorie peut avoir des enfants [COMPOSITE]
Une catégorie peut avoir des instances [CONRETE]
# PRODUCT | [AGENCY]
## [PRODUCT]DIGITALPRODUCT
## [DIGITALPRODUCT]WEBSITE 
## [DIGITALPRODUCT]EXTENSION
## [DIGITALPRODUCT]GAME
## [DIGITALPRODUCT]SOFTWARE | #SYSTEM
## [PRODUCT]PHYSICALPRODUCT
## [PRODUCT]PHYGITALPRODUCT
# SERVICE | [AGENCY]
## [SERVICE]MARKETING
## [MARKETING]WATCH
## [WATCH]MARKETWATCH
## [WATCH]COMPETITIVEWATCH
## [WATCH]STRATEGYWATCH
## [WATCH]TECHWATCH
## [TECHWATCH]AIWATCH
## [WATCH]DESIGNWATCH
## [WATCH]DATAWATCH
## [WATCH]REGULATORYWATCH
## [SERVICE]TECHNICAL
## [TECHNICAL]MAINTENANCE
## [TECHNICAL]OPTIMISATION
## [OPTIMISATION]SCALING
# END