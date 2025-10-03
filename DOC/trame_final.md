# TRAME ZORBEC
# Définitions
## Identité
### AGENCE <!-- SECTION:AGENCE -->

#### Définitions (identité)
remanier scenarios
moteur de methodes : passer en catalogue
agents / entity / equipes
Présence sur les réseaux

reprendre toute la doc : chaque rubrique doit correspondre à objet - règle, objet - description, objet - schema, objet - example.
et aussi comportements / relations avec autres objets
Normalement, ça couvre tout ce qu'il y a à créer
faire lire à claude : manque t'il des infos ? y a t'il des incohérences ?  A/R chatgpt pour finaliser la doc
peut-on remplir un json complet avec tout ce qui concerne chaque objet ? (on doit pouvoir identifier ce qui est lié aux méthodes de classes transversales et aux injections)
=> doc sous forme de objet et elements

#### Règles (identité)
<!-- à remplir -->
#### Options (identité)
<!-- à remplir -->
### AGENCE FRACTALE <!-- SECTION:AGENCE FRACTALE -->

#### Définitions (identité)
<!-- 
Contenu attendu :
- Paramètres runtime : device, marché, featureFlags, inputs variables.
Règles :
- Appliquer la règle du 20/80 (ne garder que les 20% qui expliquent 80% des variations).
- Poser TTL (time-to-live) : les options expirées doivent être revues ou purgées.
- Ne jamais y stocker de structures stables ni d’enfants.
-->
<!-- Adaptations aux environnements, aux clients, aux projets et aux scénarios particuliers. -->

#### Règles (identité)
<!-- à remplir -->
#### Options (identité)
<!-- à remplir -->
### AGENCE2 <!-- SECTION:AGENCE2 -->

#### Définitions (identité)
remanier scenarios
moteur de methodes : passer en catalogue
agents / entity / equipes
Présence sur les réseaux

reprendre toute la doc : chaque rubrique doit correspondre à objet - règle, objet - description, objet - schema, objet - example.
et aussi comportements / relations avec autres objets
Normalement, ça couvre tout ce qu'il y a à créer
faire lire à claude : manque t'il des infos ? y a t'il des incohérences ?  A/R chatgpt pour finaliser la doc
peut-on remplir un json complet avec tout ce qui concerne chaque objet ? (on doit pouvoir identifier ce qui est lié aux méthodes de classes transversales et aux injections)
=> doc sous forme de objet et elements

#### Règles (identité)
<!-- à remplir -->
#### Options (identité)
<!-- à remplir -->
### AGENTS <!-- SECTION:AGENTS -->

#### Définitions (identité)
Le système intégrera un laboratoire vivant, espace où de nouvelles approches, outils et comportements d’agents pourront être testés en conditions contrôlées. Ce labo sera également chargé  de la veille technologique et marketing, jouant un rôle de vigie pour l’agence en anticipant les tendances, en identifiant les innovations et en guidant l’évolution des scénarios. Il offrira la possibilité de simuler des stratégies, d’expérimenter des méthodes inédites et d’évaluer leurs impacts avant une mise en production. Il sera ainsi le moteur de l’adaptation continue et du positionnement stratégique de l’agence.

#### Règles (identité)
<!-- à remplir -->
#### Options (identité)
<!-- à remplir -->
### CATALOGUES <!-- SECTION:CATALOGUES -->

#### Définitions (identité)
Les catalogues trouvent leur utilité dans plusieurs situations concrètes :
- Centraliser des définitions communes et éviter les redondances, par exemple un champ identity.name utilisé dans de nombreux modules et projets
- Permettre la navigation dans la matrice relationnelle, en suivant les liens label_of ou related_to
- Générer des vues adaptées selon le profil (relatif par défaut, absolu pour l’exécution ou l’audit)
- Rejouer des états passés pour l’audit ou la traçabilité
- Servir de base pour l’export et l’interopérabilité avec d’autres systèmes
En pratique, les cas d’usage illustrent pourquoi les catalogues sont un composant central du système, garantissant à la fois cohérence, performance et traçabilité.

#### Règles (identité)
<!-- à remplir -->
#### Options (identité)
<!-- à remplir -->
### ENTITIES <!-- SECTION:ENTITIES -->

