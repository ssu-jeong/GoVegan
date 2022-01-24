"""empty message

Revision ID: 04de7b8d2c53
Revises: 79bf22824769
Create Date: 2021-12-19 17:01:27.654256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04de7b8d2c53'
down_revision = '79bf22824769'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.Text(), nullable=True),
    sa.Column('page_url', sa.Text(), nullable=True),
    sa.Column('image_url', sa.Text(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###