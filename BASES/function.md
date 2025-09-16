# [OBJECT]FUNCTION

# [FUNCTION]METHOD | [ SYSTEM ] 
<!-- method est alias de fonction mais apporte les règles méthodes et attributs spécifiques -->
## IDENTITY.DEFINITION
## RULE
Toute méthode importe pour son exécution un objet de type [STEP].
# [METHOD]METAMOTOR
## IDENTITY
### DEFINITION
Cette méthode ultra-modulaire permet d'exécuter n'imprte quel type de fonction sur n'importe quel typer d'objet avec nimporte quel types de paramètres
### RULE
Required : { inputs, outputs, hooks, lifecycle}
### OPTION

## [METHOD]CENTRALMETHOD 
## [METHOD]SECONDARYMETHOD
## RULE
Toute méthode d'objet peut être lié par la relation [DEPENDS_ON] à un ou plusieurs objets de type  [STEP] en tant que [TARGET]. Il sera donc par ailleurs lié à un objet [TRIPLET] parallèlement à cet objet par la relation [RELATED_TO].

<!-- SCOPEMETHODS -->
# [INHERITANCERELATION]SCOPE_OF

# [METHODTYPE]LOOP | [ SYSTEM ]

# [OBJECT]FUNCTION
## IDENTITY
### DEFINITION
### RULE
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION

existe pour elle-même mais si elle n'est attachée à aucun objet via une méthode, on doit le faire (cron à exécuter)
# [OBJECT]METHOD
depends_on [FUNCTION] 
a un bu