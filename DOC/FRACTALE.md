# 1. Définitions
## 1.1 Identité
<!-- 
Essence de l’objet : ce qu’il est de manière intrinsèque, indépendante de toute circonstance.
Inclut : nom canonique, description stable, nature fondamentale, relations natives (ex. child_of).
Règles :
- Toujours présent (socle incompressible).
- Doit refléter la stabilité ontologique (jamais dépendant d’un contexte).
- Les enfants ne vivent pas ici → ils deviennent eux-mêmes des fractales autonomes, reliées par child_of.
-->

## 1.2 Vue
<!-- 
Forme manifeste de l’objet : comment il se présente, se matérialise ou se projette.
Inclut : livrables, apparences, représentations, variantes de rendu.
Règles :
- Ne doit contenir que des expressions visibles ou perceptibles de l’objet.
- Ne jamais y placer des éléments structurels (enfants, parties internes).
- Peut contenir plusieurs variantes de rendu (via Options).
-->

## 1.3 Contexte
<!-- 
Conditions d’existence et d’usage de l’objet : environnement, interactions, temporalité.
Inclut : paramètres runtime, influences externes, situations d’activation.
Règles :
- Tout ce qui varie selon l’environnement va ici.
- Ne jamais y placer d’éléments invariants ou identitaires.
- Sert de médiateur entre Identité (ce que c’est) et Vue (comment ça se manifeste).
-->

# 2. Règles
## 2.1 Identité
<!-- 
Contraintes invariantes liées à l’essence de l’objet.
Exemples : unicité, compatibilité, intégrité, normes ontologiques.
Règles :
- Protège la cohérence interne de l’objet.
- Ne doit jamais être conditionnée par l’extérieur.
-->

## 2.2 Vue
<!-- 
Contraintes liées à la qualité et à la validité des manifestations.
Exemples : accessibilité, performance, respect de formats.
Règles :
- Toute Vue doit satisfaire ses Règles pour être valide.
- Ne pas confondre avec des contraintes contextuelles (elles vont en 2.3).
-->

## 2.3 Contexte
<!-- 
Contraintes d’adaptation : conditions qui régissent la relation objet ↔ environnement.
Exemples : « si mobile → choisir la variante statique », « si RGPD → anonymiser ».
Règles :
- Ne pas modifier l’essence de l’objet (Identité).
- Ne pas définir les livrables eux-mêmes (Vue).
- Servent uniquement à orienter l’adaptation.
-->

# 3. Options
## 3.1 Identité
<!-- 
Variantes stables de l’objet : presets, éditions, alias.
Exemples : « version light », « édition premium ».
Règles :
- Options ici = configurations intrinsèques, stables.
- Ne pas y placer de paramètres temporaires.
-->

## 3.2 Vue
<!-- 
Variantes de manifestation : différentes formes d’affichage ou de rendu.
Exemples : clair/sombre, vue complète/vue réduite, format PDF/HTML.
Règles :
- Options limitées aux apparences et livrables.
- Ne pas y placer de conditions d’usage (ça appartient au Contexte).
-->

## 3.3 Contexte
<!-- 
Paramètres d’adaptation dynamiques : variables runtime et signaux externes.
Exemples : device, marché, langue, featureFlags.
Règles :
- Appliquer la règle du 20/80 pour éviter la surcharge.
- Poser TTL (time-to-live) : les options expirées doivent être revues ou purgées.
- Ne jamais y stocker d’enfants ou de structures stables.
-->