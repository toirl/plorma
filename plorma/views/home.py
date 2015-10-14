from pyramid.view import view_config
from ringo.views.request import handle_history
from ringo.model.base import get_item_list

from plorma.model.sprint import Sprint


@view_config(route_name='home', renderer='/index.mako')
def index_view(request):
    handle_history(request)
    values = {}
    sprints = get_item_list(request, Sprint, request.user)
    values['sprints'] = [item for item in sprints.items if item.sprint_state_id == 2]
    return values
