from urllib.parse import urlparse

from url_shortener.db.repo import url_repo
from url_shortener.domain.entities import short_url
from url_shortener.domain.strategies.base import base_strategy
from url_shortener.services.exceptions import invalid_url, short_code_generation_failed

ALLOWED_SCHEMES = {"http", "https"}
MAX_GENERATION_ATTEMPTS = 5


class url_service:
    """Service class for URL shortening operations."""

    def __init__(self, strategy: base_strategy, repo: url_repo) -> None:
        self._strategy = strategy
        self._repo = repo

    def shorten_url(self, original_url: str) -> short_url:
        """Shorten the given original URL, reusing an existing entry if one exists."""
        if not self._is_valid_url(original_url):
            raise invalid_url(f"Invalid URL: {original_url}")

        existing_entry = self._repo.get_url_by_original_url(original_url)
        if existing_entry is not None:
            return existing_entry

        for _ in range(MAX_GENERATION_ATTEMPTS):
            short_code = self._strategy.generate_short_code(original_url)
            if self._repo.get_url_by_short_code(short_code) is None:
                new_entry = short_url(original_url=original_url, short_code=short_code)
                return self._repo.create_url(new_entry)

        raise short_code_generation_failed(
            "Failed to generate a unique short code after multiple attempts."
        )

    def resolve(self, short_code: str) -> short_url | None:
        """Look up the URL entry for a short code, if one exists."""
        return self._repo.get_url_by_short_code(short_code)

    def _is_valid_url(self, url: str) -> bool:
        """Validate that the URL has an allowed scheme and a host."""
        parsed = urlparse(url)
        return parsed.scheme in ALLOWED_SCHEMES and bool(parsed.netloc)