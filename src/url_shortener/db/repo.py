from sqlalchemy.orm import Session
from url_shortener.domain.entities import short_url
from url_shortener.db.models import url_model

class url_repo:
    """Repository class for managing URL entities in the database."""

    def __init__(self, db: Session):
        self.db = db

    def _to_short_url(self, model: url_model) -> short_url:
        return short_url(original_url=model.original_url, short_code=model.short_code)

    def create_url(self, url_entity: short_url) -> short_url:
        """Create a new URL entry in the database."""
        db_url = url_model(
            original_url=url_entity.original_url,
            short_code=url_entity.short_code
        )
        self.db.add(db_url)
        self.db.commit()
        self.db.refresh(db_url)
        return self._to_short_url(db_url)

    def get_url_by_short_code(self, short_code: str) -> short_url | None:
        """Retrieve a URL entry by its short code."""
        db_url = self.db.query(url_model).filter(url_model.short_code == short_code).first()
        return self._to_short_url(db_url) if db_url else None

    def get_url_by_original_url(self, original_url: str) -> short_url | None:
        """Retrieve a URL entry by its original URL."""
        db_url = self.db.query(url_model).filter(url_model.original_url == original_url).first()
        return self._to_short_url(db_url) if db_url else None