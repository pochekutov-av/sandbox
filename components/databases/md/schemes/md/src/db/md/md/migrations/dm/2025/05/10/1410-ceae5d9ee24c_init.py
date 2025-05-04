"""init

Revision ID: ceae5d9ee24c
Revises: 
Create Date: 2025-05-10 14:10:11.116547+00:00

"""
from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = 'ceae5d9ee24c'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = ('dm', )
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
