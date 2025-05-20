"""
Базы данных.

[ident] базы данных служит для уникальной идентификации, общая рекомендация
форировать его из имени хоста и имени БД.

Соглашение: Считаем сочетание (host, port) уникальным.

Для MS-SQL:
В случае именованых экземпляров заполняется один из [port], [mssql_instance].

"""

from db.md.md.dd.metadata import (
    METADATA,
    Column,
    Columns,
    Integer,
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
    Columns.note(),
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
        'mssql_instance',
        Text,
        nullable=False,
        server_default='',
        comment='MS-SQL Instance',
    ),
    Column(
        'oracle_sid',
        Text,
        nullable=False,
        server_default='',
        comment='Oracle SID',
    ),
    Column(
        'oracle_service_name',
        Text,
        nullable=False,
        server_default='',
        comment='Oracle Service Name',
    ),
    UniqueConstraint(
        'host',
        'name',
    ),
    comment='Базы данных'
)
