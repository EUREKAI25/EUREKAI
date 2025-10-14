import os, json, sqlite3, urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from .helpers.slugify import slugify
from .helpers.ensure_dir import ensure_dir
from .helpers.write_env_file import write_env_file
from .helpers.env_utils import read_env

from .db.init_graph_schema import init_graph_schema
from .db.seed_ontology import seed_ontology
from .db.seed_project_instance import seed_project_instance

from .ui.pages import render_install_page, render_home

HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", "8081"))
BASE_DIR = Path(os.environ.get("BASE_DIR") or Path(__file__).resolve().parents[2])

def agency_db_path():
    env = read_env(BASE_DIR)
    slug = env.get("PROJECT_SLUG", "agence")
    return (BASE_DIR / "data" / f"{slug}_database.db")

def _build_options_js():
    import json as _json
    dbp = agency_db_path()
    fallback_dbs = [
        {"key":"sqlite","label":"SQLite","devDefault":True,"isVector":False},
        {"key":"vector","label":"Base vectorielle V","devDefault":True,"isVector":True},
        {"key":"mongodb","label":"MongoDB","devDefault":False,"isVector":False},
        {"key":"postgres","label":"PostgreSQL","devDefault":False,"isVector":False},
        {"key":"mysql","label":"MySQL","devDefault":False,"isVector":False},
        {"key":"mariadb","label":"MariaDB","devDefault":False,"isVector":False},
        {"key":"redis","label":"Redis","devDefault":False,"isVector":False},
        {"key":"elasticsearch","label":"Elasticsearch","devDefault":False,"isVector":False},
        {"key":"neo4j","label":"Neo4j","devDefault":False,"isVector":False},
    ]
    dbs = []
    if not dbp.exists():
        dbs = fallback_dbs
    else:
        with sqlite3.connect(str(dbp)) as conn:
            cur = conn.cursor()
            cur.execute("SELECT id FROM objects WHERE key='database'")
            row = cur.fetchone()
            if not row:
                dbs = fallback_dbs
            else:
                parent_id = row[0]
                cur.execute("""
                    SELECT DISTINCT o.key, COALESCE(l.FR,o.key)
                    FROM objects o
                    JOIN rel_inherits_from r ON r.src_object = o.id
                    LEFT JOIN labels l ON l.object_id = o.id
                    WHERE r.target_object=? AND (o.key LIKE '%_db' OR o.key='vector_db')
                    ORDER BY o.key
                """, (parent_id,))
                seen=set()
                for k,label in cur.fetchall():
                    if k in seen: 
                        continue
                    seen.add(k)
                    short = k[:-3] if k.endswith("_db") else k
                    is_vector = False
                    try:
                        cur.execute("SELECT id FROM objects WHERE key=?", (k,))
                        oid = cur.fetchone()[0]
                        cur.execute("SELECT o.id FROM objects o WHERE o.key='vectordb'")
                        aid = cur.fetchone()[0]
                        cur.execute("SELECT value FROM properties WHERE object_id=? AND attr_id=?", (oid, aid))
                        v = cur.fetchone()
                        is_vector = (v and str(v[0]).lower() in ("1","true","yes","y","on"))
                    except Exception:
                        is_vector = (k == "vector_db" or short == "vector")
                    dbs.append({
                        "key": short,
                        "label": f"{label} {'V' if is_vector else ''}".rstrip(),
                        "devDefault": (short in ("sqlite","vector")),
                        "isVector": is_vector
                    })
    aiModels = {
        "openai": ["gpt-4o","gpt-4o-mini","o4-mini","gpt-4-turbo","gpt-3.5-turbo"],
        "anthropic": ["claude-3-opus","claude-3-sonnet","claude-3-haiku"],
        "google": ["gemini-1.5-pro","gemini-1.5-flash","palm-2"],
        "mistral": ["mistral-large","mistral-medium","mistral-small","mixtral-8x7b"]
    }
    clients = ["Agence","Client Alpha","Client Beta","Client Gamma"]
    payload = {"dbs": dbs, "aiModels": aiModels, "clients": clients}
    return "window.APP_OPTIONS = " + _json.dumps(payload, ensure_ascii=False) + ";"

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
            meta_path = proj_dir / "meta.json"
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
            js = _build_options_js()
            self.send_response(200)
            self.send_header("Content-Type","application/javascript; charset=utf-8")
            self.end_headers()
            self.wfile.write(js.encode("utf-8"))
            return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
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

        self.send_response(404)
        self.end_headers()

    def handle_install(self, payload: dict, root_env: bool):
        from .db.set_attr_value import set_attr_value

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
        if not any(d.get("type")=="vector" for d in dbs):
            dbs.append({"type":"vector"})

        data_dir = BASE_DIR / "data"
        ensure_dir(data_dir)
        sqlite_path = data_dir / (slug + "_database.db")

        init_graph_schema(sqlite_path)
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
            set_attr_value(conn, f"{slug}_sqlite", "db_path", str(sqlite_path.resolve()))

        proj_dir = BASE_DIR / "projects" / slug
        ensure_dir(proj_dir)
        (proj_dir/"README.md").write_text("# "+name+"\\nType: "+proj_type+"\\nClient: "+client+"\\n", encoding="utf-8")
        (proj_dir/"meta.json").write_text(json.dumps({"name": name, "slug": slug, "type": proj_type, "client": client}, ensure_ascii=False), encoding="utf-8")
        ensure_dir(proj_dir/"uploads")

        env = {"PROJECT_NAME": name, "PROJECT_SLUG": slug, "PROJECT_TYPE": proj_type, "PROJECT_CLIENT": client}
        write_env_file(proj_dir/".env", env)
        if root_env:
            write_env_file(BASE_DIR/".env", env)

        if root_env:
            return self.ok_json({"status":"completed","slug": slug,"home_url": "/project/"+slug+"/","admin_url": "/admin","message":"Agence installée."})
        else:
            return self.ok_json({"status":"completed","slug": slug,"home_url": "/project/"+slug+"/","admin_url": "/admin/"+slug,"message":"Projet installé."})

    def ok_html(self, html: str):
        self.send_response(200)
        self.send_header("Content-Type","text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def ok_json(self, obj: dict):
        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.end_headers()
        self.wfile.write(json.dumps(obj).encode("utf-8"))

def run():
    print(f"UI d'installation: http://{HOST}:{PORT}")
    HTTPServer((HOST, PORT), Handler).serve_forever()
