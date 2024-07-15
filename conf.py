import os.path

PROJECT_DIR = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(PROJECT_DIR, "templates")
MIGRATIONS_DIR = os.path.join(PROJECT_DIR, "db", "migrations")
DB_FILENAME = "database.sqlite"

DB_CONNECTION_STR = f"sqlite+aiosqlite:///{os.path.join(PROJECT_DIR, DB_FILENAME)}"
# DB_CONNECTION_STR = f"mysql+asyncmy://{username}:{password}@{host}:{port}/{db_name}"
