from db.md.md.dd import tables
from db.md.md.dd.metadata import METADATA


class BaseMixin:

    def test_in_metadata(self):
        assert self.table in METADATA


class TestUsers(BaseMixin):
    table = tables.users


class TestSites(BaseMixin):
    table = tables.sites


class TestDbVendors(BaseMixin):
    table = tables.db_vendors


class TestDbServerTypes(BaseMixin):
    table = tables.db_server_types


class TestDbDatabases(BaseMixin):
    table = tables.db_databases
