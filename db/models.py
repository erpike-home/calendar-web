"""
канон - kanon 
first troparion, junction, Irmos - ирмос
theotokion - Богородичен
troichen - Троичен
song? - песнь
chorus - припев
"""

from datetime import datetime
from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Field, SQLModel, func
from sqlmodel.ext.asyncio.session import AsyncSession
from conf import DB_CONNECTION_STR


engine = create_async_engine(DB_CONNECTION_STR)


class BaseModel(SQLModel, table=False):
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    modified_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={"onupdate": func.now(), "default": func.now()},
    )

    class Config:
        orm_mode = True


class KanonBase(BaseModel):
    name: str = Field(nullable=False, max_length=512)


class Kanon(KanonBase, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)


class KanonCreate(KanonBase):
    pass


class KanonPublic(KanonBase):
    id: int


class KanonUpdate(SQLModel):
    name: Optional[str] = None


# def get_session():
#     with Session(engine) as session:
#         yield session


async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session
