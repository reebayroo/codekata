from weather import *

from behave import register_type, given
import parse

@parse.with_pattern(r"\d+(\.\d+)?")
def parse_number(text):
	return float(text)
# -- REGISTER TYPE-CONVERTER: With behave
register_type(Number=parse_number)

@given(u'The Weather Entry: id=1, min=10, max=20')
def step_impl(context):
	context.entries = [ WeatherEntry(id=1, min=10, max=20) ]

@given(u'another Weather Entry: id=second, min=15, max=20')
def step_impl(context):
	context.entries.append( WeatherEntry(id="second", min=15, max=20) )

@when(u'we compare entries')
def step_impl(context):
	context.selected = WeatherSelector.find_smallest_spread(context.entries)
@then(u'the entries with the smallest spread will be: id=second, min=15, max=20')
def step_impl(context):
	assert context.selected == "second"
