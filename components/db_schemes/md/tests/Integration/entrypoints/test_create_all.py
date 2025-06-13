from db.md.entrypoints import create_tables


def test_make_config():
    """Дымовой тест. Проверка импорта."""
    assert create_tables.create_tables == create_tables.create_tables


def test_environment_variables():
    """Проверить переменные окружения.
        - хост, локальный сервер разработки (TODO: подумать как будет в CI)
        - указана тестовая БД.
     """
    db = create_tables.DataBaseSettings()
    assert db.DATABASE_HOST == '127.0.0.1'
    assert db.DATABASE_NAME.startswith('test_')
