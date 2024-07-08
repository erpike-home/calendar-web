from fastapi import FastAPI

from routes.api.kanon.kanon import router as api_kanon_router
from routes.index import router as index_router


class ChurchCalendar(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init()

    def init(self):
        self.init_database()
        self.include_router(index_router)
        self.include_router(api_kanon_router)

    @staticmethod
    def init_database():
        pass
