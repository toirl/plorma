import sqlalchemy as sa
from ringo.model import Base
from ringo.model.base import BaseItem
from ringo.model.mixins import (
Owned
)

class Sprint(BaseItem, Owned, Base):
    __tablename__ = 'sprints'
    _modul_id = 1003
    id = sa.Column(sa.Integer, primary_key=True)
    start = sa.Column('start', sa.Date)
    end = sa.Column('end', sa.Date)
    strength = sa.Column('strength', sa.Integer)
