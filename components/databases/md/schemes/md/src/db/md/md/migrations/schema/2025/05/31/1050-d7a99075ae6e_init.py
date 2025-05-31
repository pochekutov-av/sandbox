"""init

Revision ID: d7a99075ae6e
Revises: 
Create Date: 2025-05-31 10:58:37.060656+00:00

"""
from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = 'd7a99075ae6e'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = ('schema', )
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
