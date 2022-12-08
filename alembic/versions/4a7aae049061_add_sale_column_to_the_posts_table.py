"""add sale column to the posts table

Revision ID: 4a7aae049061
Revises: 9d959f9e3bed
Create Date: 2022-12-04 21:42:09.217626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a7aae049061'
down_revision = '9d959f9e3bed'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('sale',sa.BOOLEAN(),server_default='TRUE',nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','sale')
    pass
