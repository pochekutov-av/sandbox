import psycopg as pg
from psycopg import sql

from db.md import schema


class TestCase:

    def fetchall(self, conn: pg.Connection,
                 table: schema.Table | schema.View) -> list[tuple]:
        order_by = ','.join(table.order_by)
        query = sql.SQL('SELECT * FROM {schema}.{name} ORDER BY {order_by}'
                        ).format(
                            schema=sql.Identifier(table.schema),
                            name=sql.Identifier(table.name),
                            order_by=sql.Identifier(order_by),
                        )
        cursor = conn.execute(query)
        return cursor.fetchall()
