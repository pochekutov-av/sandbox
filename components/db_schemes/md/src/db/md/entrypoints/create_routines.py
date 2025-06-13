"""
Создание процедур, функций, представлений.

Последовательность установки:
    1. views
    2. function
    3. procedures
"""

import pathlib

import psycopg as pg

from db.md.fixtures.tools import create_conn, execute_script


def create_routines(conn: pg.Connection):
    modules_path = pathlib.Path(__file__).parent.parent.resolve() / 'modules'
    for path in modules_path.rglob('v_*.sql'):
        execute_script(conn=conn, script_path=path)


if __name__ == '__main__':    # pragma: no cover
    with create_conn() as conn:
        create_routines(conn=conn)
