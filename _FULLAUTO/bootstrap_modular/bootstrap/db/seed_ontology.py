
from .upsert_object import upsert_object
from .link import link
from .set_attr_value import set_attr_value

def seed_ontology(conn):
    for k, lbl in [
        ("object","Objet"), ("entity","Entité"),
        ("company","Entreprise"), ("provider","Fournisseur"),
        ("ai_provider","Fournisseur IA"),
        ("endpoint","Endpoint"), ("mga_endpoint","Endpoint MGA"),
        ("user","Utilisateur"), ("admin","Administrateur"),
        ("login","Identifiants"),
        ("project","Projet"),
        ("document","Document"), ("brief_doc","Brief"),
        ("spec_doc","Cahier des charges"), ("text_note","Note"),
        ("chunk","Chunk"),
        ("catalog","Catalogue JSON"),
        ("database","Base de données"),
        ("sqlite_db","SQLite"),
        ("mongodb_db","MongoDB"),
        ("postgres_db","PostgreSQL"),
        ("mysql_db","MySQL"),
        ("mariadb_db","MariaDB"),
        ("redis_db","Redis"),
        ("elasticsearch_db","Elasticsearch"),
        ("neo4j_db","Neo4j"),
        ("vector_db","Base vectorielle"),
        ("vector_index","Index vectoriel"),
        ("digitalproduct","Produit numérique"), ("product","Produit"),
        ("website","Site Web"),
        ("relation","Relation"),
        ("attribute","Attribut"),
        ("tag","Tag"), ("security","Sécurité"),
        ("auth","Authentification"), ("secretkey","Clé secrète"),
        ("text_value","Valeur textuelle")
    ]:
        upsert_object(conn, k, "object", lbl)

    for child, parent in [
        ("entity","object"),
        ("company","entity"),
        ("provider","company"),
        ("ai_provider","provider"),
        ("endpoint","object"),
        ("mga_endpoint","endpoint"),
        ("user","entity"),
        ("admin","user"),
        ("login","object"),
        ("project","entity"),
        ("document","object"),
        ("brief_doc","document"),
        ("spec_doc","document"),
        ("text_note","document"),
        ("chunk","object"),
        ("catalog","object"),
        ("database","object"),
        ("sqlite_db","database"),
        ("mongodb_db","database"),
        ("postgres_db","database"),
        ("mysql_db","database"),
        ("mariadb_db","database"),
        ("redis_db","database"),
        ("elasticsearch_db","database"),
        ("neo4j_db","database"),
        ("vector_db","database"),
        ("vector_index","object"),
        ("product","object"),
        ("digitalproduct","product"),
        ("website","digitalproduct"),
        ("relation","object"),
        ("attribute","object"),
        ("tag","object"),
        ("security","tag"),
        ("auth","object"),
        ("secretkey","object"),
        ("text_value","object")
    ]:
        link(conn, "rel_inherits_from", child, "inherits_from", parent)

    for rel_key, lbl, card in [
        ("inherits_from","hérite de","(1..n)->(0..1)"),
        ("depends_on","dépend de","(0..n)->(0..n)"),
        ("element_of","est élément de","(0..n)->(0..n)"),
        ("related_to","est lié à","(0..n)->(0..n)")
    ]:
        upsert_object(conn, rel_key, "relation", lbl, cardinality=card)

    attrs = [
        "name","ident","description","vector_ident",
        "path","owner","created_at","created_by",
        "db_host","db_port","db_user","db_pwd","db_path",
        "host","port","token","email","login","hash","text",
        "vectordb","index_type","metric","dim","model_name",
        "catalog_path"
    ]
    for a in attrs:
        upsert_object(conn, a, "attribute", a)

    set_attr_value(conn, "vector_db", "vectordb", "true")
    for klass in ["sqlite_db","mongodb_db","postgres_db","mysql_db","mariadb_db","redis_db","elasticsearch_db","neo4j_db"]:
        set_attr_value(conn, klass, "vectordb", "false")

    link(conn, "rel_depends_on", "product", "depends_on", "user")
    upsert_object(conn, "security", "tag", "Sécurité")
    upsert_object(conn, "auth", "object", "Authentification")
    link(conn, "rel_related_to", "auth", "related_to", "security")

    for a in attrs:
        link(conn, "rel_depends_on", a, "depends_on", "website")
