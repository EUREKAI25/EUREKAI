
def write_env_file(env_path, mapping: dict):
    lines = [f'{k}="{str(v).replace("\n","\\n")}"' for k,v in mapping.items()]
    env_path.write_text("\n".join(lines), encoding="utf-8")
