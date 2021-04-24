# Python Challenge
Homework 3 Python Challenge

## Table of Contents ##
* [Part 1 - PyBank](https://github.com/adriana-icasiano/python-challenge#Part-1---PyBank)
* [Summary of Codes Used - PyBank](https://github.com/adriana-icasiano/python-challenge#Summary-of-Codes-Used---PyBank)
* [Screenshot of Terminal- PyBank](https://github.com/adriana-icasiano/python-challenge#Screenshot-of-Terminal---PyBank)
* [Part 2 - PyPoll](https://github.com/adriana-icasiano/python-challenge#Part-2---PyPoll)
* [Summary of Codes Used - PyPoll](https://github.com/adriana-icasiano/python-challenge#Summary-of-Codes-Used--PyPoll)
* [Screenshot of Terminal - PyPoll](https://github.com/adriana-icasiano/python-challenge#Screenshot-of-Terminal--PyPoll)

# Part 1 - PyBank #
Students are tasked with creating a Python script for analyzing the financial records of your company based on a set of financial data called [budget_data.csv](https://github.com/adriana-icasiano/python-challenge/blob/9b7a19e581d6dfd9c6897b94bce1d91c497227a7/PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. Students are asked to 

# Summary of Codes Used - PyBank #
* import os and csv libaries, using the path module, and join function to read csv file
* with open to read csv file
* for loops to iterate to the csv data
* dictionary to store month, P&L and P&L change data
* len() 
* variables to track various financial values of interest
* with open to write text file
* text_file.write() to write into csv file
* print() to print on terminal

# Screenshot of Terminal - PyBank #
![](https://github.com/adriana-icasiano/python-challenge/blob/131ba25dcb4c58bce8229fb7524a0513170b9b45/PyBank/Images/solved_terminal_pybank.PNG)


# Part 2 - PyPoll #

Students are tasked with helping a small, rural town modernize its vote counting process. Students are given a set of poll data called [election_data.csv](https://github.com/adriana-icasiano/python-challenge/blob/de3d65b0651d3da6da167636094f7d599bc84982/PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Students are tasked to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* In addition, the final script should both print the analysis to the terminal and export a text file with the results.

# Summary of Codes Used - PyPoll #
* import os and csv libaries, using the path module, and join function to read csv file
* with open to read csv file
* for loops to iterate to the csv data
* variables to track total votes, winner, candidate votes
* with open to write text file
* text_file.write() to write into csv file
* print() to print on terminal

# Screenshot of Terminal - PyPoll #
![](https://github.com/adriana-icasiano/python-challenge/blob/de3d65b0651d3da6da167636094f7d599bc84982/PyPoll/Images/solution_terminal_pypoll.PNG)
