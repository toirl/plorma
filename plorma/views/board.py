from pyramid.view import view_config
from ringo.lib.helpers import get_action_routename
from ringo.views.request import (
            handle_history, 
            get_item_from_request, 
            get_return_value
)
from plorma.model.sprint import Sprint

@view_config(route_name=get_action_routename(Sprint, 'board'),
             renderer='/sprint/board.mako',
             permission='update')
def board(request):
    handle_history(request)
    rvalues = get_return_value(request)
    return rvalues
