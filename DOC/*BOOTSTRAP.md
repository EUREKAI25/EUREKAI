# 1. Rôle du bootstrap
Le bootstrap est un lanceur universel. Il installe les catalogues initiaux, initialise la base, charge règles et vecteurs, et vérifie l’environnement. Il s’emploie pour l’agence elle-même comme pour tout projet généré.

# 2. Modes d’exécution
Le bootstrap s’exécute depuis GitHub, une archive ZIP ou l’interface de l’agence. Dans tous les cas, il applique la même séquence, versionnée et traçable.

# 3. Séquence d’initialisation
Chargement des catalogues de base, génération des schémas via MetaMetaclass, connexion base choisie, enregistrement des statuts universels, activation du cron central, vérifications de sécurité et création des premiers utilisateurs et rôles.

# 4. Rejouabilité et journalisation
Chaque étape écrit un journal structuré et idempotent. Le redéploiement détecte l’état courant et applique seulement les manquants, avec rollbacks en cas d’échec.

# 1. Introduction
## Rôle du bootstrap
## Universalité du mécanisme (agence et projets dérivés)

# 2. Modes d’exécution
## Depuis GitHub
## Depuis une archive locale (ZIP)
## Depuis l’agence elle-même

# 3. Prérequis et dépendances
## Environnements supportés
## Outils requis (Python, etc.)
## Variables d’environnement initiales

# 4. Initialisation
## Déploiement des catalogues initiaux
## Chargement des métadonnées et règles
## Installation de la base de données

# 5. Exécution
## Lancement unique (première initialisation)
## Relance pour nouveaux projets
## Vérification et logs automatiques

# 6. Autonomie et réutilisation
## Compatibilité avec tous les types de projets
## Génération dynamique et full dynamique
## Mises à jour et auto-maintenance

# 7. Perspectives d’évolution
## Intégration CI/CD
## Packaging en exécutable universel
## Sécurité et durcissement