import sqlalchemy as sa
from ringo.model import Base
from ringo.model.base import BaseItem
from ringo.model.mixins import (
Owned
)

estimatelog_table = sa.Table(
    'estimatelog', Base.metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('sprint_id', sa.Integer, sa.ForeignKey('sprints.id')),
    sa.Column('date', sa.Date),
    sa.Column('estimate', sa.Integer)
)

class Estimatelog(Base):
    __tablename__ = 'estimatelog'


class Sprint(BaseItem, Owned, Base):
    __tablename__ = 'sprints'
    _modul_id = 1003
    id = sa.Column(sa.Integer, primary_key=True)
    start = sa.Column('start', sa.Date)
    end = sa.Column('end', sa.Date)
    strength = sa.Column('strength', sa.Integer)
    estimatelog = sa.orm.relationship("Estimatelog", cascade="all")

    @property
    def estimate(self):
        """Returns the sum of estimate of all tasks in the sprint"""
        sum = 0
        for task in self.tasks:
            if task.total_estimate is not None:
                sum += task.total_estimate
        return sum

    def get_length(self):
        """Returns the number of days of the sprint"""
        td = self.end - self.start
        return td.days

    def get_tasks(self, type=None):
        if type is None:
            return self.tasks
        else:
            tasks = []
            for task in self.tasks:
                if type == "open" and task.task_state_id in [1,2,7]:
                    tasks.append(task)
                elif type == "progress" and task.task_state_id in [3]:
                    tasks.append(task)
                elif type == "testable" and task.task_state_id in [4]:
                    tasks.append(task)
                elif type == "finished" and task.task_state_id in [5,6]:
                    tasks.append(task)
            return tasks
