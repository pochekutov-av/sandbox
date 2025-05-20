"""
Создание всех таблиц описаных в metadata.

Используется при локальной разработке, с нуля создается БД затем выполняется
создание всех таблиц, накатывание начальных справочных данных,
объектов БД (процедур, представлений..).
"""

from sqlalchemy import create_engine
from sqlalchemy.sql.ddl import CreateSchema

from db.md.md.dd import logging
from db.md.md.dd.settings import DataBaseSettings
from db.md.md.dd.tables import METADATA


class Settings:
    db = DataBaseSettings()


class Logger:
    logging.configure(Settings.db.LOGGING_CONFIG)


def create_all():
    engine = create_engine(
        Settings.db.database_url,
        echo=Settings.db.SA_ECHO,
        echo_pool=Settings.db.SA_ECHO_POOL
    )

    # Создать схему указаную в METADATA
    with engine.connect() as conn:
        existed_schemas = conn.dialect.get_schema_names(conn)
        if METADATA.schema not in existed_schemas:
            conn.execute(CreateSchema(METADATA.schema))
            conn.commit()

    # Создать таблицы
    METADATA.create_all(engine)


if __name__ == '__main__':
    create_all()
