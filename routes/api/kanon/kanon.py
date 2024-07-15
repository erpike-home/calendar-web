from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from db.models import KanonPublic, get_session, KanonCreate, Kanon, KanonUpdate


router = APIRouter(tags=["api/kanon"], prefix="/api/kanon")


async def check_if_exists(session, item_id):
    res = await session.exec(select(Kanon).where(Kanon.id == item_id))
    if not (item := res.one_or_none()):
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
    return (await session.exec(select(Kanon))).all()


@router.put("/{item_id}", response_model=KanonPublic)
async def update_kanon(item_id: int, updated: KanonUpdate, *, session: AsyncSession = Depends(get_session)):
    kanon = await check_if_exists(session, item_id)
    kanon.update(name=updated.name)
    await session.commit()
    await session.refresh(kanon)
    return kanon


@router.delete("/{item_id}")
async def delete_kanon(item_id: int, *, session: AsyncSession = Depends(get_session)):
    kanon = await check_if_exists(session, item_id)
    await session.delete(kanon)
    await session.commit()
    return {"message": "Kanon successfully deleted"}
