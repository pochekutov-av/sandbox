from db.md.md.dd.metadata import (
    METADATA,
    Columns,
    Table,
)

users = Table(
    'users',
    METADATA,
    Columns.primary_key_integer(),
    Columns.created_at(),
    Columns.created_by(),
    Columns.modified_at(),
    Columns.modified_by(),
    Columns.deleted(),

    # TODO: username, name, email, password, last_login
    comment='Пользователи'
)