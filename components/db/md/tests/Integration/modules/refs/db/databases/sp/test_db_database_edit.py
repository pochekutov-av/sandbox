from dataclasses import asdict, dataclass
from datetime import UTC, datetime

import psycopg as pg

from db.md.schema import procedures, tables
from db.md.test import TestCase


@dataclass
class ProcParams:
    user_id: int
    now: datetime
    mode: str
    ident: str
    host: str
    name: str
    port: int
    type_id: int
    mssql_instance: str
    note: str


class TestCase_db_database_edit(TestCase):

    def get_params(self, mode: str = 'add'):
        return ProcParams(
            user_id=1,
            now=datetime.now(UTC),
            mode='add',
            ident='the-ident',
            host='the-host',
            name='the-name',
            port=123,
            type_id=1,
            mssql_instance='the-mssql_instance',
            note='the-note',
        )

    def test_add_success(self, conn: pg.Connection):
        """Добавление новой БД, указываются все возможные поля."""
        params = self.get_params()
        res = self.call(
            conn, procedures.db_database_edit, params=asdict(params)
        )
        assert res.output.id
        assert res.output.errors is None

        databases = self.fetchall(conn, tables.db_databases)
        assert len(databases) == 1
        db = databases[0]
        assert db.id == res.output.id
        assert db.created_at == params.now
        assert db.created_by_id == params.user_id
        assert db.modified_at == params.now
        assert db.modified_by_id == params.user_id
        assert db.deleted is False
        assert db.ident == params.ident
        assert db.host == params.host
        assert db.name == params.name
        assert db.port == params.port
        assert db.type_id == params.type_id
        assert db.mssql_instance == params.mssql_instance
        assert db.note == params.note
    
    def test_delete_success(self, conn: pg.Connection):
        assert 1 == 2
