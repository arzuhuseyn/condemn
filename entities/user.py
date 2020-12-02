from dataclasses import dataclass
from core.entities import Entity


@dataclass
class User(Entity):
    username: str
    email: str
    password: str
    is_active: bool