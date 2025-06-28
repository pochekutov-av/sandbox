"""
Вариант когда начальные данные вставляются через T-SQL скрипт.
"""

import pathlib

import psycopg as pg

from db.md.contrib.db import create_conn, execute_script


def loaddata(conn: pg.Connection):
    parent_path = pathlib.Path(__file__).parent.resolve()
    script_path = parent_path / 'initial.sql'
    execute_script(conn=conn, script_path=script_path)


if __name__ == '__main__':    # pragma: no cover
    with create_conn() as conn:
        loaddata(conn=conn)
