"""Added basic fields to the task module

Revision ID: 1b2b8a6b6252
Revises: 39b671757752
Create Date: 2015-02-01 22:33:34.916964

"""

# revision identifiers, used by Alembic.
revision = '1b2b8a6b6252'
down_revision = '39b671757752'

from alembic import op
import sqlalchemy as sa


INSERTS = """"""
DELETES = """"""


def iter_statements(stmts):
    for st in [x for x in stmts.split('\n') if x]:
        op.execute(st)


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('description', sa.Text(), server_default='', nullable=False))
    op.add_column('tasks', sa.Column('name', sa.Text(), server_default='', nullable=False))
    op.add_column('tasks', sa.Column('priority', sa.Integer(), nullable=True))
    op.add_column('tasks', sa.Column('severity', sa.Integer(), nullable=True))
    ### end Alembic commands ###
    iter_statements(INSERTS)


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'severity')
    op.drop_column('tasks', 'priority')
    op.drop_column('tasks', 'name')
    op.drop_column('tasks', 'description')
    ### end Alembic commands ###
    iter_statements(DELETES)
