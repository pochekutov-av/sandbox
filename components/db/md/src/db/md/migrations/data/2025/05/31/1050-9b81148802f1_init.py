"""init

Revision ID: 9b81148802f1
Revises: 
Create Date: 2025-05-31 10:58:40.959806+00:00

"""
from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = '9b81148802f1'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = ('data', )
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
