"""add content column to posts table

Revision ID: 89fa59fa8cc4
Revises: f2e0a300c6dd
Create Date: 2026-07-21 02:10:36.884513

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89fa59fa8cc4'
down_revision: Union[str, Sequence[str], None] = 'f2e0a300c6dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    
