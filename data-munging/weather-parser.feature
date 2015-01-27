Feature: Weather Parser 
	Scenario: Heather Line
		Given The line: "Dy MxT   MnT   AvT   HDDay  AvDP 1HrP TPcpn WxType PDir AvSp Dir MxS SkyC MxR MnR AvSLP"
		when we parse the line
		then there will be no parsed WeatherEntry
	Scenario: Empty Line
		Given an empty line
		when we parse the line
		then there will be no parsed WeatherEntry
	Scenario: First Line
		Given The line: " 1  88    59    74          53.8       0.00 F       280  9.6 270  17  1.6  93 23 1004.5"
		when we parse the line
		then there will be a parsed weatherEntry with max temp "88" min temp "59" and id "1"
	Scenario: Line with float values
		Given The line: " 12  88.5    73.3    81          68.7       0.00 RTH     250  8.1 270  21  7.9  94 51 1007.0 "
		when we parse the line
		then there will be a parsed weatherEntry with max temp "88.5" min temp "73.3" and id "12"
	Scenario: Average of the month line
		Given The line: " mo  82.9  60.5  71.7    16  58.8       0.00              6.9          5.3"
		when we parse the line
		then there will be a parsed weatherEntry with max temp "82.9" min temp "60.5" and id "mo"

