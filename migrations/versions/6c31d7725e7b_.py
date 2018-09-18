"""empty message

Revision ID: 6c31d7725e7b
Revises: fd29632f91b5
Create Date: 2018-09-17 07:47:04.532715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c31d7725e7b'
down_revision = 'fd29632f91b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('caste', sa.Enum('sc', 'st', 'obc', 'general', 'other', name='caste'), nullable=True))
    op.add_column('students', sa.Column('family_member_income_detail', sa.Text(), nullable=True))
    op.add_column('students', sa.Column('monthly_family_member', sa.Integer(), nullable=True))
    op.add_column('students', sa.Column('religion', sa.Enum('hindu', 'muslim', 'christian', 'jain', name='religion'), nullable=True))
    op.add_column('students', sa.Column('total_family_member', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'total_family_member')
    op.drop_column('students', 'religion')
    op.drop_column('students', 'monthly_family_member')
    op.drop_column('students', 'family_member_income_detail')
    op.drop_column('students', 'caste')
    # ### end Alembic commands ###
