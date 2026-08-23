from fastapi import FastAPI
from url_shortener.api.routes import router

app = FastAPI(title="URL Shortener API", version="0.1.0")

@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    """Returns service health status"""
    return {"status": "ok"}

app.include_router(router)