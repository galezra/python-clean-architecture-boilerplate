"""
Use cases for the application.
"""

from abc import ABC, abstractmethod
from collections.abc import Callable
from enum import Enum
from logging import Logger
from typing import Any, Generic, Optional, TypeVar, Union

from fastapi import HTTPException

T_co = TypeVar("T_co", covariant=True)
P = TypeVar("P")


class UseCaseResultStatus(Enum):
    COMPLETED = "COMPLETED"
    FORBIDDEN = "FORBIDDEN"
    ERROR = "ERROR"


class UseCaseResult(Generic[T_co]):
    def __init__(
        self,
        data: T_co,
        status: UseCaseResultStatus = UseCaseResultStatus.COMPLETED,
        error_message: Optional[str] = None,
        error_code: int = 0,
    ) -> None:
        self.data: T_co = data
        self.status: UseCaseResultStatus = status
        self.error_message: Optional[str] = error_message
        self.error_code: int = error_code


class BaseUseCase(ABC, Generic[P, T_co]):
    def __init__(self, logger: Logger) -> None:
        self.logger = logger

    async def execute(self, params: P) -> UseCaseResult[Union[T_co, None]]:
        try:
            result = await self.execute_use_case(params)
            return UseCaseResult(data=result)
        except Exception as e:
            self.logger.exception("Error executing use case")
            return UseCaseResult(
                data=None,
                status=UseCaseResultStatus.ERROR,
                error_message=str(e),
                error_code=e.status_code if hasattr(e, "status_code") else 500,
            )

    @abstractmethod
    async def execute_use_case(self, params: P) -> T_co:
        pass


def handle_use_case_result(
    use_case_result: UseCaseResult[T_co],
    on_completed: Callable[[T_co], Any],
) -> Union[T_co, None]:
    if use_case_result.status == UseCaseResultStatus.COMPLETED:
        return on_completed(use_case_result.data)
    if use_case_result.status == UseCaseResultStatus.FORBIDDEN:
        msg = "Forbidden"
        raise PermissionError(msg)
    if use_case_result.status == UseCaseResultStatus.ERROR:
        raise HTTPException(
            status_code=use_case_result.error_code,
            detail=use_case_result.error_message,
        )
    return None
