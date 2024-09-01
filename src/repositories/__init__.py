"""
Repository interfaces and implementations.
"""

from abc import ABC, abstractmethod

from src.entities.user import UserEntity


class UserRepositoryInterface(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> UserEntity | None:
        pass
