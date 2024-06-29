from datetime import datetime

from peewee import Proxy, Model, DateTimeField, CharField, TextField
from peewee_migrate import Router
from playhouse.sqlite_ext import SqliteExtDatabase

from config import DB_FILENAME, MIGRATIONS_DIR


db = SqliteExtDatabase(
    DB_FILENAME,
    autoconnect=False,
    pragmas={"foreign_keys": 1}
)
db_proxy = Proxy()


class BaseModel(Model):
    class Meta:
        database = db

    created_at = DateTimeField(default=datetime.utcnow)
    modified_at = DateTimeField(default=datetime.utcnow)

    def save(self, *args, **kwargs):
        self.modified_at = datetime.utcnow()
        return super().save(*args, **kwargs)


class PrayerSection(BaseModel):
    name = CharField(max_length=125, unique=True)
    cslavonic_name = CharField(max_length=125, unique=True)


class Prayer(BaseModel):
    title = CharField(max_length=125, unique=True)
    text = TextField(null=True)

    cslavonic_title = CharField(max_length=125, unique=True)
    cslavonic_text = CharField(null=True)


def init_db():
    db_proxy.initialize(db)
    router = Router(db, migrate_dir=MIGRATIONS_DIR)
    with db_proxy:
        router.run()
