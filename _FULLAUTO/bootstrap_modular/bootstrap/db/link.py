
from ._obj_helpers import _obj_id
def link(conn, table: str, src_key: str, predicate: str, tgt_key: str):
    cur = conn.cursor()
    sid = _obj_id(conn, src_key); tid = _obj_id(conn, tgt_key)
    if sid is None or tid is None:
        raise ValueError(f"link: unknown key(s): {src_key} -> {tgt_key}")
    cur.execute(f"INSERT OR IGNORE INTO {table}(src_object,predicate,target_object) VALUES(?,?,?)", (sid, predicate, tid))
    conn.commit()
