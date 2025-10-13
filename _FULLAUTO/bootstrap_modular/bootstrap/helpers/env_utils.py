
from pathlib import Path
def read_env(base_dir: Path) -> dict:
    envp = base_dir / ".env"
    env = {}
    if envp.exists():
        for line in envp.read_text(encoding="utf-8").splitlines():
            if "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"')
    return env
