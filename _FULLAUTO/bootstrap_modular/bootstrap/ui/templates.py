from .assets import OPTIONS_JS

INSTALL_TEMPLATE = """<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>__TITLE__</title>
<style>
body{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;margin:0;padding:24px;background:#f7f7f9}
.card{max-width:980px;margin:0 auto;background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:24px;box-shadow:0 2px 10px rgba(0,0,0,.05)}
h1{margin:0 0 12px 0;font-size:22px}h2{font-size:16px;margin-top:20px}
label{display:block;margin:8px 0 4px;color:#374151}
input[type=text],input[type=email],input[type=password],input[type=number]{width:360px;max-width:100%;padding:10px;border:1px solid #d1d5db;border-radius:8px}
select{width:360px;max-width:100%;padding:10px;border:1px solid #d1d5db;border-radius:8px}
.row{display:flex;gap:24px;flex-wrap:wrap}.box{flex:1 1 300px;background:#fafafa;padding:16px;border:1px solid #eee;border-radius:8px}
.muted{color:#6b7280;font-size:12px}.ok{color:#059669}.err{color:#dc2626;white-space:pre-wrap}
button.primary{margin-top:16px;padding:12px 16px;border:0;background:#111827;color:#fff;border-radius:10px;cursor:pointer}
.list{margin:8px 0}.hidden{display:none}.mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.small{font-size:12px;color:#6b7280}
</style>
<script src="/assets/options.js"></script>
<script>const INSTALL_MODE="__MODE__"; const SUBMIT_PATH="__SUBMIT_PATH__";</script>
</head>
<body>
<div class="card">
  <h1>__TITLE__</h1>
  <p class="muted">Remplis les infos. À la validation, l’installation se fait et tu es redirigé(e) vers la page suivante.</p>

  <div class="row">
    <div class="box">
      <h2>1) Projet</h2>
      <label>Nom du projet</label>
      <input id="project_name" type="text" placeholder="Agence" value="__DEFAULT_NAME__"/>
      <div class="muted">Nom de la base (si SQLite) : <b id="db_preview">__DB_PREVIEW__</b></div>
    </div>

    <div class="box" id="box_admin">
      <h2>2) Administrateur</h2>
      <label>Identifiant</label><input id="admin_login" type="text" placeholder="admin"/>
      <label>Email</label><input id="admin_email" type="email" placeholder="admin@example.com"/>
      <label>Mot de passe</label><input id="admin_password" type="password" placeholder="••••••••"/>
      <div class="small">(Masqué automatiquement si “Interne + Agence”)</div>
    </div>
  </div>

  <div class="row">
    <div class="box">
      <h2>3) Bases de données</h2>
      <div id="db_checks" class="list"></div>
      <div id="db_sqlite" class="dbgrp">
        <div class="muted">SQLite est <b>toujours</b> créée en développement.</div>
      </div>
      <div id="db_mongodb" class="dbgrp hidden">
        <label>URI MongoDB</label>
        <input id="mongo_uri" type="text" placeholder="mongodb://user:pass@host:27017/dbname"/>
      </div>
      <div id="db_postgres" class="dbgrp hidden">
        <label>Host</label><input id="pg_host" type="text" placeholder="127.0.0.1"/>
        <label>Port</label><input id="pg_port" type="number" placeholder="5432"/>
        <label>Database</label><input id="pg_db" type="text" placeholder="mydb"/>
        <label>User</label><input id="pg_user" type="text" placeholder="user"/>
        <label>Password</label><input id="pg_pwd" type="password" placeholder="••••••••"/>
      </div>
      <div id="db_mysql" class="dbgrp hidden">
        <label>Host</label><input id="my_host" type="text" placeholder="127.0.0.1"/>
        <label>Port</label><input id="my_port" type="number" placeholder="3306"/>
        <label>Database</label><input id="my_db" type="text" placeholder="mydb"/>
        <label>User</label><input id="my_user" type="text" placeholder="user"/>
        <label>Password</label><input id="my_pwd" type="password" placeholder="••••••••"/>
      </div>
      <div id="db_mariadb" class="dbgrp hidden">
        <label>Host</label><input id="ma_host" type="text" placeholder="127.0.0.1"/>
        <label>Port</label><input id="ma_port" type="number" placeholder="3306"/>
        <label>Database</label><input id="ma_db" type="text" placeholder="mydb"/>
        <label>User</label><input id="ma_user" type="text" placeholder="user"/>
        <label>Password</label><input id="ma_pwd" type="password" placeholder="••••••••"/>
      </div>
      <div id="db_redis" class="dbgrp hidden">
        <label>Host</label><input id="re_host" type="text" placeholder="127.0.0.1"/>
        <label>Port</label><input id="re_port" type="number" placeholder="6379"/>
      </div>
      <div id="db_elasticsearch" class="dbgrp hidden">
        <label>URL</label><input id="es_host" type="text" placeholder="http://127.0.0.1:9200"/>
      </div>
      <div id="db_neo4j" class="dbgrp hidden">
        <label>URI</label><input id="nj_host" type="text" placeholder="bolt://127.0.0.1:7687"/>
        <label>User</label><input id="nj_user" type="text" placeholder="neo4j"/>
        <label>Password</label><input id="nj_pwd" type="password" placeholder="••••••••"/>
      </div>
    </div>

    <div class="box">
      <h2>4) IA (optionnel)</h2>
      <div class="list">
        <label><input type="checkbox" class="ai_provider" value="openai"/> OpenAI</label>
        <div style="margin-left:18px" id="openai_models"></div>
        <label><input type="checkbox" class="ai_provider" value="anthropic"/> Anthropic</label>
        <div style="margin-left:18px" id="anthropic_models"></div>
        <label><input type="checkbox" class="ai_provider" value="google"/> Google</label>
        <div style="margin-left:18px" id="google_models"></div>
        <label><input type="checkbox" class="ai_provider" value="mistral"/> Mistral</label>
        <div style="margin-left:18px" id="mistral_models"></div>
      </div>
      <div class="muted">Ne coche rien si tu n'as pas besoin d'IA maintenant.</div>
    </div>
  </div>

  <div class="row">
    <div class="box" id="box_mga">
      <h2>5) MGA</h2>
      <label>Host</label><input id="mga_host" type="text" placeholder="127.0.0.1" value="127.0.0.1"/>
      <label>Port (facultatif)</label><input id="mga_port" type="number" placeholder="8090"/>
      <label>Token (facultatif)</label><input id="mga_token" type="text" placeholder="(optionnel)"/>
      <div class="muted">Si le port est vide, on tentera 8090 puis le prochain libre.</div>
      <div class="small">(Masqué automatiquement si “Interne + Agence”)</div>
    </div>

    <div class="box">
      <h2>6) Assistance</h2>
      <label>Niveau</label>
      <select id="assistant_level">
        <option value="" selected>(laisser vide)</option>
        <option value="0">Assisté (pose des questions / crée des tâches)</option>
        <option value="1">Full auto</option>
      </select>
      <div class="muted">Si vide, on utilisera 0 par défaut.</div>
    </div>

    __CLIENT_SECTION__
  </div>

  <button class="primary" id="btn_install">Valider la configuration</button>
  <div id="msg" class="muted mono" style="margin-top:12px"></div>
</div>

<script>
function slugify(s){return (s||"").toLowerCase().trim().replace(/[^\\w\\s-]/g,"").replace(/[\\s-]+/g,"_").replace(/^_+|_+$/g,"")||"agence";}

function renderDBChecks(){
  const container = document.getElementById('db_checks');
  container.innerHTML = "";
  const dbs = (window.APP_OPTIONS && window.APP_OPTIONS.dbs) || [];
  dbs.forEach(d => {
    const id = 'db_' + d.key + '_cb';
    const lbl = document.createElement('label');
    lbl.innerHTML = '<input id="'+id+'" type="checkbox" class="db_choice" value="'+d.key+'" '+(d.devDefault?'checked':'')+'> '+d.label;
    container.appendChild(lbl);
  });
  document.querySelectorAll(".db_choice").forEach(cb => {
    const grp = document.getElementById("db_" + cb.value);
    const sync = () => grp && grp.classList.toggle("hidden", !cb.checked);
    cb.addEventListener("change", sync); sync();
  });
}

function renderAIProviderChecks(){
  const modelsCatalog = (window.APP_OPTIONS && window.APP_OPTIONS.aiModels) || {};
  document.querySelectorAll(".ai_provider").forEach(cb => {
    cb.addEventListener("change", e => {
      const provider = e.target.value;
      const host = document.getElementById(provider + "_models");
      if (e.target.checked) {
        host.innerHTML = "";
        (modelsCatalog[provider] || []).forEach(m => {
          const label = document.createElement("label");
          label.style.display = "block";
          label.innerHTML = '<input type="checkbox" class="ai_model" data-provider="'+provider+'" value="'+m+'"/> '+m;
          host.appendChild(label);
        });
      } else {
        host.innerHTML = "";
      }
    });
  });
}

function setupClientRadios(){
  const block = document.getElementById('client_block');
  if (!block) return;
  const list = (window.APP_OPTIONS && window.APP_OPTIONS.clients) || ["Agence"];
  const sel = document.getElementById('client_select');
  sel.innerHTML = list.map(c => '<option value="'+c+'">'+c+'</option>').join('');
  sel.value = "Agence";
  const radios = document.querySelectorAll('input[name="proj_type"]');
  const boxAdmin = document.getElementById('box_admin');
  const boxMGA = document.getElementById('box_mga');

  function syncVisibility(){
    const v = document.querySelector('input[name="proj_type"]:checked').value;
    const c = sel.value;
    const hide = (v === 'interne' && c === 'Agence');
    block.classList.toggle('hidden', v !== 'client');
    if (boxAdmin) boxAdmin.classList.toggle('hidden', hide);
    if (boxMGA) boxMGA.classList.toggle('hidden', hide);
  }

  radios.forEach(r => r.addEventListener('change', syncVisibility));
  sel.addEventListener('change', syncVisibility);
  syncVisibility();
}

document.addEventListener('DOMContentLoaded', () => {
  renderDBChecks();
  renderAIProviderChecks();
  setupClientRadios();
  const pn = document.getElementById('project_name');
  pn && pn.addEventListener('input', e => {
    const slug = slugify(e.target.value||"agence");
    const preview = document.getElementById('db_preview');
    if (preview) preview.textContent = slug + "_database.db";
  });
});

async function postJSON(path, payload){
  const r = await fetch(path,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(payload)});
  const t = await r.text(); try{ return JSON.parse(t);}catch(e){ throw new Error(path+" -> "+r.status+"\\n"+t); }
}

document.getElementById("btn_install").addEventListener("click", async ()=>{
  const msg=document.getElementById("msg");
  msg.className="muted mono"; msg.textContent="Installation en cours…";

  const projectName=(document.getElementById("project_name").value||"Agence").trim();

  const adminBoxHidden = document.getElementById("box_admin").classList.contains("hidden");
  const admin={
    login: adminBoxHidden ? "" : (document.getElementById("admin_login").value||"admin").trim(),
    email: adminBoxHidden ? "" : (document.getElementById("admin_email").value||"admin@example.com").trim(),
    password: adminBoxHidden ? "" : (document.getElementById("admin_password").value||"admin")
  };

  const providers=[];
  document.querySelectorAll(".ai_provider:checked").forEach(p=>{
    const ident=p.value; const models=[];
    document.querySelectorAll("#"+ident+"_models .ai_model:checked").forEach(m=>models.push(m.value));
    providers.push({provider:ident,models});
  });

  const dbs=[];
  document.querySelectorAll(".db_choice:checked").forEach(d=>{
    const v=d.value;
    if(v==="sqlite"){ dbs.push({type:"sqlite"}); }
    else if(v==="mongodb"){ dbs.push({type:"mongodb", mongo_uri:(document.getElementById("mongo_uri")?.value||"").trim()}); }
    else if(v==="postgres"){ dbs.push({type:"postgres", pg:{
      host:(document.getElementById("pg_host")?.value||"").trim(),
      port:parseInt(document.getElementById("pg_port")?.value||"5432",10),
      db:(document.getElementById("pg_db")?.value||"").trim(),
      user:(document.getElementById("pg_user")?.value||"").trim(),
      pwd:(document.getElementById("pg_pwd")?.value||"")
    }}); }
    else if(v==="mysql"){ dbs.push({type:"mysql", my:{
      host:(document.getElementById("my_host")?.value||"").trim(),
      port:parseInt(document.getElementById("my_port")?.value||"3306",10),
      db:(document.getElementById("my_db")?.value||"").trim(),
      user:(document.getElementById("my_user")?.value||"").trim(),
      pwd:(document.getElementById("my_pwd")?.value||"")
    }}); }
    else if(v==="mariadb"){ dbs.push({type:"mariadb", ma:{
      host:(document.getElementById("ma_host")?.value||"").trim(),
      port:parseInt(document.getElementById("ma_port")?.value||"3306",10),
      db:(document.getElementById("ma_db")?.value||"").trim(),
      user:(document.getElementById("ma_user")?.value||"").trim(),
      pwd:(document.getElementById("ma_pwd")?.value||"")
    }}); }
    else if(v==="redis"){ dbs.push({type:"redis", re:{
      host:(document.getElementById("re_host")?.value||"").trim(),
      port:parseInt(document.getElementById("re_port")?.value||"6379",10)
    }}); }
    else if(v==="elasticsearch"){ dbs.push({type:"elasticsearch", es:{ host:(document.getElementById("es_host")?.value||"").trim() }}); }
    else if(v==="neo4j"){ dbs.push({type:"neo4j", nj:{
      host:(document.getElementById("nj_host")?.value||"").trim(),
      user:(document.getElementById("nj_user")?.value||"").trim(),
      pwd:(document.getElementById("nj_pwd")?.value||"")
    }}); }
  });

  let project_type="interne"; let client="Agence";
  const r=document.querySelector('input[name="proj_type"]:checked');
  if(r){ project_type=r.value; if(project_type==="client"){ const s=document.getElementById("client_select"); if(s) client=s.value||"Agence"; } }

  const mgaBoxHidden = document.getElementById("box_mga").classList.contains("hidden");
  const mga = mgaBoxHidden ? {host:"",port:null,token:""} : {
    host:(document.getElementById("mga_host")?.value||"127.0.0.1").trim(),
    port: document.getElementById("mga_port")?.value ? parseInt(document.getElementById("mga_port").value,10) : null,
    token:(document.getElementById("mga_token")?.value||"").trim()
  };

  try{
    const payload={
      project:{ name: projectName, type: project_type, client: client },
      admin, dbs, ai_providers: providers,
      mga, assistance:(()=>{ const v=document.getElementById("assistant_level").value; return (v===""||v===null)?0:parseInt(v,10); })()
    };

    const res = await postJSON(SUBMIT_PATH, payload);
    if(res.status!=="completed") throw new Error(res.message||"Installation incomplète");

    if(INSTALL_MODE==="agency"){
      window.location.href="/admin";
    }else{
      window.location.href = (res.admin_url || ("/admin/"+encodeURIComponent(res.slug)));
    }
  }catch(e){
    msg.className="err"; msg.textContent="❌ "+e.message;
  }
});
</script>
</body></html>
"""

