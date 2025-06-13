import psycopg as pg
import sqlalchemy as sa
from psycopg import sql


class TestCase:

    def fetchall(self, conn: pg.Connection, table: sa.Table) -> list[tuple]:

        query = sql.SQL('SELECT * FROM {schema}.{name}').format(
            schema=sql.Identifier(table.schema),
            name=sql.Identifier(table.name),
        )
        cursor = conn.execute(query)
        return cursor.fetchall()
