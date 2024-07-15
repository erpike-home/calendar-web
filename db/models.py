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
from sqlmodel import Field, SQLModel, text, Column, DateTime
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import Optional


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

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v) if hasattr(self, k) else None
        self.modified_at = datetime.utcnow()


class KanonBase(SQLModel):
    name: str = Field(nullable=False, max_length=512)


class KanonPublic(KanonBase):
    id: int


class Kanon(BaseModel, KanonBase, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)


class KanonCreate(KanonBase):
    pass


class KanonUpdate(KanonBase):
    pass


async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession)
    async with async_session() as session:
        yield session
