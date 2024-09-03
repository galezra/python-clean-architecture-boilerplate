from src.app.api.v1 import user

ROUTERS = [
    {
        "router": user.router,
        "prefix": "/api/v1",
        "tags": ["users"],
    },
]
