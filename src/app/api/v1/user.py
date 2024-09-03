from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.app.dtos.user import UserResponse
from src.app.use_cases import handle_use_case_result
from src.app.use_cases.get_user import GetUserUseCase
from src.infra.containers import ApplicationContainer

router = APIRouter()


@router.get("/users/{user_id}")
@inject
async def get_user(
    user_id: int,
    get_user_use_case: GetUserUseCase = Depends(Provide[ApplicationContainer.get_user_use_case]),
) -> UserResponse | None:
    result = await get_user_use_case.execute(user_id)
    return handle_use_case_result(result, on_completed=lambda data: data)
