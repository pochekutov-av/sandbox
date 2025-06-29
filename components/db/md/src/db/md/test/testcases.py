from types import SimpleNamespace

import psycopg as pg
from psycopg import sql

from db.md import schema


class TestCase:

    def fetchall(self, conn: pg.Connection,
                 table: schema.Table | schema.View) -> list[tuple]:
        order_by = ','.join(table.order_by)
        query = sql.SQL('SELECT * FROM {name} ORDER BY {order_by}').format(
            name=sql.Identifier(table.schema, table.name),
            order_by=sql.Identifier(order_by),
        )
        cursor = conn.execute(query)
        return cursor.fetchall()

    def call(self, conn: pg.Connection, procedure: schema.Procedure, params):
        args = []
        args_values = {}
        for arg_name, arg_value in params.items():
            args.append(f'"{arg_name}" => %({arg_name})s')
            args_values[arg_name] = arg_value
        query = 'CALL "{schema}"."{name}"({arguments})'.format(
            schema=procedure.schema,
            name=procedure.name,
            arguments=', '.join(args)
        )
        with conn.cursor() as cur:
            output_args = cur.execute(query, args_values).fetchone()
            res = SimpleNamespace(output=output_args)
        return res
