# Extension de navigateur — Document de base

## Méta-architecture
L’extension est conçue comme un outil modulaire et adaptatif. Elle est empaquetée une seule fois et contient une batterie de modules préinstallés (menus contextuels, popup, side panel, overlays, moteurs d’animation, capture de métadonnées, file offline, notifications, badge, raccourcis clavier). Le comportement de ces modules est piloté par une configuration distante envoyée par l’API (JSON signé), qui active ou désactive les modules déjà packagés et ajuste leurs paramètres.  
Aucune mise à jour du store n’est nécessaire tant que de nouvelles capacités de code ne sont pas ajoutées.

## Possibilités d’interface prévues
Menu contextuel : options activées selon contexte (page, sélection de texte, lien, image)  
Popup : fenêtre déclenchée par l’icône d’extension, avec header et liste d’actions dynamiques  
Side panel : panneau latéral pour afficher un flux, une file d’items ou un mini-dashboard  
Overlays dans la page : bannière, bulle flottante, div central, panneau docké, toast  
Badge sur l’icône : compteur ou état en temps réel  
Notifications système : confirmation, erreur ou proposition d’action  
Raccourcis clavier : déclenchement rapide d’actions définies par configuration  
Omnibox : commandes déclenchées depuis la barre d’URL  

## Adaptation client et configuration sans repackaging
L’extension est conçue pour être livrée une fois et configurée à 100 % depuis le back-office, sans nouvelle publication. À l’installation, elle embarque tous les modules et moteurs nécessaires ; leur activation dépend du contexte (tenant, utilisateur, rôle, permissions, plan d’abonnement).  
Une configuration distante signée définit les feature flags, textes, emplacements, règles d’affichage, endpoints et limites d’usage. Le branding, les couleurs, les libellés et les actions disponibles sont appliqués à la volée selon le profil.  
Les mises à jour ne sont requises qu’en cas d’ajout d’une capacité totalement nouvelle ou d’évolution de dépendances ; le fonctionnement courant, y compris la création de variantes pour des clients différents, se fait sans repackaging grâce aux permissions, politiques et modèles déclaratifs.

## Stratégie d’adaptation
Un noyau commun : regroupe toutes les capacités packagées, moteur de configuration JSON, et logique de validation  
Adaptateurs spécifiques par hôte : pour gérer les API propres à chaque plateforme (menus contextuels, notifications, stockage, side panel, sécurité)  
Matrice des capacités : tableau de compatibilité qui précise pour chaque plateforme ce qui est identique, ce qui diffère et ce qui est indisponible  

## Portabilité navigateur
Chrome et Edge : quasi identiques, basés sur Chromium. Seule différence : packaging, identifiant et publication  
Opera et Brave : aussi Chromium, compatibles avec Chrome Web Store  
Firefox : compatible WebExtensions, mais MV3 encore partiel. Quelques ajustements nécessaires (service worker, règles réseau, side panel)  
Safari : possible avec Safari Web Extensions. Conversion via Xcode et distribution App Store. Plus contraignant, à envisager en phase ultérieure  

# Usages personnels

## Fonctionnalité initiale — Référencement des sites à scraper
Le besoin immédiat est de permettre, via un clic droit, de référencer un site dans la liste des outils à scraper.  
- Un module contextuel “Référencer ce site” est disponible par défaut  
- Lors de l’action, l’extension capture l’URL, le titre et les métadonnées de la page  
- Ces données sont transmises à l’API “scrape_registry.add”  
- Une confirmation visuelle est affichée (toast, badge sur l’icône), avec gestion des erreurs et mode offline (IndexedDB et resoumission automatique)  
- Ce module constitue la première brique fonctionnelle et reste activable/désactivable via configuration API  

## Fonctionnalité complémentaire — Gestion avancée du copier-coller

Rétention et purge  
L’historique conserve les éléments pendant 24h glissantes. Les éléments marqués comme épinglés ne sont jamais purgés. L’épinglage est automatique pour tout élément auquel un raccourci clavier est attribué. La suppression intervient uniquement sur les éléments non épinglés au-delà de 24h ou sur action manuelle.

Raccourcis clavier  
L’extension expose des slots de raccourcis prédéclarés (ex. Alt+Shift+1..9, Alt+Shift+A..L). L’utilisateur assigne un élément à un slot depuis l’interface. Tant qu’un slot est attribué, l’élément est épinglé et exclu de la purge. Le désassigner retire l’épingle et rend l’élément à la rétention 24h. Un raccourci global peut ouvrir une palette rapide pour sélectionner et coller un élément de l’historique.

Insertion et comportements  
Sur activation d’un raccourci, l’extension tente d’insérer directement dans le champ actif. Si l’insertion directe n’est pas possible, l’élément est copié dans le presse-papiers et une notification invite à coller. Les éléments peuvent être du texte, des extraits HTML sûrs ou des snippets de commande (affichés avant insertion).

Interface de gestion  
Une vue dédiée (popup ou side panel) liste l’historique, les épinglés, les slots de raccourcis, la recherche et les tags. Depuis cette vue, l’utilisateur peut épingler, désépingler, renommer, tagger, attribuer ou retirer un raccourci.

Sécurité et confidentialité  
Stockage local chiffré. Aucune synchronisation distante par défaut. Les champs sensibles peuvent être marqués pour exclusion de l’historique. Les actions sont journalisées de manière minimale pour diagnostic local.

Paramétrage  
Options de limites (nombre d’éléments non épinglés), formats autorisés (texte, HTML sûr), domaines où l’insertion est autorisée, et choix de la surface d’interface (popup ou side panel).