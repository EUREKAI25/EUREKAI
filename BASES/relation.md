# RELATION
## IDENTITY.DEFINITION
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
### IDENTITY.DEFINITION
Relation symétrique (si A est lié à B, on peut dire aussi que B est lié à A).
### RULE
#### AUTOMATION 
Tout objet de type RELATED_TO a automatiquementaussi l'alias <object.type>_of de depends_on le liant à cet objet target
## [RELATIONTYPE]INHERITANCERELATION  
## IDENTITY.DEFINITION  
Lien où un objet hérite des attributs et règles d’un autre objet.  
## [RELATIONTYPE]DEPENDENCYRELATION  
## IDENTITY.DEFINITION  
Lien où un objet dépend d’un autre pour exister ou fonctionner.  
## [RELATIONTYPE]ASSOCIATIONRELATION  
## IDENTITY.DEFINITION  
Lien contextuel ou collaboratif entre deux objets indépendants.  
## EXAMPLE
## [RELATIONTYPE]COMPOSITIONRELATION  
## IDENTITY.DEFINITION  
Lien où un objet est constitué d’un ou plusieurs sous-objets.  
## [RELATIONTYPE]TAGGINGRELATION  
### IDENTITY.DEFINITION  
Lien qui associe un objet à un ou plusieurs tags.  
## [RELATIONTYPE]REFERENCERELATION  
### IDENTITY.DEFINITION  
Lien où un objet pointe vers un autre comme source d’information.  
### RULE
#### OPTION
Toute relation est forcément depends_on, related_to ou inherits_from.
