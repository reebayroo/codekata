import re
import os.path
class WeatherSelector:
	FILE_NAME='weather.dat'
	def find_smallest_spread(self):
		assert os.path.isfile(self.FILE_NAME), "File %s " % file_name
		def clear_none(n): 
			return n
		def create_item(l): 
			return WeatherEntry.from_weather_file_line(l)
		def get_list():
			f = open(self.FILE_NAME, "r")
			try:
				return filter(clear_none,
					map(create_item, f.readlines()))
			finally:
				f.close()
		return self._find_smallest_spread(get_list())

	def _find_smallest_spread(self, weatherEntries):
		assert weatherEntries
		def spread(item):
			return item.max - item.min
		entriesBySpread = sorted(weatherEntries, key=spread)
		return entriesBySpread[0].id
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

