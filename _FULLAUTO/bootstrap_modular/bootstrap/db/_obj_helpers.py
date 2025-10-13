
def _obj_id(conn, key: str) -> int:
    cur = conn.cursor()
    cur.execute("SELECT id FROM objects WHERE key=?", (key,))
    row = cur.fetchone()
    return row[0] if row else None

def upsert_label(conn, key: str, fr_value: str):
    oid = _obj_id(conn, key)
    if oid is None: return
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO labels(object_id, FR) VALUES(?,?)", (oid, fr_value))
    cur.execute("UPDATE labels SET FR=? WHERE object_id=? AND (FR IS NULL OR FR='')", (fr_value, oid))
    conn.commit()
