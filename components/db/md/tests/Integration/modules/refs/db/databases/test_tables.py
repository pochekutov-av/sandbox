import psycopg as pg

from db.md.schema import tables
from db.md.test import TestCase


class TestCase_db_server_types(TestCase):

    def test_fields(self, conn: pg.Connection):
        types = self.fetchall(conn, tables.db_server_types)
        t = types[0]
        assert t.id == 1
        assert t.ident == 'pg/16.9'
        assert not t.deleted