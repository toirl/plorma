import sqlalchemy as sa
from ringo.model import Base
from ringo.model.base import BaseItem
from ringo.model.mixins import (
    Owned
)


class Task(BaseItem, Owned, Base):
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

    @property
    def weight(self):
        """Calculated value of the task based on the priority and
        severity of the task. This value is used to order the tasks in
        the overview. The priority of the task is weighted with a factor
        1.5.
        :returns: Integer value
        """
        return int(round((self.priority) * self.severity * 2.77))
