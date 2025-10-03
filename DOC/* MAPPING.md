# 1. Introduction
Le mapping désigne la correspondance systématique entre les objets internes de l’agence et les éléments externes (DOM, API, bases de données, fichiers, etc.).  
Son objectif est double : assurer la réutilisabilité des objets dans tout contexte, et garantir la cohérence fractale de leurs représentations.  
Chaque élément récupéré (ex. un nœud HTML, une entrée API, un champ de base de données) est normalisé dans un format propriétaire, basé sur identité, vue, contexte enrichis de définitions, règles et options.

# 2. Rôle du mapping
## 2.1 Normalisation
Le mapping transforme toute donnée hétérogène en un objet fractal standard.  
Cela permet aux scénarios et catalogues de fonctionner sans dépendre du format source.  
Exemple : une balise `<div>` HTML est enregistrée comme un objet `Element` avec ses propriétés (id, classes, styles, contenu).

## 2.2 Réutilisation
Un objet mappé peut être réinjecté dans n’importe quel projet, indépendamment de son origine.  
La logique fractale garantit que l’élément conserve ses règles et options, quel que soit le contexte.

## 2.3 Auditabilité
Chaque correspondance est enregistrée dans les catalogues.  
Cela assure une traçabilité complète : origine, transformations appliquées, destination, version.

# 3. Typologie des mappings
## 3.1 Mapping structurel
Correspondance des éléments hiérarchiques (DOM → objets, JSON → catalogues, tables → entités).  
Chaque élément est transformé en objet fractal avec ses relations natives.

## 3.2 Mapping fonctionnel
Correspondance des comportements (fonctions → scénarios, méthodes API → boucles fractales).  
Chaque action est encapsulée en scénario universel avec get → execute → validate → render.

## 3.3 Mapping contextuel
Correspondance dépendante d’un environnement ou d’une contrainte.  
Exemples :  
- mapping responsive (desktop → mobile),  
- mapping de sécurité (RGPD → anonymisation),  
- mapping linguistique (texte source → traduction normalisée).

# 4. Processus de mapping
## 4.1 Collecte
Extraction des éléments sources (DOM, API, BDD, fichiers).  
Outils utilisés : parsers HTML, introspection API, introspection SQL/NoSQL.

## 4.2 Transformation
Conversion en fractale : identité (nom, type, relations), vue (forme rendue), contexte (conditions d’usage).  
Chaque transformation est documentée et versionnée.

## 4.3 Injection
Intégration dans les catalogues avec identifiant unique.  
Les objets deviennent alors disponibles pour les scénarios, agents et produits.

# 5. Outils et catalogues associés
- **catalog_mapping.json** : conserve les schémas de correspondance.  
- **catalog_objects.json** : reçoit les objets transformés.  
- **catalog_relations.json** : enregistre les liens entre objets mappés.  
- **scenarios_mapping/** : bibliothèque de scénarios dédiés au traitement et à la normalisation.

# 6. Cas d’usage
## 6.1 Recyclage d’éléments web
Un formulaire d’inscription d’un site A est mappé et intégré dans un projet B, avec ses règles de validation intactes.  

## 6.2 Migration de données
Des tables SQL sont converties en objets fractals, puis réinjectées dans MongoDB sans perte de cohérence.  

## 6.3 Intégration API
Un endpoint externe est mappé en scénario interne avec vecteurs standardisés, ce qui permet de remplacer l’API sans changer le reste du système.  

# 7. Perspectives d’évolution
- **Mapping intelligent** : IA pour proposer automatiquement les correspondances probables.  
- **Mapping rétroactif** : comparer les évolutions d’un même objet au fil du temps.  
- **Mapping multi-projets** : partager un même mapping validé entre différents projets clients.  