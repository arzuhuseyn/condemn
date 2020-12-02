from dataclasses import dataclass
from core.entities import Entity, User


@dataclass
class UserProfile(Entity):
    user: User
    name: str
    surname: str
    image: None