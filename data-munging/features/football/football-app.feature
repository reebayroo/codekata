
Feature: Parsing and Evaluating the team with the smallest difference of for and against goals
	Scenario: The Real File
		Given data/football.dat 
		When the FootballApp parses it
        Then there final team will be: id=8, name=Aston_Villa, gf=46, ga=47