#### Définitions (identité)
<!-- à remplir -->
#### Règles (identité)
<!-- à remplir -->
#### Options (identité)
<!-- à remplir -->
### ETHIQUE <!-- SECTION:ETHIQUE -->
#### Définitions (identité)
##### Principes
Transparence, respect des personnes, responsabilité, non-manipulation. L’éthique est un cadre appliqué à toutes les décisions, prompts, scénarios et rendus.
##### Intégration opérationnelle
La charte éthique est encodée dans des règles héritées. Les steps validate rejettent automatiquement ce qui viole le cadre. Les agents sont contraints par brief, permissions et validations contextuelles.
##### Audit et traçabilité
Les décisions sensibles sont journalisées avec justification, alternatives et impacts. Des agents externes auditent périodiquement la conformité et émettent des recommandations.
##### Amélioration continue
La charte évolue par retours, veille et incidents. Les changements sont versionnés et rétro-testés.
data_governance, transparence, engagement
#### Règles (identité)
- Règle 1 (ETHIQUE) : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
#### Options (identité)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### EXTENSION <!-- SECTION:EXTENSION2 -->
#### Définitions (identité)
##### Objet
Mécanisme de plug-ins internes: ajout/remplacement de capacités sans modifier le cœur (API internes, adaptateurs, hooks)..
##### Portée
S’applique à l’agence et à tous les projets dérivés. Intégré aux catalogues, scénarios et contrôles.
##### Notes source
le constitue la première brique fonctionnelle et reste activable/désactivable via configuration API  
##### Fonctionnalité complémentaire — Gestion avancée du copier-coller
Rétention et purge  
L’historique conserve les éléments pendant 24h glissantes. Les éléments marqués comme épinglés ne sont jamais purgés. L’épinglage est automatique pour tout élément auquel un raccourci clavier est attribué. La suppression intervient uniquement sur les éléments non épinglés au-delà de 24h ou sur action manuelle.
##### Raccourcis clavier  
L’extension expose des slots de raccourcis prédéclarés (ex. Alt+Shift+1..9, Alt+Shift+A..L). L’utilisateur assigne un élément à un slot depuis l’interface. Tant qu’un slot est attribué, l’élément est épinglé et exclu de la purge. Le désassigner retire l’épingle et rend l’élément à la rétention 24h. Un raccourci global peut ouvrir une palette rapide pour sélectionner et coller un élément de l’historique.
##### Insertion et comportements  
Sur activation d’un raccourci, l’extension tente d’insérer directement dans le champ actif. Si l’insertion directe n’est pas possible, l’élément est copié dans le presse-papiers et une notification invite à coller. Les éléments peuvent être du texte, des extraits HTML sûrs ou des snippets de commande (affichés avant insertion).
##### Interface de gestion  
Une vue dédiée (popup ou side panel) liste l’historique, les épinglés, les slots de raccourcis, la recherche et les tags. Depuis cette vue, l’utilisateur peut épingler, désépingler, renommer, tagger, attribuer ou retirer un raccourci.
##### Sécurité et confidentialité  
Stockage local chiffré. Aucune synchronisation distante par défaut. Les champs sensibles peuvent être marqués pour exclusion de l’historique. Les actions sont journalisées de manière minimale pour diagnostic local.
##### Paramétrage  
Options de limites (nombre d’éléments non épinglés), formats autorisés (texte, HTML sûr), domaines où l’insertion est autorisée, et choix de la surface d’interface (popup ou side panel).
#### Règles (identité)
##### Exigences
- Unicité de la nomenclature et traçabilité par identifiant.
- Validation automatique (get → execute → validate → render).
- Journalisation et versioning sémantique.
- Sécurité by design (permissions, secrets, conformité).
##### Conformité
Règles intégrées aux tests CI/CD; tout échec bloque la mise en production.
##### Standardisation des appels
Cycle get → execute → validate → render; journalisation obligatoire.
#### Options (identité)
##### Variantes
- Niveaux d’activation: off, basic, strict.
- Paramètres par projet via catalogues.
- Intégration progressive (feature flags).
##### Perspectives
- CI/CD avancé
- Packaging exécutable
- Durcissement sécurité
### FRACTALE <!-- SECTION:FRACTALE -->
#### Définitions (identité)
Options.
Paramètres activables pour « 3. Options » : seuils, variantes, stratégies alternatives et modes de dégradation contrôlée. Toute option doit être documentée et testée.
#### Règles (identité)
<!-- à remplir -->
#### Options (identité)
<!-- à remplir -->
### HEBERGEMENT <!-- SECTION:HEBERGEMENT -->
#### Définitions (identité)
##### Introduction
L’hébergement fournit l’infrastructure modulaire, sécurisée et scalable qui supporte l’agence, le labo et chaque client. Le modèle retenu repose sur des cubes isolés (agence, labo, un cube par client), chacun contenant des conteneurs par projet. L’ensemble s’exécute prioritairement sur Yunos Cloud, sans dépendance forte à un fournisseur.
##### Architecture par cubes et conteneurs
Chaque cube est un périmètre d’isolation réseau, stockage, secrets et monitoring. À l’intérieur, chaque projet tourne dans un conteneur distinct, avec son stockage dédié, ses clés et son réseau virtuel. Cette granularité permet mises à jour indépendantes, rollbacks rapides, et migrations sans interruption.
##### Sécurité, sauvegardes et supervision
Le chiffrement est appliqué en transit et au repos, avec des coffres de secrets par cube. Les sauvegardes sont différentielles avec tests de restauration réguliers. Les métriques (latence, erreurs, saturation) et journaux sont centralisés, avec alertes sur seuils et anomalies comportementales.
##### Scalabilité et portabilité
Le scale-out se fait par réplication de conteneurs et extension horizontale de cubes. La portabilité est assurée par des manifests d’infrastructure déclaratifs, garantissant des déploiements reproductibles sur d’autres clouds ou on-premise.
##### Objectifs de l’hébergement
##### Modularité et adaptabilité
##### Infrastructure de base
###### Localisation principale (Yunos Cloud)
###### Définition des cubes de serveurs
###### Séparation agence, clients et labo
##### Organisation par cube
###### Cube agence
###### Cube labo
###### Cube client
###### Gestion multi-projets par Docker
##### Sécurité et isolation
###### Cloisonnement des données
###### Sécurisation par défaut
###### Gestion des accès et permissions
##### Gestion des données
###### Stockage et sauvegardes
###### Chiffrement
###### Conformité et auditabilité
##### Scalabilité et optimisation
###### Adaptation dynamique de la charge
###### Ajout de nouveaux cubes
###### Monitoring des performances
##### Administration et maintenance
###### Automatisation des déploiements
###### Gestion des mises à jour
###### Supervision et alertes
##### Perspectives d’évolution
###### Multi-cloud et redondance
###### Optimisation coûts/performances
###### Intégration avec la logique fractale
#### Règles (identité)
- Règle 1 (HEBERGEMENT) : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
#### Options (identité)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### IA <!-- SECTION:IA -->
#### Définitions (identité)
##### Introduction
Présentation du rôle de l’IA dans le système, son articulation avec les agents et son intégration fractale.
##### Modèles d’IA
###### Typologie des modèles utilisés
###### Gestion multi-modèles et spécialisation
###### Stratégies de sélection et fallback
###### Versionning et compatibilité des modèles
##### Prompts
###### Définition et rôle des prompts
###### Structure fractale des prompts (identité, contexte, vue, vecteur secondaire)
###### Gestion des prompts dans les catalogues
###### Génération automatique et personnalisation
###### Prompts stratégiques, prompts créatifs et prompts techniques
###### Héritage et construction contextuelle des prompts
Les prompts ne sont jamais conçus isolément : ils dérivent d’un métaprompt, défini comme modèle générique. Chaque prompt hérite de ce métaprompt et se spécialise en fonction des spécificités du contexte. Les vecteurs (identité, contexte, vue, enrichis de définition, règles et options) alimentent la construction du prompt. Les missions confiées, les rôles de l’agent, les règles applicables, ainsi que la documentation ou les ressources disponibles, viennent compléter et affiner le contenu. Cette approche garantit que chaque prompt est cohérent, contextualisé et conforme aux contraintes imposées par le système.
##### Exécution et orchestration
###### Appels aux modèles via API internes
###### Normalisation des entrées et sorties
###### Validation des résultats et corrections automatiques
###### Récursivité et enchaînement des prompts
##### Gouvernance et traçabilité
###### Permissions et rôles des agents IA
###### Journalisation des appels et archivage
###### Suivi des performances et métriques
###### Audit des biais et des dérives
##### Optimisation et performance
###### Mise en cache des résultats
###### Réutilisation des prompts optimisés
###### Ajustement dynamique en fonction du contexte
###### Tests comparatifs et apprentissage continu
##### Perspectives d’évolution
###### IA générative multi-modale
###### Intégration de modèles propriétaires
###### Approfondissement du rôle des prompts
###### Scénarios d’expérimentation et laboratoire
#### Règles (identité)
- Règle 1 (IA) : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
#### Options (identité)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### IN OUT <!-- SECTION:IN OUT -->
#### Définitions (identité)
##### Introduction
###### Dualité entre coulisses et interface
###### Objectif de transparence et de performance
##### Le Labo (coulisses)
###### Recherche et développement
###### Veille stratégique
###### Veille technique
###### Veille marketing
###### Entraînement et adaptation des modèles
###### Production de ressources internes (guides, tutos, datasets)
##### L’Interface (monde extérieur)
###### Blog et documentation publique
###### FAQ et support utilisateur
###### Vitrine temps réel des performances et résultats
###### Stratégies de communication et réseaux sociaux
###### Relations publiques et partenariats
##### Articulation entre Labo et Interface
###### Flux d’information sortants
###### Retour utilisateur comme input stratégique
###### Gouvernance et contrôle de cohérence
##### Perspectives
###### Évolution du rôle du Labo
###### Expansion des canaux d’interface
###### Renforcement de la transparence et de la confiance
#### Règles (identité)
- Règle 1 (IN_OUT) : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
#### Options (identité)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### INITIAL <!-- SECTION:INITIAL -->
#### Définitions (identité)
##### Introduction
###### Objectif du document
###### Rôle fondateur et portée
###### Public concerné (IA, humains, partenaires, investisseurs)
##### Philosophie et charte
###### Principes fondamentaux (humanisme, transparence, éthique)
###### Place de l’IA (outil au service de l’humain, cadre et limites)
###### Vision long terme et engagements
###### Valeurs prioritaires (innovation, stabilité, accessibilité)
##### Choix conceptuels
###### Tout est objet et logique fractale
###### Méta-objets et rôle de MetaMetaclass
###### Full dynamique et récursivité
###### Universalité et adaptabilité
##### Choix techniques
###### Langage principal (Python)
###### Environnement initial (Docker, GitHub, CI/CD)
###### Base de données (MongoDB, RDF, SQL en option)
###### Catalogues et schémas initiaux
###### Ressources de bootstrap (prompts, agents, scénarios)
##### Gouvernance et évolutivité
###### Gestion des versions (règles SemVer adaptées : 1.0.1 / 1.1.0 / 2.0.0)
###### Impact des évolutions sur la structure
###### Compatibilité ascendante et migrations
###### Réversibilité des choix
##### Organisation et responsabilités
###### Rôle des agents IA et des humains
###### Définition des espaces (admin, back-office, client, labo, vitrine)
###### Transparence et auditabilité
##### Sécurité et conformité
###### Permissions et droits d’accès
###### Logs, traçabilité et audit
###### Résilience et sauvegardes
###### Alignement avec les chartes légales et éthiques
##### Adaptabilité et ouverture
###### Multi-bases de données
###### Multi-langages et interopérabilité
###### Multi-agents et intégration de modèles externes
###### Interaction avec l’écosystème (API, extensions, partenaires)
##### Principes économiques et stratégiques
###### Pérennité et scalabilité
###### Optimisation des coûts
###### Modèle d’évolution en réseau
###### Priorité aux projets humanistes
##### Conclusion
##### Synthèse des choix fondateurs
##### Engagements pour les versions futures
##### Importance du respect de ce socle
#### Règles (identité)
- Règle 1 : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
#### Options (identité)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### MATRIX <!-- SECTION:MATRIX -->
#### Définitions (identité)
##### Logique matricielle
Le système est un graphe d’objets reliés par relations typées. La navigation se fait par les triplets, en respectant permissions et contextes.
##### Fractale des objets
Chaque objet possède un vecteur principal (identité, contexte, vue) et un vecteur secondaire (définition, règle, option). Les méthodes de vecteur exposent ces informations de manière uniforme.
##### Vecteur comme langage
Le vecteur est l’interface universelle entre scénarios, agents et données. Il porte les paramètres d’exécution, les options et les règles, évitant toute recherche heuristique.
##### Conséquences
Uniformité d’exécution, auto-documentation et auto-validation, générativité maximale avec un minimum de code spécifique.
plans, vecteurs, fractale, dimensions
#### Règles (identité)
- Règle 1 (MATRIX) : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
#### Options (identité)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### OPTIMISATION<!-- SECTION:OPTIMISATION -->
#### Définitions (identité)
##### Objet
Boucles d’amélioration continue: QA automatisée, A/B tests, analyse de performance/coût/impact..
Définir une syntaxe unique pour décrire objets, vecteurs, scénarios, relations et catalogues, afin d’unifier la lecture/écriture par humains et agents.
##### Conventions
Chemins vectoriels en notation pointée, types explicites, alias normalisés, et schémas JSON de référence. Les mêmes conventions s’appliquent aux prompts et à la documentation.
##### Interopérabilité
Le métalangage se sérialise en JSON/YAML, alimente les API internes et génère les validations. Il évite la divergence entre intention et exécution.
##### Évolution
Versionné, testé et documenté, il s’adapte sans rupture via compatibilité ascendante et dépréciations guidées.
##### Portée
S’applique à l’agence et à tous les projets dérivés. Intégré aux catalogues, scénarios et contrôles.
##### Notes source
##### Zéro bug et performance
Les validations fractales bloquent la propagation d’erreurs. Les budgets de performance sont suivis en continu, avec alertes et remédiations automatiques.
##### QA systématique
Tests unitaires par fonction, intégration par scénario, tests de charge et de non-régression. Les résultats alimentent des catalogues de qualité avec seuils minimaux de sortie.
##### Tests A/B et comparatifs
Les variantes de rendu et de logique sont orchestrées par scénarios. Les métriques déterminent la promotion ou la purge des variantes, avec journal des décisions.
##### Optimisation H24
Des agents d’optimisation surveillent erreurs, latences et coûts, appliquent des correctifs et ouvrent des tickets humains si nécessaire.
100% scalabilité
#### Règles (identité)
##### Exigences
- Unicité de la nomenclature et traçabilité par identifiant.
- Validation automatique (get → execute → validate → render).
- Journalisation et versioning sémantique.
- Sécurité by design (permissions, secrets, conformité).
##### Conformité
Règles intégrées aux tests CI/CD; tout échec bloque la mise en production.
##### Standardisation des appels
Cycle get → execute → validate → render; journalisation obligatoire.
#### Options (identité)
##### Variantes
- Niveaux d’activation: off, basic, strict.
- Paramètres par projet via catalogues.
- Intégration progressive (feature flags).
##### Perspectives
- CI/CD avancé
- Packaging exécutable
- Durcissement sécurité
### PROMPTS <!-- SECTION:PROMPTS -->
#### Définitions (identité)
La charte et les permissions bornent l’espace d’action. Les prompts sensibles exigent validations supplémentaires et recours possible à agents humains.
##### Objet
Gouvernance des prompts: conception, versioning, tests et sûre exploitation par les agents..
##### Portée
S’applique à l’agence et à tous les projets dérivés. Intégré aux catalogues, scénarios et contrôles.
##### Notes source
##### Métaprompt et héritage
Les prompts sont générés à partir d’un métaprompt qui hérite du contexte, des règles et des objectifs. Le métaprompt assemble dynamique des blocs en fonction du vecteur de l’objet ou du scénario.
##### Construction contextuelle
Le prompt inclut mission, rôle, contraintes, données utiles, format attendu et critères de validation. Les options contrôlent le degré de liberté, les ressources autorisées et les bornes de sortie.
##### Journalisation et évaluation
Chaque prompt, entrée et sortie est journalisé avec justification de choix. Les résultats sont évalués par métriques et comparés entre modèles pour sélectionner la meilleure réponse.
##### Gouvernance
La charte et les permissions bornent l’espace d’action. Les prompts sensibles exigent validations supplémentaires et recours possible à agents humains.
#### Règles (identité)
##### Exigences
- Unicité de la nomenclature et traçabilité par identifiant.
- Validation automatique (get → execute → validate → render).
- Journalisation et versioning sémantique.
- Sécurité by design (permissions, secrets, conformité).
##### Conformité
Règles intégrées aux tests CI/CD; tout échec bloque la mise en production.
##### Standardisation des appels
Cycle get → execute → validate → render; journalisation obligatoire.
#### Options (identité)
##### Variantes
- Niveaux d’activation: off, basic, strict.
- Paramètres par projet via catalogues.
- Intégration progressive (feature flags).
##### Perspectives
- CI/CD avancé
- Packaging exécutable
- Durcissement sécurité
### REGLES ET CONVENTIONS <!-- SECTION:REGLES ET CONVENTIONS -->
#### Définitions (identité)
Agents : à partir de executor, les agents ont à leur disposition la charte, les règles internes, la nomenclature, le metaschema (creator), des howto/readme + éventuellement des docs tuto ou des sources de création
#### Règles (identité)
<!-- à remplir -->
#### Options (identité)
<!-- à remplir -->
### RELATIONS TRIPLETS <!-- SECTION:RELATIONS TRIPLETS -->
#### Définitions (identité)
Les catalogues de relations alimentent les scénarios, vues et API, avec génération à la volée de vues dérivées si nécessaire.
##### Objet
Modélisation relationnelle: triplets (sujet, relation, objet) pour lier entités, scénarios et catalogues..
##### Portée
S’applique à l’agence et à tous les projets dérivés. Intégré aux catalogues, scénarios et contrôles.
##### Notes source
##### Modèle
Les relations sont des objets de première classe. Le graphe s’appuie sur des triplets type subject–predicate–object, stockés par tables de relation typées pour optimiser les requêtes.
##### Tables par type de relation
Une table par type garantit indexation ciblée, contraintes adaptées et performances. Les relations portent leurs statuts, règles et métadonnées de traçabilité.
##### Navigation et cohérence
La matrice se parcourt par relations, filtrées par permissions et contextes. Les transitions d’objets et de relations sont validées avant propagation.
##### Intégration
Les catalogues de relations alimentent les scénarios, vues et API, avec génération à la volée de vues dérivées si nécessaire.
#### Règles (identité)
##### Exigences
- Unicité de la nomenclature et traçabilité par identifiant.
- Validation automatique (get → execute → validate → render).
- Journalisation et versioning sémantique.
- Sécurité by design (permissions, secrets, conformité).
##### Conformité
Règles intégrées aux tests CI/CD; tout échec bloque la mise en production.
##### Standardisation des appels
Cycle get → execute → validate → render; journalisation obligatoire.
#### Options (identité)
##### Variantes
- Niveaux d’activation: off, basic, strict.
- Paramètres par projet via catalogues.
- Intégration progressive (feature flags).
##### Perspectives
- CI/CD avancé
- Packaging exécutable
- Durcissement sécurité
### SCENARIOS <!-- SECTION:SCENARIOS -->
#### Définitions (identité)
{
  "meta": {
    "id": "page-001",
    "name": "Landing Page",
    "class": "Page",
    "version": "1.0.0"
  },
  "status": {
    "families": ["lifecycle"],
    "allowed": ["draft", "active", "archived"],
    "initial": "draft",
    "transitions": [
      {"from": "draft", "to": "active"},
      {"from": "active", "to": "archived"}
    ]
  },
  "permissions": {
    "read": ["user", "admin"],
    "write": ["admin"]
  },
  "definition": {
    "attributes": {
      "title": "string",
      "slug": "string"
    }
  },
  "view": {
    "template": "landing_default",
    "format": "html"
  }
}
insights agrégés
traçabilité complète
export et analyses
#### Règles (identité)
<!-- à remplir -->#### Options (identité)
<!-- à remplir -->### SECURITE <!-- SECTION:SECURITE -->

