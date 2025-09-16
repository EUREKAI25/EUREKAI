# METHODS
- create() : vector_method_create_<uuid>
- read() : vector_method_read_<uuid>
- update() : vector_method_update_<uuid>
- delete() : vector_method_delete_<uuid> <!-- on checke toutes les implications, on supprime les reliquats inutiles après suppression -->
- execute() : vector_method_execute_<uuid>
- render() : vector_method_render_<uuid>
- engage() : vector_method_engage_<uuid>
- inject_vectors(object) : vector_method_inject_vectors_<uuid>
- inject_metadata(object) : vector_method_inject_metadata_<uuid> <!-- ajoute created_at, created_by, updated_at, updated_by -->
- generate_bundle(bundle_ident) : vector_method_generate_bundle_<uuid> <!-- récupère tous les objets liés par Relations: element_of(bundle_ident), construit le bundle dynamiquement (sans recursion), met à jour relation_bundle et enregistre linked_to(bundle_ident) sur chaque élément -->
- generate_catalog(object_type) : vector_method_generate_catalog_<uuid> <!-- crée le Catalog pour <object_type> s’il n’existe pas, initialise items -->
- register_in_catalog(object) : vector_method_register_in_catalog_<uuid> <!-- ajoute {object.ident: ObjectRef} dans le Catalog de son type -->
- unregister_from_catalog(object) : vector_method_unregister_from_catalog_<uuid> <!-- retire l’entrée du Catalog -->
- generate_all_catalogs() : vector_method_generate_all_catalogs_<uuid> <!-- itère sur tous les types connus et appelle generate_catalog -->
automate XTtype, XBundle, Xof (si method), XSchema, XTemplate (si content)





