"""empty message

Revision ID: 9d959f9e3bed
Revises: 
Create Date: 2022-12-03 14:49:10.861969

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision = '9d959f9e3bed'
down_revision = None
branch_labels = None
depends_on = None

#make changes
def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(), nullable=False,primary_key=True)
                    ,sa.Column('name',sa.String(), nullable=False),
                    sa.Column('type',sa.String(),nullable=False)
                    ,sa.Column('reg',sa.String(),nullable=False))
    pass

#making a rollback
def downgrade():
    op.drop_table('posts')
    pass
