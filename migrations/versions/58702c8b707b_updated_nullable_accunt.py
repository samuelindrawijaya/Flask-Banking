"""Updated nullable accunt

Revision ID: 58702c8b707b
Revises: 7cacd153a0c2
Create Date: 2024-10-30 21:03:48.203453

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '58702c8b707b'
down_revision = '7cacd153a0c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions', schema=None) as batch_op:
        batch_op.alter_column('from_account_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.alter_column('to_account_id',
               existing_type=mysql.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions', schema=None) as batch_op:
        batch_op.alter_column('to_account_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.alter_column('from_account_id',
               existing_type=mysql.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
