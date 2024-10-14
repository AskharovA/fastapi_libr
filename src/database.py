from sqlalchemy import NullPool
from sqlalchemy.orm import declared_attr, DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from src.config import settings

engine = create_async_engine(settings.db_url)
engine_null_pool = create_async_engine(settings.db_url, poolclass=NullPool)


async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)
async_session_maker_null_pool = async_sessionmaker(bind=engine_null_pool, expire_on_commit=False)


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        if hasattr(cls, 'table_name'):
            return cls.table_name
        return cls.__name__.lower() + "s"
