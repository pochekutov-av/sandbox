"""
Импортирование всех таблиц, для возможности использования при автогенерации
через alembic миграций БД.

Сюда же импортируем METADATA, чтобы в migrations.env.py использовать её.
"""

from .metadata import METADATA
from .refs.sites import sites
from .refs.users import users

__all__ = [
    'METADATA',
    'sites',
    'users',
]
