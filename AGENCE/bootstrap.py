#!/usr/bin/env python3
# Single-file bootstrap — catalogues minimaux (template dynamique + install wizard),
# hooks (base -> alias), scenario d'installation, serveur unique (statique + API sur 8081),
# ouverture auto du navigateur.

import os, json, time, webbrowser
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime, timezone
from threading import Thread

PORT = int(os.environ.get("BOOTSTRAP_PORT", "8081"))  # http + api on the same port

# -----------------------------
# Utils (logs & fs)
# -----------------------------
def now_iso():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

def ensure_dirs(root):
    for p in ["catalogs/templates", "catalogs/ui", "catalogs/data", "public", "logs", "reports", "config"]:
        (root / p).mkdir(parents=True, exist_ok=True)

def write_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)

def append_log(root, line):
    with open(root / "logs/bootstrap.log", "a", encoding="utf-8") as f:
        f.write(line.rstrip() + "\n")

def append_report(root, ident, payload):
    entry = {"timestamp": now_iso(), "ident": ident, **payload}
    with open(root / "reports/install_report.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

# -----------------------------
# Catalogs (minima)
# -----------------------------
def install_min_catalogs(root: Path):
    # dynamic template pieces
    write_json(root / "catalogs/templates/lang.json",
               {"identity":{"ident":"lang","name":"Langue"},
                "definitions":{"value":"en"}})
    write_json(root / "catalogs/templates/head.json",
               {"identity":{"ident":"head","name":"Head"},
                "definitions":{"value":"<head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1'><title>LaNostrAI - Setup</title></head>"}})
    write_json(root / "catalogs/templates/body.json",
               {"identity":{"ident":"body","name":"Body"},
                "definitions":{"value":"<body><!-- placeholder:dynamic_content --></body>"}})
    write_json(root / "catalogs/templates/dynamic_template.json",
               {"identity":{"ident":"dynamic_template","name":"Template HTML dynamique"},
                "definitions":{"value":"<!DOCTYPE html><html lang=\"{lang}\">{head}{body}</html>"},
                "context":{"relations":{"consumes":["lang","head","body"]}}})

    # data catalogs
    write_json(root / "catalogs/data/ai_providers.json",
               {"providers":[
                   {"ident":"openai","label":"OpenAI"},
                   {"ident":"anthropic","label":"Anthropic"},
                   {"ident":"google","label":"Google"},
                   {"ident":"mistral","label":"Mistral"}
               ]})
    write_json(root / "catalogs/data/db_types.json",
               {"types":[
                   {"ident":"json","label":"JSON (fichier)",
                    "params_schema":[{"name":"file_path","type":"text","placeholder":"config/data.json"}]},
                   {"ident":"sqlite","label":"SQLite",
                    "params_schema":[{"name":"file_path","type":"text","placeholder":"config/data.sqlite"}]},
                   {"ident":"mongodb","label":"MongoDB",
                    "params_schema":[{"name":"host","type":"text"},{"name":"port","type":"number"},
                                     {"name":"user","type":"text"},{"name":"password","type":"password"},{"name":"db","type":"text"}]},
                   {"ident":"postgres","label":"PostgreSQL",
                    "params_schema":[{"name":"host","type":"text"},{"name":"port","type":"number"},
                                     {"name":"user","type":"text"},{"name":"password","type":"password"},{"name":"db","type":"text"}]}
               ]})

    # pages/modules/forms
    write_json(root / "catalogs/ui/page_install.json",
               {"identity":{"ident":"page_install","name":"Page d'installation"},
                "context":{"relations":{"loads":["module_config"]}}})
    write_json(root / "catalogs/ui/page_home.json",
               {"identity":{"ident":"page_home","name":"Page d'accueil"},
                "context":{"relations":{"loads":["module_login"]}}})
    write_json(root / "catalogs/ui/module_config.json",
               {"identity":{"ident":"module_config","name":"Module de configuration"},
                "definitions":{"value":"FORM_INSTALL"},
                "context":{"relations":{"contains":["form_install"]}}})
    write_json(root / "catalogs/ui/module_login.json",
               {"identity":{"ident":"module_login","name":"Module de login"},
                "definitions":{"value":"FORM_LOGIN"},
                "context":{"relations":{"contains":["form_login"]}}})

    write_json(root / "catalogs/ui/form_install.json",
               {"identity":{"ident":"form_install","name":"Formulaire d'installation"},
                "context":{"relations":{"elements":["section_admin","section_ai","section_db","btn_submit_install"]}}})
    write_json(root / "catalogs/ui/form_login.json",
               {"identity":{"ident":"form_login","name":"Formulaire de login"},
                "context":{"relations":{"elements":["input_username","input_password","btn_submit_login"]}}})

    # admin section + fields
    write_json(root / "catalogs/ui/section_admin.json",
               {"identity":{"ident":"section_admin","name":"Section Admin"},
                "context":{"relations":{"elements":["input_admin_email","input_admin_login","input_admin_password"]}}})
    write_json(root / "catalogs/ui/input_admin_email.json",
               {"identity":{"ident":"input_admin_email","name":"Email admin"},
                "definitions":{"type":"email","placeholder":"you@example.com","required":True}})
    write_json(root / "catalogs/ui/input_admin_login.json",
               {"identity":{"ident":"input_admin_login","name":"Login admin"},
                "definitions":{"type":"text","placeholder":"admin","required":True}})
    write_json(root / "catalogs/ui/input_admin_password.json",
               {"identity":{"ident":"input_admin_password","name":"Mot de passe admin"},
                "definitions":{"type":"password","placeholder":"********","required":True}})

    # IA & BDD (mode "sélection + Ajouter")
    write_json(root / "catalogs/ui/section_ai.json",
               {"identity":{"ident":"section_ai","name":"Section IA"},
                "definitions":{"mode":"adder","group":["select_ai_provider","input_ai_key","btn_add_ai_provider"]}})
    write_json(root / "catalogs/ui/section_db.json",
               {"identity":{"ident":"section_db","name":"Section BDD"},
                "definitions":{"mode":"adder","group":["select_db_type","fieldset_db_params","chk_default_db","btn_add_db_option"]}})

    # login form generic (username au lieu de login pour éviter conflit global)
    write_json(root / "catalogs/ui/input_username.json",
               {"identity":{"ident":"input_username","name":"Identifiant"},
                "definitions":{"type":"text","placeholder":"admin","required":True}})
    write_json(root / "catalogs/ui/input_password.json",
               {"identity":{"ident":"input_password","name":"Mot de passe"},
                "definitions":{"type":"password","placeholder":"********","required":True}})
    write_json(root / "catalogs/ui/btn_submit_login.json",
               {"identity":{"ident":"btn_submit_login","name":"Bouton login"},
                "definitions":{"type":"button","action":"submit_login","label":"Se connecter"}})
    write_json(root / "catalogs/ui/btn_submit_install.json",
               {"identity":{"ident":"btn_submit_install","name":"Bouton installer"},
                "definitions":{"type":"button","action":"submit_install","label":"Installer"}})

# -----------------------------
# Hooks (base -> alias)
# -----------------------------
HOOK_REGISTRY = {"hook_before": [], "hook_after": [], "hook_onfailure": []}

def register_hook_alias(base_hook: str, alias_ident: str, actions):
    HOOK_REGISTRY.setdefault(base_hook, []).append({"alias": alias_ident, "actions": actions})

def call_hook(root: Path, base_hook: str, context: dict):
    append_log(root, f"[hook] {base_hook} entered (aliases={len(HOOK_REGISTRY.get(base_hook, []))})")
    for entry in HOOK_REGISTRY.get(base_hook, []):
        alias = entry["alias"]
        for action in entry.get("actions", []):
            try:
                append_log(root, f"[hook] run {alias} -> {action}")
                if action == "render_install_page":
                    render_install_page(root)
                elif action == "persist_install_snapshot":
                    persist_install_snapshot(root, context)
                elif action == "switch_to_home":
                    render_home_login(root)
                else:
                    append_log(root, f"[hook] unknown action: {action}")
            except Exception as e:
                append_log(root, f"[hook][error] {alias}:{action} failed: {e}")
    append_log(root, f"[hook] {base_hook} exited")

def persist_install_snapshot(root: Path, context: dict):
    write_json(root / "config/install_snapshot.json", {"status": "in_progress", "ctx": context, "created_at": now_iso()})
    append_report(root, "install_snapshot", {"status": "in_progress"})

# -----------------------------
# Rendering helpers
# -----------------------------
def render_from_dynamic_template(root: Path, body_html: str):
    with open(root / "catalogs/templates/lang.json","r",encoding="utf-8") as f:
        lang = json.load(f)["definitions"]["value"]
    with open(root / "catalogs/templates/head.json","r",encoding="utf-8") as f:
        head = json.load(f)["definitions"]["value"]
    html = "<!DOCTYPE html><html lang='"+lang+"'>"+head+"<body>"+body_html+"</body></html>"
    (root / "public").mkdir(exist_ok=True)
    with open(root / "public/index.html","w",encoding="utf-8") as f:
        f.write(html)
    append_log(root, "[render] public/index.html updated")

def render_install_page(root: Path):
    # Page d'install épurée (pas de commentaires, pas de "modèle préféré")
    body_html = """
<div id='app' style='max-width:900px;margin:40px auto;font-family:system-ui, -apple-system, Segoe UI, Roboto;'>

  <h1>Installation</h1>

  <h2>Admin</h2>
  <label>Email<br><input id='admin_email' type='email' placeholder='you@example.com' required></label><br><br>
  <label>Login<br><input id='admin_login' type='text' placeholder='admin' required></label><br><br>
  <label>Mot de passe<br><input id='admin_password' type='password' placeholder='********' required></label>

  <h2>IA</h2>
  <div id='ai_current'></div>
  <button id='ai_add'>Ajouter</button>
  <ul id='ai_list'></ul>

  <h2>Base de donnees</h2>
  <div id='db_current'></div>
  <button id='db_add'>Ajouter</button>
  <ul id='db_list'></ul>

  <hr style='margin:24px 0'>
  <button id='submit_install' style='padding:10px 16px;'>Installer</button>

  <p id='msg' style='color:green;'></p>
</div>

<script>
async function loadJSON(path){ const r = await fetch(path); return await r.json(); }
let providers = []; let dbTypes = [];
let aiItems = []; let dbItems = [];

function ui_ai_current(){
  const wrap = document.createElement('div');
  const selProv = document.createElement('select');
  selProv.id = 'ai_provider';
  selProv.innerHTML = '<option value=\"\">-- provider --</option>';
  providers.forEach(p=>{ const o=document.createElement('option'); o.value=p.ident; o.text=p.label; selProv.append(o); });
  const key = document.createElement('input'); key.type='text'; key.placeholder='API key'; key.size=34; key.id='ai_key'; key.style.marginLeft='8px';
  wrap.append('Provider: ', selProv, ' Cle: ', key);
  return wrap;
}

function render_ai_list(){
  const ul = document.getElementById('ai_list'); ul.innerHTML='';
  aiItems.forEach((it, i)=>{
    const li = document.createElement('li');
    li.textContent = it.provider + ' (clé masquée)';
    const del = document.createElement('button'); del.textContent = 'Supprimer'; del.style.marginLeft='8px';
    del.onclick = ()=>{ aiItems.splice(i,1); render_ai_list(); };
    li.appendChild(del); ul.appendChild(li);
  });
}

function ui_db_current(){
  const wrap = document.createElement('div');
  const selType = document.createElement('select'); selType.id = 'db_type';
  selType.innerHTML = '<option value=\"\">-- type de base --</option>';
  dbTypes.forEach(t=>{ const o=document.createElement('option'); o.value=t.ident; o.text=t.label; selType.append(o); });
  const paramsZone = document.createElement('span'); paramsZone.id='db_params'; paramsZone.style.marginLeft='8px';
  const chkDefault = document.createElement('input'); chkDefault.type='checkbox'; chkDefault.id='db_default'; chkDefault.title='Par defaut'; chkDefault.style.marginLeft='8px';
  selType.addEventListener('change', ()=>{
    const t = dbTypes.find(x=>x.ident===selType.value); paramsZone.innerHTML='';
    if (t) {
      (t.params_schema||[]).forEach(field=>{
        const inp=document.createElement('input');
        inp.type=(field.type==='number'?'number':(field.type==='password'?'password':'text'));
        inp.placeholder=field.placeholder||field.name; inp.dataset.name=field.name; inp.style.marginLeft='6px';
        paramsZone.append(inp);
      });
    }
  });
  wrap.append('Type: ', selType, paramsZone, ' Par defaut ', chkDefault);
  return wrap;
}

function render_db_list(){
  const ul = document.getElementById('db_list'); ul.innerHTML='';
  dbItems.forEach((it, i)=>{
    const li = document.createElement('li');
    const defTxt = it.is_default ? ' [defaut]' : '';
    li.textContent = it.type + defTxt;
    const del = document.createElement('button'); del.textContent = 'Supprimer'; del.style.marginLeft='8px';
    del.onclick = ()=>{ dbItems.splice(i,1); render_db_list(); };
    li.appendChild(del); ul.appendChild(li);
  });
}

async function init(){
  providers = (await loadJSON('/catalogs/data/ai_providers.json')).providers;
  dbTypes   = (await loadJSON('/catalogs/data/db_types.json')).types;

  document.getElementById('ai_current').appendChild(ui_ai_current());
  document.getElementById('db_current').appendChild(ui_db_current());

  document.getElementById('ai_add').onclick = ()=>{
    const prov = document.getElementById('ai_provider').value;
    const key  = document.getElementById('ai_key').value.trim();
    if (!prov || !key) return;
    aiItems.push({ provider: prov, key: key, active: true });
    document.getElementById('ai_current').innerHTML=''; document.getElementById('ai_current').appendChild(ui_ai_current());
    render_ai_list();
  };

  document.getElementById('db_add').onclick = ()=>{
    const type = document.getElementById('db_type').value;
    if (!type) return;
    const params = {};
    document.querySelectorAll('#db_params input').forEach(inp=>{ params[inp.dataset.name]=inp.value; });
    let isDef = document.getElementById('db_default').checked;
    if (isDef) { dbItems.forEach(x=> x.is_default=false); } // garantir unicite visuelle
    dbItems.push({ type, params, is_default: isDef, active: true });
    document.getElementById('db_current').innerHTML=''; document.getElementById('db_current').appendChild(ui_db_current());
    render_db_list();
  };

  document.getElementById('submit_install').onclick = async ()=>{
    const admin = {
      email: document.getElementById('admin_email').value.trim(),
      login: document.getElementById('admin_login').value.trim(),
      password: document.getElementById('admin_password').value
    };

    // normalisation silencieuse: s'il n'y a aucune BDD par defaut, mettre la premiere
    if (dbItems.length>0 && !dbItems.some(x=>x.is_default)) { dbItems[0].is_default = true; }

    const r = await fetch('/api/install', {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify({ admin, ai: aiItems, db: dbItems })
    });
    const j = await r.json();
    const msg = document.getElementById('msg'); msg.textContent = j.message || 'OK';
    if (j.status === 'completed') setTimeout(()=> location.reload(), 600);
  };
}
init();
</script>
"""
    render_from_dynamic_template(root, body_html)

def render_home_login(root: Path):
    body_html = """
<div style='max-width:520px;margin:40px auto;font-family:system-ui'>
  <h1>Connexion</h1>
  <form onsubmit='event.preventDefault(); doLogin();'>
    <label>Identifiant<br><input id='username' type='text' required></label><br><br>
    <label>Mot de passe<br><input id='pwd' type='password' required></label><br><br>
    <button type='submit'>Se connecter</button>
  </form>
  <p id='msg' style='color:crimson'></p>
</div>
<script>
async function doLogin(){
  const payload = { login: document.getElementById('username').value, password: document.getElementById('pwd').value };
  const r = await fetch('/api/login', { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload) });
  const j = await r.json();
  const msg = document.getElementById('msg');
  if(j.status==='ok'){
    msg.style.color='green'; msg.textContent='Connecte !';
    const redirect = j.redirect || '/';
    window.location.href = redirect;
  } else {
    msg.textContent = j.message || 'Echec';
  }
}
</script>
"""
    render_from_dynamic_template(root, body_html)

def render_home_app(root: Path):
    # Page d'accueil minimaliste (cadre vierge dynamique)
    body_html = """
<div style='max-width:900px;margin:40px auto;font-family:system-ui'>
  <h1>Accueil</h1>
  <div id='app_home'><!-- contenu dynamique a venir --></div>
</div>
"""
    render_from_dynamic_template(root, body_html)

# -----------------------------
# Scenario: install_wizard (GET/EXECUTE/VALIDATE/RENDER)
# -----------------------------
def scenario_install_wizard(root: Path):
    ctx = {"phase": "install"}
    append_log(root, "[scenario] install_wizard::GET")
    write_json(root / "config/install_snapshot.json", {"status": "in_progress", "created_at": now_iso()})
    append_report(root, "install_snapshot", {"status": "in_progress"})
    append_log(root, "[scenario] install_wizard::EXECUTE")
    append_log(root, "[scenario] install_wizard::VALIDATE")
    append_log(root, "[scenario] install_wizard::RENDER")
    call_hook(root, "hook_after", ctx)

# -----------------------------
# Hook aliases registration
# -----------------------------
def register_install_hooks():
    register_hook_alias("hook_after", "hook_after_config_install", actions=["render_install_page"])

# -----------------------------
# Unified HTTP server (static + API on same port)
# -----------------------------
class AppHandler(BaseHTTPRequestHandler):
    def _json(self, code, obj):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(obj, ensure_ascii=False).encode("utf-8"))

    def _read_json(self):
        ln = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(ln) if ln else b"{}"
        try: return json.loads(data.decode("utf-8"))
        except: return {}

    def do_GET(self):
        root = Path(__file__).parent.resolve()

        if self.path.startswith("/api/"):
            return self._json(200, {"status":"api-ok","hint":"POST /api/install or /api/login"})

        if self.path == "/favicon.ico":
            self.send_response(204); self.end_headers(); return

        # Serve catalogs (JSON) and other files if under /catalogs
        fs_path = (root / self.path.lstrip("/")).resolve()
        catalogs_root = (root / "catalogs").resolve()
        if str(fs_path).startswith(str(catalogs_root)) and fs_path.exists():
            try:
                data = fs_path.read_bytes()
                self.send_response(200)
                self.send_header("Content-Type", "application/json" if fs_path.suffix == ".json" else "application/octet-stream")
                self.end_headers()
                self.wfile.write(data)
                return
            except Exception:
                pass

        # / -> public/index.html
        if self.path in ("/", "/index.html"):
            index_path = root / "public" / "index.html"
            if index_path.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(index_path.read_bytes())
                return

        self.send_response(404); self.end_headers()

    def do_POST(self):
        root = Path(__file__).parent.resolve()

        if self.path == "/api/install":
            payload = self._read_json()
            admin_ok = bool(payload.get("admin", {}).get("login") and payload.get("admin", {}).get("password"))
            dbs = payload.get("db", []) or []
            if not admin_ok:
                return self._json(400, {"status":"error","message":"Admin login & password requis"})

            # Normalisation silencieuse: si aucune base n'est par defaut, forcer la premiere (s'il y en a)
            if dbs and not any(d.get("is_default") for d in dbs):
                dbs[0]["is_default"] = True
                payload["db"] = dbs

            write_json(root / "config/system_config.json", payload)
            write_json(root / "config/admin_account.json", payload.get("admin"))
            append_report(root, "install_completed", {"status": "completed"})
            append_log(root, "[install] configuration persisted (system_config.json)")

            render_home_login(root)
            return self._json(200, {"status":"completed","message":"Installation terminee. Redirection..."})

        if self.path == "/api/login":
            payload = self._read_json()
            try:
                with open(root / "config/admin_account.json","r",encoding="utf-8") as f:
                    admin = json.load(f)
            except FileNotFoundError:
                return self._json(400, {"status":"error","message":"Aucun compte admin configure"})
            ok = (payload.get("login")==admin.get("login")) and (payload.get("password")==admin.get("password"))
            if ok:
                # Rendre la page d'accueil et proposer l'URL de redirection
                render_home_app(root)
                return self._json(200, {"status":"ok", "redirect": "/"})
            return self._json(200, {"status":"error","message":"Identifiants invalides"})

        self._json(404, {"status":"error","message":"Not found"})

def start_and_open(root: Path, port: int):
    httpd = HTTPServer(("", port), AppHandler)

    def run():
        print(f"[server] http on http://localhost:{port}")
        append_log(root, f"[server] http on {port}")
        httpd.serve_forever()

    Thread(target=run, daemon=True).start()

    time.sleep(0.6)  # laisser index.html etre ecrit
    try:
        webbrowser.open_new_tab(f"http://localhost:{port}/")
        append_log(root, "[browser] auto-opened install page")
    except Exception as e:
        append_log(root, f"[browser][error] {e}")

    while True:
        time.sleep(1)

# -----------------------------
# Main
# -----------------------------
def main():
    root = Path(__file__).parent.resolve()
    ensure_dirs(root); append_log(root, "[bootstrap] start")
    install_min_catalogs(root); append_log(root, "[bootstrap] catalogs installed")

    # hooks: base -> alias
    register_install_hooks()
    append_log(root, "[bootstrap] hooks registered")

    # scenario: install (calls hook_after => render_install_page)
    scenario_install_wizard(root); append_log(root, "[bootstrap] scenario_install_wizard executed")

    # single server + auto-open
    start_and_open(root, PORT)

if __name__ == "__main__":
    main()
