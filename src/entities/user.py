from dataclasses import dataclass
from typing import Optional, TypedDict

from entities import BaseEntity


class User(TypedDict):
    id: Optional[int]
    name: str
    email: str


@dataclass
class UserEntity(BaseEntity):
    id: Optional[int]
    name: str
    email: str

    @classmethod
    def from_dict(cls, other: dict) -> "UserEntity":
        return cls(
            id=other.get("id"),
            name=other["name"],
            email=other["email"],
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }
