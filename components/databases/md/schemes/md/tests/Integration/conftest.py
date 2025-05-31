import os
from dataclasses import dataclass

import pytest
import sqlalchemy as sa

from db.md.md.entrypoints.create_all import METADATA, create_all
from db.md.md.fixtures.init.load import loaddata
from db.md.md.settings import DataBaseSettings

os.environ["DATABASE_NAME"] = "test_md"
"""Принудительно выставим название тестовой БД, чтобы гарантировать
изолированность основной БД от тестов."""


@dataclass
class DataBase:
    engine: sa.Engine
    conn: sa.Connection | None = None
    """Connection c открытой транзакцией для которой будет сделан
    rollback по завершению теста."""


@pytest.fixture(name='db_settings', scope='session')
def fixture_db_settings():
    """Настройки подключения к БД и логирования."""
    db_settings = DataBaseSettings()
    # Uncomment logging.configure for display sqlalchemy.engine logs
    # from db.md.md import logging
    # logging.configure(db_settings.LOGGING_CONFIG)
    return db_settings


@pytest.fixture(name='engine', scope='session')
def fixture_engine(db_settings):
    """Создание sqlalchemy engine."""

    return sa.create_engine(
        db_settings.database_url,
        echo=False,    # set True for more details
        echo_pool=False    # set True for more details
    )


@pytest.fixture(name='db_init', scope='session')
def fixture_db_init(engine: sa.Engine) -> DataBase:
    """Готовая БД для работы: создана схема, накачена init fixture, накачены
    все представления, хранимые процедуры и функции.
    Важно: транзакции открытой нет, все изменения будут сохранены.
    """

    # При повторном запуске структура таблиц могла измениться,
    # поэтому нужно начать с чистого листа - удаляем схему и все что в ней.
    def drop_all():
        with engine.connect() as conn:
            stmt = sa.text(f'DROP SCHEMA IF EXISTS {METADATA.schema} CASCADE;')
            conn.execute(stmt)
            conn.commit()

    drop_all()
    create_all(engine=engine)
    db = DataBase(engine=engine)

    # TODO: создать views, procedures, functions
    with engine.connect() as conn:
        loaddata(conn=conn)
        conn.commit()
    return db


@pytest.fixture(name='db', scope='function')
def fixture_db(db_init: DataBase) -> DataBase:
    """Оборачиваем транзакцией и откатом."""
    with db_init.engine.connect() as conn, conn.begin() as transaction:
        db_init.conn = conn
        try:
            yield db_init
        finally:
            transaction.rollback()
