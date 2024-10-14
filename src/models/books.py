from typing import TYPE_CHECKING
from datetime import UTC, datetime

from sqlalchemy import ForeignKey, Integer, String, DateTime, Boolean, JSON, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.models.users import AuthorsOrm


class BooksOrm(Base):
    table_name = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    image_path: Mapped[str | None] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC), index=True)
    views_count: Mapped[int] = mapped_column(Integer, default=0)
    downloads_count: Mapped[int] = mapped_column(Integer, default=0)
    published: Mapped[bool] = mapped_column(Boolean, default=False, index=True)

    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["AuthorsOrm"] = relationship("AuthorsOrm", back_populates="books")

    metadata_id: Mapped[int] = mapped_column(ForeignKey("books_metadata.id"), unique=True)
    metadata: Mapped["BooksMetaDataOrm"] = relationship("BooksMetaDataOrm", back_populates="book")

    quotes: Mapped[list["QuotesOrm"]] = relationship("QuotesOrm", back_populates="book")


class BooksMetaDataOrm(Base):
    table_name = "books_metadata"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    release_year: Mapped[int] = mapped_column(Integer)
    age_rating: Mapped[int] = mapped_column(Integer)
    time_to_read: Mapped[int] = mapped_column(Integer)
    pages_count: Mapped[int] = mapped_column(Integer)
    other_data: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    book: Mapped["BooksOrm"] = relationship("BooksOrm", back_populates="metadata", uselist=False)


class QuotesOrm(Base):
    table_name = "quotes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    text: Mapped[str] = mapped_column(Text)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC))

    book: Mapped["BooksOrm"] = relationship("BooksOrm", back_populates="quotes")
