import sqlalchemy as sa
from ringo.model import Base
from ringo.model.base import BaseItem
from ringo.model.statemachine import (
        Statemachine, State,
        null_handler as handler,
        null_condition as condition
)
from ringo.model.mixins import (
    Owned, StateMixin
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



def start_handler(sprint, transition):
    # When the sprint is started we will calculate the intial story
    # points of the sprint based on the selected tasks.
    size = 0
    for task in sprint.tasks:
        size += task.estimate
    sprint.size = size
    return sprint


def start_condition(sprint, transition):
    # To be able to start the sprint the following conditions must be
    # set:

    # 1. The strength of the sprint must be set.
    if sprint.strength == None:
        return False
    # 2. All selected tasks must be estimated.
    if len(sprint.tasks) == 0:
        return False
    for task in sprint.tasks:
        if task.estimate == None:
            return False
    return True


class SprintStatemachine(Statemachine):
    def setup(self):
        # Dummy translation method. Used to mark strings as
        # translateable for gettext.
        _ = lambda x : x
        s1 = State(self, 1, _("Planning"))
        s2 = State(self, 2, _("Running"))
        s3 = State(self, 3, _("Aborted"), disabled_actions={"productowner": ["update"]})
        s4 = State(self, 4, _("Finished"), disabled_actions={"productowner": ["update"]})
        s1.add_transition(s2, _("Start sprint"),
                          start_handler, start_condition)
        s2.add_transition(s3, _("Abort sprint"), handler, condition)
        s2.add_transition(s4, _("Finish sprint"), handler, condition)
        return s1


class SprintStateMixin(StateMixin):
     # Mixin inherited from the StateMixin to add the Foobar
     # state machine

     # Attach the statemachines to an internal dictionary
     _statemachines = {'sprint_state_id': SprintStatemachine}

     # Configue a field in the model which saves the current
     # state per state machine
     sprint_state_id = sa.Column(sa.Integer, default=1)

     # Optional. Create a property to access the statemachine
     # like an attribute. This gets usefull if you want to access
     # the state in overview lists.
     @property
     def sprint_state(self):
         state = self.get_statemachine('sprint_state_id')
         return state.get_state()


class Sprint(BaseItem, Owned, SprintStateMixin, Base):
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
        if self.size:
            return self.size - self.estimate
        return None

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
