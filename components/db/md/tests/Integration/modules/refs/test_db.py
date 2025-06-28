import psycopg as pg

from db.md.schema import tables, views
from db.md.test import TestCase


class TestCase_v_db_server_types(TestCase):

    def test_fields(self, conn: pg.Connection):
        types = self.fetchall(conn, views.v_db_server_types)
        t = types[0]
        assert t.id == 1
        assert t.ident == 'pg/16.9'
        assert t.vendor == 'PostgreSQL'
        assert t.note == 'PostgreSQL 16.9'
        assert t.modified_at
        assert t.modified_by == 'Приложение'
        assert t.created_at
        assert t.created_by == 'Приложение'
        assert t.position == 10
        assert not t.deleted


class TestCase_db_server_types(TestCase):

    def test_fields(self, conn: pg.Connection):
        types = self.fetchall(conn, tables.db_server_types)
        t = types[0]
        assert t.id == 1
        assert t.ident == 'pg/16.9'
        assert not t.deleted
