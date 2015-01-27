Feature: Weather Selector 
	Scenario: Find the smallest spread
		Given The Weather Entry: id=1, min=10, max=20
		and another Weather Entry: id=second, min=15, max=20
		when we compare entries
		then the entries with the smallest spread will be: id=second, min=15, max=20
