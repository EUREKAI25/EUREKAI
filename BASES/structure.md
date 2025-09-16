# STRUCTURE | [ABSTRACT]
## IDENTITY
### DEFINITION
#### DESCRIPTION
L’objet Structure est un objet qui définit un cadre d’organisation pour d’autres objets, en fixant les règles de hiérarchie, de composition et de relations possibles.
### RULE
#### EXAMPLE
Catalogue est une Structure qui organise des catégories et des objets associés.
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION

# [OBJECT]STRUCTURE | [ABSTRACT]
## IDENTITY
### DEFINITION
#### DESCRIPTION
L’objet Structure est un objet qui définit un cadre d’organisation pour d’autres objets, en fixant les règles de hiérarchie, de composition et de relations possibles.
### RULE
#### EXAMPLE
Catalogue est une Structure qui organise des catégories et des objets associés.
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION
# [STRUCTURE]CATALOG | [SYSTEM]
# [STRUCTURE]CATALOG | 
# [STRUCTURE]CATALOG
# [STRUCTURE]LAYER | [ABSTRACT]
# [STRUCTURE]LIST
## IDENTITY
### DEFINITION
### RULE
la nature de liste impose ses règles
par défaut choice : false
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION
# [LIST]OPTIONLIST
## IDENTITY
### DEFINITION
attributes : choice : true
### RULE
choice : true - 
validation.conformite : le type auquel se ratache le bundle est obligatoirement séfini 
ex : [MODEBUNDLE] actif : on doit avoir "mode" = x non nul
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION
# [LIST]SELECTLIST
choice : multiple possible [BUNDLE DE NATURES LISTE  CHOIX]
on doit faire un choix - multiple ou pas selon les règles de l'objet
# [STRUCTURE]BUNDLE
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
# [BUNDLE]MODEBUNDLE | [OPTIONLIST]
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
# [BUNDLE]NATUREBUNDLE | [OPTIONLIST]
## IDENTITY
### DEFINITION
### RULE
tout objet a un [NATURE] (relative/absolute) -> [OPTIONLIST]

### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION



# [STRUCTURE]CATALOG | [SYSTEM]
# [STRUCTURE]CATALOG | 
# [STRUCTURE]CATALOG
# [STRUCTURE]LAYER | [ABSTRACT]

#
---
# SCRIPT
# FORMAT

# GRID
# MODULE
# ACCORDION
# ANIMATION
# CSSANIMATION
# JSANIMATION
# DESIGN
# FORMAT
# [SCHEMA]REGEX
# FILE
# DIRECTORY
# REPOSITORY
# TREE
# DOCUMENTATION
# README
# HOWTO
# BUNDLE
# NOMENCLATURE
# SPECIFICATION
# [TAG]HTMLTAG

