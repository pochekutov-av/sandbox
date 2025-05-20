"""
Версии серверов БД.

Конкретные версии БД, указывается номер версии.
"""
from db.md.md.dd.metadata import (
    METADATA,
    Column,
    Columns,
    ForeignKey,
    SmallInteger,
    Table,
)

db_server_types = Table(
    'db_server_types',
    METADATA,
    Columns.primary_key_smallint(autoincrement=False),
    Columns.created_at(),
    Columns.created_by(),
    Columns.modified_at(),
    Columns.modified_by(),
    Columns.deleted(),
    Columns.position(),
    Columns.note(),
    Columns.ident(),
    Column(
        'vendor_id',
        SmallInteger,
        ForeignKey('db_vendors.id'),
        index=True,
        nullable=False,
        comment='Производитель'
    ),
    comment='Версии серверов БД'
)
