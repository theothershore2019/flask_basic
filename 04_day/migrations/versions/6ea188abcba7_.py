"""empty message

Revision ID: 6ea188abcba7
Revises: 
Create Date: 2019-09-11 20:37:52.231635

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6ea188abcba7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('email', table_name='tbl_users')
    op.drop_index('name', table_name='tbl_users')
    op.drop_table('tbl_users')
    op.drop_index('name', table_name='tbl_roles')
    op.drop_table('tbl_roles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_roles',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('name', 'tbl_roles', ['name'], unique=True)
    op.create_table('tbl_users',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('password', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('role_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['tbl_roles.id'], name='tbl_users_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('name', 'tbl_users', ['name'], unique=True)
    op.create_index('email', 'tbl_users', ['email'], unique=True)
    # ### end Alembic commands ###
