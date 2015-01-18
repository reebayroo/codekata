import unittest
from main import *

class Kata04Test(unittest.TestCase):
	def setUp(self):
		self.instance = Kata04()
	def test_find_smallest_spread(self):
		temps = [
			WeatherEntry(id=1, min=10, max=20),
			WeatherEntry(id=2, min=15, max=20)]
		self.assertEqual(2, self.instance.find_smallest_spread(temps));
	def test_find_smallest_spread_from_file(self):
		self.assertEqual(14, self.instance.find_smallest_spread_in_file('weather.dat'))

class  WeatherEntryTest(unittest.TestCase):
	def test_load_line(self):
		line = " 3  77    55    66          39.6       0.00         350  5.0 350   9  2.8  59 24 1016.8"
		actual = WeatherEntry.from_weather_file_line(line)
		expected = WeatherEntry(id=3, min=55, max=77)
		self.assertEqual(expected, actual, "%s != %s" % (expected, actual))

	def test_line_with_asterisk(self):
		line = " 26  97*   64    81          70.4       0.00 H       050  5.1 200  12  4.0 107 45 1014.9"

		actual = WeatherEntry.from_weather_file_line(line)
		expected = WeatherEntry(id=26, min=64, max=97)
		self.assertEqual(expected, actual, "%s != %s" % (expected, actual))
	def test_validate_empty_lines(self):
		self.assertRaises(AssertionError, WeatherEntry.from_weather_file_line, None)

	def test_invalid_line_will_return_none(self):
		line = " mo  82.9  60.5  71.7    16  58.8       0.00              6.9          5.3"

		actual = WeatherEntry.from_weather_file_line(line)
		self.assertIsNone(actual)

if (__name__== '__main__'):
	unittest.main();
