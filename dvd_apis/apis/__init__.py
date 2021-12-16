from fastapi import FastAPI
from . import series, titles


def config_route(app: FastAPI, dependencies=None, prefix=None):
    app.include_router(series.router, prefix=f"/{prefix}/{series.PREFIX}", tags=[series.PREFIX])
    app.include_router(titles.router, prefix=f"/{prefix}/{titles.PREFIX}", tags=[titles.PREFIX])
