from dataclasses import dataclass


@dataclass
class Procedure:
    """Класс для описания хранимой процедуры (procedure) в базе данных."""
    name: str
    schema: str = 'md'

    def __str__(self):
        return f'{self.schema}.{self.name}'

    @property
    def ident(self):
        return f'{self.schema}.{self.name}'


db_database_edit = Procedure('db_database_edit')