CLIENT_SECTION = """
<div class="box">
  <h2>Type de projet</h2>
  <label><input type="radio" name="proj_type" value="interne" checked> Interne</label>
  <label><input type="radio" name="proj_type" value="client"> Projet client</label>
  <div id="client_block" class="hidden" style="margin-top:8px">
    <label>Client</label>
    <select id="client_select" style="width:360px;max-width:100%;padding:10px;border:1px solid #d1d5db;border-radius:8px"></select>
    <div class="muted">Liste fictive pour test (non connectée).</div>
  </div>
</div>
"""

ADMIN_HTML = """<!doctype html>
<meta charset="utf-8"/>
<title>Admin — Agence</title>
<style>
body{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;padding:24px;background:#f7f7f9}
.card{max-width:1100px;margin:auto;background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:24px}
h1{margin:0 0 12px 0;font-size:22px}
label{display:block;margin:6px 0 4px}
input,button,select{padding:10px;border-radius:8px;border:1px solid #d1d5db}
button{background:#111827;color:#fff;border:0;cursor:pointer}
a.button{display:inline-block;padding:10px 12px;border-radius:8px;background:#111827;color:#fff;text-decoration:none}
.muted{color:#6b7280;font-size:12px}
.tabs{display:flex;gap:8px;margin:12px 0 16px}
.tab{padding:8px 10px;border-radius:8px;border:1px solid #d1d5db;background:#f3f4f6;cursor:pointer}
.tab.active{background:#111827;color:#fff;border-color:#111827}
.section{display:none}
.section.active{display:block}
.grid{display:grid;grid-template-columns: 1.2fr 2fr 1.8fr; gap:16px}
.box{border:1px solid #e5e7eb;border-radius:10px;padding:12px;background:#fafafa;min-height:120px}
.list{max-height:380px;overflow:auto;border:1px solid #eee;border-radius:8px;background:#fff}
.row{display:flex;justify-content:space-between;gap:8px;padding:8px 10px;border-bottom:1px solid #f1f5f9}
.row:hover{background:#f9fafb}
.key{font-family:ui-monospace,Menlo,monospace}
.badge{display:inline-block;background:#e5e7eb;border-radius:999px;padding:2px 8px;font-size:12px;margin-left:6px}
ul{margin:8px 0 0 16px;padding:0}
</style>

<div class="card">
  <h1>Admin — Agence</h1>
  <div class="tabs">
    <div id="tab-create" class="tab active">Créer un projet</div>
    <div id="tab-catalog" class="tab">Catalogue RDF</div>
  </div>

  <div id="sec-create" class="section active">
    <p class="muted">Créer un nouveau projet.</p>
    <label>Nom du projet</label>
    <input id="proj" type="text" placeholder="MonProjet"/>
    <div class="muted">La base (SQLite dev) sera <b><span id="dbp">monprojet_database.db</span></b></div>
    <p><a id="go" class="button" href="#">Créer le projet</a></p>
  </div>

  <div id="sec-catalog" class="section">
    <div class="grid">
      <div class="box">
        <b>Types d’objets</b>
        <div class="muted" style="margin-top:6px">Sélectionne un type pour lister ses instances.</div>
        <select id="type_select" style="width:100%;margin-top:8px"></select>
        <div id="type_stats" class="muted" style="margin-top:8px"></div>
      </div>

      <div class="box">
        <b>Objets du type</b> <span id="obj_count" class="badge">0</span>
        <div id="obj_list" class="list" style="margin-top:8px"></div>
      </div>

      <div class="box">
        <b>Détails & relations</b>
        <div id="obj_details" class="muted" style="margin-top:8px">Sélectionne un objet pour voir ses relations.</div>
      </div>
    </div>
  </div>
</div>

<script>
const tCreate = document.getElementById('tab-create');
const tCat = document.getElementById('tab-catalog');
const sCreate = document.getElementById('sec-create');
const sCat = document.getElementById('sec-catalog');
function activate(tab){
  [tCreate,tCat].forEach(el=>el.classList.remove('active'));
  [sCreate,sCat].forEach(el=>el.classList.remove('active'));
  if(tab==='catalog'){ tCat.classList.add('active'); sCat.classList.add('active'); loadTypes(); }
  else { tCreate.classList.add('active'); sCreate.classList.add('active'); }
}
tCreate.onclick=()=>activate('create');
tCat.onclick=()=>activate('catalog');

function slugify(s){return (s||"").toLowerCase().trim().replace(/[^\\w\\s-]/g,"").replace(/[\\s-]+/g,"_").replace(/^_+|_+$/g,"")||"monprojet";}
const i=document.getElementById('proj');const dbp=document.getElementById('dbp');const go=document.getElementById('go');
i.addEventListener('input',()=>{dbp.textContent=slugify(i.value||"monprojet")+"_database.db";});
go.addEventListener('click', (e)=>{
  e.preventDefault();
  const name = i.value || "MonProjet";
  const url = "/project/new?name=" + encodeURIComponent(name);
  window.location.href = url;
});

const sel = document.getElementById('type_select');
const list = document.getElementById('obj_list');
const count = document.getElementById('obj_count');
const details = document.getElementById('obj_details');
const typeStats = document.getElementById('type_stats');

async function loadTypes(){
  sel.innerHTML = '<option>(chargement…)</option>';
  typeStats.textContent = '';
  const r = await fetch('/api/types'); const j = await r.json();
  const items = j.types || [];
  sel.innerHTML = items.map(t => '<option value="'+t.key+'">'+t.key+' ('+t.count+')</option>').join('');
  if(items.length){ sel.value = items[0].key; loadObjects(); }
  else { list.innerHTML = ''; count.textContent = '0'; details.textContent = 'Aucun type disponible.'; }
}

async function loadObjects(){
  const tk = sel.value;
  const r = await fetch('/api/objects?type='+encodeURIComponent(tk));
  const j = await r.json();
  const objs = j.objects || [];
  count.textContent = String(objs.length);
  list.innerHTML = objs.map(o => (
    '<div class="row" data-key="'+o.key+'"><div><span class="key">'+o.key+'</span></div><div>'+ (o.label||'') +'</div></div>'
  )).join('');
  details.textContent = 'Sélectionne un objet pour voir ses relations.';
  Array.from(list.querySelectorAll('.row')).forEach(row=>{
    row.addEventListener('click', ()=> showRelations(row.dataset.key));
  });
  typeStats.textContent = 'Type: '+tk;
}

async function showRelations(key){
  details.innerHTML = '<div class="muted">Chargement…</div>';
  const r = await fetch('/api/object/relations?key='+encodeURIComponent(key));
  const j = await r.json();
  const sect = (arr) => {
    if(!arr || !arr.length) return '<li><i>(aucune)</i></li>';
    return arr.map(it => '<li><span class="key">'+it.src+'</span> — <b>'+it.predicate+'</b> → <span class="key">'+it.tgt+'</span></li>').join('');
  };
  details.innerHTML = `
    <div><b>Objet</b> : <span class="key">${key}</span></div>
    <div style="margin-top:8px"><b>inherits_from</b><ul>${sect(j.inherits_from)}</ul></div>
    <div style="margin-top:8px"><b>depends_on</b><ul>${sect(j.depends_on)}</ul></div>
    <div style="margin-top:8px"><b>element_of</b><ul>${sect(j.element_of)}</ul></div>
    <div style="margin-top:8px"><b>related_to</b><ul>${sect(j.related_to)}</ul></div>
  `;
}

sel.addEventListener('change', loadObjects);
</script>
"""

