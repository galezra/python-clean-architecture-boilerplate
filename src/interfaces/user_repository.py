from abc import ABC, abstractmethod

from src.entities.user import UserEntity


class IUserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> UserEntity | None:
        pass
