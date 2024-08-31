from logging import Logger

from entities.user import UserEntity
from repositories import UserRepositoryInterface
from use_cases import BaseUseCase


class GetUserUseCase(BaseUseCase[int, UserEntity | None]):
    user_repository: UserRepositoryInterface

    def __init__(self, user_repository: UserRepositoryInterface, logger: Logger) -> None:
        super().__init__(logger)
        self.user_repository = user_repository

    async def execute_use_case(self, params: int) -> UserEntity | None:
        user = self.user_repository.get_by_id(params)

        if user is None:
            return None

        return user