#### Définitions (identité)
<!-- à remplir -->
#### Règles (identité)
<!-- à remplir -->
#### Options (identité)
<!-- à remplir -->### ENV-PERMISSIONS <!-- SECTION:ENV-PERMISSIONS -->
#### Définitions (identité)
Traçabilité, rapports périodiques, runbooks incidents, sauvegardes et exercices de restauration.
#### Règles (identité)
<!-- à remplir -->#### Options (identité)
<!-- à remplir -->### STRATEGIE PRODUIT <!-- SECTION:STRATEGIE PRODUIT -->
#### Définitions (identité)
Les décisions d’évolution s’appuient sur A/B tests, analyses d’usage, feedbacks et coûts infra, avec publication de roadmaps et impacts attendus.
#### Règles (identité)
<!-- à remplir -->#### Options (identité)
<!-- à remplir -->### VECTEUR <!-- SECTION:VECTEUR -->
#### Définitions (identité)
##### Logique matricielle
Le système est un graphe d’objets reliés par relations typées. La navigation se fait par les triplets, en respectant permissions et contextes.
##### Fractale des objets
Chaque objet possède un vecteur principal (identité, contexte, vue) et un vecteur secondaire (définition, règle, option). Les méthodes de vecteur exposent ces informations de manière uniforme.
##### Vecteur comme langage
Le vecteur est l’interface universelle entre scénarios, agents et données. Il porte les paramètres d’exécution, les options et les règles, évitant toute recherche heuristique.
##### Conséquences
Uniformité d’exécution, auto-documentation et auto-validation, générativité maximale avec un minimum de code spécifique.
plans, vecteurs, fractale, dimensions
#### Règles (identité)
- Règle 1 : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
#### Options (identité)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### WEBSITE <!-- SECTION:WEBSITE -->
#### Définitions (identité)
Le site web de l’agence n’est pas une vitrine statique mais une démonstration vivante de ses capacités. Il incarne la logique fractale du système, la fonction récursive universelle et l’intégration des agents IA dans l’expérience utilisateur. Chaque page, chaque module et chaque interaction sont générés à la volée, validés par schéma et enrichis par les catalogues.  
Cette approche garantit une cohérence totale, une adaptabilité permanente et une transparence mesurable. Les utilisateurs ne découvrent pas seulement un site, ils vivent une expérience directe de l’agence : interaction avec un agent incarné, accès aux informations en temps réel, possibilité de piloter leurs projets et visibilité sur les résultats de l’écosystème.  
La valeur ajoutée réside dans cette combinaison unique : un outil de communication, de relation et de pilotage qui reflète exactement ce que l’agence propose à ses clients — un système autonome, évolutif et orienté vers l’humain.
##### Objet
Couches UI/Front: site vitrine et hub documentaire; expose les composants, docs et écrans de contrôle..
##### Notes source
. Les campagnes (SEO, SEA, emailing, réseaux sociaux) sont conçues et déployées par les agents à partir des objectifs définis dans les catalogues et ajustées en fonction des résultats. Les indicateurs de performance (trafic, engagement, conversions) sont collectés en continu, validés par les hooks et enregistrés dans les bases. Ces données alimentent des boucles de test et d’optimisation (A/B testing, multivarié) permettant d’améliorer en permanence la visibilité et l’efficacité des actions marketing.  
Le blog et l’espace transparence participent également à la stratégie : chaque contenu est pensé pour être à la fois informatif et générateur de visibilité. Les FAQ interactives et les dialogues avec les agents renforcent le référencement naturel en enrichissant continuellement le contenu du site.  
L’ensemble des actions marketing respecte la charte centrale : pas de pratiques trompeuses, priorité à des projets et des communications humanistes, alignés avec les valeurs éthiques de l’agence.     
##### Valeur ajoutée  
Le site web de l’agence n’est pas une vitrine statique mais une démonstration vivante de ses capacités. Il incarne la logique fractale du système, la fonction récursive universelle et l’intégration des agents IA dans l’expérience utilisateur. Chaque page, chaque module et chaque interaction sont générés à la volée, validés par schéma et enrichis par les catalogues.  
Cette approche garantit une cohérence totale, une adaptabilité permanente et une transparence mesurable. Les utilisateurs ne découvrent pas seulement un site, ils vivent une expérience directe de l’agence : interaction avec un agent incarné, accès aux informations en temps réel, possibilité de piloter leurs projets et visibilité sur les résultats de l’écosystème.  
La valeur ajoutée réside dans cette combinaison unique : un outil de communication, de relation et de pilotage qui reflète exactement ce que l’agence propose à ses clients — un système autonome, évolutif et orienté vers l’humain.
##### Portée
S’applique à l’agence et à tous les projets dérivés. Intégré aux catalogues, scénarios et contrôles.
#### Règles (identité)
##### Exigences
- Unicité de la nomenclature et traçabilité par identifiant.
- Validation automatique (get → execute → validate → render).
- Journalisation et versioning sémantique.
- Sécurité by design (permissions, secrets, conformité).
##### Conformité
Règles intégrées aux tests CI/CD; tout échec bloque la mise en production.
##### Standardisation des appels
Cycle get → execute → validate → render; journalisation obligatoire.#### Options (identité)
#### Options (identité)
##### Variantes
- Niveaux d’activation: off, basic, strict.
- Paramètres par projet via catalogues.
- Intégration progressive (feature flags).
##### Perspectives
- CI/CD avancé
- Packaging exécutable
- Durcissement sécurité
## Vue
### SECURITE ENV PERMISSIONS <!-- SECTION:  SECURITE ENV PERMISSIONS -->
#### Définitions (vue)
<!-- à remplir -->
#### Règles (vue)
<!-- à remplir -->
#### Options (vue)
<!-- à remplir -->
### AGENCE <!-- SECTION:AGENCE -->

