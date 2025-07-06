"""
Версии серверов БД.

Конкретные версии БД, указывается номер версии.
"""
from db.md.schema.metadata import (
    METADATA,
    Columns,
    Table,
)

db_server_types = Table(
    'db_server_types',
    METADATA,
    Columns.primary_key_smallint(),
    Columns.created_at(),
    Columns.created_by(),
    Columns.modified_at(),
    Columns.modified_by(),
    Columns.deleted(),
    Columns.position(),
    Columns.ident(),
    Columns.foreign_key_smallint(
        'vendor_id', 'db_vendors.id', comment='Производитель'
    ),
    Columns.note(),
    comment='Версии серверов БД'
)
