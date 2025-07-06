from db.md.schema.metadata import (
    METADATA,
    Columns,
    Table,
)

sites = Table(
    'sites',
    METADATA,
    Columns.primary_key_int(autoincrement=False),
    Columns.created_at(),
    Columns.created_by(),
    Columns.modified_at(),
    Columns.modified_by(),
    Columns.deleted(),
    Columns.position(),
    Columns.note(),
    Columns.name(),
    Columns.foreign_key_int(
        'parent_id', 'sites.id', nullable=True, comment='Родитель'
    ),
    comment='Производственные площадки'
)
