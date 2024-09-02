from logging import getLogger

from dependency_injector import containers, providers

from src.repositories.user import UserRepository
from src.use_cases.get_user import GetUserUseCase


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config/configuration.yaml"])
    logger = providers.Singleton(getLogger, name="app")

    user_repository = providers.Singleton(UserRepository)

    get_user_use_case = providers.Factory(
        GetUserUseCase,
        user_repository=user_repository,
        logger=logger,
    )


def get_application_container() -> Container:
    return Container()