#### Définitions (vue)
<!-- à remplir -->
#### Règles (vue)
<!-- à remplir -->
#### Options (vue)
<!-- à remplir -->
### AGENCE FRACTALE <!-- SECTION:AGENCE FRACTALE -->
#### Définitions (vue)
<!-- à remplir -->#### Règles (vue)
<!-- à remplir -->#### Options (vue)
<!-- à remplir -->### AGENTS <!-- SECTION:AGENTS -->
#### Définitions (vue)
<!-- à remplir -->
#### Règles (vue)
<!-- à remplir -->
#### Options (vue)
<!-- à remplir -->### CATALOGUES <!-- SECTION:CATALOGUES -->
#### Définitions (vue)
<!-- à remplir -->
#### Règles (vue)
<!-- à remplir -->
#### Options (vue)
<!-- à remplir -->### ENTITIES <!-- SECTION:ENTITIES -->

#### Définitions (vue)
<!-- à remplir -->
#### Règles (vue)
<!-- à remplir -->
#### Options (vue)
<!-- à remplir -->### ETHIQUE <!-- SECTION:ETHIQUE -->
#### Définitions (vue)
##### Principes
Transparence, respect des personnes, responsabilité, non-manipulation. L’éthique est un cadre appliqué à toutes les décisions, prompts, scénarios et rendus.
##### Intégration opérationnelle
La charte éthique est encodée dans des règles héritées. Les steps validate rejettent automatiquement ce qui viole le cadre. Les agents sont contraints par brief, permissions et validations contextuelles.
##### Audit et traçabilité
Les décisions sensibles sont journalisées avec justification, alternatives et impacts. Des agents externes auditent périodiquement la conformité et émettent des recommandations.
##### Amélioration continue
La charte évolue par retours, veille et incidents. Les changements sont versionnés et rétro-testés.
#### Règles (vue)
- Règle 1 : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
data_governance, transparence, engagement
#### Options (vue)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### EXTENSION <!-- SECTION:EXTENSION2 -->
#### Définitions (vue)
##### Représentation
Mécanisme de plug-ins internes: ajout/remplacement de capacités sans modifier le cœur (API internes, adaptateurs, hooks)..
##### Portée
S’applique à l’agence et à tous les projets dérivés. Intégré aux catalogues, scénarios et contrôles.
#### Règles (vue)
##### Conventions de rendu
- Composants atomiques
- Contrats stables
- Versioning sémantique + migrations UI
#### Options (vue)
##### Modes d’affichage
- Vues réduites/complètes/agrégées
- Dashboards en temps réel
- Diffusions: interne/bêta/publique
<!-- à remplir -->
### FRACTALE <!-- SECTION:FRACTALE -->
#### Définitions (vue)
## Contexte
### SECURITE ENV PERMISSIONS <!-- SECTION:  SECURITE ENV PERMISSIONS -->
#### Définitions (contexte)
<!-- à remplir -->
#### Règles (contexte)
<!-- à remplir -->
#### Options (contexte)
<!-- à remplir -->
### AGENCE <!-- SECTION:AGENCE -->

