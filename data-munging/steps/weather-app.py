
from weather import *

from behave import register_type, given
import parse

@parse.with_pattern(r"\d+(\.\d+)?")
def parse_number(text):
	return float(text)
# -- REGISTER TYPE-CONVERTER: With behave
register_type(Number=parse_number)
@given(u'data/weather.dat')
def step_impl(context):
    context.file_name='data/weather.dat'

@when(u'the WeatherApp parses it')
def step_impl(context):
    app = WeatherApp.init(context.file_name)
    context.actual = app.find_entry_with_smallest_spread()
    assert context.actual

@then(u'there will be a selected weather entry with: id={ident}, min={min:Number}, max={max:Number}')
def step_impl(context, ident, min, max):
    expected = WeatherEntry(id=ident, min=min, max=max)
    assert context.actual == expected, "Expected %s got %s " % (context.actual, expected)
