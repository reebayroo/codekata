import re
import os.path
class Kata04:

	def find_smallest_spread(self, weatherEntries):
		def spread(item):
			return item.max - item.min
		entriesBySpread = sorted(weatherEntries, key=spread)
		return entriesBySpread[0].id
	def find_smallest_spread_in_file(self, file_name):
		result = []
		assert os.path.isfile(file_name), "Invalid file %s " % file_name
		f = open(file_name, "r")
		lines = f.readlines()
		for l in lines[2:]:
			print "the line"
			print l
			entry = WeatherEntry.from_weather_file_line(l)
			if entry:
				result.append(entry)

		f.close()
		return self.find_smallest_spread(result)

class WeatherEntry:
	def __init__(self, id, min, max):
		self.min = min
		self.max = max
		self.id = id
	def __unicode__(self):
		return "id %s min %s max %s" % (self.id, self.min, self.max)
	def __str__(self):
		return unicode(self)
	@staticmethod
	def from_weather_file_line(line):
		assert line, "Line is required. Got %s " % line
		def to_int(index):
			assert columns, "Columns should be a valid array"
			return int(re.sub(r"\D", "", columns[index]))
		columns = line.split()
		try:
			return WeatherEntry(id=to_int(0), min=to_int(2), max=to_int(1))
		except:
			return None
	def __eq__(self, other):
		return other.min == self.min and \
			other.max == self.max and \
			other.id == self.id

