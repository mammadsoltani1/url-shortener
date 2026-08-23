from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from url_shortener.services.dependencies import get_url_service
from url_shortener.api.schemas import shorten_url_req, shorten_url_res
from url_shortener.core.config import settings
from url_shortener.services.exceptions import invalid_url, short_code_generation_failed
from url_shortener.services.urlService import url_service

router = APIRouter(tags=["url"])


@router.post("/shorten", response_model=shorten_url_res, status_code=status.HTTP_201_CREATED)
def shorten_url(payload: shorten_url_req, service: url_service = Depends(get_url_service)) -> shorten_url_res:
    """Endpoint to shorten a given URL."""
    try:
        short_url_entry = service.shorten_url(payload.original_url)
        return shorten_url_res(
            short_code=short_url_entry.short_code,
            short_url=f"{settings.BASE_URL}/{short_url_entry.short_code}",
            original_url=short_url_entry.original_url,
        )
    except invalid_url as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)) from e
    except short_code_generation_failed as e:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,detail=str(e)) from e

@router.get("/{short_code}", response_class=RedirectResponse, status_code=status.HTTP_307_TEMPORARY_REDIRECT)
def redirect_to_original(short_code: str, service: url_service = Depends(get_url_service)) -> RedirectResponse:
    """Endpoint to redirect to the original URL based on the short code."""
    short_url_entry = service.resolve(short_code)
    if short_url_entry is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shortened url not found.")
    return RedirectResponse(url=short_url_entry.original_url, status_code=status.HTTP_307_TEMPORARY_REDIRECT)