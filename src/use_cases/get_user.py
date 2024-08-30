from logging import Logger

from fastapi import HTTPException

from dtos.user import UserResponse
from repositories import UserRepositoryInterface
from use_cases import BaseUseCase


class GetUserUseCase(BaseUseCase[int, UserResponse | None]):
    user_repository: UserRepositoryInterface

    def __init__(self, user_repository: UserRepositoryInterface, logger: Logger) -> None:
        super().__init__(logger)
        self.user_repository = user_repository

    async def execute_use_case(self, params: int) -> UserResponse | None:
        user = self.user_repository.get_by_id(params)

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        return UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
        )
