"""empty message

Revision ID: 441dca328887
Revises: 1b5a9f7af28e
Create Date: 2023-12-05 10:36:32.487659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '441dca328887'
down_revision = '1b5a9f7af28e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('future_task',
    sa.Column('guid', sa.String(length=36), nullable=False),
    sa.Column('run_at_in_seconds', sa.Integer(), nullable=False),
    sa.Column('completed', sa.Boolean(), nullable=False),
    sa.Column('updated_at_in_seconds', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('guid')
    )
    with op.batch_alter_table('future_task', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_future_task_completed'), ['completed'], unique=False)
        batch_op.create_index(batch_op.f('ix_future_task_run_at_in_seconds'), ['run_at_in_seconds'], unique=False)

    op.create_table('task_instructions_for_end_user',
    sa.Column('task_guid', sa.String(length=36), nullable=False),
    sa.Column('instruction', sa.Text(), nullable=False),
    sa.Column('process_instance_id', sa.Integer(), nullable=False),
    sa.Column('has_been_retrieved', sa.Boolean(), nullable=False),
    sa.Column('timestamp', sa.DECIMAL(precision=17, scale=6), nullable=False),
    sa.ForeignKeyConstraint(['process_instance_id'], ['process_instance.id'], ),
    sa.PrimaryKeyConstraint('task_guid')
    )
    with op.batch_alter_table('task_instructions_for_end_user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_task_instructions_for_end_user_has_been_retrieved'), ['has_been_retrieved'], unique=False)
        batch_op.create_index(batch_op.f('ix_task_instructions_for_end_user_process_instance_id'), ['process_instance_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_task_instructions_for_end_user_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task_instructions_for_end_user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_task_instructions_for_end_user_timestamp'))
        batch_op.drop_index(batch_op.f('ix_task_instructions_for_end_user_process_instance_id'))
        batch_op.drop_index(batch_op.f('ix_task_instructions_for_end_user_has_been_retrieved'))

    op.drop_table('task_instructions_for_end_user')
    with op.batch_alter_table('future_task', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_future_task_run_at_in_seconds'))
        batch_op.drop_index(batch_op.f('ix_future_task_completed'))

    op.drop_table('future_task')
    # ### end Alembic commands ###