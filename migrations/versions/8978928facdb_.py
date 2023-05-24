"""empty message

Revision ID: 8978928facdb
Revises: d752e51ce0da
Create Date: 2023-05-19 12:23:56.591083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8978928facdb'
down_revision = 'd752e51ce0da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_subscribed', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_subscribed')
    # ### end Alembic commands ###
