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
    #print(f"CSV Header: {csv_header}")

    month_list = []
    pl_list = []
    tot_pl = 0
    pl_prev = 0
    pl_chng_list = []
    counter = 0
    tot_chng = 0
    
    #Read each row of data after the header
    for row in csvreader:
        month_list.append(row[0])
        pl_list.append(int(row[1]))
        tot_pl = tot_pl + int(row[1])
        if counter >= 1:
            pl_chng = int(row[1]) - int(pl_prev)
            pl_chng_list.append(pl_chng)
            pl_prev = int(row[1])
            counter = counter +1
        else: 
            pl_chng = int(row[1]) - int(row[1])
            pl_chng_list.append(pl_chng)
            pl_prev = int(row[1])
            counter = counter +1
            
    for row in pl_chng_list:
        tot_chng = int(row [1]) + int(tot_chng)


#to determine total month
tot_months =(len(month_list))
tot_avg_chng = tot_chng/ len(pl_chng_list)
print(f"Financial Analysis")
print("--------------------------")
print(f"Total Month: {tot_months}")
print(f"Total: $ {tot_pl}")
print(pl_list)
print(month_list)
print(pl_chng_list)
print(len(pl_chng_list))
print(tot_chng)
print(tot_avg_chng)
