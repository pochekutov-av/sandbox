import sqlalchemy as sa

from db.md.md.fixtures.tools import create_engine


def test_create_engine():
    """Проверить создание engine."""
    assert isinstance(create_engine(), sa.Engine)
