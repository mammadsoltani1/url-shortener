from fastapi import Depends
from sqlalchemy.orm import Session

from url_shortener.db.database import get_session
from url_shortener.db.repo import url_repo
from url_shortener.domain.strategies.factory import get_short_code_strategy
from url_shortener.services.urlService import url_service

def get_url_service(session: Session = Depends(get_session)) -> url_service:
    """Factory function to create a url_service instance with the appropriate strategy and repository."""
    strategy = get_short_code_strategy()
    repo = url_repo(session)
    return url_service(strategy=strategy, repo=repo)