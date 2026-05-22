from pathlib import Path

MEW_HOME = Path.home() / ".mew"
ENVS_DIR = MEW_HOME / "envs"
REGISTRY_FILE = MEW_HOME / "registry.json"

MEW_HOME.mkdir(exist_ok=True)
ENVS_DIR.mkdir(exist_ok=True)