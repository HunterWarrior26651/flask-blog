"""Add Posts Model

Revision ID: 3a451e84125d
Revises: 67bd56c61ec4
Create Date: 2022-09-16 18:55:26.910697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a451e84125d'
down_revision = '67bd56c61ec4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('author', sa.String(length=255), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###
