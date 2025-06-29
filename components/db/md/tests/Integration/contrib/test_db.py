from db.md.contrib import db


def test_create_conn():
    assert db.create_conn()
