"""
Создание процедур, функций, представлений.

Последовательность установки:
    1. views
    2. function
    3. procedures
"""

import pathlib

import psycopg as pg

from db.md.contrib.db import create_conn, execute_script


def create_routines(conn: pg.Connection):
    """Обходит все *.sql файлы в папках ['v', 'sp'], выполняет их на БД."""
    modules_path = pathlib.Path(__file__).parent.parent.resolve() / 'modules'
    views = []
    sp = []
    for path in modules_path.rglob('*.sql'):
        parent_name = str(path.parent.name)
        if parent_name == 'v':
            views.append(path)
        elif parent_name == 'sp':
            sp.append(path)
    for path in views + sp:
        execute_script(conn=conn, script_path=path)
        conn.commit()


if __name__ == '__main__':    # pragma: no cover
    with create_conn() as conn:
        create_routines(conn=conn)
