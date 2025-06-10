"""
Вспомогательные функции для модуля fixtures.
"""

import sqlalchemy as sa

from db.md.md.settings import DataBaseSettings


def create_engine():
    db_setting = DataBaseSettings()
    engine = sa.create_engine(
        db_setting.database_url,
        echo=db_setting.SA_ECHO,
        echo_pool=db_setting.SA_ECHO_POOL
    )
    return engine


def execute_script(conn: sa.Connection, script_path: str):
    with open(script_path) as f:
        script_text = sa.text(f.read())
        conn.execute(script_text)
