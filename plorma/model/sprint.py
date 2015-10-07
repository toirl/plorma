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
    """Sum of availablity points of all developers of the sprint team"""
    title = sa.Column('title', sa.String)
    """Short name of the sprint"""
    description = sa.Column('description', sa.String)
    """Longer description of the sprint. e.g name goals of the sprint."""
    size = sa.Column('size', sa.Integer)
    """Initial sum of the story points of all tasks in the sprint"""
    estimatelog = sa.orm.relationship("Estimatelog", cascade="all")

    @property
    def estimate(self):
        """Returns the sum of estimate of all tasks in the sprint"""
        sum = 0
        for task in self.tasks:
            if task.estimate is not None:
                sum += task.estimate
        return sum

    @property
    def velocity(self):
        return self.size - self.estimate

    def get_length(self):
        """Returns the number of days of the sprint"""
        td = self.end - self.start
        return td.days

    def get_tasks(self, type=None):
        tasks = self.tasks
        if type is None:
            return tasks
        else:
            ttasks = []
            for task in tasks:
                if type == "open" and task.task_state_id in [1,2,7]:
                    ttasks.append(task)
                elif type == "progress" and task.task_state_id in [3]:
                    ttasks.append(task)
                elif type == "testable" and task.task_state_id in [4]:
                    ttasks.append(task)
                elif type == "finished" and task.task_state_id in [5,6]:
                    ttasks.append(task)
            return ttasks
