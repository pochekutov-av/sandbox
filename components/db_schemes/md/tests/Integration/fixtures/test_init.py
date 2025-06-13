import psycopg as pg

from db.md.schema import tables
from db.md.test import TestCase


class TestCaseInit(TestCase):

    def test_schema(self, schema):
        """Создание схемы БД."""
        assert schema

    def test_vendors(self, conn: pg.Connection):
        vendors_etalon = [
            (1, 'Clickhouse'),
            (2, 'MS SQL'),
            (3, 'Oracle'),
            (4, 'PostgreSQL'),
            (5, 'PostgresPro'),
        ]
        vendors = self.fetchall(conn, tables.db_vendors)
        assert len(vendors_etalon) == len(vendors)
        for index, vendor in enumerate(vendors_etalon):
            assert vendor[0] == vendors[index].id
            assert vendor[1] == vendors[index].name

    def test_server_types(self, conn: pg.Connection):
        types_etalon = [
            (10, 'pg/16.9', 4, 'PostgreSQL 16.9'),
            (10, 'mssql/2019', 2, 'MS-SQL 2019'),
        ]
        types = self.fetchall(conn, tables.db_server_types)
        assert len(types_etalon) == len(types)
        for index, type_ in enumerate(types_etalon):
            assert type_[0] == types[index].position
            assert type_[1] == types[index].ident
            assert type_[2] == types[index].vendor_id
            assert type_[3] == types[index].note
