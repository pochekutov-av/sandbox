import pathlib
from dataclasses import dataclass
from types import SimpleNamespace

import psycopg as pg
import pytest

from db.md.contrib.db import execute_script


@dataclass
class User:
    """Класс строки для таблицы [users]."""
    id: int


@dataclass
class DbServerType:
    """Класс строки для таблицы [db_server_types]."""
    id: int


def loaddata(filename: str, conn: pg.Connection):
    parent_path = pathlib.Path(__file__).parent.resolve()
    script_path = parent_path / 'fixtures' / filename
    execute_script(conn=conn, script_path=script_path)


@pytest.fixture(name='users', scope='session')
def fixture_users(private_connection) -> pg.Connection:
    loaddata('users.sql', conn=private_connection)
    private_connection.commit()
    return SimpleNamespace(app=User(id=1), app2=User(id=2))


@pytest.fixture(name='db_server_types', scope='session')
def fixture_db_server_types() -> pg.Connection:
    return SimpleNamespace(
        pg16_9=DbServerType(id=1),
        mssql2019=DbServerType(id=2),
    )
