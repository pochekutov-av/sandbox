from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,  # 4 bytes, -2 147 483 648 to +2 147 483 647
    MetaData,
    SmallInteger,  # 2 bytes, -32 768 to +32 767
    String,
    Table,  # noqa: F401
    Text,
    UniqueConstraint,  # noqa: F401
)
from sqlalchemy import DateTime as OriginDateTime

SCHEMA = 'md'


class DateTime(OriginDateTime):
    """Использовать timezone всегда."""

    def __init__(self):
        super().__init__(timezone=True)


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
    'Text',
    'UniqueConstraint',
]

MAX_IDENT_LENGTH = 63
"""Максимальная длина идентификатора, берем значение как в PostgreSQL 2^6-1."""


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
    def primary_key_smallint(autoincrement: bool = True) -> Column:
        return Column(
            'id',
            SmallInteger,
            primary_key=True,
            autoincrement=autoincrement,
        )

    @staticmethod
    def created_at(index: bool = False) -> Column:
        """
        Для created_at modified_at, "server_default=UTCNOW" не ставим, поскольку
        хочется чтобы все объекты созданные в рамках одной транзакции имели
        совпадающее время создания и изменения.
        """
        return Column(
            'created_at',
            DateTime,
            index=index,
            nullable=False,
            comment='Время создания'
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
            'modified_at', DateTime, nullable=False, comment='Время изменения'
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
    def note() -> Column:
        """Comments vs Notes
        Будем считать, коментарии применяются там где есть место обсуждения -
        комментарии от нескольких лиц, если же имеет место лишь одно едиственно
        уточнение используем термин примечание.

        https://support.microsoft.com/en-us/office
        /insert-comments-and-notes-in-excel-bdcc9f5d-38e2-45b4-9a92-0b2b5c7bf6f8
        """
        return Column(
            'note',
            Text,
            nullable=False,
            comment='Примечание',
            server_default='',
        )

    @staticmethod
    def ident() -> Column:
        return Column(
            'ident',
            String(MAX_IDENT_LENGTH),
            nullable=False,
            index=True,
            unique=True,
            comment='Уникальный идентификатор',
        )

    @staticmethod
    def name() -> Column:
        return Column(
            'name',
            String,
            nullable=False,
            comment='Наименование',
        )

    @staticmethod
    def position() -> Column:
        return Column(
            'position', Integer, nullable=True, comment='Порядок элемента'
        )

    @staticmethod
    def email() -> Column:
        return Column(
            'email',
            String,
            nullable=False,
            index=True,
            server_default='',
            comment='E-mail',
        )

    @staticmethod
    def varchar(*, name: str, comment: str, nullable: bool = True) -> Column:
        return Column(
            name,
            String,
            comment=comment,
            nullable=nullable,
        )
