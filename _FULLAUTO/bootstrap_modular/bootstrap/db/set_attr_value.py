
from .upsert_object import upsert_object
from .link import link
from ._obj_helpers import upsert_label
def set_attr_value(conn, target_key: str, attr_key: str, value_fr: str):
    upsert_object(conn, attr_key, "attribute", attr_key)
    val_key = f"{target_key}__{attr_key}"
    upsert_object(conn, val_key, attr_key, f"{attr_key} de {target_key}")
    link(conn, "rel_inherits_from", val_key, "inherits_from", attr_key)
    link(conn, "rel_element_of", val_key, "element_of", target_key)
    upsert_label(conn, val_key, value_fr or "")
