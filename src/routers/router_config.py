from routers.v1 import user

# Import additional routers here as your application grows
# from routers.v1 import items, auth, etc.

ROUTERS = [
    {"router": user.router, "prefix": "/api/v1/users", "tags": ["users"]},
    # Add more routers as your application expands, for example:
]
