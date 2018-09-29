"""empty message

Revision ID: 5ab30371173e
Revises: 0184b8ee0081
Create Date: 2018-08-14 16:09:49.045436

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5ab30371173e'
down_revision = '0184b8ee0081'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student_contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contact', sa.String(length=10), nullable=True),
    sa.Column('main_contact', sa.Boolean(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('username', table_name='sample')
    op.drop_table('sample')
    op.add_column('students', sa.Column('mobile', sa.String(length=10), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'mobile')
    op.create_table('sample',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('username', 'sample', ['username'], unique=True)
    op.drop_table('student_contacts')
    # ### end Alembic commands ###