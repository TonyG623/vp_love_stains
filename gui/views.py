from pyramid.response import Response
from pyramid.view import view_config
from scripts.teams import *
from scripts.history import *

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )


header = """
        <div class="navbar navbar-inverse">
          <div class="navbar-inner">
            <a class="brand" href="#">VP Love Stains</a>
            <ul class="nav">
              <li><a href="/">Home</a></li>
              <li><a href="http://fantasy.nfl.com/league/744960">NFL.com League</a></li>
              <li><a href="rules">Rules</a></li>
              <li><a href="teams">Current Rosters</a></li>
              <li><a href="history">History</a></li>
              <li><a href="board">2014 Draft Board</a></li>
              <li><a href="2013draft">2013 Draft Board</a></li>
            </ul>
          </div>
        </div>
        """




@view_config(route_name='index', renderer='templates/index.mako')
def index_view(request):


    return {'header':header}

@view_config(route_name='rules', renderer='templates/rules.mako')
def rules_view(request):

    return {'header':header}

@view_config(route_name='board', renderer='templates/board.mako')
def board_view(request):

    return {'header':header}

@view_config(route_name='2013draft', renderer='templates/2013draft.mako')
def previous_draft_view(request):

    return {'header':header}

@view_config(route_name='teams', renderer='templates/teams.mako')
def teams_view(request):
    team_links = create_team_table()

    return {'header':header,'team_links':team_links}

@view_config(route_name='history', renderer='templates/history.mako')
def history_view(request):
    history = create_history()

    return {'header':header,'history':history}


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_gui_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

