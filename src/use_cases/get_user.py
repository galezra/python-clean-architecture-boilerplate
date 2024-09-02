from logging import Logger

from src.dtos.user import UserResponse
from src.interfaces.user_repository import IUserRepository
from src.use_cases import BaseUseCase


class GetUserUseCase(BaseUseCase[int, UserResponse | None]):
    user_repository: IUserRepository

    def __init__(self, user_repository: IUserRepository, logger: Logger) -> None:
        super().__init__(logger)
        self.user_repository = user_repository

    async def execute_use_case(self, params: int) -> UserResponse | None:
        user = self.user_repository.get_by_id(params)

        if user is None:
            return None

        return UserResponse.model_validate(user.to_dict())
