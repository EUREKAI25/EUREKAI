
tout est objet
les ojets sont définis au format une classe
pas de classe autre qu'objet
les vecteurs objets passifs désignent tous une instance de méthode exécutée (<method>.<object>.<bundleparams>)
toutes les methodes sont réduites au ppcm (factorisation)

# TYPE | [ABSTRACT]
# SCHEMA
depends_on [TYPE]
attributelist = vecteurattributelist = list.attribute.<self>
methodlist = vecteurmethodlist = list.attribute.<self>

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



# OBJECT
# [OBJECT]PASSIVEOBJECT
Passif : porte des données et des règles mais n’initie aucune action (ex. type, spec, catalogue d’objets).
RULES : PRECONDS, POSTCONDS pré à la définition (cohérence, unicité), post = invariants du type.
# [OBJECT]REACTIVEOBJECT
Réactif : transforme ou réagit à des entrées/événements pour produire un résultat sans modifier d’état global (idéalement pur)
RULES : pré (validité des entrées, dépendances résolues), post (conformité du vecteur produit, ordre, unicité, provenance) - IDEMPOTENT
Récursion bien fondée (réactif) : elle s’appelle elle-même en diminuant un paramètre (ou en progressant vers un cas de base). C’est OK si : cas de base garanti, pas d’effets de bord, et memoization possible.
# [OBJECT]ACTIVEOBJECT
 : initie des effets (écritures, changements de statut, envoi réseau, incrément) — c’est la seule catégorie autorisée à avoir des effets de bord.
 Actif : pré (droit/condition d’agir, lock, version), post (état modifié comme attendu, idempotence opérationnelle si requise


fractal
definitionrule :
ordre unicité, cardinalité, nullempty, purity IDEMPPOTENT
method rule : precnds, postcnds
un élément de niveau N ne peut dépendre que d’éléments de niveaux ≤ N, 

# RULE 
# [RULE]CONDITIONALRULE 
schema si method : preconditions, postcondition
# CONDITION
# [CONDITION]PRECONDITION
# [CONDITION]POSTCONDITION

method globale is_ si methode bool, list si methode render, execute / status