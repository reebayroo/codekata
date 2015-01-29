Feature: Soccer Data Parser
	Scenario: Header Parsing
		Given a line in the soccer league table:  Team            P     W    L   D    F      A     Pts
		When the soccer parser parses the line
		Then there will be no TeamScoreEntry
	Scenario: Regular Line 
		Given a line in the soccer league table:  1. Arsenal         38    26   9   3    79  -  36    87
		When the soccer parser parses the line
		Then there will be TeamScoreEntry(1, Arsenal, 79, 36)
		
	Scenario: Regular Line :
		Given a line in the soccer league table: line
		When the soccer parser parses the line
		Then there will be TeamScoreEntry(1, Arsenal, 79, 36)
