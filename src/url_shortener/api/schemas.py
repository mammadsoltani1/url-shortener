from typing import Annotated

from pydantic import AfterValidator, BaseModel, HttpUrl


def _stringify_url(value: HttpUrl) -> str:
    return str(value)


ValidatedUrl = Annotated[HttpUrl, AfterValidator(_stringify_url)]


class shorten_url_req(BaseModel):
    """Schema for the request body when shortening a URL."""
    original_url: ValidatedUrl

class shorten_url_res(BaseModel):
    """Schema for the response body after shortening a URL."""
    short_code: str
    short_url: str
    original_url: str