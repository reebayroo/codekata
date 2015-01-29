from soccer import *
from behave import given 
import parse
@given(u'a line in the soccer league table: "{soccer_line}"') 
def step_impl(context, soccer_line):
	context.parsing_line = soccer_line

@when(u'the soccer parser parses the line')
def step_impl(context):
	context.parsed_content = TeamScoreEntryParser.parse(context.line)

@then(u'there will be no TeamScoreEntry')
def step_impl(context):
	assert context.parsed_content == None

@then(u'there will be TeamScoreEntry(1, Arsenal, 79, 36)')
def step_impl(context):
	assert False
