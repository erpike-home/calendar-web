from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from templates import tpl


router = APIRouter(tags=["Root"])


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    # Render the 'index.html' template with some context
    return tpl.TemplateResponse(
        "index.html",
        {
            "request": request,
            "message": "Hello, FastAPI with Jinja2!"
        },
    )
