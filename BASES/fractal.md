# FRACTAL 
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
------------------------------------------------------------------
#

# [OBJECT]FRACTAL 
## IDENTITY
### DEFINITION
- Description : Ensemble complet structuré par ses plans et dimensions, c’est l’objet autonome et auto-référentiel structurant chaque objet.
### RULE
- Structure : contient 1 objet [GLOBALPLANESET]
- Example : Un “Utilisateur” est fractal car on peut identifier son identité (nom), sa vue (profil affiché), et son contexte (rôle, permissions), chacun avec définition, règles et options.
- Question : null
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION

##

# [OBJECT]VECTOR
## IDENTITY
### DEFINITION
- Description : Brique élémentaire de la fractale, un vecteur porte une information unique (identité, règle, option, etc.) qui peut être combinée avec d’autres.
- Question (création) : Quelle information unique dois-je définir pour que ce vecteur existe et puisse être combiné dans un plan ?
### RULE
- Example : Le vecteur « Identity.Definition » : il définit l’identifiant unique d’un objet.
- format : vector_<methodname>_<objectname>_<object>_<uuid>
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION
------------------------------------------------------------------

# [VECTOR]PLANE
## IDENTITY
### DEFINITION
- Description : Regroupement de trois vecteurs homogènes qui structurent une partie de la fractale.
- Question (création) : Quels trois vecteurs dois-je réunir pour constituer ce plan ?
### RULE
- Example : Le plane externe d’un projet est composé de Identity, View et Context.
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION


# [PLANE]PLANESET 
## IDENTITY
### DEFINITION
- Description : Collection structurée de vecteurs regroupés en plans. Un PlaneSet peut être global (association externe + interne), primaire (un plan homogène de trois vecteurs), ou transversal (croisement interne/externe).
- Question (création) : Quel type de PlaneSet (global, primaire, transversal) dois-je créer, et quels vecteurs ou plans dois-je y associer ?
### RULE
- question : optionlist
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION


# [PLANESET]GLOBALPLANESET 
## IDENTITY
### DEFINITION
- Description : Association structurante des deux plans fondamentaux d’une fractale — le plan externe (Identity–View–Context) et le plan interne (Definition–Rule–Option). Il constitue la base matricielle de tout objet fractal.
- Question (création) : Quels trois vecteurs issus du croisement interne/externe dois-je réunir pour former ce plan transversal ?
### RULE
- Structure : le bundle de plans doit contenir 2 objets de type [TRANSVERSALPLANESET] 
- Example : Le GlobalPlaneSet d’un projet combine le plan externe IVC et le plan interne DRO pour former sa structure de base.
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION


# [PLANESET]TRANSVERSALPLANESET 
## IDENTITY
### DEFINITION
- Description : Ensemble de trois vecteurs issus du croisement d’un plane interne et d’un plane externe.
- Question (création) : Quels trois vecteurs issus du croisement interne/externe dois-je réunir pour former ce plan transversal ?
### RULE
- structure : le bundle de plans doit contenir 2 objets de type [TRANSVERSALPLANESET] 
- Example : IdentityDefinition, ViewRule et ContextOption constituent un TransversalPlaneSet
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION

# [PLANESET]PRIMARYPLANESET 
## IDENTITY
### DEFINITION
- Description : Ensemble de trois vecteurs formant un plan homogène, interne (Definition–Rule–Option) ou externe (Identity–View–Context).
- Question (création) : Quels trois vecteurs homogènes dois-je associer pour constituer ce plane ?
### RULE
- structure : le bundle de plans doit contenir 3 objets de type [PRIMARYPLANESET] 
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION


# [PLANESET]IVC
## IDENTITY
### DEFINITION
### RULE
- structure : comporte obligatoirement les objets [IDENTITY] [VIEW] [CONTEXT]
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION
------------------------------------------------------------------

# [PLANESET]DRO
## IDENTITY
### DEFINITION
### RULE
- structure : comporte obligatoirement les objets [DEFINITION] [RULE] [OPTION]
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION
------------------------------------------------------------------

