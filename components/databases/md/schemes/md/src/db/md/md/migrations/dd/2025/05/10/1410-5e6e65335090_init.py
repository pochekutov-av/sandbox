"""init

Revision ID: 5e6e65335090
Revises: 
Create Date: 2025-05-10 14:10:06.220313+00:00

"""
from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = '5e6e65335090'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = ('dd', )
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
