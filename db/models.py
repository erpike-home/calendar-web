"""
канон - kanon 
first troparion, junction, Irmos - ирмос
theotokion - Богородичен
troichen - Троичен
song? - песнь
chorus - припев
"""

from datetime import datetime

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Field, SQLModel, text, Column, DateTime, select
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import Optional, List, Sequence

from conf import DB_CONNECTION_STR


engine = create_async_engine(DB_CONNECTION_STR)


class BaseModel(SQLModel, table=False):
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.utcnow(),
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
        )
    )
    modified_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.utcnow(),
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
        )
    )

    class Config:
        from_attributes = True

    async def update(self, session: AsyncSession, **kwargs) -> "BaseModel":
        for k, v in kwargs.items():
            setattr(self, k, v) if hasattr(self, k) else None
        self.modified_at = datetime.utcnow()
        await session.commit()
        await session.refresh(self)
        return self

    async def delete(self, session: AsyncSession) -> None:
        await session.delete(self)
        await session.commit()

    @classmethod
    async def list(cls, session: AsyncSession) -> Sequence["BaseModel"]:
        return (await session.exec(select(cls))).all()

    @classmethod
    async def get_by_id(cls, session: AsyncSession, pk: int) -> "BaseModel":
        return (await session.exec(select(cls).where(cls.id == pk))).one_or_none()


class KanonDefault(SQLModel):
    name: str = Field(nullable=False, max_length=512)


class KanonPublic(KanonDefault):
    id: int


class Kanon(BaseModel, KanonDefault, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)


class KanonCreate(KanonDefault):
    pass


class KanonUpdate(KanonDefault):
    pass


async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession)
    async with async_session() as session:
        yield session
