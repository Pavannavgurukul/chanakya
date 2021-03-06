"""empty message

Revision ID: 85426e793060
Revises: 7d46ed05464c
Create Date: 2018-05-01 11:00:27.575107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85426e793060'
down_revision = '7d46ed05464c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('network_speed', sa.Float(), nullable=True))
    op.add_column('student', sa.Column('user_agent', sa.String(length=150), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'user_agent')
    op.drop_column('student', 'network_speed')
    # ### end Alembic commands ###
