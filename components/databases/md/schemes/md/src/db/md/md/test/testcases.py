import psycopg as pg
import sqlalchemy as sa


class TestCase:

    def fetchall(self, conn: pg.Connection, table: sa.Table) -> list[tuple]:
        stmt = f'SELECT * FROM {table.schema}.{table.name}'
        cursor = conn.execute(stmt)
        return cursor.fetchall()
