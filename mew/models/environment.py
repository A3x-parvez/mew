from pydantic import BaseModel
from typing import Optional


class Environment(BaseModel):
    id: str
    name: str
    backend: str
    python_version: str
    path: str
    created_at: str
    last_used: Optional[str] = None
    locked: bool = False