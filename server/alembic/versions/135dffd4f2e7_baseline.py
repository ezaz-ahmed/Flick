"""baseline

Revision ID: 135dffd4f2e7
Revises: 
Create Date: 2026-09-27 00:02:30.896834

"""
from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = '135dffd4f2e7'
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""


def downgrade() -> None:
    """Downgrade schema."""
