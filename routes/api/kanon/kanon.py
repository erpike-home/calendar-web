from typing import Type

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from db.models import KanonPublic, get_session, KanonCreate, Kanon, KanonUpdate, BaseModel

router = APIRouter(tags=["api/kanon"], prefix="/api/kanon")


async def check_if_exists(session: AsyncSession, klass: Type[BaseModel], item_id: int):
    if not (item := await klass.get_by_id(session, item_id)):
        raise HTTPException(status_code=404, detail="Kanon not found")
    return item


@router.post("/", response_model=KanonPublic)
async def create_kanon(*, session: AsyncSession = Depends(get_session), kanon: KanonCreate):
    db_kanon = Kanon.model_validate(kanon)
    session.add(db_kanon)
    await session.commit()
    await session.refresh(db_kanon)
    return db_kanon


@router.get("/", response_model=list[Kanon])
async def get_kanon(*, session: AsyncSession = Depends(get_session)):
    return await Kanon.list(session)


@router.patch("/{item_id}", response_model=KanonPublic)
async def update_kanon(item_id: int, updated: KanonUpdate, *, session: AsyncSession = Depends(get_session)):
    updated = updated.model_dump(exclude_unset=True)
    kanon = await check_if_exists(session, Kanon, item_id)
    kanon = await kanon.update(session, **updated)
    return kanon


@router.delete("/{item_id}")
async def delete_kanon(item_id: int, *, session: AsyncSession = Depends(get_session)):
    kanon = await check_if_exists(session, Kanon, item_id)
    await kanon.delete(session)
    return {"message": "Kanon successfully deleted"}
