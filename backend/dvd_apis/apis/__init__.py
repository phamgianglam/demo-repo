from fastapi import FastAPI
from .user import router


def config_route(app: FastAPI, dependencies=None, prefix=None):
    app.include_router(router)
