from db.md.schema.metadata import (
    METADATA,
    Column,
    Columns,
    DateTime,
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
    Columns.ident(),    # Логин, domain\ivanov_av, или ivanov_av
    Columns.name(),    # Имя "Иванов А.В."
    Columns.email(),    # уникальности НЕ требуем
    Column(
        'last_login',
        DateTime,
        nullable=True,
        comment='Дата последнего успешного ввода пароля'
    ),
    Column(
        'last_activity',
        DateTime,
        nullable=True,
        comment='Дата последней активности (точность около часа)'
    ),
    Columns.varchar(name='password', comment='Пароль'),
    comment='Пользователи'
)
