from db.md.md.entrypoints import create_all


def test_make_config():
    """Дымовой тест. Проверка импорта."""
    assert create_all.create_all == create_all.create_all


def test_environment_variables():
    """Проверить переменные окружения.
        - хост, локальный сервер разработки (TODO: подумать как будет в CI)
        - указана тестовая БД.
     """
    db = create_all.DataBaseSettings()
    assert db.DATABASE_HOST == '127.0.0.1'
    assert db.DATABASE_NAME == 'test_md'
