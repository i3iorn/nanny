import sqlite3
from backend.config.loader import Config


def get_connection(db_path=None):
    if db_path is None:
        db_path = Config().get("database", {}).get("path", "data.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_db():
    from pathlib import Path
    schema_file = Path(__file__).parent / "schema.sql"
    conn = get_connection()
    with open(schema_file, 'r') as f:
        schema = f.read()
    conn.executescript(schema)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
