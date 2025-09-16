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
### IDENTITY.DEFINITION
Un objet abstrait est un objet qui sert uniquement de modèle ou de référence.
### EXAMPLE 
Un tag comme #AI est un objet abstrait : il définit une étiquette, mais n’existe jamais comme instance autonome.
## [TAG]CONCRETE
### IDENTITY.DEFINITION
Un objet concrete sert principalement à accueillir directement des instances 
### EXAMPLE 
La catégorie Livre qui contient des objets concrets de type Livre
### RULE
## [TAG]COMPOSITE
### IDENTITY.DEFINITION
Un objet composite sert à structurer d’autres catégories
### EXAMPLE 
La catégorie Produit contient les catégries Livre, Application, Formation
### USECASE
Site e-commerce, Blog
# [TAG]CATEGORY 
### IDENTITY.DEFINITION
Une catégorie est un tag qui a pour particularité de pouvoir ordonner, classifier
### RULE
Une catégorie peut avoir des enfants [COMPOSITE]
Une catégorie peut avoir des instances [CONRETE]

# [CATEGORY]SYSTEM

# [CATEGORY]AUTOMATION 
## RULE
### VALIDATION 
Tout objet de la catégorie AUTOMATION est forcément lié par bundle_of à un objet comportant des objets de type RULE taggés "automation"


<!--        DATABASE    -->

# [CATEGORY]AUTOMATION | [SCOPE]
## IDENTITY
### DEFINITION
### RULE
transversal [SCOPE] (il faut que scope soit présent dans les atributs)
tout objet concerné
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE

### OPTION

# [TAG]STATUSTAG
# [STATUSTAG]ACTIVE
