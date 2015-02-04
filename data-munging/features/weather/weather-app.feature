
Feature: Parsing and Evaluating a weather entry with the smallest temperature spread
	Scenario: The Real File
		Given data/weather.dat 
		When the WeatherApp parses it
        Then there will be a selected weather entry with: id=14, min=59, max=61
