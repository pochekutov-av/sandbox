from db.md.md import logging
from db.md.md.settings import DataBaseSettings


def test_import_settings():
    db_settings = DataBaseSettings()
    logging.configure(db_settings.LOGGING_CONFIG)
