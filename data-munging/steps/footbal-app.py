
from footbal import *

@given(u'data/football.dat')
def step_impl(context):
    context.file_name='data/football.dat'

@when(u'the FootballApp parses it')
def step_impl(context):
    app = FootballApp.init(context.file_name)
    context.actual = app.display_team_with_least_difference()
    assert context.actual
    


@then(u'there final team will be: id={ident}, name={team}, gf={favor}, ga={against}')
def step_impl(context, ident, team, favor, against):
    expected = TeamEntry(ident, team, int(favor), int(against))
    assert context.actual == expected, "Expected %s got %s " % (context.actual, expected)

