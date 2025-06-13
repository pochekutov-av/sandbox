"""
Вариант когда начальные данные вставляются через sqlalchemy.

Вариант не используется, оставлен в коде как пример, в каких то случаях
будет удобнее сделать миграцию через sqlalchemy.
"""

from dataclasses import asdict, dataclass
from datetime import UTC, datetime

import sqlalchemy as sa

from db.md.schema.metadata import METADATA
from db.md.settings import DataBaseSettings

users = sa.table(
    'users',
    sa.column('id'),
    sa.column('created_at'),
    sa.column('created_by_id'),
    sa.column('modified_at'),
    sa.column('modified_by_id'),
    sa.column('deleted'),
    sa.column('ident'),
    sa.column('name'),
    schema=METADATA.schema,
)

db_vendors = sa.table(
    'db_vendors',
    sa.column('id'),
    sa.column('created_at'),
    sa.column('created_by_id'),
    sa.column('modified_at'),
    sa.column('modified_by_id'),
    sa.column('deleted'),
    sa.column('position'),
    sa.column('name'),
    schema=METADATA.schema,
)


@dataclass
class User:
    id: int
    created_at: datetime
    created_by_id: int
    modified_at: datetime
    modified_by_id: int
    deleted: bool
    ident: str
    name: str


@dataclass
class Vendor:
    id: int
    created_at: datetime
    created_by_id: int
    modified_at: datetime
    modified_by_id: int
    deleted: bool
    position: int
    name: str


def create_user(now: datetime) -> User:
    user_id = 1
    user = User(
        id=user_id,
        created_at=now,
        created_by_id=user_id,
        modified_at=now,
        modified_by_id=user_id,
        deleted=False,
        ident='app',
        name='Приложение',
    )
    return user


def create_vendors(user: User, now: datetime) -> list[Vendor]:
    vendors = [
        (1, 'Clickhouse'),
        (2, 'MS SQL'),
        (3, 'MySQL'),
        (4, 'Oracle'),
        (5, 'PostgreSQL'),
        (6, 'PostgresPro'),
    ]
    result = []
    for vendor in vendors:
        result.append(
            Vendor(
                created_at=now,
                created_by_id=user.id,
                modified_at=now,
                modified_by_id=user.id,
                deleted=False,
                id=vendor[0],  # считаем, что совпадает с порядковым номером
                position=vendor[0],
                name=vendor[1],
            )
        )
    return result


def loaddata(engine):
    now = datetime.now(UTC)
    user = create_user(now=now)
    vendors = create_vendors(user=user, now=now)
    with engine.connect() as conn:
        # user:
        stmt = users.insert().values(asdict(user))
        conn.execute(stmt)
        # vendors:
        stmt = db_vendors.insert().values(
            [asdict(vendor) for vendor in vendors]
        )
        conn.execute(stmt)
        # commit
        conn.commit()


if __name__ == '__main__':

    class Settings:
        db = DataBaseSettings()

    engine = sa.create_engine(
        Settings.db.database_url,
        echo=Settings.db.SA_ECHO,
        echo_pool=Settings.db.SA_ECHO_POOL
    )
    loaddata(engine=engine)
