# 1. Technique
## 1.1 Catalogues
### Identité
- Définition : types de catalogues (primaires, dérivés, virtuels).
- Règle : unicité et traçabilité des entrées.
- Option : formats d’export et d’affichage.
### Vue
- Définition : structure fractale des entrées.
- Règle : cohérence et exhaustivité.
- Option : vues réduites ou complètes.
### Contexte
- Définition : usage dans les scénarios et les requêtes.
- Règle : compatibilité avec les bases de données.
- Option : instances générées (MongoDB, SQL, fichiers).
## 1.2 Scénarios
### Identité
- Définition : unité canonique d’exécution (get, execute, validate, render).
- Règle : un seul type et une seule intention par scénario.
- Option : sous-scénarios composés.
### Vue
- Définition : steps fractals (get, execute, validate, render).
- Règle : ordre obligatoire et validation locale.
- Option : visualisation (graphes, logs, rapports).
### Contexte
- Définition : environnement d’exécution (agents, triggers).
- Règle : permissions obligatoires.
- Option : instances générées (tests, batchs, audits).
## 1.3 API
### Identité
- Définition : API internes et externes.
- Règle : standardisation via API internes.
- Option : catalogues d’API branchées.
### Vue
- Définition : points de terminaison et méthodes exposées.
- Règle : uniformité et respect des conventions.
- Option : vues par service, produit, ou client.
### Contexte
- Définition : environnement d’intégration.
- Règle : sécurité et permissions.
- Option : instances générées (connecteurs, wrappers).
# 2. Organisation
## 2.1 Agents
### Identité
- Définition : exécuteurs, créateurs, stratèges, décideurs, externes.
- Règle : degré de liberté strictement défini.
- Option : rôles hybrides.
### Vue
- Définition : missions attribuées et livrables attendus.
- Règle : traçabilité et justification des choix.
- Option : reporting par vue (historique, statistiques).
### Contexte
- Définition : couche d’intervention (exécution, décision, création, audit).
- Règle : séparation stricte des couches.
- Option : instances générées (équipes, managers, sous-agents).
## 2.2 Permissions et sécurité
### Identité
- Définition : niveaux d’accès (utilisateur, agent, manager, root).
- Règle : unicité et non-cumul des privilèges.
- Option : délégués temporaires.
### Vue
- Définition : schéma des droits appliqués aux objets.
- Règle : auditabilité obligatoire.
- Option : vues réduites pour utilisateurs.
### Contexte
- Définition : environnement de sécurité.
- Règle : chiffrement et journalisation.
- Option : instances générées (tokens, clés).
# 3. Éthique et gouvernance
## 3.1 Charte et valeurs
### Identité
- Définition : valeurs fondamentales, mission
- Règle :  normes éthiques obligatoires, applicables à tous les objets et agents.
- Option : déclinaisons possibles, ajustements contextuels.
### Vue
- Définition : documents publics et internes,  image projetée, perception voulue
- Règle :  contraintes de communication, transparence.
- Option : déclinaisons (produits, projets),  variantes de ton, styles de communication
### Contexte
- Définition : environnement culturel et stratégique, champ d’application, limites
- Règle : obligations légales, culturelles
- Option : instances générées (rapports, audits éthiques), scénarios d’adaptation aux environnements
## 3.2 Nomenclature et conventions
### Définitions
- Identité : formats de base, terminologie
- Vue : représentations standardisées (markdown, json)
- Contexte : domaines d’usage (technique, organisationnel)
### Règles
- Identité : cohérence des noms et alias
- Vue : conventions graphiques et syntaxiques
- Contexte : contraintes de compatibilité entre couches
### Options
- Identité : alternatives de nommage
- Vue : options de présentation ou de rendu
- Contexte : variations selon public cible ou outil utilisé
## 3.3 Audit et supervision
### Identité
- Définition : agents et processus externes.
- Règle : indépendance et objectivité.
- Option : audits automatisés.
### Vue
- Définition : rapports de performance, conformité, sécurité.
- Règle : exhaustivité et traçabilité.
- Option : formats (rapports, dashboards).
### Contexte
- Définition : situations auditées (produits, scénarios, agents).
- Règle : périodicité obligatoire.
- Option : instances générées (alertes, logs, tickets).
# 4. Ressources techniques
## 4.1 Hébergement
### Identité
- Définition : architecture modulaire en cubes et dockers.
- Règle : séparation stricte agence / labo / client.
- Option : déploiements hybrides.
### Vue
- Définition : ressources serveur, stockage, réseaux.
- Règle : isolation et scalabilité horizontale.
- Option : vues d’usage (par client, par projet).
### Contexte
- Définition : environnement cloud (YunOS, etc.).
- Règle : sécurité et réplication.
- Option : instances générées (backups, clusters).
## 4.2 Bootstrap et organes vitaux
### Identité
- Définition : bootstrap, moteur de méthodes, cron.
- Règle : initialisation obligatoire, pulsation permanente.
- Option : extensions modulaires.
### Vue
- Définition : processus de démarrage et organes actifs.
- Règle : cohérence fractale.
- Option : vues techniques (logs, monitorings).
### Contexte
- Définition : environnement d’initialisation.
- Règle : portabilité (zip, GitHub, auto-install).
- Option : instances générées (projets, agences).
# 5. Production et interface externe

## 5.1 Production
### Identité
- Définition : sites, SaaS, apps, extensions, contenus.
- Règle : standards de qualité.
- Option : types de produits disponibles.
### Vue
- Définition : livrables attendus par produit.
- Règle : cohérence visuelle et technique.
- Option : niveaux de détail fournis.
### Contexte
- Définition : cadre de production.
- Règle : délais et compatibilité client.
- Option : instances générées (projets, campagnes).

## 5.2 Labo
### Identité
- Définition : rôle du labo (veille, innovation).
- Règle : rigueur et indépendance.
- Option : thématiques explorées.
### Vue
- Définition : livrables (rapports, prototypes, expérimentations).
- Règle : uniformité des formats.
- Option : niveaux de diffusion (interne, public).
### Contexte
- Définition : environnement technologique et marketing.
- Règle : alignement stratégique.
- Option : instances générées (datasets, tests).

## 5.3 Interface publique
### Identité
- Définition : canaux de diffusion (blog, FAQ, vitrine).
- Règle : validation éditoriale.
- Option : choix des supports.
### Vue
- Définition : contenus publiés (résultats, performances).
- Règle : cohérence et accessibilité.
- Option : granularité de diffusion.
### Contexte
- Définition : relation avec utilisateurs, clients, influenceurs.
- Règle : transparence.
- Option : instances générées (posts, rapports live).