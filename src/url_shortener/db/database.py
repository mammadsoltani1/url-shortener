from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from url_shortener.core.config import settings
from collections.abc import Generator

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=True)

class Base(DeclarativeBase):
    pass

def get_session() -> Generator[Session, None, None]:
    """Get a new database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()