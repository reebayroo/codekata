import re
import os.path
class WeatherApp:
    def __init__(self, file_name):
        self.file_name = file_name
    @staticmethod
    def init(file_name):
        return WeatherApp(file_name)
    
    def find_entry_with_smallest_spread(self):
        assert os.path.isfile(self.file_name), "File %s " % self.file_name
        def clear_none(n): 
            return n
        def create_item(l): 
            return WeatherEntryParser.parse_line(l)
        def get_list():
            f = open(self.file_name, "r")
            try:
                return filter(clear_none,
                        map(create_item, f.readlines()))
            finally:
                f.close()
        return WeatherSelector.find_smallest_spread(get_list())

class WeatherSelector:
    @staticmethod
    def find_smallest_spread(weatherEntries):
        assert weatherEntries
        def spread(item1, item2):
            def diff(i):
                return i.max - i.min
            return item1 if (diff(item1) < diff(item2)) else item2
        return reduce(spread, weatherEntries)

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

