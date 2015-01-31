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
		self.favor = favor
		self.against = against
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
