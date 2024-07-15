from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from sqlmodel.ext.asyncio.session import AsyncSession

from db.models import Kanon, get_session
from templates import tpl


router = APIRouter(tags=["Root"])


@router.get("/", response_class=HTMLResponse)
async def index(request: Request, session: AsyncSession = Depends(get_session)):
    kanons = await Kanon.list(session)
    return tpl.TemplateResponse(
        "index.html",
        {
            "request": request,
            "kanons": kanons,
        },
    )
