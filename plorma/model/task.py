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
from ringo_comment.model import Commented
from ringo_tag.model import Tagged

# NM-Table to assign users for the nosy list of the task
nm_task_users = sa.Table(
    'nm_task_users', Base.metadata,
    sa.Column('task_id', sa.Integer, sa.ForeignKey('tasks.id')),
    sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'))
)

# NM-Table to assign tasks to the sprints
nm_task_sprints = sa.Table(
    'nm_task_sprints', Base.metadata,
    sa.Column('task_id', sa.Integer, sa.ForeignKey('tasks.id')),
    sa.Column('sprint_id', sa.Integer, sa.ForeignKey('sprints.id'))
)

def close_handler(task, transition):
    # When the task is finally closed than set remaining estimate to 0
    task.estimate = 0
    return task

def reopen_handler(task, transition):
    # The QA fails. There will be some work to be done. Enforce the
    # developer to set a new estimate by setting the current estimation
    # to unknown.
    task.estimate = None
    return task

class TaskStatemachine(Statemachine):
    def setup(self):
        # Dummy translation method. Used to mark strings as
        # translateable for gettext.
        _ = lambda x : x
        s1 = State(self, 1, _("New"))
        s2 = State(self, 2, _("Open"))
        s3 = State(self, 3, _("Assigned"))
        s4 = State(self, 4, _("Resolved"))
        s5 = State(self, 5, _("Verified"))
        s6 = State(self, 6, _("Closed"))
        s7 = State(self, 2, _("Reopen"))
        s1.add_transition(s2, _("Verify task"), handler, condition)
        s1.add_transition(s4, _("Resolve task"), handler, condition)
        s2.add_transition(s3, _("Assign task"), handler, condition)
        s2.add_transition(s4, _("Resolve task"), handler, condition)
        s7.add_transition(s4, _("Resolve task"), handler, condition)
        s3.add_transition(s4, _("Resolve task"), handler, condition)
        s4.add_transition(s5, _("Verify solution"), handler, condition)
        s4.add_transition(s7, _("Reopen task"), reopen_handler, condition)
        s5.add_transition(s7, _("Reopen task"), reopen_handler, condition)
        s5.add_transition(s6, _("Close task"), close_handler, condition)
        s6.add_transition(s7, _("Reopen task"), reopen_handler, condition)
        return s1


class TaskStateMixin(StateMixin):
     # Mixin inherited from the StateMixin to add the Foobar
     # state machine

     # Attach the statemachines to an internal dictionary
     _statemachines = {'task_state_id': TaskStatemachine}

     # Configue a field in the model which saves the current
     # state per state machine
     task_state_id = sa.Column(sa.Integer, default=1)

     # Optional. Create a property to access the statemachine
     # like an attribute. This gets usefull if you want to access
     # the state in overview lists.
     @property
     def task_state(self):
         state = self.get_statemachine('task_state_id')
         return state.get_state()


class Task(BaseItem, Tagged, Commented, TaskStateMixin, Owned, Base):
    """A task is a general container for all kind of tasks, defects,
    feature requests or any other issue in your product.
    """
    __tablename__ = 'tasks'
    _modul_id = 1000
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column('name', sa.Text, nullable=False, server_default="")
    """Name or title of the tasks. This should summarize in a few words
    what this ticket is about."""
    description = sa.Column('description', sa.Text,
                            nullable=False, server_default="")
    """Longer detailed description of the task"""
    priority = sa.Column('priority', sa.Integer)
    """
    Priority should normally be set by the managers, maintainers. There
    are the following priorities (Taken from the bugzilla defintion):

     * immediate: Must be fixed immediately (means: "Drop any other
       work"). Reports must have an assignee set in the "Assigned to" field.
     * very high: Should be fixed as next task by maintainers and
       certainly before the next release. Reports should have an assignee
       set in the "Assigned to" field.
     * high: Not the next task, but should be fixed soon. Depending on
       teams & manpower this can take between one and six months.
     * normal: Medium priority; would be good to get fixed somewhere in
       the future. Contributed patches might speed fixing up.
     * low: This can be fixed, but we're not going to worry about it.
       Patches very welcome and required for progress.
     * very low: This can be fixed, but we're not going to worry about it.
       Patches very welcome and required for progress.
    """
    severity = sa.Column('severity', sa.Integer)
    """
    Severity describes the impact on the product and further development
    and/or testing:

     * Blocker: Blocks further development and/or testing work
     * Critical: Crashes, loss of data (internally, not your edit
       preview!) in a widely used and important component.
     * Major: Major loss of function in an important area.
     * Normal: Default/average
     * Minor: Minor loss of function, or other problem that does not
       affect many people or where an easy workaround is present.
     * Trivial: Cosmetic problem like misspelled words or misaligned
       text which does not really cause problems.
    """
    resolution = sa.Column('resolution', sa.Integer)
    """
    Resultion describes the solution someone has choosen to resolve a task:

     * Done: Task is done and is ready for QA.
     * Works for me: Can not reproduce the defect or issue. Everything
       works as expected.
     * Need more info: It is unclear what exactly to do here. More
       information is needed before the work can continue here.
     * Won't do: Task will not be resolved for any reason.
     * Duplicate: Task is duplicate of another task.
     * Invalid: Task is invalid and will not be done for any other
       reason the the formed named resolutions.
    """
    estimate = sa.Column('estimate', sa.Integer)
    """The estimate indicates how much work remains to be done until the
    task is completely resolved. The estimate is usally given as value
    with in a fibunacci sequence to regard larger inaccurany in complex
    tasks."""
    assignee_id = sa.Column('assignee_id',
                            sa.Integer, sa.ForeignKey("users.id"))
    """Id of the user this task is assigned to"""
    assignee = sa.orm.relationship("User",
                                   primaryjoin="User.id==Task.assignee_id")
    """Id of the user this task is assigned to """
    nosy = sa.orm.relationship("User", secondary="nm_task_users")
    """List of users who are involved in some way into this task. All
    users in the nosylist will be notified on updated in the task."""
    sprints = sa.orm.relationship("Sprint", secondary="nm_task_sprints",
                                  backref="tasks")
    """List of sprints where the task is planned to be worked on"""

    @property
    def weight(self):
        """Calculated weight of the task based on the priority and
        severity of the task. This value is used to priorize the tasks
        in the overview. The priority of the task is weighted with a
        factor 2.77.
        :returns: Integer value
        """
        return int(round((self.priority) * self.severity * 2.77))
