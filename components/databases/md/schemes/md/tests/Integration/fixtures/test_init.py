import sqlalchemy as sa


def test_load(db_init):
    """Проверить успешную загрузку данных из init fixture."""
    assert isinstance(db_init.engine, sa.Engine)
