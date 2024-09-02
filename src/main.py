from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api import router_config
from src.infra.containers import Container, get_application_container

container = Container()


def init_routers(app: FastAPI) -> None:
    for router_info in router_config.ROUTERS:
        app.include_router(
            router_info["router"],
            prefix=router_info["prefix"],
            tags=router_info["tags"],
        )


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    container.init_resources()
    init_routers(app)
    try:
        yield
    finally:
        container.shutdown_resources()


def create_app() -> FastAPI:
    get_application_container().wire(
        modules=[__name__],
        packages=["src.api"],
    )
    return FastAPI(lifespan=lifespan)


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
