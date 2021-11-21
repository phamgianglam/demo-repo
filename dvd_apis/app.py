from fastapi import FastAPI
from dvd_apis.config import config
from dvd_apis.apis import config_route

app = FastAPI(docs_url=f"/{config.API_PREFIX}/")

config_route(app, prefix=config.API_PREFIX )
