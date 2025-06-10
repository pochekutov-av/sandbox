from db.md.md.settings import DataBaseSettings


def test_settings():
    db_settings = DataBaseSettings()
    assert isinstance(db_settings.LOGGING_CONFIG, dict)
