from main import *

from behave import register_type, given
import parse

@parse.with_pattern(r"\d+(\.\d+)?")
def parse_number(text):
	return float(text)

# -- REGISTER TYPE-CONVERTER: With behave
register_type(Number=parse_number)



@given(u'The line: "{line}"')
def step_impl(context,line):
	assert line
	context.parsing_line = line

@when(u'we parse the line')
def step_impl(context):
	assert context.parsing_line
	context.parsed_content = WeatherEntryParser.parse_line(context.parsing_line)

@then(u'there will be no parsed WeatherEntry')
def step_impl(context):
    	assert context.parsed_content is None


@given(u'an empty line')
def step_impl(context):
	context.parsing_line = "                    "

@then(u'there will be a parsed weatherEntry with max temp "{maxTemp:Number}" min temp "{minTemp:Number}" and id "{expectedId}"')
def step_impl(context, maxTemp, minTemp, expectedId):
	assert context.parsed_content is not None
	assert context.parsed_content.max == maxTemp
	assert context.parsed_content.min == minTemp
	assert context.parsed_content.id == expectedId, "expecting %s and got %s" % (context.parsed_content.id, expectedId)
