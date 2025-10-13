
import sqlite3
def init_graph_schema(db_path):
    db_path.parent.mkdir(parents=True, exist_ok=True)
    db_path.touch(exist_ok=True)
    with sqlite3.connect(str(db_path)) as conn:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS objects(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE NOT NULL,
            type_key TEXT,
            cardinality TEXT
        );""")
        cur.execute("""
        CREATE TABLE IF NOT EXISTS labels(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            object_id INTEGER NOT NULL,
            FR TEXT, EN TEXT, DE TEXT, ES TEXT, IT TEXT, PO TEXT,
            FOREIGN KEY(object_id) REFERENCES objects(id) ON DELETE CASCADE
        );""")
        for rel in ("rel_inherits_from","rel_depends_on","rel_element_of","rel_related_to"):
            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {rel}(
                src_object INTEGER NOT NULL,
                predicate TEXT NOT NULL,
                target_object INTEGER NOT NULL,
                UNIQUE(src_object,predicate,target_object),
                FOREIGN KEY(src_object) REFERENCES objects(id) ON DELETE CASCADE,
                FOREIGN KEY(target_object) REFERENCES objects(id) ON DELETE CASCADE
            );""")
        conn.commit()
