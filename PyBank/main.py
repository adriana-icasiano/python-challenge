#import os module
import os

#import csv module
import csv

csvpath = os.path.join('Resources',"budget_data.csv")

with open(csvpath) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    month_list = []
    #pl_list = []
    tot_pl = 0
    #Read each row of data after the header
    for row in csvreader:
        month_list.append(row[0])
        #pl_list.append(int(row[1]))
        tot_pl = tot_pl + int(row[1])

#to determine total month
tot_months =(len(month_list))  

