from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import api, experiments, web


app = FastAPI(title="badanie_demo1")

STATIC_DIR = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

app.include_router(web.router)
app.include_router(api.router, prefix="/api/v1")
app.include_router(experiments.router, prefix="/api/v1")
