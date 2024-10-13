from pydantic import BaseModel

from src.repositories.mappers.base import DataMapper


class BaseRepository:
    model = None
    mapper: DataMapper = None

    def __init__(self, session):
        self.session = session

    async def get_filtered(self, **filter_by) -> list[dict]:
        pass

    async def get_all(self) -> list[dict]:
        pass

    async def get_one_or_none(self, **filter_by) -> dict:
        pass

    async def add(self, data: BaseModel) -> dict:
        pass

    async def add_bulk(self, data: list[BaseModel]) -> None:
        pass

    async def update(self, data: BaseModel) -> None:
        pass

    async def delete(self, **filter_by) -> None:
        pass
