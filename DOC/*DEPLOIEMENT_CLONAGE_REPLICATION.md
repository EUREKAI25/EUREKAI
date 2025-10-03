# 1. Déploiement
Le déploiement applique le bootstrap, paramètre l’environnement, charge catalogues et secrets, exécute migrations et vérifications, puis met en ligne les services.

# 2. Clonage
Le clonage réplique un projet existant (catalogues, relations, états) vers un nouvel espace. Les identifiants sont régénérés si nécessaire, les permissions recalculées, les secrets réassignés.

# 3. Réplication
La réplication distribue données et services sur plusieurs nœuds/zones. Les mécanismes de cohérence s’appuient sur journaux d’opérations, validations idempotentes et tests de reprise.

# 4. Traçabilité
Chaque opération écrit des entrées d’audit, avec durées, statuts, erreurs et remédiations appliquées.
