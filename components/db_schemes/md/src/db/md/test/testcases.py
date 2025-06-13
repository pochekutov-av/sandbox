import psycopg as pg
import sqlalchemy as sa

# TODO: sql: https://www.psycopg.org/psycopg3/docs/api/sql.html#module-psycopg.sql

class TestCase:

    def fetchall(self, conn: pg.Connection, table: sa.Table) -> list[tuple]:
        stmt = f'SELECT * FROM {table.schema}.{table.name}'
        cursor = conn.execute(stmt)
        return cursor.fetchall()
