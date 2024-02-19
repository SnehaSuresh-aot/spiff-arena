"""empty message

Revision ID: 60c13a48d675
Revises: 29b261f5edf4
Create Date: 2024-02-01 08:43:01.666683

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '60c13a48d675'
down_revision = '29b261f5edf4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # with op.batch_alter_table('kkv_data_store', schema=None) as batch_op:
    #     batch_op.drop_index('ix_kkv_data_store_secondary_key')
    #     batch_op.drop_index('ix_kkv_data_store_top_level_key')

    op.drop_table('kkv_data_store')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kkv_data_store',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('top_level_key', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('secondary_key', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('value', mysql.JSON(), nullable=False),
    sa.Column('updated_at_in_seconds', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at_in_seconds', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('kkv_data_store', schema=None) as batch_op:
        batch_op.create_index('ix_kkv_data_store_top_level_key', ['top_level_key'], unique=False)
        batch_op.create_index('ix_kkv_data_store_secondary_key', ['secondary_key'], unique=False)

    # ### end Alembic commands ###