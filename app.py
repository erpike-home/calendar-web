from fastapi import FastAPI

from db.models import init_db
from routes.index import router as index_router


class ChurchCalendar(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init()

    def init(self):
        self.init_database()
        self.include_router(index_router)

    @staticmethod
    def init_database():
        init_db()
