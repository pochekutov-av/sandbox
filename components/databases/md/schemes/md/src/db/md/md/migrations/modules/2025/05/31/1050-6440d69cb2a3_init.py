"""init

Revision ID: 6440d69cb2a3
Revises: 
Create Date: 2025-05-31 10:58:45.599783+00:00

"""
from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = '6440d69cb2a3'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = ('modules', )
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
