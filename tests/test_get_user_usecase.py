from http import HTTPStatus
from logging import Logger, getLogger

import pytest

from dtos.user import UserResponse
from entities.user import UserEntity
from repositories import UserRepositoryInterface
from use_cases import UseCaseResultStatus
from use_cases.get_user import GetUserUseCase


class MockUserRepository(UserRepositoryInterface):
    def __init__(self, users: list[UserEntity]) -> None:
        self.users = users

    def get_by_id(self, user_id: int) -> UserEntity | None:
        for user in self.users:
            if user.id == user_id:
                return user
        return None


@pytest.fixture
def mock_logger() -> Logger:
    return getLogger("test")


@pytest.fixture
def mock_user_repository() -> MockUserRepository:
    users = [
        UserEntity(id=1, name="John Doe", email="john.doe@example.com"),
        UserEntity(id=2, name="Jane Doe", email="jane.doe@example.com"),
    ]
    return MockUserRepository(users)


@pytest.fixture
def get_user_use_case(mock_user_repository: MockUserRepository, mock_logger: Logger) -> GetUserUseCase:
    return GetUserUseCase(mock_user_repository, mock_logger)


@pytest.mark.asyncio
async def test_get_user_success(get_user_use_case: GetUserUseCase) -> None:
    user_id = 1
    result = await get_user_use_case.execute(user_id)

    pytest.assume(result.data == UserResponse(id=1, name="John Doe", email="john.doe@example.com"))


@pytest.mark.asyncio
async def test_get_user_not_found(get_user_use_case: GetUserUseCase) -> None:
    user_id = 999

    result = await get_user_use_case.execute(user_id)

    pytest.assume(result.status.value == UseCaseResultStatus.ERROR.value)
    pytest.assume(result.error_code == HTTPStatus.NOT_FOUND.value)
