"""
Базы данных.

[ident] базы данных служит для уникальной идентификации, общая рекомендация
формировать его из [host] и [name].

Сущность "сервер" обдуманно решил не вводить, поскольку чаще всего одна БД
будет находиться на одном сервере, а скорее даже иначе - одна запись в
[db_databases] будет соответствовать кластеру серверов, тут нужно будет
создать сущность "db_nodes".

Для MS-SQL:
В случае именованых экземпляров заполняется один из [port], [mssql_instance].
"""

from db.md.md.schema.metadata import (
    METADATA,
    Column,
    Columns,
    ForeignKey,
    Integer,
    SmallInteger,
    Table,
    Text,
    UniqueConstraint,
)

db_databases = Table(
    'db_databases',
    METADATA,
    Columns.primary_key_smallint(),
    Columns.created_at(),
    Columns.created_by(),
    Columns.modified_at(),
    Columns.modified_by(),
    Columns.deleted(),
    Columns.ident(),
    Column(
        'host',
        Text,
        nullable=False,
        comment='Хост',
    ),
    Column(
        'name',
        Text,
        nullable=False,
        comment='Имя',
    ),
    Column(
        'port',
        Integer,
        nullable=True,
        comment='Порт',
    ),
    Column(
        'type_id',
        SmallInteger,
        ForeignKey('db_server_types.id'),
        index=True,
        nullable=False,
        comment='Версии сервера'
    ),
    Column(
        'mssql_instance',
        Text,
        nullable=False,
        server_default='',
        comment='MS-SQL Instance',
    ),
    Columns.note(),
    UniqueConstraint(
        'host',
        'name',
    ),
    comment='Базы данных'
)
