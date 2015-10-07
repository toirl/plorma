from pyramid.config import Configurator
from pyramid.i18n import TranslationStringFactory

from ringo.lib.sql.db import setup_db_session, setup_db_engine
from ringo.model import Base
from ringo.resources import get_resource_factory 
from ringo.config import setup_modules
from ringo.lib.i18n import translators
from ringo.lib.helpers import get_action_routename
from plorma.model import extensions
from plorma.model.sprint import Sprint

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = setup_db_engine(settings)
    setup_db_session(engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    # Include basic ringo configuration.
    config.include('ringo')
    config.include('plorma')
    for extension in extensions:
        config.include(extension)
    config.scan()
    return config.make_wsgi_app()

def includeme(config):
    # Now configure the application and optionally overwrite previously
    translators.append(TranslationStringFactory('plorma'))
    config.add_translation_dirs('plorma:locale/')
    config.add_static_view('plorma-static', path='plorma:static',
                           cache_max_age=3600)

    config.add_route('renderburndown',
                     'sprints/burndown/{id}',
                     factory=get_resource_factory(Sprint))
    config.add_route(get_action_routename(Sprint, 'board'),
                     'sprintboard/{id}',
                     factory=get_resource_factory(Sprint))
