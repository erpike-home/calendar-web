from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from db.models import KanonPublic, get_session, KanonCreate, Kanon


router = APIRouter(tags=["Root"], prefix="/api/kanon")


@router.post("/", response_model=KanonPublic)
async def create_kanon(*, session: AsyncSession = Depends(get_session), kanon: KanonCreate):
    db_kanon = Kanon.model_validate(kanon)
    session.add(db_kanon)
    await session.commit()
    await session.refresh(db_kanon)
    return db_kanon
