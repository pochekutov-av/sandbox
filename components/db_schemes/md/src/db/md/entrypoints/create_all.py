"""
Создание всех таблиц описаных в metadata.

Используется при локальной разработке, с нуля создается БД затем выполняется
создание всех таблиц, накатывание начальных справочных данных,
объектов БД (процедур, представлений..).
"""

from sqlalchemy import create_engine
from sqlalchemy.sql.ddl import CreateSchema

from db.md import logging
from db.md.schema.tables import METADATA
from db.md.settings import DataBaseSettings


def create_all(engine):
    # Создать схему указаную в METADATA
    with engine.connect() as conn:
        existed_schemas = conn.dialect.get_schema_names(conn)
        if METADATA.schema not in existed_schemas:
            conn.execute(CreateSchema(METADATA.schema))
            conn.commit()

    # Создать таблицы
    METADATA.create_all(engine)


if __name__ == '__main__':    # pragma: no cover
    db_settings = DataBaseSettings()
    logging.configure(db_settings.LOGGING_CONFIG)
    engine = create_engine(
        db_settings.database_url,
        echo=db_settings.SA_ECHO,
        echo_pool=db_settings.SA_ECHO_POOL
    )
    create_all(engine=engine)
