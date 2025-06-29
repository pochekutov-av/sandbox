import os

import psycopg
import psycopg as pg
import pytest
import sqlalchemy as sa

from db.md.entrypoints.create_routines import create_routines
from db.md.entrypoints.create_tables import METADATA, create_tables
from db.md.fixtures.init.load import loaddata
from db.md.settings import DataBaseSettings

# Указание названия БД для тестов - обязательно.
assert os.environ["TEST_DATABASE_NAME"]

# Название тестовой БД обязательно должно начинаться с "test_".
assert os.environ["TEST_DATABASE_NAME"].startswith('test_')

# Принудительно выставим название тестовой БД, чтобы гарантировать
# изолированность основной БД от тестов.
os.environ["DATABASE_NAME"] = os.environ["TEST_DATABASE_NAME"]


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


@pytest.fixture(name='private_connection', scope='session')
def fixture_private_connection() -> psycopg.Connection:
    """Подключение к БД не обернутое rollback,
    в тестах не должно использоваться."""
    return create_conn()


@pytest.fixture(name='schema', scope='session')
def fixture_schema(private_connection: pg.Connection) -> bool:
    """Готовая БД для работы: создана схема, накачена init fixture, накачены
    все представления, хранимые процедуры и функции.
    Важно: транзакции открытой нет, все изменения будут сохранены.
    """

    db_settings = DataBaseSettings()
    engine = sa.create_engine(
        db_settings.database_url,
        echo=False,    # set True for more details
        echo_pool=False    # set True for more details
    )

    # При повторном запуске структура таблиц могла измениться,
    # поэтому нужно начать с чистого листа - удаляем схему и все что в ней.
    def drop_all():
        with engine.connect() as conn:
            stmt = sa.text(f'DROP SCHEMA IF EXISTS {METADATA.schema} CASCADE;')
            conn.execute(stmt)
            conn.commit()

    drop_all()
    create_tables(engine=engine)

    with create_conn() as conn:
        loaddata(conn=conn)
        conn.commit()
        create_routines(conn=conn)
        conn.commit()
    return True


@pytest.fixture(name='conn', scope='function')
def fixture_conn(private_connection, schema) -> psycopg.Connection:
    """Подключение к БД для использования в тестах, делает rollback.

    Зависимость от fixture schema обязательна для актуальности кода routines.
    """
    try:
        yield private_connection
    finally:
        private_connection.rollback()
