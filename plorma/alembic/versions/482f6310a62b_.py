"""Added table to track user logins.

Revision ID: 482f6310a62b
Revises: 49d74299025
Create Date: 2015-12-01 22:04:27.207562

"""

# revision identifiers, used by Alembic.
revision = '482f6310a62b'
down_revision = '49d74299025'

from alembic import op
import sqlalchemy as sa


INSERTS = """"""
DELETES = """"""


def iter_statements(stmts):
    for st in [x for x in stmts.split('\n') if x]:
        op.execute(st)


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_logins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.Column('success', sa.Boolean(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###
    iter_statements(INSERTS)


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_logins')
    ### end Alembic commands ###
    iter_statements(DELETES)