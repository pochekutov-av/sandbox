"""
Импортирование всех таблиц, для возможности использования при автогенерации
через alembic миграций БД.

Сюда же импортируем METADATA, чтобы в migrations.env.py использовать её.
"""

from .metadata import METADATA
from .refs.db.db_databases import db_databases
from .refs.db.db_server_types import db_server_types
from .refs.db.db_vendors import db_vendors
from .refs.sites import sites
from .refs.users import users

__all__ = [
    'METADATA',
    'db_databases',
    'db_server_types',
    'db_vendors',
    'sites',
    'users',
]
