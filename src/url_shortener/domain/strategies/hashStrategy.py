import hashlib
from src.url_shortener.domain.strategies.base import base_strategy

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

class hash_strategy(base_strategy):
    """Hash strategy for generating short codes."""


    def generate_short_code(self, url: str) -> str:
        """Generate a hash-based short code for the given URL."""
        # Create a SHA-256 hash of the URL
        hash_object = hashlib.sha256(url.encode())
        # Convert the hash to a hexadecimal string
        hex_dig = hash_object.hexdigest()
        # Convert the hexadecimal string to an integer
        int_value = int(hex_dig, 16)
        # Generate a short code by mapping the integer to the alphabet
        short_code = ''
        while int_value > 0 and len(short_code) < self._length:
            short_code += alphabet[int_value % len(alphabet)]
            int_value //= len(alphabet)
        return short_code[:self._length]