# python-challenge
Homework 3 Python Challenge
# Part 1 - PyBank #
Students are tasked with creating a Python script for analyzing the financial records of your company based on a set of financial data called [budget_data.csv](https://github.com/adriana-icasiano/python-challenge/blob/9b7a19e581d6dfd9c6897b94bce1d91c497227a7/PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. Students are asked to 

* Ccreate a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* In addition, the final script should both print the analysis to the terminal and export a text file with the results.

# Summary of Codes Used #
* import os and csv libaries, using the path module, and join function to read csv file
* with open to read csv file
* for loops to iterate to the csv data
* dictionary to store month, P&L and P&L change data
* len() 
* variables to track various financial values of interest
* with open to write text file
* text_file.write() to write into csv file
* print() to print on terminal

# Screenshot of Terminal#
(https://github.com/adriana-icasiano/python-challenge/blob/131ba25dcb4c58bce8229fb7524a0513170b9b45/PyBank/Images/solved_terminal_pybank.PNG)


# Part 2 - PyPoll #
