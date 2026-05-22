import shutil
from pathlib import Path

from mew.config import ENVS_DIR


class Storage:

    @staticmethod
    def env_path(name: str, env_id: str) -> Path:
        return ENVS_DIR / f"{name}-{env_id}"

    @staticmethod
    def delete_env(path: str):
        shutil.rmtree(path, ignore_errors=True)