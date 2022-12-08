"""users login

Revision ID: 25ca0093fc35
Revises: 4a7aae049061
Create Date: 2022-12-04 22:14:05.868007

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision = '25ca0093fc35'
down_revision = '4a7aae049061'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table ('users',
        sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
        sa.Column('email',sa.String(),nullable=False,unique=True),
        sa.Column('username',sa.String(),nullable=False),
        sa.Column('password', sa.String(),nullable=False),
        sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')))
     
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
