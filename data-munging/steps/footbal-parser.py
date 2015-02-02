from footbal import *
@given(u'The footbal line: {pline}')
def step_impl(context, pline):
	context.parsed_line = pline

@when(u'the soccer parser parses the line')
def step_impl(context):
	context.parsed_content = TeamEntryParser.parse(context.parsed_line) 

@then(u'there will be no TeamScoreEntry')
def step_impl(context):
	    assert context.parsed_content is None


@then(u'There will be TeamScoreEntry({ident}, {team}, {favor}, {against})')
def step_impl(context, ident, team, favor, against):
	expected = TeamEntry(ident, team, int(favor), int(against))
	assert context.parsed_content == expected, "Expecting [%s] got [%s] instead" % (expected, context.parsed_content)
