import pygal                                                       # First import pygal
import datetime
from pygal.style import BlueStyle
from pyramid.view import view_config
from ringo.views.request import handle_history, get_item_from_request
from ringo.views.base import create, update
from ringo.lib.helpers import get_action_routename
from ringo.model.base import get_item_list

from plorma.model.sprint import Sprint
from plorma.model.sprint import Estimatelog


def get_estimate_history(sprint):
    logs = []
    for day in range(0, sprint.get_length()+1):
        date = sprint.start + datetime.timedelta(days=day)
        for log in sprint.estimatelog:
            if log.date == date:
                logs.append(log.estimate)
                continue
            logs.append(None)
    return logs

def get_x_labels(sprint):
    labels = []
    for days in range(0, sprint.get_length()+1):
        labels.append(sprint.start + datetime.timedelta(days=days))
    return labels


@view_config(route_name='renderburndown')
def burndown_view(request):
    """Returns a SVG grafic representing the burndown chart of the sprint"""
    _ = request.translate
    sprint = get_item_from_request(request)
    response = request.response
    request.response.content_type ='image/svg+xml'
    #response.content_disposition = 'attachment; filename="%s"' % item.name
    chart = pygal.Line(height=200, style=BlueStyle, 
                       x_label_rotation=20,
                       show_legend=False)
    chart.x_labels = map(str, get_x_labels(sprint))
    get_x_labels(sprint)
    history = get_estimate_history(sprint)
    chart.add(_('Progress'), history)

    ideal = map(lambda x: None, range(0, len(history)))
    ideal[-1] = 0
    ideal[0]  = history[0]
    chart.add(_('Ideal'), ideal)
    response.body = chart.render()
    return response


def create_callback(request, sprint):
    return update_callback(request, sprint)


def update_callback(request, sprint):
    for log in sprint.estimatelog:
        if log.date == datetime.date.today():
            log.estimate = sprint.estimate
            return sprint
    nlog = Estimatelog()
    nlog.estimate = sprint.estimate
    nlog.date = datetime.date.today()
    sprint.estimatelog.append(nlog)

@view_config(route_name=get_action_routename(Sprint, 'create'),
             renderer='/default/create.mako',
             permission='create')
def create_(request):
    return create(request, create_callback)

@view_config(route_name=get_action_routename(Sprint, 'update'),
             renderer='/default/update.mako',
             permission='update')
def update_(request):
    return update(request, update_callback)
