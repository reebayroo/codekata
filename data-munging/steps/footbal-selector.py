from footbal import *
@given(u'The Team: id={ident}, name={team}, gf={favor}, ga={against}')
def step_impl(context, ident, team, favor, against):
    context.entries = [TeamEntry(ident, team, favor, against)]

@given(u'another team: id={ident}, name={team}, gf={favor}, ga={against}')
def step_impl(context, ident, team, favor, against):
    context.entries.append(TeamEntry(ident, team, favor, against))

@when(u'we compare team entries')
def step_impl(context):
    context.actual = TeamSelector.find_smallest_goal_difference(context.entries) 

@then(u'the entries with the smallest goal difference will be: id={ident}, name={team}, gf={favor}, ga={against}')
def step_impl(context, ident, team, favor, against):
    assert context.actual, "nothing was found"
    context.expected = TeamEntry(ident, team, favor, against)
    assert context.actual == context.expected, "Expecting %s got %s instead" % (context.actual,context.expected)
@given(u'No Team')
def step_impl(context):
    context.entries = []

@given(u'No Team what so ever')
def step_impl(context):
    context.entries = None

@then(u'there will be no result')
def step_impl(context):
    assert context.actual == None
