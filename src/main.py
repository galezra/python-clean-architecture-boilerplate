from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.api import router_config
from src.infra.containers import ApplicationContainer, get_application_container

container = ApplicationContainer()


def init_routers(app: FastAPI) -> None:
    for router_info in router_config.ROUTERS:
        app.include_router(**router_info)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    container.init_resources()
    init_routers(app)
    try:
        yield
    finally:
        container.shutdown_resources()


def init_app() -> FastAPI:
    get_application_container().wire(
        modules=[__name__],
        packages=["src.api"],
    )
    return FastAPI(lifespan=lifespan)


app = init_app()

if __name__ == "__main__":
    container = get_application_container()
    uvicorn.run(
        "main:app",
        host=container.config.server.host(),
        port=container.config.server.port(),
    )
