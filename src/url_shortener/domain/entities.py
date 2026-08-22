from dataclasses import dataclass

@dataclass
class short_url:
    """Domain entity representing a shortened URL, independent of any
    persistence or web framework concern."""

    original_url: str
    short_code: str