PROJECT_HOME_TPL = """<!doctype html>
<meta charset="utf-8"/>
<title>__NAME__ — Accueil</title>
<style>
body{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;padding:24px;background:#f7f7f9}
.card{max-width:880px;margin:auto;background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:24px}
a.button{display:inline-block;padding:10px 12px;border-radius:8px;background:#111827;color:#fff;text-decoration:none}
.muted{color:#6b7280;font-size:12px}
</style>
<div class="card">
  <h1>__NAME__ — Accueil</h1>
  <p class="muted">Projet <b>__SLUG__</b> — Type: __TYPE__ — Client: __CLIENT__</p>
  <p><a class="button" href="/project/config/__SLUG__">Configurer (brief, CDC, texte libre)</a></p>
</div>
"""

CONFIG_HTML = """<!doctype html>
<meta charset="utf-8"/>
<title>Configuration projet</title>
<style>
body{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;padding:24px;background:#f7f7f9}
.card{max-width:880px;margin:auto;background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:24px}
h1{margin:0 0 12px 0;font-size:22px}
.muted{color:#6b7280;font-size:12px}
label{display:block;margin:6px 0 4px}
input,textarea,button{padding:10px;border-radius:8px;border:1px solid #d1d5db}
button{background:#111827;color:#fff;border:0;cursor:pointer}
.row{display:flex;gap:16px;flex-wrap:wrap;margin-top:12px}
.area{width:100%;min-height:120px}
</style>
<div class="card">
  <h1>Configuration du projet — <span id="proj"></span></h1>
  <p class="muted">Éléments requis : <b>Brief (fichier)</b>, <b>Cahier des charges (fichier)</b>. Facultatif : <b>Texte libre</b>.</p>

  <div class="row">
    <div class="box">
      <label>Brief (PDF/DOC/texte)</label>
      <input id="brief_file" type="file" />
    </div>
    <div class="box">
      <label>Cahier des charges (PDF/DOC/texte)</label>
      <input id="cdc_file" type="file" />
    </div>
  </div>

  <label>Texte libre (facultatif)</label>
  <textarea class="area" id="free_text" placeholder="Idée, notes, etc."></textarea>

  <button id="send">Envoyer</button>
  <div id="msg" class="muted" style="margin-top:8px"></div>
</div>
<script>
const slug = location.pathname.split('/').pop();
document.getElementById('proj').textContent = slug;

document.getElementById('send').addEventListener('click', async ()=>{
  const msg = document.getElementById('msg');
  msg.textContent = "Envoi en cours…";
  const fd = new FormData();
  const bf = document.getElementById('brief_file').files[0];
  const cf = document.getElementById('cdc_file').files[0];
  if (bf) fd.append('brief', bf);
  if (cf) fd.append('cdc', cf);
  fd.append('free_text', document.getElementById('free_text').value || "");

  try{
    const r = await fetch('/api/project/config/upload/'+slug, { method:'POST', body: fd });
    const t = await r.text(); let j; try{ j=JSON.parse(t);}catch(e){ throw new Error(t); }
    if (j.status !== "ok") throw new Error(j.message||"Erreur");
    msg.textContent = "✅ Configuration enregistrée.";
  }catch(e){
    msg.textContent = "❌ " + e.message;
  }
});
</script>
"""

