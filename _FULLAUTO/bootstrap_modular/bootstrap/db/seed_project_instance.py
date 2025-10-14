import hashlib, json
from pathlib import Path
from datetime import datetime

from .upsert_object import upsert_object
from .set_attr_value import set_attr_value
from .link import link

BASE_DIR = Path(__file__).resolve().parents[2]

def _now_iso():
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

def seed_project_instance(conn, site_slug: str, site_name: str, is_agency: bool,
                          dbs: list, providers: list, mga: dict,
                          admin_login: str, admin_email: str, admin_pwd: str,
                          client: str, proj_type: str):
    proj_key = site_slug
    upsert_object(conn, proj_key, "project", site_name)
    website_key = f"{site_slug}_website"
    upsert_object(conn, website_key, "website", f"Site {site_name}")
    link(conn, "rel_element_of", website_key, "element_of", proj_key)
    set_attr_value(conn, proj_key, "name", site_name)
    set_attr_value(conn, proj_key, "ident", site_slug)
    if client: set_attr_value(conn, proj_key, "owner", client)
    set_attr_value(conn, proj_key, "description", f"Projet {site_name}")

    if not (proj_type == "interne" and (client or "agence").lower() == "agence"):
        admin_key = f"{site_slug}_admin"
        upsert_object(conn, admin_key, "admin", f"Admin {site_name}")
        link(conn, "rel_element_of", admin_key, "element_of", proj_key)
        login_key = f"{site_slug}_admin_login"
        upsert_object(conn, login_key, "login", f"Login {site_name}")
        link(conn, "rel_related_to", login_key, "related_to", admin_key)
        link(conn, "rel_element_of", login_key, "element_of", proj_key)
        set_attr_value(conn, login_key, "login", admin_login or "")
        set_attr_value(conn, login_key, "email", admin_email or "")

    sqlite_key = f"{site_slug}_sqlite"
    upsert_object(conn, sqlite_key, "sqlite_db", f"SQLite {site_name}")
    link(conn, "rel_element_of", sqlite_key, "element_of", proj_key)
    set_attr_value(conn, sqlite_key, "vectordb", "false")

    type_map = {
        "mongodb":"mongodb_db","postgres":"postgres_db","mysql":"mysql_db","mariadb":"mariadb_db",
        "redis":"redis_db","elasticsearch":"elasticsearch_db","neo4j":"neo4j_db","vector":"vector_db"
    }

    want_vector = any(d.get("type") == "vector" for d in dbs)
    cat_dir = BASE_DIR / "data" / "catalogs" / site_slug
    if want_vector:
        cat_dir.mkdir(parents=True, exist_ok=True)
        meta = {
            "backend": "catalog",
            "catalog_path": str((cat_dir / "catalog.json").as_posix()),
            "dim": 0,
            "metric": "",
            "model_name": "",
            "created_at": _now_iso(),
            "version": 1
        }
        (cat_dir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        if not (cat_dir / "catalog.json").exists():
            (cat_dir / "catalog.json").write_text("[]", encoding="utf-8")

    for d in dbs:
        t = d.get("type")
        if t == "sqlite":
            continue
        klass = type_map.get(t)
        if not klass:
            continue
        key = f"{site_slug}_{t}"
        upsert_object(conn, key, klass, f"{t.upper()} {site_name}")
        link(conn, "rel_element_of", key, "element_of", proj_key)

        if t == "mongodb":
            set_attr_value(conn, key, "db_host", d.get("mongo_uri",""))
            set_attr_value(conn, key, "vectordb", "false")
        elif t == "postgres":
            pg = (d.get("pg") or {})
            for k in ("host","db","user","pwd"):
                set_attr_value(conn, key, "db_"+("path" if k=="db" else k), pg.get(k,""))
            set_attr_value(conn, key, "db_port", str(pg.get("port","") or ""))
            set_attr_value(conn, key, "vectordb", "false")
        elif t in ("mysql","mariadb"):
            pref = {"mysql":"my","mariadb":"ma"}[t]
            m = (d.get(pref) or {})
            for k in ("host","db","user","pwd"):
                set_attr_value(conn, key, "db_"+("path" if k=="db" else k), m.get(k,""))
            set_attr_value(conn, key, "db_port", str(m.get("port","") or ""))
            set_attr_value(conn, key, "vectordb", "false")
        elif t == "redis":
            re_ = (d.get("re") or {})
            set_attr_value(conn, key, "db_host", re_.get("host",""))
            set_attr_value(conn, key, "db_port", str(re_.get("port","") or ""))
            set_attr_value(conn, key, "vectordb", "false")
        elif t == "elasticsearch":
            es = (d.get("es") or {})
            set_attr_value(conn, key, "db_host", es.get("host",""))
            set_attr_value(conn, key, "vectordb", "false")
        elif t == "neo4j":
            nj = (d.get("nj") or {})
            set_attr_value(conn, key, "db_host", nj.get("host",""))
            set_attr_value(conn, key, "db_user", nj.get("user",""))
            set_attr_value(conn, key, "db_pwd",  nj.get("pwd",""))
            set_attr_value(conn, key, "vectordb", "false")
        elif t == "vector":
            set_attr_value(conn, key, "db_path", str(cat_dir))
            set_attr_value(conn, key, "vectordb", "true")
            set_attr_value(conn, key, "index_type", "catalog")
            set_attr_value(conn, key, "metric", "")
            set_attr_value(conn, key, "dim", "0")
            vidx = f"{site_slug}_vector_catalog"
            upsert_object(conn, vidx, "catalog", f"Catalogue {site_name}")
            link(conn, "rel_depends_on", vidx, "depends_on", key)
            link(conn, "rel_element_of", vidx, "element_of", proj_key)
            set_attr_value(conn, vidx, "catalog_path", str((cat_dir / "catalog.json").as_posix()))

    if mga and (mga.get("host") or mga.get("port") or mga.get("token")):
        mga_key = f"{site_slug}_mga"
        upsert_object(conn, mga_key, "mga_endpoint", f"MGA {site_name}")
        link(conn, "rel_element_of", mga_key, "element_of", proj_key)
        for k in ("host","token"):
            set_attr_value(conn, mga_key, k, mga.get(k,""))
        set_attr_value(conn, mga_key, "port", str(mga.get("port") or ""))

    upsert_object(conn, "security", "tag", "Sécurité")
    upsert_object(conn, "auth", "object", "Authentification")
    link(conn, "rel_related_to", "auth", "related_to", "security")

    user_ident = (admin_login or "admin").lower()
    sk_key = f"openai_{user_ident}_secret_key"
    upsert_object(conn, sk_key, "secretkey", f"Clé OpenAI ({user_ident})")
    link(conn, "rel_related_to", sk_key, "related_to", "security")
    hashed = hashlib.sha256(f"{site_slug}:{user_ident}".encode("utf-8")).hexdigest()
    set_attr_value(conn, sk_key, "hash", hashed)

    for doc_key, klass, label in [
        (f"{site_slug}_brief", "brief_doc", f"Brief {site_name}"),
        (f"{site_slug}_spec", "spec_doc", f"Cahier des charges {site_name}"),
        (f"{site_slug}_idea", "text_note", f"Idée {site_name}")
    ]:
        upsert_object(conn, doc_key, klass, label)
        link(conn, "rel_element_of", doc_key, "element_of", proj_key)
