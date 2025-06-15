from db.md.entrypoints import alembic


def test_make_config():
    """Дымовой тест."""
    config = alembic.make_config()
    assert config