CONFIG_HTML_ADMIN = """<!doctype html>
<meta charset="utf-8"/>
<title>Admin projet — Configuration</title>
<style>
body{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;padding:24px;background:#f7f7f9}
.card{max-width:880px;margin:auto;background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:24px}
h1{margin:0 0 12px 0;font-size:22px}
.muted{color:#6b7280;font-size:12px}
label{display:block;margin:6px 0 4px}
input,textarea,button{padding:10px;border-radius:8px;border:1px solid #d1d5db}
button{background:#111827;color:#fff;border:0;cursor:pointer}
.row{display:flex;gap:16px;flex-wrap:wrap;margin-top:12px}
.area{width:100%;min-height:120px}
</style>
<div class="card">
  <h1>Administration du projet — <span id="proj_admin"></span></h1>
  <p class="muted">Téléverse les documents requis et renseigne un texte libre si nécessaire.</p>

  <div class="row">
    <div class="box">
      <label>Brief (PDF/DOC/texte)</label>
      <input id="brief_file" type="file" />
    </div>
    <div class="box">
      <label>Cahier des charges (PDF/DOC/texte)</label>
      <input id="cdc_file" type="file" />
    </div>
  </div>

  <label>Texte libre (facultatif)</label>
  <textarea class="area" id="free_text" placeholder="Idée, notes, etc."></textarea>

  <button id="send">Enregistrer la configuration</button>
  <div id="msg" class="muted" style="margin-top:8px"></div>
</div>
<script>
const slug = location.pathname.split('/').pop();
document.getElementById('proj_admin').textContent = slug;

document.getElementById('send').addEventListener('click', async ()=>{
  const msg = document.getElementById('msg');
  msg.textContent = "Envoi en cours…";
  const fd = new FormData();
  const bf = document.getElementById('brief_file').files[0];
  const cf = document.getElementById('cdc_file').files[0];
  if (bf) fd.append('brief', bf);
  if (cf) fd.append('cdc', cf);
  fd.append('free_text', document.getElementById('free_text').value || "");

  try{
    const r = await fetch('/api/project/config/upload/'+slug, { method:'POST', body: fd });
    const t = await r.text(); let j; try{ j=JSON.parse(t);}catch(e){ throw new Error(t); }
    if (j.status !== "ok") throw new Error(j.message||"Erreur");
    msg.textContent = "✅ Configuration enregistrée.";
    setTimeout(()=>{ window.location.href="/project/"+slug+"/"; }, 600);
  }catch(e){
    msg.textContent = "❌ " + e.message;
  }
});
</script>
"""
