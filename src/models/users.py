from typing import TYPE_CHECKING
from datetime import datetime, UTC

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, Text

from src.database import Base

if TYPE_CHECKING:
    from src.models import BooksOrm


class UsersOrm(Base):
    table_name = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255))
    hashed_password: Mapped[str] = mapped_column(String(255))

    profile_id: Mapped[int] = mapped_column(ForeignKey("profiles.id"), unique=True)
    profile: Mapped["ProfilesOrm"] = relationship("ProfilesOrm", back_populates="user")


class ProfilesOrm(Base):
    table_name = "profiles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(255))
    display_name: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC))
    about: Mapped[str | None] = mapped_column(Text, nullable=True)

    user: Mapped["UsersOrm"] = relationship("UsersOrm", back_populates="profile")


class FollowsOrm(Base):
    table_name = "follows"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    follower_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


class AuthorsOrm(Base):
    table_name = "authors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    about: Mapped[str | None] = mapped_column(Text, nullable=True)

    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)

    books: Mapped[list["BooksOrm"]] = relationship("BooksOrm", back_populates="author")
