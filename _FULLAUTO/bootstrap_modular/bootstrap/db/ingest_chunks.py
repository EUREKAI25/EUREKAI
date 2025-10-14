from .upsert_object import upsert_object
from .set_attr_value import set_attr_value
from .link import link

def ingest_chunks(conn, site_slug: str, doc_key: str, chunks: list):
    """
    Enregistre des chunks (unités de texte) comme objets RDF.
    Chaque chunk devient un objet de type 'chunk' :
      - element_of -> <site_slug> (le projet)
      - related_to -> <doc_key> (le document d'origine : brief/spec/idea...)
      - depends_on -> <site_slug>_vector (si la base vectorielle existe)
      - attribut 'text' (contenu du chunk)
    """
    proj_key = site_slug
    vec_key = f"{site_slug}_vector"  # instance vector_db si elle existe

    for i, ch in enumerate(chunks or []):
        cid = ch.get("id", i)
        key = f"{doc_key}_chunk_{cid}"
        upsert_object(conn, key, "chunk", f"Chunk {cid}")
        link(conn, "rel_element_of", key, "element_of", proj_key)
        link(conn, "rel_related_to", key, "related_to", doc_key)
        try:
            link(conn, "rel_depends_on", key, "depends_on", vec_key)
        except Exception:
            pass
        if ch.get("text"):
            set_attr_value(conn, key, "text", ch["text"])
