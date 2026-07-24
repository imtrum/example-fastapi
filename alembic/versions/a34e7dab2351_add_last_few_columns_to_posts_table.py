"""add last few columns to posts table

Revision ID: a34e7dab2351
Revises: a7fdc61dcff4
Create Date: 2026-07-23 16:58:51.912549

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a34e7dab2351'
down_revision: Union[str, Sequence[str], None] = 'a7fdc61dcff4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.add_column(
        'posts',
        sa.Column(
            'published',
            sa.Boolean(),
            nullable=True,
            server_default='TRUE'
        )
    )

    op.add_column(
        'posts',
        sa.Column(
            'created_at',
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text('NOW()')
        )
    )
    pass


def downgrade():
    """Downgrade schema."""
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    pass
