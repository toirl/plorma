import datetime
from pyramid.view import view_config
from ringo.views.base import create, update, delete
from ringo.lib.helpers import get_action_routename

from plorma.model.task import Task
from plorma.model.sprint import Estimatelog


def create_callback(request, task):
    return update_callback(request, task)

def delete_callback(request, task):
    return update_callback(request, task)

def _add_user_to_nosy(task, user):
    if user.id not in [u.id for u in task.nosy]:
        task.nosy.append(user)
    return task

def _add_estimatelog(task):
    for sprint in task.sprints:
        nlog = Estimatelog()
        nlog.estimate = sprint.estimate
        nlog.date = datetime.date.today()
        sprint.estimatelog.append(nlog)
    return task

def update_callback(request, task):
    #for ptask in task.get_parents():
    #    _add_estimatelog(ptask)
    #else:
    #    _add_estimatelog(task)
    _add_estimatelog(task)
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

@view_config(route_name=get_action_routename(Task, 'delete'),
             renderer='/default/confirm.mako',
             permission='delete')
def delete_(request):
    return delete(request, delete_callback)