#### Définitions (contexte)
<!-- à remplir -->
#### Règles (contexte)
<!-- à remplir -->
#### Options (contexte)
<!-- à remplir -->
### AGENCE FRACTALE <!-- SECTION:AGENCE FRACTALE -->
#### Définitions (contexte)
<!-- à remplir -->
#### Règles (contexte)
<!-- à remplir -->
#### Options (contexte)
<!-- à remplir -->
### AGENTS <!-- SECTION:AGENTS -->
#### Définitions (contexte)
<!-- à remplir -->
#### Règles (contexte)
<!-- à remplir -->
#### Options (contexte)
<!-- à remplir -->
### CATALOGUES <!-- SECTION:CATALOGUES -->
#### Définitions (contexte)
<!-- à remplir -->
#### Règles (contexte)
<!-- à remplir -->
#### Options (contexte)
<!-- à remplir -->
### ENTITIES <!-- SECTION:ENTITIES -->
#### Définitions (contexte)
<!-- à remplir -->
#### Règles (contexte)
<!-- à remplir -->
#### Options (contexte)
<!-- à remplir -->
### ETHIQUE <!-- SECTION:ETHIQUE -->
#### Définitions (contexte)
##### Principes
Transparence, respect des personnes, responsabilité, non-manipulation. L’éthique est un cadre appliqué à toutes les décisions, prompts, scénarios et rendus.
##### Intégration opérationnelle
La charte éthique est encodée dans des règles héritées. Les steps validate rejettent automatiquement ce qui viole le cadre. Les agents sont contraints par brief, permissions et validations contextuelles.
##### Audit et traçabilité
Les décisions sensibles sont journalisées avec justification, alternatives et impacts. Des agents externes auditent périodiquement la conformité et émettent des recommandations.
##### Amélioration continue
La charte évolue par retours, veille et incidents. Les changements sont versionnés et rétro-testés.
data_governance, transparence, engagement
#### Règles (contexte)
- Règle 1 (ETHIQUE) : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
#### Options (contexte)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### EXTENSION <!-- SECTION:EXTENSION -->
#### Définitions (contexte)
##### Environnements
- Dév / Recette / Prod
- Intégrations externes via API interne
##### EXTENSION en contexte
Piloté par catalogues et secrets chiffrés.
#### Règles (contexte)
##### Sécurité et permissions
- Accès via API interne uniquement
- Permissions par rôle et statut d’entité
- Chiffrement au repos/en transit
#### Options (contexte)
##### Cas d’usage & évolutions
- Migration de données
- Intégration/remplacement d’API
- Learning loop & A/B tests
### HEBERGEMENT <!-- SECTION:HEBERGEMENT -->
#### Définitions (contexte)
##### Introduction
L’hébergement fournit l’infrastructure modulaire, sécurisée et scalable qui supporte l’agence, le labo et chaque client. Le modèle retenu repose sur des cubes isolés (agence, labo, un cube par client), chacun contenant des conteneurs par projet. L’ensemble s’exécute prioritairement sur Yunos Cloud, sans dépendance forte à un fournisseur.
##### Architecture par cubes et conteneurs
Chaque cube est un périmètre d’isolation réseau, stockage, secrets et monitoring. À l’intérieur, chaque projet tourne dans un conteneur distinct, avec son stockage dédié, ses clés et son réseau virtuel. Cette granularité permet mises à jour indépendantes, rollbacks rapides, et migrations sans interruption.
##### Sécurité, sauvegardes et supervision
Le chiffrement est appliqué en transit et au repos, avec des coffres de secrets par cube. Les sauvegardes sont différentielles avec tests de restauration réguliers. Les métriques (latence, erreurs, saturation) et journaux sont centralisés, avec alertes sur seuils et anomalies comportementales.
##### Scalabilité et portabilité
Le scale-out se fait par réplication de conteneurs et extension horizontale de cubes. La portabilité est assurée par des manifests d’infrastructure déclaratifs, garantissant des déploiements reproductibles sur d’autres clouds ou on-premise.
##### Objectifs de l’hébergement
##### Modularité et adaptabilité
##### Infrastructure de base
###### Localisation principale (Yunos Cloud)
###### Définition des cubes de serveurs
###### Séparation agence, clients et labo
##### Organisation par cube
###### Cube agence
###### Cube labo
###### Cube client
###### Gestion multi-projets par Docker
##### Sécurité et isolation
###### Cloisonnement des données
###### Sécurisation par défaut
###### Gestion des accès et permissions
##### Gestion des données
###### Stockage et sauvegardes
###### Chiffrement
###### Conformité et auditabilité
##### Scalabilité et optimisation
###### Adaptation dynamique de la charge
###### Ajout de nouveaux cubes
###### Monitoring des performances
##### Administration et maintenance
###### Automatisation des déploiements
###### Gestion des mises à jour
###### Supervision et alertes
##### Perspectives d’évolution
###### Multi-cloud et redondance
###### Optimisation coûts/performances
###### Intégration avec la logique fractale
#### Règles (contexte)
- Règle 1 (HEBERGEMENT) : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
#### Options (contexte)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### IA <!-- SECTION:IA -->
#### Définitions (contexte)
##### Introduction
Présentation du rôle de l’IA dans le système, son articulation avec les agents et son intégration fractale.
##### Modèles d’IA
###### Typologie des modèles utilisés
###### Gestion multi-modèles et spécialisation
###### Stratégies de sélection et fallback
###### Versionning et compatibilité des modèles
##### Prompts
###### Définition et rôle des prompts
###### Structure fractale des prompts (identité, contexte, vue, vecteur secondaire)
###### Gestion des prompts dans les catalogues
###### Génération automatique et personnalisation
###### Prompts stratégiques, prompts créatifs et prompts techniques
###### Héritage et construction contextuelle des prompts
Les prompts ne sont jamais conçus isolément : ils dérivent d’un métaprompt, défini comme modèle générique. Chaque prompt hérite de ce métaprompt et se spécialise en fonction des spécificités du contexte. Les vecteurs (identité, contexte, vue, enrichis de définition, règles et options) alimentent la construction du prompt. Les missions confiées, les rôles de l’agent, les règles applicables, ainsi que la documentation ou les ressources disponibles, viennent compléter et affiner le contenu. Cette approche garantit que chaque prompt est cohérent, contextualisé et conforme aux contraintes imposées par le système.
##### Exécution et orchestration
###### Appels aux modèles via API internes
###### Normalisation des entrées et sorties
###### Validation des résultats et corrections automatiques
###### Récursivité et enchaînement des prompts
##### Gouvernance et traçabilité
###### Permissions et rôles des agents IA
###### Journalisation des appels et archivage
###### Suivi des performances et métriques
###### Audit des biais et des dérives
##### Optimisation et performance
###### Mise en cache des résultats
###### Réutilisation des prompts optimisés
###### Ajustement dynamique en fonction du contexte
###### Tests comparatifs et apprentissage continu
##### Perspectives d’évolution
###### IA générative multi-modale
###### Intégration de modèles propriétaires
###### Approfondissement du rôle des prompts
###### Scénarios d’expérimentation et laboratoire
#### Règles (contexte)
- Règle 1 (IA) : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
#### Options (contexte)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### IN OUT <!-- SECTION:IN OUT -->
#### Définitions (contexte)
##### Introduction
###### Dualité entre coulisses et interface
###### Objectif de transparence et de performance
##### Le Labo (coulisses)
###### Recherche et développement
###### Veille stratégique
###### Veille technique
###### Veille marketing
###### Entraînement et adaptation des modèles
###### Production de ressources internes (guides, tutos, datasets)
##### L’Interface (monde extérieur)
###### Blog et documentation publique
###### FAQ et support utilisateur
###### Vitrine temps réel des performances et résultats
###### Stratégies de communication et réseaux sociaux
###### Relations publiques et partenariats
##### Articulation entre Labo et Interface
###### Flux d’information sortants
###### Retour utilisateur comme input stratégique
###### Gouvernance et contrôle de cohérence
##### Perspectives
###### Évolution du rôle du Labo
###### Expansion des canaux d’interface
###### Renforcement de la transparence et de la confiance
#### Règles (contexte)
- Règle 1 (IN_OUT) : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
#### Options (contexte)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### INITIAL <!-- SECTION:INITIAL -->
#### Définitions (contexte)
##### Introduction
###### Objectif du document
###### Rôle fondateur et portée
###### Public concerné (IA, humains, partenaires, investisseurs)
##### Philosophie et charte
###### Principes fondamentaux (humanisme, transparence, éthique)
###### Place de l’IA (outil au service de l’humain, cadre et limites)
###### Vision long terme et engagements
###### Valeurs prioritaires (innovation, stabilité, accessibilité)
##### Choix conceptuels
###### Tout est objet et logique fractale
###### Méta-objets et rôle de MetaMetaclass
###### Full dynamique et récursivité
###### Universalité et adaptabilité
##### Choix techniques
###### Langage principal (Python)
###### Environnement initial (Docker, GitHub, CI/CD)
###### Base de données (MongoDB, RDF, SQL en option)
###### Catalogues et schémas initiaux
###### Ressources de bootstrap (prompts, agents, scénarios)
##### Gouvernance et évolutivité
###### Gestion des versions (règles SemVer adaptées : 1.0.1 / 1.1.0 / 2.0.0)
###### Impact des évolutions sur la structure
###### Compatibilité ascendante et migrations
###### Réversibilité des choix
##### Organisation et responsabilités
###### Rôle des agents IA et des humains
###### Définition des espaces (admin, back-office, client, labo, vitrine)
###### Transparence et auditabilité
##### Sécurité et conformité
###### Permissions et droits d’accès
###### Logs, traçabilité et audit
###### Résilience et sauvegardes
###### Alignement avec les chartes légales et éthiques
##### Adaptabilité et ouverture
###### Multi-bases de données
###### Multi-langages et interopérabilité
###### Multi-agents et intégration de modèles externes
###### Interaction avec l’écosystème (API, extensions, partenaires)
##### Principes économiques et stratégiques
###### Pérennité et scalabilité
###### Optimisation des coûts
###### Modèle d’évolution en réseau
###### Priorité aux projets humanistes
##### Conclusion
###### Synthèse des choix fondateurs
###### Engagements pour les versions futures
###### Importance du respect de ce socle
#### Règles (contexte)
- Règle 1 (INITIAL) : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
#### Options (contexte)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### LAYERS <!-- SECTION:LAYERS -->
#### Définitions (contexte)
##### But
Structurer le travail en couches orchestrées, capables d’exécuter, créer, analyser, décider et superviser en parallèle, avec vues multiples d’un même problème.
##### Organisation
Layers d’exécution, création, stratégie, décision, supervision. Chaque layer regroupe des agents dédiés, scénarios, métriques et règles propres, avec interfaces d’échange standardisées.
##### Expérimentation parallèle
Plusieurs approches peuvent être évaluées simultanément. Les résultats sont comparés et archivés, permettant rétro-tests et reproductibilité.
##### Intégration
Les layers s’articulent avec catalogues, MetaMetaclass et triggers. Ils fournissent une base pour gouvernance avancée et arbitrages multi-critères.
#### Règles (contexte)
- Règle 1 (LAYERS) : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
#### Options (contexte)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### MATRIX <!-- SECTION:MATRIX -->
#### Définitions (contexte)
##### Logique matricielle
Le système est un graphe d’objets reliés par relations typées. La navigation se fait par les triplets, en respectant permissions et contextes.
##### Fractale des objets
Chaque objet possède un vecteur principal (identité, contexte, vue) et un vecteur secondaire (définition, règle, option). Les méthodes de vecteur exposent ces informations de manière uniforme.
##### Vecteur comme langage
Le vecteur est l’interface universelle entre scénarios, agents et données. Il porte les paramètres d’exécution, les options et les règles, évitant toute recherche heuristique.
##### Conséquences
Uniformité d’exécution, auto-documentation et auto-validation, générativité maximale avec un minimum de code spécifique.
plans, vecteurs, fractale, dimensions
#### Règles (contexte)
- Règle 1 (MATRIX) : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
#### Options (contexte)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### METALANGAGE <!-- SECTION:METALANGAGE -->
#### Définitions (contexte)
##### Objet
Définir une syntaxe unique pour décrire objets, vecteurs, scénarios, relations et catalogues, afin d’unifier la lecture/écriture par humains et agents.
##### Conventions
Chemins vectoriels en notation pointée, types explicites, alias normalisés, et schémas JSON de référence. Les mêmes conventions s’appliquent aux prompts et à la documentation.
##### Interopérabilité
Le métalangage se sérialise en JSON/YAML, alimente les API internes et génère les validations. Il évite la divergence entre intention et exécution.
##### Évolution
Versionné, testé et documenté, il s’adapte sans rupture via compatibilité ascendante et dépréciations guidées.
#### Règles (contexte)
- Règle 1 (METALANGAGE) : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
#### Options (contexte)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### OPTIMISATION QA AB2 <!-- SECTION:OPTIMISATION QA AB2 -->
#### Définitions (contexte)
##### Environnements
- Dév / Recette / Prod
- Intégrations externes via API interne

