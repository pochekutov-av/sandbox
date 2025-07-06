from dataclasses import asdict, dataclass
from datetime import UTC, datetime, timedelta

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
    # Optional
    id: int = None


class TestCase_db_database_edit(TestCase):

    def call_proc(self, conn: pg.Connection, params: ProcParams):
        return self.call(
            conn, procedures.db_database_edit, params=asdict(params)
        )

    def create_params(
        self,
        *,
        mode: str,
        user_id: int = 1,
        now: datetime = None,
        postfix: str = '',
        port: int = 123,
        type_id: int = 1,
        id: int = None
    ):
        return ProcParams(
            user_id=user_id,
            now=datetime.now(UTC) if now is None else now,
            mode=mode,
            ident='the-ident' + postfix,
            host='the-host' + postfix,
            name='the-name + postfix',
            port=port,
            type_id=type_id,
            mssql_instance='the-mssql_instance' + postfix,
            note='the-note' + postfix,
            id=id
        )

    def test_add_success(self, conn: pg.Connection):
        """Успешное добавление, указываются все возможные поля."""
        params = self.create_params(mode='add')
        res = self.call_proc(conn, params)
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

    def test_change_success(self, users, db_server_types, conn: pg.Connection):
        """Успешное изменение, указываются все возможные поля."""
        add_params = self.create_params(
            mode='add',
            type_id=db_server_types.pg16_9.id,
        )
        add_res = self.call_proc(conn, add_params)
        change_params = self.create_params(
            mode='change',
            id=add_res.output.id,
            user_id=users.app2.id,
            now=add_params.now + timedelta(1),
            port=add_params.port + 1,
            type_id=db_server_types.mssql2019.id,
            postfix='_changed',
        )
        change_res = self.call_proc(conn, change_params)

        assert add_params.user_id != change_params.user_id
        assert add_params.now < change_params.now
        assert add_params.ident != change_params.ident
        assert add_params.port != change_params.port
        assert add_params.type_id != change_params.type_id

        assert add_res.output.id == change_res.output.id

        databases = self.fetchall(conn, tables.db_databases)
        assert len(databases) == 1
        db = databases[0]
        assert db.id == change_res.output.id
        assert db.created_at == add_params.now
        assert db.created_by_id == add_params.user_id
        assert db.modified_at == change_params.now
        assert db.modified_by_id == change_params.user_id
        assert db.deleted is False
        assert db.ident == change_params.ident
        assert db.host == change_params.host
        assert db.name == change_params.name
        assert db.port == change_params.port
        assert db.type_id == change_params.type_id
        assert db.mssql_instance == change_params.mssql_instance
        assert db.note == change_params.note

    def test_change_where_id(self, users, db_server_types, conn: pg.Connection):
        """Успешное изменение только для переданного ИД.

        Создадим две записи, изменим одну, убедимся, что вторая без изменений.
        """
        db1_params = self.create_params(mode='add', postfix='db1')
        db1_res = self.call_proc(conn, db1_params)
        db2_params = self.create_params(mode='add', postfix='db2')
        db2_res = self.call_proc(conn, db2_params)
        db1_change_params = self.create_params(
            mode='change', id=db1_res.output.id, postfix='db1_change'
        )
        self.call_proc(conn, db1_change_params)

        databases = self.fetchall(conn, tables.db_databases)
        assert len(databases) == 2
        db1 = databases[0]
        db2 = databases[1]
        assert db1.id == db1_res.output.id
        assert db1.ident == db1_change_params.ident
        assert db2.id == db2_res.output.id
        assert db2.ident == db2_params.ident
