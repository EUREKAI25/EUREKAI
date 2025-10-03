# 1. Définitions
<!-- 
Cette partie décrit l'essence de l'objet.
On y trouve les définitions canoniques, stables et non contextuelles.
Règles :
- Toujours remplir (jamais laisser vide).
- Ne pas stocker ici de données runtime.
- Les enfants ne sont PAS listés ici en détail → chaque enfant est un objet fractal autonome.
- Les relations (dont child_of) sont déclarées ici, sous Identité–Relations.
-->

## 1.1 Identité
<!-- 
Contenu attendu :
- Nom canonique de l'objet.
- Description stable (essence).
- Relations natives (ex : child_of, inherits_from, related_to).
- Taxonomie (type, sous-type).
Règles :
- child_of : un seul parent par objet.
- Les alias peuvent être définis, mais doivent pointer vers leur type.
- Ne jamais stocker ici de données de contexte ou de variantes de rendu.
-->
<!-- Description de l’agence, de ses objets fondamentaux, de ses catalogues initiaux et de ses méta-objets. -->

## 1.2 Vue
<!-- 
Contenu attendu :
- Image / Forme / Manifestation de l'objet (le terme peut varier : Vue, Formes, Manifestations…).
- Livrables attendus (schéma, fichier, rendu visuel…).
- Variantes possibles de rendu.
Règles :
- Uniquement ce qui concerne le rendu ou l'expression externe.
- Ne pas mélanger ici les enfants (ils vivent comme fractales autonomes).
- Toute variante de sortie va dans Vue–Options.
-->
<!-- Image globale de l’agence : scénarios, organes vitaux, livrables et représentations fractales.-->

## 1.3 Contexte
<!-- 
Contenu attendu :
- Champ d’action et conditions d’usage.
- Marché, environnement technique, client, device, contraintes externes.
Règles :
- Ce qui dépend du temps, de la situation, de l’environnement.
- Pas de définition canonique ici.
- Pas d’enfants ni de structures stables.
-->
<!-- Champ d’action de l’agence : marché, clients, environnement technique et culturel. -->

# 2. Règles
<!-- 
Cette partie fixe les contraintes et garde-fous.
Elles assurent la cohérence de la fractale et évitent les engorgements.
-->

## 2.1 Identité
<!-- 
Contenu attendu :
- Contraintes invariantes de l'objet (unicité, licence, namespace, sécurité).
Règles :
- Toujours vérifier l’intégrité de l’identité.
- Ne pas mettre de règles dépendantes du contexte.
-->
<!-- Normes éthiques, unicité des objets, cohérence de la gouvernance et de la nomenclature. -->

## 2.2 Vue
<!-- 
Contenu attendu :
- Contraintes de rendu : accessibilité, performance, tests, validations.
Règles :
- Chaque variante doit passer ses règles de sortie.
- Ne pas inclure de règles contextuelles ici.
-->
<!-- Conventions de représentation : schémas fractals, étapes des scénarios, validation obligatoire. -->

## 2.3 Contexte
<!-- 
Contenu attendu :
- Contraintes d’adaptation : « si mobile → variante X », « si RGPD → anonymiser ».
Règles :
- Les règles de contexte doivent s’appuyer sur des paramètres explicites.
- Elles ne doivent jamais redéfinir l’identité.
-->
<!-- Contraintes externes : légales, techniques, culturelles et interopérabilité avec l’écosystème. -->

# 3. Options
<!-- 
Cette partie regroupe les alternatives et variantes.
Elles servent à donner de la souplesse sans engorger l’identité ou le contexte.
-->

## 3.1 Identité
<!-- 
Contenu attendu :
- Presets canoniques, éditions stables, alias.
Règles :
- Ne pas y mettre d’options temporaires.
- Options ici = configurations de base, non runtime.
-->
<!-- Variantes possibles des objets, déclinaisons de rôles, choix de structures alternatives. -->

## 3.2 Vue
<!-- 
Contenu attendu :
- Variantes de rendu ou d’affichage (ex : thème clair/sombre, layout A/B).
Règles :
- Doit rester limité aux apparences ou livrables.
- Ne pas stocker de paramètres de contexte.
-->
<!-- Modes d’affichage ou de rendu (vues réduites, complètes, agrégées, comparatives). -->

## 3.3 Contexte
<!-- 
Contenu attendu :
- Paramètres runtime : device, marché, featureFlags, inputs variables.
Règles :
- Appliquer la règle du 20/80 (ne garder que les 20% qui expliquent 80% des variations).
- Poser TTL (time-to-live) : les options expirées doivent être revues ou purgées.
- Ne jamais y stocker de structures stables ni d’enfants.
-->
<!-- Adaptations aux environnements, aux clients, aux projets et aux scénarios particuliers. -->
