import uvicorn
from fastapi import FastAPI

from routers import router_config

app = FastAPI()


def init_routers(app: FastAPI) -> None:
    for router_info in router_config.ROUTERS:
        app.include_router(
            router_info["router"],
            prefix=router_info["prefix"],
            tags=router_info["tags"],
        )


def create_app() -> FastAPI:
    init_routers(app)
    return app


def main() -> None:
    app = create_app()
    uvicorn.run(app, host="127.0.0.1", port=8000)  # Should change to 0.0.0.0 in production


if __name__ == "__main__":
    main()
