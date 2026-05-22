import os
import subprocess
from pathlib import Path

from mew.config import ENVS_DIR
from mew.core.ids import generate_id
from mew.models.environment import Environment
from mew.registry import Registry


registry = Registry()


class Scanner:

    @staticmethod
    def sync_venvs():

        existing = registry.get_all()

        existing_paths = {
            env.path for env in existing
        }

        synced = []

        if not ENVS_DIR.exists():
            return synced

        for env_dir in ENVS_DIR.iterdir():

            if not env_dir.is_dir():
                continue

            activate_path = (
                env_dir / "Scripts" / "activate.bat"
            )

            if not activate_path.exists():
                continue

            path_str = str(env_dir)

            if path_str in existing_paths:
                continue

            name_parts = env_dir.name.rsplit("-", 1)

            if len(name_parts) == 2:
                name, env_id = name_parts
            else:
                name = env_dir.name
                env_id = generate_id()

            env = Environment(
                id=env_id,
                name=name,
                backend="venv",
                python_version="unknown",
                path=path_str,
                created_at="synced"
            )

            registry.add(env)

            synced.append(env)

        return synced

    @staticmethod
    def sync_conda():

        synced = []

        try:

            output = subprocess.check_output(
                ["conda", "env", "list"],
                text=True
            )

        except Exception:

            return synced

        existing = registry.get_all()

        existing_names = {
            f"{env.name}-{env.id}"
            for env in existing
            if env.backend == "conda"
        }

        lines = output.splitlines()

        for line in lines:

            if line.startswith("#"):
                continue

            parts = line.split()

            if len(parts) < 2:
                continue

            env_name = parts[0]

            if env_name in existing_names:
                continue

            if "-" in env_name:

                split = env_name.rsplit("-", 1)

                name = split[0]
                env_id = split[1]

            else:

                name = env_name
                env_id = generate_id()

            env = Environment(
                id=env_id,
                name=name,
                backend="conda",
                python_version="unknown",
                path=f"conda:{env_name}",
                created_at="synced"
            )

            registry.add(env)

            synced.append(env)

        return synced