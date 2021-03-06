"""empty message

Revision ID: 5e721df1403c
Revises: 
Create Date: 2018-06-23 09:03:45.285381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e721df1403c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('bid', sa.Integer(), nullable=False),
    sa.Column('b_name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('bid'),
    sa.UniqueConstraint('b_name')
    )
    op.create_table('user',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('is_active', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('book')
    # ### end Alembic commands ###
