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

from db.md.schema.metadata import (
    METADATA,
    Columns,
    Table,
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
    Columns.varchar('host', comment='Хост'),
    Columns.varchar('name', comment='Имя'),
    Columns.int('port', nullable=True, comment='Порт'),
    Columns.foreign_key_smallint(
        'type_id', 'db_server_types.id', comment='Версия сервера'
    ),
    Columns.varchar('mssql_instance', comment='MS-SQL Instance'),
    Columns.note(),
    UniqueConstraint(
        'host',
        'name',
    ),
    comment='Базы данных'
)
