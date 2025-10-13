
from ._obj_helpers import _obj_id, upsert_label
def upsert_object(conn, key: str, type_key: str = None, label_fr: str = None, cardinality: str = None):
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO objects(key, type_key, cardinality) VALUES(?,?,?)", (key, type_key, cardinality))
    if type_key is not None:
        cur.execute("UPDATE objects SET type_key=? WHERE key=? AND (type_key IS NULL OR type_key!=?)", (type_key, key, type_key))
    if cardinality is not None:
        cur.execute("UPDATE objects SET cardinality=? WHERE key=?", (cardinality, key))
    oid = _obj_id(conn, key)
    if label_fr is not None and oid is not None:
        upsert_label(conn, key, label_fr)
    conn.commit()
    return oid
