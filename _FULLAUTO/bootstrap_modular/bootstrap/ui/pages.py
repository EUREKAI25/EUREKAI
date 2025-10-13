
from .templates import INSTALL_TEMPLATE, ADMIN_HTML, PROJECT_HOME_TPL, CONFIG_HTML, CONFIG_HTML_ADMIN, CLIENT_SECTION
from ..helpers.slugify import slugify

def render_install_page(title: str, submit_path: str, default_name: str, include_client: bool, mode: str):
    html = INSTALL_TEMPLATE
    html = html.replace("__TITLE__", title)
    html = html.replace("__MODE__", mode)
    html = html.replace("__SUBMIT_PATH__", submit_path)
    html = html.replace("__DEFAULT_NAME__", default_name)
    html = html.replace("__DB_PREVIEW__", slugify(default_name) + "_database.db")
    html = html.replace("__CLIENT_SECTION__", CLIENT_SECTION if include_client else "")
    return html

def render_home(name, slug, proj_type, client):
    html = PROJECT_HOME_TPL
    return (html
            .replace("__NAME__", name)
            .replace("__SLUG__", slug)
            .replace("__TYPE__", proj_type)
            .replace("__CLIENT__", client))
