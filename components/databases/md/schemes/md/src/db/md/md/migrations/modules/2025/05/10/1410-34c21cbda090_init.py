"""init

Revision ID: 34c21cbda090
Revises: 
Create Date: 2025-05-10 14:10:14.608088+00:00

"""
from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = '34c21cbda090'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = ('modules', )
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
