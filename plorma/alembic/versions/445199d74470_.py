"""Move tags module into the user-menu

Revision ID: 445199d74470
Revises: 482f6310a62b
Create Date: 2015-12-01 23:55:21.981144

"""

# revision identifiers, used by Alembic.
revision = '445199d74470'
down_revision = '482f6310a62b'

from alembic import op
import sqlalchemy as sa


INSERTS = """
UPDATE modules set display='user-menu' where name = 'tags';
"""
DELETES = """
UPDATE modules set display='admin-menu' where name = 'tags';
"""


def iter_statements(stmts):
    for st in [x for x in stmts.split('\n') if x]:
        op.execute(st)


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###
    iter_statements(INSERTS)


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###
    iter_statements(DELETES)
