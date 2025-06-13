from db.md import logging
from db.md.settings import DataBaseSettings


def test_import_settings():
    db_settings = DataBaseSettings()
    logging.configure(db_settings.LOGGING_CONFIG)
