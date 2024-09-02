from src.entities.user import UserEntity
from src.interfaces.user_repository import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self) -> None:
        self.data = [UserEntity(id=1, name="John Doe", email="john.doe@example.com")]

    def get_by_id(self, user_id: int) -> UserEntity | None:
        for entity in self.data:
            if entity.id == user_id:
                return entity
        return None
