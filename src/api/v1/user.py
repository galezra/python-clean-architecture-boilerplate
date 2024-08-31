from logging import getLogger

from fastapi import APIRouter

from dtos.user import UserResponse
from repositories.user import UserRepository
from use_cases import handle_use_case_result
from use_cases.get_user import GetUserUseCase

router = APIRouter()
repo = UserRepository()
logger = getLogger(__name__)


@router.get("/users/{user_id}")
async def get_user(user_id: int) -> UserResponse | None:
    result = await GetUserUseCase(repo, logger).execute(user_id)
    return handle_use_case_result(result, on_completed=lambda data: data)
