
import os, json, sqlite3, urllib.parse, hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from .helpers.slugify import slugify
from .helpers.ensure_dir import ensure_dir
from .helpers.write_env_file import write_env_file
from .helpers.env_utils import read_env

from .db.init_graph_schema import init_graph_schema
from .db.seed_ontology import seed_ontology
from .db.seed_project_instance import seed_project_instance

from .ui.assets import OPTIONS_JS
from .ui.pages import render_install_page, render_home

HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", "8081"))
BASE_DIR = Path(os.environ.get("BASE_DIR") or Path(__file__).resolve().parents[2])

def agency_db_path():
    env = read_env(BASE_DIR)
    slug = env.get("PROJECT_SLUG", "agence")
    return (BASE_DIR / "data" / f"{slug}_database.db")

def label_fr(conn, key: str) -> str:
    cur = conn.cursor()
    cur.execute("SELECT id FROM objects WHERE key=?", (key,))
    row = cur.fetchone()
    if not row: return ""
    oid = row[0]
    cur.execute("SELECT FR FROM labels WHERE object_id=?", (oid,))
    r = cur.fetchone()
    return r[0] if r and r[0] else ""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/" or path.startswith("/index"):
            page = render_install_page("Installation — Agence", "/api/install", "Agence", include_client=False, mode="agency")
            return self.ok_html(page)

        if path == "/admin":
            from .ui.templates import ADMIN_HTML
            return self.ok_html(ADMIN_HTML)

        if path == "/project/new":
            q = urllib.parse.parse_qs(parsed.query or "")
            name = q.get("name", ["MonProjet"])[0]
            page = render_install_page("Nouveau projet", "/api/project/install", name, include_client=True, mode="project")
            return self.ok_html(page)

        if path.startswith("/project/config/"):
            from .ui.templates import CONFIG_HTML
            return self.ok_html(CONFIG_HTML)

        if path.startswith("/project/") and path.endswith("/"):
            slug = path.split("/")[2]
            proj_dir = BASE_DIR / "projects" / slug
            meta_path = proj_dir/"meta.json"
            if meta_path.exists():
                meta = json.loads(meta_path.read_text(encoding="utf-8") or "{}")
            else:
                meta = {"name": slug, "type": "interne", "client": "Agence"}
            page = render_home(meta.get("name", slug), slug, meta.get("type","interne"), meta.get("client","Agence"))
            return self.ok_html(page)

        if path.startswith("/admin/"):
            from .ui.templates import CONFIG_HTML_ADMIN
            return self.ok_html(CONFIG_HTML_ADMIN)

        if path == "/api/status":
            return self.ok_json({"ok": True})

        if path == "/assets/options.js":
            self.send_response(200); self.send_header("Content-Type","application/javascript; charset=utf-8"); self.end_headers()
            self.wfile.write(OPTIONS_JS.encode("utf-8")); return

        # --- API catalogue RDF ---
        if path == "/api/types":
            dbp = agency_db_path()
            if not dbp.exists():
                return self.ok_json({"types": []})
            with sqlite3.connect(str(dbp)) as conn:
                cur = conn.cursor()
                cur.execute("SELECT COALESCE(type_key,'(none)') AS t, COUNT(*) FROM objects GROUP BY COALESCE(type_key,'(none)') ORDER BY t")
                types = [{"key": t, "count": c} for (t, c) in cur.fetchall()]
            return self.ok_json({"types": types})

        if path == "/api/objects":
            q = urllib.parse.parse_qs(parsed.query or "")
            t = q.get("type", [""])[0]
            dbp = agency_db_path()
            if not dbp.exists():
                return self.ok_json({"objects": []})
            with sqlite3.connect(str(dbp)) as conn:
                cur = conn.cursor()
                if t:
                    cur.execute("SELECT key FROM objects WHERE COALESCE(type_key,'(none)')=? ORDER BY key LIMIT 2000", (t,))
                else:
                    cur.execute("SELECT key FROM objects ORDER BY key LIMIT 2000")
                keys = [r[0] for r in cur.fetchall()]
                objs = [{"key": k, "label": label_fr(conn, k)} for k in keys]
            return self.ok_json({"objects": objs})

        if path == "/api/object/relations":
            q = urllib.parse.parse_qs(parsed.query or "")
            key = q.get("key", [""])[0]
            dbp = agency_db_path()
            if not dbp.exists() or not key:
                return self.ok_json({"inherits_from": [], "depends_on": [], "element_of": [], "related_to": []})
            with sqlite3.connect(str(dbp)) as conn:
                cur = conn.cursor()
                cur.execute("SELECT id FROM objects WHERE key=?", (key,))
                r = cur.fetchone()
                if not r:
                    return self.ok_json({"inherits_from": [], "depends_on": [], "element_of": [], "related_to": []})
                oid = r[0]
                def fetch(rel_table):
                    cur.execute(f"SELECT src_object,predicate,target_object FROM {rel_table} WHERE src_object=? OR target_object=?", (oid, oid))
                    rows = cur.fetchall()
                    out=[]
                    for (s,p,t) in rows:
                        cur.execute("SELECT key FROM objects WHERE id=?", (s,)); sk=cur.fetchone()
                        cur.execute("SELECT key FROM objects WHERE id=?", (t,)); tk=cur.fetchone()
                        out.append({"src": sk[0] if sk else str(s), "predicate": p, "tgt": tk[0] if tk else str(t)})
                    return out
                return self.ok_json({
                    "inherits_from": fetch("rel_inherits_from"),
                    "depends_on":    fetch("rel_depends_on"),
                    "element_of":    fetch("rel_element_of"),
                    "related_to":    fetch("rel_related_to")
                })

        if path == "/favicon.ico":
            self.send_response(404); self.end_headers(); return

        self.send_response(404); self.end_headers()

    def do_POST(self):
        ctype = self.headers.get("Content-Type","")
        if self.path.startswith("/api/project/config/upload/") and ctype.startswith("multipart/form-data;"):
            slug = self.path.split("/")[-1]
            return self.handle_upload(slug, ctype)

        ln = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(ln)
        try:
            data = json.loads(raw or b"{}")
        except Exception:
            data = {}

        if self.path == "/api/install":
            return self.handle_install(data, root_env=True)

        if self.path == "/api/project/install":
            return self.handle_install(data, root_env=False)

        self.send_response(404); self.end_headers()

    # ---- impl ----
    def handle_install(self, payload: dict, root_env: bool):
        from datetime import datetime
        project = payload.get("project") or {}
        admin = payload.get("admin") or {}
        dbs = payload.get("dbs") or [{"type":"sqlite"}]
        providers = payload.get("ai_providers") or []
        mga = payload.get("mga") or {}
        assistance = payload.get("assistance", 0)

        name = project.get("name") or "Agence"
        proj_type = project.get("type") or "interne"
        client = project.get("client") or "Agence"
        slug = slugify(name)
        if not any(d.get("type")=="sqlite" for d in dbs):
            dbs = [{"type":"sqlite"}] + dbs

        data_dir = BASE_DIR / "data"; ensure_dir(data_dir)
        sqlite_path = data_dir / (slug + "_database.db")

        from .db.init_graph_schema import init_graph_schema
        from .db.seed_ontology import seed_ontology
        from .db.seed_project_instance import seed_project_instance

        init_graph_schema(sqlite_path)
        import sqlite3
        with sqlite3.connect(str(sqlite_path)) as conn:
            seed_ontology(conn)
            seed_project_instance(
                conn,
                site_slug=slug,
                site_name=name,
                is_agency=root_env,
                dbs=dbs,
                providers=providers,
                mga=mga,
                admin_login=(admin.get("login") or "admin"),
                admin_email=(admin.get("email") or "admin@example.com"),
                admin_pwd=(admin.get("password") or "admin"),
                client=client,
                proj_type=proj_type
            )
            from .db.set_attr_value import set_attr_value
            set_attr_value(conn, f"{slug}_sqlite", "db_path", str(sqlite_path.resolve()))

        proj_dir = BASE_DIR / "projects" / slug; ensure_dir(proj_dir)
        (proj_dir/"README.md").write_text("# "+name+"\nType: "+proj_type+"\nClient: "+client+"\n", encoding="utf-8")
        (proj_dir/"meta.json").write_text(json.dumps({"name": name, "slug": slug, "type": proj_type, "client": client}, ensure_ascii=False), encoding="utf-8")
        ensure_dir(proj_dir/"uploads")

        env = {"PROJECT_NAME": name, "PROJECT_SLUG": slug, "PROJECT_TYPE": proj_type, "PROJECT_CLIENT": client}
        write_env_file(proj_dir/".env", env)
        if root_env: write_env_file(BASE_DIR/".env", env)

        if root_env:
            return self.ok_json({"status":"completed","slug": slug,"home_url": "/project/"+slug+"/","admin_url": "/admin","message":"Agence installée."})
        else:
            return self.ok_json({"status":"completed","slug": slug,"home_url": "/project/"+slug+"/","admin_url": "/admin/"+slug,"message":"Projet installé."})

    def handle_upload(self, slug: str, content_type: str):
        try:
            boundary = content_type.split("boundary=")[1]
        except Exception:
            self.send_response(400); self.end_headers(); return
        boundary = boundary.encode("utf-8")
        ln = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(ln)
        parts = body.split(b"--"+boundary)
        dest = BASE_DIR / "projects" / slug / "uploads"; ensure_dir(dest)

        saved = []; free_text = ""
        for part in parts:
            if not part or part in (b"--\r\n", b"--"): continue
            try:
                header_block, file_data = part.split(b"\r\n\r\n", 1)
            except ValueError:
                continue
            headers = header_block.decode("utf-8", "ignore").split("\r\n")
            disposition = next((h for h in headers if h.lower().startswith("content-disposition:")), "")
            if file_data.endswith(b"\r\n"): file_data = file_data[:-2]
            name = ""; filename = ""
            for token in disposition.split(";"):
                token = token.strip()
                if token.startswith("name="): name = token.split("=",1)[1].strip().strip('"')
                if token.startswith("filename="): filename = token.split("=",1)[1].strip().strip('"')
            if filename:
                safe = filename.replace("/","_").replace("\\","_")
                (dest/safe).write_bytes(file_data)
                saved.append((name, safe))
            else:
                val = file_data.decode("utf-8","ignore")
                if name == "free_text": free_text = val

        db_path = BASE_DIR / "data" / f"{slug}_database.db"
        if db_path.exists():
            import sqlite3
            with sqlite3.connect(str(db_path)) as conn:
                from .db.set_attr_value import set_attr_value
                for field, fname in saved:
                    if field == "brief":
                        set_attr_value(conn, f"{slug}_brief", "path", str((dest/fname).resolve()))
                    elif field == "cdc":
                        set_attr_value(conn, f"{slug}_spec", "path", str((dest/fname).resolve()))
                if free_text.strip():
                    set_attr_value(conn, f"{slug}_idea", "text", free_text.strip())

        return self.ok_json({"status":"ok","saved": [n for _,n in saved], "message":"Pièces enregistrées."})

    # ---- utils http ----
    def ok_html(self, html: str):
        self.send_response(200); self.send_header("Content-Type","text/html; charset=utf-8"); self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def ok_json(self, obj: dict):
        self.send_response(200); self.send_header("Content-Type","application/json"); self.end_headers()
        self.wfile.write(json.dumps(obj).encode("utf-8"))

def run():
    print(f"UI d'installation: http://{HOST}:{PORT}")
    HTTPServer((HOST, PORT), Handler).serve_forever()
