from db.md.md.dd.metadata import METADATA
from db.md.md.dd.tables import (
    sites,
    users,
)


class TestUsers:

    def test_in_metadata(self):
        assert users in METADATA


class TestSites:

    def test_in_metadata(self):
        assert sites in METADATA
