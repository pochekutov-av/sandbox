"""
Вариант когда начальные данные вставляются через T-SQL скрипт.
"""

import pathlib

import sqlalchemy as sa

from db.md.md.fixtures.tools import create_engine, execute_script


def loaddata(conn: sa.Connection):
    parent_path = pathlib.Path(__file__).parent.resolve()
    script_path = parent_path / 'initial.sql'
    execute_script(conn=conn, script_path=script_path)


if __name__ == '__main__':    # pragma: no cover
    engine = create_engine()
    with engine.connect() as conn:
        loaddata(conn=conn)
        conn.commit()