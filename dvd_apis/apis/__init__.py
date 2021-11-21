from fastapi import FastAPI
from . import series


def config_route(app: FastAPI, dependencies=None, prefix=None):
    app.include_router(series.router,prefix=f"/{prefix}/{series.PREFIX}", tags=[series.PREFIX])
