from db.md.schema.metadata import (
    METADATA,
    Columns,
    Table,
)

users = Table(
    'users',
    METADATA,
    Columns.primary_key_int(),
    Columns.created_at(),
    Columns.created_by(),
    Columns.modified_at(),
    Columns.modified_by(),
    Columns.deleted(),
    Columns.ident(),    # Логин, domain\ivanov_av, или ivanov_av
    Columns.name(),    # Имя "Иванов А.В."
    Columns.email(),    # уникальности НЕ требуем
    Columns.datetime(
        'last_login',
        nullable=True,
        comment='Дата последнего успешного ввода пароля'
    ),
    Columns.datetime(
        'last_activity',
        nullable=True,
        comment='Дата последней активности (точность около часа)'
    ),
    Columns.varchar('password', nullable=True, comment='Пароль'),
    comment='Пользователи'
)
