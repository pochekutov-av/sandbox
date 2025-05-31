from db.md.md.schema.metadata import (
    METADATA,
    Column,
    Columns,
    ForeignKey,
    Integer,
    Table,
)

sites = Table(
    'sites',
    METADATA,
    Columns.primary_key_integer(autoincrement=False),
    Columns.created_at(),
    Columns.created_by(),
    Columns.modified_at(),
    Columns.modified_by(),
    Columns.deleted(),
    Columns.position(),
    Columns.note(),
    Columns.name(),
    Column(
        'parent_id',
        Integer,
        ForeignKey('sites.id'),
        index=True,
        nullable=True,
        comment='Родитель'
    ),
    comment='Производственные площадки'
)
