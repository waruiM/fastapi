"""filling all details for post section

Revision ID: a31a9b0bb561
Revises: 9671dbf0bcf2
Create Date: 2022-12-05 22:00:33.272756

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision = 'a31a9b0bb561'
down_revision = '9671dbf0bcf2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=text('now()')))
    
    


def downgrade() :
    op.drop_column('posts','created_at')