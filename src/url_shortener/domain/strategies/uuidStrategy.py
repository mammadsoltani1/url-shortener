import uuid
from src.url_shortener.domain.strategies.base import base_strategy

class uuid_strategy(base_strategy):
    """UUID strategy for generating short codes."""

    def generate_short_code(self, url: str) -> str:
        """Generate a UUID-based short code for the given URL."""
        # Generate a UUID and convert it to a string
        unique_id = str(uuid.uuid4())
        # Return the first 'length' characters of the UUID
        return unique_id[:self._length]