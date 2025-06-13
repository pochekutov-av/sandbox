"""
Вспомогательные функции для модуля fixtures.
"""
import psycopg as pg

from db.md.settings import DataBaseSettings


def execute_script(conn: pg.Connection, script_path: str):
    with open(script_path) as f:
        script_text = f.read()
        conn.execute(script_text)


def create_conn():
    settings = DataBaseSettings()
    return pg.connect(
        host=settings.DATABASE_HOST,
        port=settings.DATABASE_PORT,
        dbname=settings.DATABASE_NAME,
        user=settings.DATABASE_USER,
        password=settings.DATABASE_PASS,
    # row_factory - результаты возвращать в виде named-tuple
        row_factory=pg.rows.namedtuple_row,
    )
