"""create posts table

Revision ID: f2e0a300c6dd
Revises: 
Create Date: 2026-07-21 00:29:48.279005

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2e0a300c6dd'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, 
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
   

def downgrade():
    op.drop_table("posts")
    """Downgrade schema."""
    
