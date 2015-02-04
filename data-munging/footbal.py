class TeamEntryParser:
	@staticmethod
	def parse(line):
		pieces = line.split() if line else None
		return TeamEntry(pieces[0].replace(".",""),
				 pieces[1],
				 int(pieces[6]),
				 int(pieces[8])) if pieces and len(pieces) > 8 else None

# 1. Arsenal         38    26   9   3    79  -  36    87
class TeamEntry:
	def __init__(self, identifier, team, favor, against):
		self.identifier = identifier
		self.team = team
		self.favor = int(favor)
		self.against = int(against)
	def __str__(self):
		return unicode(self)
	def __unicode__(self):
		return "%s %s %s %s" % (
			self.identifier, 
			self.team, 
			self.favor, 
			self.against )
	def __eq__(self, other):
		return (self.identifier == other.identifier and 
			self.team == other.team and 
			self.favor == other.favor and 
			self.against == other.against)        
        
class TeamSelector:
    @staticmethod
    def find_smallest_goal_difference(list_of_teams):
        def smallest_diff(item1, item2):
            def diff(item):
                return abs(item.favor - item.against)
            return item1 if (diff(item1) < diff(item2)) else item2
        return reduce(smallest_diff, list_of_teams)

class FootballApp:
    def __init__(self, file_name):
        self.file_name = file_name

    @staticmethod
    def init(file_name):
        return FootballApp(file_name)

    def display_team_with_least_difference(self):
        def clear_none(n):
            return n
        def create_item(line):
            return TeamEntryParser.parse(line)
        def get_list():
            f = open(self.file_name, "r")
            try:
                return filter(clear_none, 
                        map(create_item, 
                            f.readlines()))
            finally:
                f.close()
        return TeamSelector.find_smallest_goal_difference(get_list())
