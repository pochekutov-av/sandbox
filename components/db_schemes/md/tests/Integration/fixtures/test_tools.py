from db.md.fixtures import tools


def test_create_conn():
    assert tools.create_conn()
