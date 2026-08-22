import secrets
from url_shortener.domain.strategies.base import base_strategy

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

class random_strategy(baseStrategy):
    """Random strategy for generating short codes."""

    def generate_short_code(self, url: str) -> str:
        """Generate a random short code for the given URL."""
        return ''.join(secrets.choice(alphabet) for _ in range(6))