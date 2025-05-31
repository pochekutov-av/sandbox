"""
Производители серверов БД.

name;
Clickhouse
MS SQL
MySQL
Oracle
PostgreSQL
PostgresPro
"""
from db.md.md.schema.metadata import (
    METADATA,
    Columns,
    Table,
)

db_vendors = Table(
    'db_vendors',
    METADATA,
    Columns.primary_key_smallint(autoincrement=False),
    Columns.created_at(),
    Columns.created_by(),
    Columns.modified_at(),
    Columns.modified_by(),
    Columns.deleted(),
    Columns.position(),
    Columns.name(),
    comment='Производители серверов БД'
)