##### OPTIMISATION QA AB en contexte
Piloté par catalogues et secrets chiffrés.

#### Règles (contexte)
##### Sécurité et permissions
- Accès via API interne uniquement
- Permissions par rôle et statut d’entité
- Chiffrement au repos/en transit

#### Options (contexte)
##### Cas d’usage & évolutions
- Migration de données
- Intégration/remplacement d’API
- Learning loop & A/B tests
### ORGANES <!-- SECTION:ORGANES -->
#### Définitions (contexte)
<!-- à remplir -->
#### Règles (contexte)
<!-- à remplir -->
#### Options (contexte)
<!-- à remplir -->
### PROMPTS <!-- SECTION:PROMPTS-->
#### Définitions (contexte)
##### Environnements
- Dév / Recette / Prod
- Intégrations externes via API interne
##### PROMPTS en contexte
Piloté par catalogues et secrets chiffrés.
#### Règles (contexte)
##### Sécurité et permissions
- Accès via API interne uniquement
- Permissions par rôle et statut d’entité
- Chiffrement au repos/en transit
#### Options (contexte)
##### Cas d’usage & évolutions
- Migration de données
- Intégration/remplacement d’API
- Learning loop & A/B tests
### REGLES ET CONVENTIONS <!-- SECTION:REGLES ET CONVENTIONS -->
#### Définitions (contexte)
<!-- à remplir -->
#### Règles (contexte)
<!-- à remplir -->
#### Options (contexte)
<!-- à remplir -->
### RELATIONS TRIPLETS <!-- SECTION:RELATIONS TRIPLETS -->
#### Définitions (contexte)
##### Environnements
- Dév / Recette / Prod
- Intégrations externes via API interne
##### RELATIONS TRIPLETS en contexte
Piloté par catalogues et secrets chiffrés.
#### Règles (contexte)
##### Sécurité et permissions
- Accès via API interne uniquement
- Permissions par rôle et statut d’entité
- Chiffrement au repos/en transit
#### Options (contexte)
##### Cas d’usage & évolutions
- Migration de données
- Intégration/remplacement d’API
- Learning loop & A/B tests
### SCENARIOS <!-- SECTION:SCENARIOS -->
#### Définitions (contexte)
<!-- à remplir -->
#### Règles (contexte)
<!-- à remplir -->
#### Options (contexte)
<!-- à remplir -->
### SECURITE <!-- SECTION:SECURITE -->
#### Définitions (contexte)
<!-- à remplir -->
#### Règles (contexte)
<!-- à remplir -->
#### Options (contexte)
<!-- à remplir -->
### VECTEUR <!-- SECTION:VECTEUR -->
#### Définitions (contexte)
##### Logique matricielle
Le système est un graphe d’objets reliés par relations typées. La navigation se fait par les triplets, en respectant permissions et contextes.
##### Fractale des objets
Chaque objet possède un vecteur principal (identité, contexte, vue) et un vecteur secondaire (définition, règle, option). Les méthodes de vecteur exposent ces informations de manière uniforme.
##### Vecteur comme langage
Le vecteur est l’interface universelle entre scénarios, agents et données. Il porte les paramètres d’exécution, les options et les règles, évitant toute recherche heuristique.
##### Conséquences
Uniformité d’exécution, auto-documentation et auto-validation, générativité maximale avec un minimum de code spécifique.
plans, vecteurs, fractale, dimensions
#### Règles (contexte)
- Règle 1 (VECTEUR) : respecter la cohérence identité/contexte/vue.
- Règle 2 : traçabilité complète (catalogues, statuts, journaux).
- Règle 3 : interopérabilité et idempotence des scénarios.
#### Options (contexte)
- Option A : variantes paramétrables par projet.
- Option B : niveaux de sévérité/rigueur.
- Option C : extensions via providers/adaptateurs.
### WEBSITE <!-- SECTION:WEBSITE -->
#### Définitions (contexte)
##### Environnements
- Dév / Recette / Prod
- Intégrations externes via API interne
##### WEBSITE en contexte
Piloté par catalogues et secrets chiffrés.
#### Règles (contexte)
##### Sécurité et permissions
- Accès via API interne uniquement
- Permissions par rôle et statut d’entité
- Chiffrement au repos/en transit
#### Options (contexte)
##### Cas d’usage & évolutions
- Migration de données
- Intégration/remplacement d’API
- Learning loop & A/B tests