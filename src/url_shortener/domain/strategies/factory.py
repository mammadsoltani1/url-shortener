from url_shortener.domain.strategies.base import base_strategy
from url_shortener.domain.strategies.hashStrategy import hash_strategy
from url_shortener.domain.strategies.randomStrategy import random_strategy
from url_shortener.domain.strategies.uuidStrategy import uuid_strategy

from url_shortener.core.config import settings

STRATEGIES = {
    "random": lambda: random_strategy(length=settings.SHORTCODE_LENGTH),
    "hash": lambda: hash_strategy(length=settings.SHORTCODE_LENGTH),
    "uuid": lambda: uuid_strategy(length=settings.SHORTCODE_LENGTH),
}

def get_short_code_strategy() -> base_strategy:
    """Get the short code strategy based on the configuration."""
    strategy_name = settings.SHORTCODE_STRATEGY.lower()
    if strategy_name not in STRATEGIES:
        raise ValueError(f"Invalid short code strategy: {strategy_name}")
    return STRATEGIES[strategy_name]()