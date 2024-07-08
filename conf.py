import os.path

PROJECT_DIR = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(PROJECT_DIR, "templates")
MIGRATIONS_DIR = os.path.join(PROJECT_DIR, "db", "migrations")
DB_FILENAME = "database.sqlite"
# DB_ASYNC_CONNECTION_STR = "sqlite+aiosqlite:///" + os.path.join(PROJECT_DIR, DB_FILENAME)
# DB_CONNECTION_STR = f"sqlite:///{os.path.join(PROJECT_DIR, DB_FILENAME)}"
DB_CONNECTION_STR = f"sqlite+aiosqlite:///{os.path.join(PROJECT_DIR, DB_FILENAME)}"
