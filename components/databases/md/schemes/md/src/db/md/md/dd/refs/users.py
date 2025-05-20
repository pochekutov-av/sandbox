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
    # TODO: username, name, email, password
    # last_login - дата последнего ввода пароля
    # xxx - дата последней активности, сессии (на каждый запрос сильно часто,
    #       подумать как делать реже
    comment='Пользователи'
)