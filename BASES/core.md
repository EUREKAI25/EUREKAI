# [OBJECT]TYPE
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


# [OBJECT]METACLASS
## IDENTITY
### DEFINITION
description : objet qui définit les règles de tout le système et porte les methodes centrales
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
# [OBJECT]METAMETACLASS
ndle scope, any par défaut

# [OBJECT]ATTRIBUTE <!-- les enfants de attributes ont pr caractéristique d'être des tags de -->
Caractéristique attachée à un élément du DOM (paire nom/valeur) décrivant son identité, son rôle ou son comportement.

# [ATTRIBUTE]CLASSATTRIBUTE
Représente la/les classes CSS associées à un élément (liste de jetons utilisable pour le style et les sélecteurs).

# [ATTRIBUTE]IDATTRIBUTE
Identifiant unique d’un élément dans le document (usage : ancre, ciblage JS/CSS).

# [ATTRIBUTE]DATAATTRIBUTE
Famille d’attributs personnalisés préfixés `data-` pour stocker des métadonnées applicatives (ex. `data-user-id`).

# [ATTRIBUTE]ARIAATTRIBUTE
Famille d’attributs d’accessibilité préfixés `aria-` pour transmettre rôles/états aux technologies d’assistance (ex. `aria-label`).

# [ATTRIBUTE]EVENTHANDLERATTRIBUTE
Attributs gestionnaires d’événements préfixés `on` qui lient du code à des événements (ex. `onclick`, `oninput`).

# [ATTRIBUTE]BOOLEANATTRIBUTE
Attributs dont la **présence** seule active une fonctionnalité (ex. `disabled`, `checked`, `hidden`).

# [ATTRIBUTE]URLATTRIBUTE
Attributs contenant une URL/référence vers une ressource ou une destination (ex. `href`, `src`, `action`).

# [ATTRIBUTE]FORMATTRIBUTE
Attributs liés aux formulaires et contrôles de saisie (ex. `name`, `value`, `placeholder`, `required`).

# [ATTRIBUTE]I18NATTRIBUTE
Attributs d’internationalisation et de direction du texte (ex. `lang`, `dir`).

# [ATTRIBUTE]INTERACTIVITYATTRIBUTE
Attributs influençant le focus, l’édition et le drag & drop (ex. `tabindex`, `contenteditable`, `draggable`).
# [ATTRIBUTE]RELATIONS

# [ATTRIBUTE]MODE | [BUNDLE]
## IDENTITY
### DEFINITION

### RULE
forcément un bundle [MODEBUNDLE]
forcément un des trois actif / passif reactif
### OPTION
## VIEW
### DEFINITION
### RULE
### OPTION
## CONTEXT
### DEFINITION
### RULE
### OPTION
# [ATTRIBUTE]NATURE | [BUNDLE]
<!-- TAG -->

# [OBJECTATTRIBUTE]REQUIREDATTRIBUTE
depends_on [SCHEMA] many to one
# [METHOD]REQUIREDMETHOD
depends_on [SCHEMA] many to one
# [ATTRIBUTE]OBJECTATTRIBUTE
is. meta
# [OBJECTATTRIBUTE][IDENTITYDEFINITIONATTRIBUTE]

# [OBJECTATTRIBUTE]BUNDLE
bundle is data, 
transversals : format (list/dict)
# [BUNDLE]ATTRIBUTEBUNDLE
# [BUNDLE]METHODBUNDLE
# [BUNDLE]RULEBUNDLE
# [BUNDLE]RELATIONSBUNDLE
# [BUNDLE]LIFECYCLEBUNDLE

# LABEL
# META
# DATA

#