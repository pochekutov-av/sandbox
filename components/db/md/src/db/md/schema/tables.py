from dataclasses import dataclass, field


@dataclass
class Table:
    """Класс для описания таблицы (table) в базе данных."""
    name: str
    schema: str = 'md'
    order_by: list = field(default_factory=lambda: ['id'])

    def __str__(self):
        return f'{self.schema}.{self.name}'


db_databases = Table(name='db_databases')
db_server_types = Table(name='db_server_types')
db_vendors = Table(name='db_vendors')

sites = Table(name='sites')
users = Table(name='users')
