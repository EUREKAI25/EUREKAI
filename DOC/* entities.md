# 1. Introduction
Les entités représentent les acteurs fondamentaux du système. Elles structurent l’agence et ses projets en fournissant une modélisation claire des utilisateurs, entreprises, agents, équipements et providers. Chaque entité est inscrite dans un catalogue dédié, reliée aux autres par des relations normalisées et gérée par MetaMetaclass. Elles servent de base à la gouvernance, aux scénarios et aux interactions internes comme externes.

# 2. Typologie des entités
## Users
Les utilisateurs représentent les individus humains interagissant avec le système. Ils disposent d’une identité unique, d’un profil enrichi (rôles, préférences, permissions) et de relations avec d’autres entités (ex. appartenance à une company, utilisation d’un equip). Leurs interactions sont historisées et validées par le vecteur secondaire (règles et options).

## Companies
Les companies regroupent plusieurs users et permettent de gérer des projets ou produits au nom d’une organisation. Elles définissent les droits collectifs, les ressources partagées et les contraintes contractuelles. Une company peut posséder des agents dédiés et sponsoriser des equips ou providers.

## Agents
Les agents sont des entités IA ou hybrides qui exécutent, analysent, créent ou décident selon leur typologie. Ils héritent des mêmes règles que les autres entités mais disposent d’attributs supplémentaires liés à leur mission (brief, ressources documentaires, contraintes). Ils fonctionnent en interaction avec les scénarios et peuvent être regroupés en couches (exécution, stratégie, décision).

## Equips
Les equips désignent l’ensemble des ressources techniques, matérielles ou logicielles attribuées à des users, companies ou agents. Ils incluent des environnements d’hébergement, des applications, des outils spécialisés ou des jeux de données. Chaque equip est versionné et contrôlé par ses règles de sécurité et d’intégrité.

## Providers
Les providers représentent les entités qui fournissent des services ou ressources externes au système. Ils sont essentiels pour l’intégration de solutions tierces (API, modèles d’IA, infrastructures cloud, hébergement, services SaaS).
### Enfants du Provider
Un provider peut être spécialisé et se décliner en enfants tels que :
- API providers (connexion standardisée aux services externes via les API internes)
- Hébergeurs et infrastructures cloud
- Fournisseurs de modèles IA et moteurs de génération
- Outils tiers (monitoring, design, analytics, communication)
Chaque enfant est inscrit dans un catalogue dédié et relié aux objets qu’il alimente. Cela garantit que tout provider est interchangeable et modulable selon les besoins.

# 3. Héritage et relations
Toutes les entités héritent de MetaMetaclass, qui leur impose le vecteur identité-contexte-vue et son vecteur secondaire (définition, règle, option). Les relations permettent de modéliser les interactions : un user appartient à une company, un agent est assigné à un scénario, un equip est attribué à un user, un provider alimente un agent. Les transitions de statut des entités sont également gérées via les catalogues de relations.

# 4. Statuts et permissions
Chaque entité possède un statut (actif, inactif, suspendu, archivé) et des permissions associées. Ces permissions définissent ce qu’une entité peut voir, modifier ou exécuter. Les statuts assurent la traçabilité temporelle des opérations et garantissent que les entités évoluent selon des règles explicites et auditées.

# 5. Interopérabilité avec les catalogues
Les entités sont stockées et maintenues dans leurs catalogues respectifs. Cela permet :
- la récupération rapide par identifiant ou vecteur
- l’agrégation pour des vues virtuelles (par ex. tous les agents actifs d’une company)
- la validation systématique via les règles secondaires
- la compatibilité avec MongoDB et autres bases pour optimiser les requêtes

# 6. Perspectives d’évolution
L’évolution des entités suivra deux axes :
- Spécialisation accrue : de nouveaux types d’agents, equips ou providers pourront être introduits sans rompre la cohérence globale.
- Gouvernance distribuée : les statuts, rôles et relations entre entités pourront être modulés en temps réel pour expérimenter différents modèles organisationnels.
Cette approche fractale assure que l’agence reste modulaire, extensible et capable de s’adapter aux innovations futures.
