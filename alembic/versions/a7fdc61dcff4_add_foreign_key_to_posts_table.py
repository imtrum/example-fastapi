"""add foreign-key to posts table

Revision ID: a7fdc61dcff4
Revises: c2bcb9ec1e69
Create Date: 2026-07-23 16:45:19.527056

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7fdc61dcff4'
down_revision: Union[str, Sequence[str], None] = 'c2bcb9ec1e69'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.add_column('posts', sa.Column('owner_id',sa.Integer,nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users',local_cols=[
        'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    """Downgrade schema."""
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts','owner_id')
    pass
