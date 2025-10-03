# ORGANISATION
## tout passe par des fonctions centrales GET / EXECUTE / VALIDATE / RENDER
### tous les objets du scope des fonctions centrales portent en eux les méthodes secondaires permettant d'activer les méthdes primaires (fonctions centrales du système)
### toutes les fonctions centrales sont capables de recevoir ou de générer n'importe quel format
les methodes get et render ont dans leur step validation la conversion du format selon
## Tout est objet

## Héritage
Les objets récupèrent naturellement tous les attributs et méthodes des objets parents, des classes transversales ou injectés via la méthode d'injection de metametaclass
### MetaMetaClass et schemas
MetaMetaClass détient les méthodes dynamiques et agnostiques capables de s'adapter à tout objet
C'est elle qui crée les metaclasses, les schemas
### metaobjets
types de statuts possibles selon classes héritéese et transversales  (auto metametaclass) 

### MetaMetaClass et injections
### Transversales selon scope
### Catégories et tags

# DATABASE
## Base de données RDF - triplets
### autants de tables relations que de types de relations
### tables : objects (id), relation_*, labels 

# OBJECT
## Objet informé et autonome
Grâce à son vecteur, chaque objet dispose dans ses attributs de la liste des methodes possibles (capabilities), de ses règles de validation_rules, creation_rules, execution_rules, render_rules. ON a aussi family : parent, children, siblings
## OBJECT active / passive 
# API
## Internes
Toutes les méthodes sont des endpoints potentiels. On les appelle par le schéma api/v1/object_<method>?params=<params>&token=<vecteurtoken>
ou api/<vecteurapi>, vecteurapi intégrant le token user. la première route ne serait qu'un sas ?
## Externes
Toutes les API externes sont enregistrées dans le système et mappées pour être ccédées via une api interne par le schéma api/v1/<vecteurapi>, vecteurapi intégrant le token admin + les params d'appel api ?
# FUNCTION
### function = method = scenario
toute fonction est méthode d'un objet, de type scenario
tout scenario s'exécute par structure loop sur chacune de ses étapes GET / EXECUTE / VALIDATE / RENDER, ces étapes étant exécutées par l'intermédiaires de méthodes secondaires qui les appellent
## comportement des fonctions
chaque fonction est réduite à sa plus petite action
metafunction impose une méthode unique dynamique et agnostique pour exécuter toute fonction selon son type (linear, conditional etc)
# TEMPLATE
## function
### règles : une fonction = un fichier
# CATALOG
# TAGS NON EXCLUSIFS
# CATEGORIES (< tag)
relative / absolute : catalog
active - passive - reactive : object 
executor, screator, trategist, decidor, external : user, agent
conversion : temporal_conversion, text_conversion 
validation :validation_rules, creation_rules, execution_rules, render_rules 
# TRANSVERSALES (< method)
structural : matrix, vector, grid, hierarchical...
conceptual: time, space, geolocalisation
logical : linear / conditional 
# FORMATS
Toute fonction de catégorie conversion a les attributs input_formats (list) et output_formats (list)

Formats 
les répartir en catégories (texte, technique, temporel)
# RESOURCES
Agents : à partir de executor, les agents ont à leur disposition la charte, les règles internes, la nomenclature, le metaschema (creator), des howto/readme + éventuellement des docs tuto ou des sources de création