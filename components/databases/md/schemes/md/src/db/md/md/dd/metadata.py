from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    MetaData,
    Table,  # noqa: F401
    Text,
)

SCHEMA = 'md'

CONVENTION = {
    'ix': 'ix_%(table_name)s_%(column_0_name)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
}

METADATA = MetaData(schema=SCHEMA, naming_convention=CONVENTION)

__all_ = [
    'Boolean',
    'Column',
    'DateTime',
    'ForeignKey',
    'Integer',
    'MetaData',
    'String',
    'Table',
]


class Columns:

    @staticmethod
    def primary_key_integer(autoincrement: bool = True) -> Column:
        return Column(
            'id',
            Integer,
            primary_key=True,
            autoincrement=autoincrement,
        )

    @staticmethod
    def created_at(index: bool = False) -> Column:
        """
        Для created_at modified_at, "server_default=UTCNOW" не ставим, поскольку
        хочетс чтобы все объекты созданные в рамках одной транзакции имели
        совпадающее время создания и изменения.
        """
        return Column(
            'created_at',
            DateTime,
            index=index,
            nullable=False,
            comment='Создан'
        )

    @staticmethod
    def created_by() -> Column:
        return Column(
            'created_by_id',
            Integer,
            ForeignKey('users.id'),
            index=True,
            nullable=False,
            comment='Создал'
        )

    @staticmethod
    def modified_at(index: bool = False) -> Column:
        return Column(
            'modified_at',
            DateTime,
            nullable=False,
            comment='Время изменения записи'
        )

    @staticmethod
    def modified_by() -> Column:
        return Column(
            'modified_by_id',
            Integer,
            ForeignKey('users.id'),
            index=True,
            nullable=False,
            comment='Изменил'
        )

    @staticmethod
    def deleted() -> Column:
        return Column('deleted', Boolean, nullable=False, comment='Удален')

    @staticmethod
    def name() -> Column:
        return Column(
            'name',
            Text,
            nullable=False,
            comment='Наименование на русском языке',
        )

    @staticmethod
    def name_en() -> Column:
        return Column(
            'name_en',
            Text,
            nullable=False,
            comment='Наименование английском языке',
        )

    @staticmethod
    def position() -> Column:
        return Column(
            'position', Integer, nullable=True, comment='Порядок элемента'
        )
