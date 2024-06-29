import os.path

PROJECT_DIR = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(PROJECT_DIR, "templates")
MIGRATIONS_DIR = os.path.join(PROJECT_DIR, "db", "migrations")
DB_FILENAME = "database.sqlite"
