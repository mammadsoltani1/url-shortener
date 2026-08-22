from abc import ABC, abstractmethod
class base_strategy(ABC):
    """Base class for all strategies."""
    def __init__(self, length: int = 8) -> None:
        self._length = length

    @abstractmethod
    def generate_short_code(self, url: str) -> str:
        """Generate a short code for the given URL."""
        pass
