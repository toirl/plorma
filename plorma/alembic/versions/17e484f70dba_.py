"""Added size field of the sprint

Revision ID: 17e484f70dba
Revises: 101e3a4d237
Create Date: 2015-08-19 23:31:50.758047

"""

# revision identifiers, used by Alembic.
revision = '17e484f70dba'
down_revision = '101e3a4d237'

from alembic import op
import sqlalchemy as sa


INSERTS = """"""
DELETES = """"""


def iter_statements(stmts):
    for st in [x for x in stmts.split('\n') if x]:
        op.execute(st)


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sprints', sa.Column('size', sa.Integer(), nullable=True))
    ### end Alembic commands ###
    iter_statements(INSERTS)


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sprints', 'size')
    ### end Alembic commands ###
    iter_statements(DELETES)