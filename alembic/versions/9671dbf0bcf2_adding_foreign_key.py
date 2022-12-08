"""adding foreign key

Revision ID: 9671dbf0bcf2
Revises: 25ca0093fc35
Create Date: 2022-12-04 22:33:25.751149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9671dbf0bcf2'
down_revision = '25ca0093fc35'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_user_fk',source_table="posts",referent_table="users",
    local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")

    pass


def downgrade():
    op.drop_constraints('posts_user_fk',table_name="posts")
    op.drop_column("posts",'owner_id')
    pass
