"""Added Foreign Key

Revision ID: cca7fe0b508c
Revises: 25f247ffb599
Create Date: 2022-09-24 16:40:21.964076

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cca7fe0b508c'
down_revision = '25f247ffb599'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('poster_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'users', ['poster_id'], ['id'])
    op.drop_column('posts', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('author', mysql.VARCHAR(length=255), nullable=True))
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'poster_id')
    # ### end Alembic commands ###