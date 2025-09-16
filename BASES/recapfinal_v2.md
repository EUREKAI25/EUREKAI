<!-- on installe les objets (notamment les relations inheritance avantr la génération autonome pr ue les objets à exception soient là avant le déploiement) -->

# OBJET 
## IDENTITY
### DEFINITION
### RULE
Tout est objet
tout objet a un [MODE] (actif / passif / reactif)
tout objet a un [NATURE] (relative/absolute)
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
#### CREATE
Tout objet est créé avec la méthode centrale create portée par Object mais appelée par une éthode secondaire appliquée par l'objet de role [EXECUTOR] qui appelle la fonction 
Tout création d'objet déclenche automatiquement la création de son vecteur
Tout création d'objet déclenche automatiquement l'ajout de cet objet dans le catalogue de son type
#### READ
#### UPDATE
#### DELETE
#### EXECUTE
Toute action passe obligatoirement par la méthode récursive unique [METAMOTOR]
#### ENGAGE 
### OPTION

<!-- FUNCTIONS METHODS SCENARIOS -->

## RULE





## [VECTOR]PLANE 
### IDENTITY
#### DEFINITION
Objet de croisement de deux plans de la fractale (ex. IDENTITY×RULE) servant de conteneur navigable. 
#### RULE
- Un PLANE doit avoir un ident unique (IDENTITY, VIEW, CONTEXT, DEFINITION, RULE, OPTION).
- Un PLANE référence la liste des vecteurs qui le composent (ex : IDENTITYDEFINITION, IDENTITYRULE, IDENTITYOPTION).
- Un PLANE ne peut référencer que des vecteurs valides (issus de la fractale).
#### OPTION
- [PLANE] IDENTITY → {IDENTITYDEFINITION, IDENTITYRULE, IDENTITYOPTION}
- [PLANE] VIEW → {VIEWDEFINITION, VIEWRULE, VIEWOPTION}
- [PLANE] CONTEXT → {CONTEXTDEFINITION, CONTEXTRULE, CONTEXTOPTION}
- [PLANE] DEFINITION → {IDENTITYDEFINITION, VIEWDEFINITION, CONTEXTDEFINITION}
- [PLANE] RULE → {IDENTITYRULE, VIEWRULE, CONTEXTRULE}
- [PLANE] OPTION → {IDENTITYOPTION, VIEWOPTION, CONTEXTOPTION}

### VIEW
#### DEFINITION
#### RULE
#### OPTION

### CONTEXT
#### DEFINITION
#### RULE
#### OPTION

<!-- ORGANISATION -->


## [PLANE]VIEW 
### DEFINITION
### RULE
### OPTION

## [PLANE]CONTEXT
### DEFINITION
### RULE
### OPTION



### [PLANE]DEFINITION
#### IDENTITY
##### DEFINITION 

##### RULE
ne doit pas etre vide
doit etre multiloingue
format lang : string

###### EXAMPLE

##### OPTION
[OPTION]IDENTITYOPTION
#### VIEW
##### DEFINITION 
##### RULE
##### OPTION

#### CONTEXT
##### DEFINITION 
##### RULE
##### OPTION


### [PLANE]RULE 
#### IDENTITY
##### DEFINITION

##### RULE
###### SCHEMA


##### OPTION
#### VIEW
##### DEFINITION

##### RULE
###### SCHEMA


##### OPTION
#### CONTEXT
##### DEFINITION

##### RULE
###### SCHEMA


##### OPTION

### [PLANE]OPTION
#### IDENTITY
##### DEFINITION

##### RULE
###### SCHEMA


##### OPTION
#### VIEW
##### DEFINITION

##### RULE
###### SCHEMA


##### OPTION
#### CONTEXT
##### DEFINITION

##### RULE
###### SCHEMA


##### OPTION




### IDENTITY.DEFINITION
Un layer est une couche structurelle qui permet de moduler l’organisation afin de s’adapter à différents publics et besoins.
### RULE
Chaue layer implique des permissions diférentes et impacte les méthodes et attributs en fonction de leur catégorie de type [PERMISSION] et selon ses règles propres
### EXAMPLE
Commercial Layer ajuste la présentation d’un même contenu pour un client, un investisseur ou un développeur.
### [LAYER]COMMERCIALLAYER
### [LAYER]TECHNICALLAYER
### [LAYER]ORGANICLAYER
### [LAYER]EDUCATIONALLAYER
### [LAYER]STRATEGICLAYER
## [STRUCTURE] | MATRIX
## [STRUCTURE] | FRACTAL
rule depends_on [MATRIX]
## [STRUCTURE] | VECTOR
### IDENTITY
#### DEFINITION 
DESCRIPTION : Objet socle universel. Définit la fractale (IDENTITY, VIEW, CONTEXT).
RELATIONS depends_on [FRACTAL]
### RULE
### OPTION

## VIEW
#### DEFINITION 
#### RULE
#### OPTION

## CONTEXT
#### DEFINITION 
#### RULE
#### OPTION

### [VECTOR] | IVCVECTOR
### [VECTOR] | DROVECTOR
### [VECTOR] | PLANE
#### IDENTITY
##### DEFINITION
Objet de croisement de deux plans de la fractale (ex. IDENTITY×RULE) servant de conteneur navigable. 
##### RULE
- Un PLANE doit avoir un ident unique (IDENTITY, VIEW, CONTEXT, DEFINITION, RULE, OPTION).
- Un PLANE référence la liste des vecteurs qui le composent (ex : IDENTITYDEFINITION, IDENTITYRULE, IDENTITYOPTION).
- Un PLANE ne peut référencer que des vecteurs valides (issus de la fractale).
##### OPTION
- [PLANE] IDENTITY → {IDENTITYDEFINITION, IDENTITYRULE, IDENTITYOPTION}
- [PLANE] VIEW → {VIEWDEFINITION, VIEWRULE, VIEWOPTION}
- [PLANE] CONTEXT → {CONTEXTDEFINITION, CONTEXTRULE, CONTEXTOPTION}
- [PLANE] DEFINITION → {IDENTITYDEFINITION, VIEWDEFINITION, CONTEXTDEFINITION}
- [PLANE] RULE → {IDENTITYRULE, VIEWRULE, CONTEXTRULE}
- [PLANE] OPTION → {IDENTITYOPTION, VIEWOPTION, CONTEXTOPTION}

#### VIEW
##### DEFINITION
##### RULE
##### OPTION

#### CONTEXT
##### DEFINITION
##### RULE
##### OPTION

<!-- ORGANISATION -->

# [OBJECT]INSTANCE
## RULE
Toute instance a automatiquement la relation inherits_from avec l'objet dont elle est l'instance
Tout instance hérite automatiquement de toutes les règles et tous les attributs de ses ancêtred

# [OBJECT]ALIAS
## RULE
Tout type d'objet peut potentiellement avoir un alias sous forme **<object.type>_of**. Ce dernier sera lié par la relation [RELATED_TO] à l'objet target, mais comme tout objet lié par une relation de type related_to ou depends_on, un alias "alias_of" sera automatiquement généré à sa création.
### SCHEMA
Un alias peut avoir exceptionellement des méthodes ou attributs spécifiques définis dans les règles du type d'objet, auquel cas la relation **<object.type>_of** doit préexister dans le catalogue.
Un alias est forcément associé à un [LAYER] 

# END