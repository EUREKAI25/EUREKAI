# [OBJECT]SCENARIO | [ SYSTEM ]
## RULE
Tout scenario est obligatoirement composé de 4 objets [STEP] pour son exécution, auxquels il sera lié par [DEPENDS_ON] en tant que [TARGET].
Il sera donc par ailleurs lié à un objet [TRIPLET] par la relation [RELATED_TO] dans tous les cas.
### SCHEMA
required_attributes : steps_bundle, goal
# GOAL | [METRICS]
# STEP 
## RULE  
Tout objet [STEP] doit :  
- être obligatoirement lié en tant que **src** par [DEPENDS_ON] à un seul objet [SCENARIO] ;  
- être obligatoirement lié par [RELATED_TO] à l’objet [TRIPLET] impliqué ;  
- posséder obligatoirement un attribut d’ordre (position) unique dans le périmètre du [SCENARIO] parent.  
