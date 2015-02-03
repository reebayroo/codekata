Feature: Team Selector 
	Scenario: Find the smallest goal difference
		Given The Team: id=1, name=arsenal, gf=10, ga=5
		And another team: id=2, name=Chelsea, gf=0, ga=4
		When we compare team entries
		Then the entries with the smallest goal difference will be: id=2, name=Chelsea, gf=0, ga=4

	Scenario: Find the smallest goal difference with absolute difference
		Given The Team: id=1, name=arsenal, gf=0, ga=5
		And another team: id=2, name=Chelsea, gf=0, ga=-3
		When we compare team entries
		Then the entries with the smallest goal difference will be: id=2, name=Chelsea, gf=0, ga=-3

	Scenario: Empty array to find the smallest goal difference
		Given No Team
		When we compare team entries
		Then there will be no result


	Scenario: None being passed to find the smallest goal difference
        Given No Team what so ever
		When we compare team entries
		Then there will be no result
