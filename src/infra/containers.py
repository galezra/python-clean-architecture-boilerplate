import os
from logging import getLogger

from dependency_injector import containers, providers

from src.app.repositories.user import UserRepository
from src.app.use_cases.get_user import GetUserUseCase


class ApplicationContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    env = os.getenv("ENVIRONMENT", "default")

    config.from_yaml(f"config/{env}.yaml", required=True)

    logger = providers.Singleton(getLogger, name="app")

    user_repository = providers.Singleton(UserRepository)

    get_user_use_case = providers.Factory(
        GetUserUseCase,
        user_repository=user_repository,
        logger=logger,
    )


def get_application_container() -> ApplicationContainer:
    return ApplicationContainer()
