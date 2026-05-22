import json
from typing import List

from mew.config import REGISTRY_FILE
from mew.models.environment import Environment


class Registry:

    def __init__(self):
        self._ensure_registry()

    def _ensure_registry(self):
        if not REGISTRY_FILE.exists():
            REGISTRY_FILE.write_text("[]")

    def load(self) -> List[Environment]:
        data = json.loads(REGISTRY_FILE.read_text())
        return [Environment(**env) for env in data]

    def save(self, environments: List[Environment]):
        data = [env.model_dump() for env in environments]
        REGISTRY_FILE.write_text(json.dumps(data, indent=4))

    def add(self, environment: Environment):
        envs = self.load()
        envs.append(environment)
        self.save(envs)

    def remove(self, env_id: str):
        envs = self.load()
        envs = [env for env in envs if env.id != env_id]
        self.save(envs)

    def get_all(self) -> List[Environment]:
        return self.load()