import secrets
from src.url_shortener.domain.strategies.base import base_strategy

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

class random_strategy(base_strategy):
    """Random strategy for generating short codes."""
    
    def generate_short_code(self, url: str) -> str:
        """Generate a random short code for the given URL."""
        return ''.join(secrets.choice(alphabet) for _ in range(self._length))