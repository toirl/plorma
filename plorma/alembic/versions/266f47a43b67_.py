"""Add fields to the tags module

Revision ID: 266f47a43b67
Revises: 535fe14a8a5e
Create Date: 2014-01-02 18:58:26.066347

"""

# revision identifiers, used by Alembic.
revision = '266f47a43b67'
down_revision = '535fe14a8a5e'

from alembic import op
import sqlalchemy as sa


INSERTS = """"""
DELETES = """"""


def iter_statements(stmts):
    for st in [x for x in stmts.split('\n') if x]:
        op.execute(st)


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tags', sa.Column('description', sa.Text(), nullable=True))
    op.add_column('tags', sa.Column('name', sa.Text(), nullable=True))
    op.add_column('tags', sa.Column('type', sa.Integer(), nullable=True))
    ### end Alembic commands ###
    iter_statements(INSERTS)


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tags', 'type')
    op.drop_column('tags', 'name')
    op.drop_column('tags', 'description')
    ### end Alembic commands ###
    iter_statements(DELETES)
