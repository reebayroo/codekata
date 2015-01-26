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
