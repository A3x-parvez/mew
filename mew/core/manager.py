from datetime import datetime

from mew.backends.venv import VenvBackend
from mew.backends.conda import CondaBackend
from mew.core.ids import generate_id
from mew.core.storage import Storage
from mew.models.environment import Environment
from mew.registry import Registry


class Manager:

    def __init__(self):
        self.registry = Registry()

    def create_venv(self, name: str, python_cmd: str):
        env_id = generate_id()

        path = Storage.env_path(name, env_id)

        VenvBackend.create(
            path=str(path),
            python_executable=python_cmd
        )

        env = Environment(
            id=env_id,
            name=name,
            backend="venv",
            python_version=python_cmd,
            path=str(path),
            created_at=str(datetime.now())
        )

        self.registry.add(env)

        return env

    def create_conda(self, name: str, python_version: str):
        env_id = generate_id()

        CondaBackend.create(
            name=f"{name}-{env_id}",
            python_version=python_version
        )

        env = Environment(
            id=env_id,
            name=name,
            backend="conda",
            python_version=python_version,
            path=f"conda:{name}-{env_id}",
            created_at=str(datetime.now())
        )

        self.registry.add(env)

        return env