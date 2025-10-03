# 1. Introduction
Les API constituent l’interface normalisée entre les différents modules du système et les services extérieurs. Elles permettent de standardiser les échanges, de contrôler les accès et d’assurer la traçabilité complète des interactions. Toutes les API externes sont accessibles uniquement via une API interne qui les encapsule, garantissant l’uniformité et la cohérence.

# 2. API internes
Les API internes exposent les services natifs de l’agence : catalogues, scénarios, agents, logs, monitoring, permissions. Elles constituent la couche unique de dialogue pour tous les composants internes et pour les adaptateurs externes. Chaque appel suit la structure fractale (identité, contexte, vue enrichis de définition, règles, options).

# 3. API externes
Les API externes (services tiers comme paiement, hébergement, IA, réseaux sociaux) ne sont jamais appelées directement. Elles passent systématiquement par des adaptateurs internes qui normalisent les vecteurs, appliquent les règles de sécurité et assurent la compatibilité avec le reste du système.

# 4. Standardisation des appels
Tous les appels API suivent les mêmes conventions de structure et de cycle d’exécution (get, execute, validate, render). Les entrées et sorties sont enregistrées dans les catalogues avec leurs métadonnées. Les statuts et transitions sont uniformisés, facilitant l’audit et la reprise en cas d’incident.

# 5. Plug-in et méthodes pré-adaptées
L’intégration d’une API externe se fait par un plug-in interne qui mappe automatiquement les méthodes natives vers les étapes standardisées du système. Les fonctions externes sont converties en scénarios internes avec leurs vecteurs, statuts et hooks. Cela permet d’ajouter ou de remplacer une API tierce sans modifier le reste du système.

# 6. Sécurité et permissions
Les API internes contrôlent toutes les interactions avec l’extérieur. Les accès sont filtrés par permissions, journalisés et soumis aux règles de validation. Aucun agent ou scénario ne peut appeler directement une API externe sans passer par l’interne, garantissant un niveau constant de sécurité et de traçabilité.