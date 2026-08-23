from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from url_shortener.api.routes import router

app = FastAPI(title="URL Shortener API", version="0.1.0")

STATIC_DIR = Path(__file__).parent / "static"

@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    """Returns service health status"""
    return {"status": "ok"}

@app.get("/", include_in_schema=False)
def frontend() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")

app.include_router(router)