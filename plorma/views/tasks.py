import datetime
import logging
from pyramid.view import view_config
from envelopes import Envelope

from ringo.views.base import create, update, delete
from ringo.lib.helpers import get_action_routename
from ringo.model.user import User

from plorma.model.task import Task
from plorma.model.sprint import Estimatelog

log = logging.getLogger(__name__)


def create_callback(request, task):
    _add_estimatelog(task)
    recipients = []
    for user in request.db.query(User).all():
        email = user.profile[0].email
        if email:
            recipients.append("%s <%s>" % (user.profile[0], email))
    if recipients:
        settings = request.registry.settings
        try:
            _send_notification_mail(task, request.user, recipients, settings)
        except Exception as e:
            log.error("Can not send email: %s" % e)
    _add_user_to_nosy(task, request.user)
    return task

def _add_user_to_nosy(task, user):
    if user.id not in [u.id for u in task.nosy]:
        task.nosy.append(user)
    return task

def _send_notification_mail(task, sender, recipients, settings):
    sender = "%s <%s>" % (sender.profile[0], settings.get("mail.default_sender"))
    username = settings.get("mail.username") 
    password = settings.get("mail.password") 
    host = settings.get("mail.host") 

    # Build Mail
    if len(task.comments) > 0:
        comment = task.comments[-1].text
    else:
        comment = ""
    subject = "[tasks%s] %s" % (task.id, task.name)

    mail =  Envelope(from_addr=sender,
                     to_addr=recipients,
                     subject=subject,
                     text_body=comment)
    mail.send(host, login=username, password=password, tls=True)

def _add_estimatelog(task):
    for sprint in task.sprints:
        nlog = Estimatelog()
        nlog.estimate = sprint.estimate
        nlog.date = datetime.date.today()
        sprint.estimatelog.append(nlog)
    return task

def update_callback(request, task):
    _add_estimatelog(task)
    if request.params.get("comment"):
        msg = request.params.get("comment")
        recipients = []
        for user in task.nosy:
            email = user.profile[0].email
            if email and (user.id != request.user.id):
                recipients.append("%s <%s>" % (user.profile[0], email))
        if recipients:
            settings = request.registry.settings
            try:
                _send_notification_mail(task, request.user, recipients, settings)
            except Exception as e:
                log.error("Can not send email: %s" % e)
    _add_user_to_nosy(task, request.user)
    return task


@view_config(route_name=get_action_routename(Task, 'create'),
             renderer='/default/create.mako',
             permission='create')
def create_(request):
    return create(request, create_callback)

@view_config(route_name=get_action_routename(Task, 'update'),
             renderer='/default/update.mako',
             permission='update')
def update_(request):
    return update(request, update_callback)
