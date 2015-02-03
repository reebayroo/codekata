import re
import os.path
class WeatherSelector:
    FILE_NAME='weather.dat'
    def find_smallest_spread_from_file(self):
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

class WeatherSelector:
    @staticmethod
    def find_smallest_spread(weatherEntries):
        assert weatherEntries
        def spread(item):
            assert isinstance(item, WeatherEntry), "got %s" % item
            return item.max - item.min
        entriesBySpread = sorted(weatherEntries, key=spread)
        return entriesBySpread[0].id

class WeatherEntry:
    def __init__(self, id, min, max):
        self.min = float(min)
        self.max = float(max)
        self.id = str(id)
    def __unicode__(self):
        return "id %s min %s max %s" % (self.id, self.min, self.max)
    def __str__(self):
        return unicode(self)
    def __eq__(self, other):
        return other.min == self.min and \
                other.max == self.max and \
                other.id == self.id
class WeatherEntryParser:
    @staticmethod
    def parse_line(line):
        assert line, "Line is required. Got %s " % line
        def to_float(index):
            assert columns, "Columns should be a valid array"
            return float(re.sub(r"[^\d.]+", "", columns[index]))
        columns = line.split()
        try:
            return WeatherEntry(id=columns[0], min=to_float(2), max=to_float(1))
        except:
            return None

