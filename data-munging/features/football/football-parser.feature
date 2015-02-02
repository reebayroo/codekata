Feature: Soccer Data Parser
	Scenario: Header Parsing
		Given The footbal line: Team            P     W    L   D    F      A     Pts
		When the soccer parser parses the line
		Then there will be no TeamScoreEntry
	Scenario: regular line 
		Given The footbal line: 1. arsenal         38    26   9   3    79  -  36    87
		When The soccer parser parses the line
		Then There will be TeamScoreEntry(1, arsenal, 79, 36)
   
	Scenario: Horizontal line
		Given The footbal line: ------------------------------------------------------
		When The soccer parser parses the line
		Then there will be no TeamScoreEntry
