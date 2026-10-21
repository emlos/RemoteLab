from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse




router = APIRouter(include_in_schema=False)
INDEX_HTML = Path(__file__).resolve().parents[1] / "web" / "index.html"


@router.get("/")
def home() -> FileResponse:
    return FileResponse(INDEX_HTML)
