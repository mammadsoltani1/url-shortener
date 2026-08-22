from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from url_shortener.db.database import Base

class url_model(Base):
    """SQLAlchemy model for the URL table."""
    __tablename__ = "urls"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    original_url: Mapped[str] = mapped_column(String(2048), nullable=False)
    short_code: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)