# [PLANE]TRANSVERSALPLANE 
## IDENTITY
### DEFINITION
- Description :  intersection d’un axe interne et d’un axe externe, il précise l’objet à la fois par sa nature et par ses règles
queustion : «Que devient cet objet quand on croise ce qu’il est avec comment il est gouverné ? »
### RULE
contient obligatoirement les objets de type  [IDENTITY] [VIEW] [CONTEXT]
### OPTION
- Example : Un article possède une Identity Definition : son identifiant unique est défini par un schéma obligatoire.
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION

# [PLANE]EXTERNALPLANE 
## IDENTITY
### DEFINITION
- Description :  regroupe les éléments qui définissent l’objet en lui-même (son identité, la manière dont il se présente et le contexte immédiat de son existence)
- Question : Qu’est-ce que cet objet est, montre et situe ?
### RULE
contient obligatoirement les objets de type  [IDENTITY] [VIEW] [CONTEXT]
### OPTION
- Example : Un article est identifié par son titre, affiché en page web et situé dans une catégorie.
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION

# [PLANE]INTERNALPLANE 
## IDENTITY
### DEFINITION
- Description : regroupe les éléments qui gouvernent le fonctionnement de l’objet (ses définitions formelles, ses règles de validité et les options qui orientent son usage)
- Question : « Comment cet objet est défini, contrôlé et modulé ? 
### RULE
contient obligatoirement les objets de type  [DEFINITION] [RULE] [OPTION]
### OPTION
- Example : Un article est défini par un schéma, soumis à la règle d’avoir un auteur et peut activer ou non les commentaires
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION



# [PLANE]DIMENSION
## IDENTITY
### DEFINITION
- Description : Élément constitutif d’un plane, chaque dimension décrit un aspect unique mais incomplet de l’objet.
- Question (création) : Quelle dimension dois-je ajouter pour définir ce plan ?
### RULE
- Example : Identity est une dimension : elle identifie l’objet, mais il faut encore View et Context pour compléter le plane.
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION
------------------------------------------------------------------

# [DIMENSION]IDENTITY 
## IDENTITY
### DEFINITION
Ce qui constitue l’identité d’un objet (ident, nom, clés primaires/secondaires, version, owner, scope) et la sémantique associée (unicité, stabilité, lisibilité).
a obligatoirement un [MODE]
### RULE
contient obligatoirement un objet 
Contient description, question, 
template_path : - peut etre null [AUTOMATION][GENERATION] 


### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT


# [DIMENSION]VIEW 
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


# [DIMENSION]CONTEXT
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

# [DIMENSION]DEFINITION
## IDENTITY
#### DEFINITION 

### RULE
ne doit pas etre vide
doit etre multiloingue
format lang : string
### OPTION
[OPTION]IDENTITYOPTION
## VIEW
### DEFINITION 
### RULE
### OPTION
## CONTEXT
### DEFINITION 
### RULE
### OPTION


# [DIMENSION]RULE 
## IDENTITY
### DEFINITION

### RULE
structure : structure, schema, example, format, conditional
### OPTION
## VIEW
### DEFINITION

### RULE

### OPTION
## CONTEXT
### DEFINITION

### RULE

### OPTION

## [PLANE]OPTION
### IDENTITY
#### DEFINITION

#### RULE
#### OPTION
### VIEW
#### DEFINITION

#### RULE

#### OPTION
### CONTEXT
#### DEFINITION

#### RULE

#### OPTION

##### OPTION


# [DIMENSION]OPTION 
## IDENTITY
### DEFINITION
Ce qui constitue l’identité d’un objet (ident, nom, clés primaires/secondaires, version, owner, scope) et la sémantique associée (unicité, stabilité, lisibilité).
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


# [PLANE]IDENTITYDEFINITION
bundle des réponses selon external/internal

# [PLANE]IDENTITYRULE
bundle des réponses selon external/internal

# [PLANE]IDENTITYOPTION
bundle des réponses selon external/internal


# [PLANE]VIEWDEFINITION
bundle des réponses selon external/internal


# [PLANE]VIEWRULE
bundle des réponses selon external/internal


# [PLANE]VIEWOPTION
bundle des réponses selon external/internal


# [PLANE]CONTEXTDEFINITION
bundle des réponses selon external/internal


# [PLANE]CONTEXTRULE
bundle des réponses selon external/internal


# [PLANE]CONTEXTOPTION
bundle des réponses selon external/internal


# 