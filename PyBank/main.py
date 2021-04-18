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

    #declare variable for month list, pl list, total pl, previous pl, counter for avg, and total pl change
    month_list = []
    pl_list = []
    pl_chng_list = []
    pl_chng_m_list = []
    tot_pl = 0
    pl_prev = 0
    counter = 0
    tot_chng = 0
    great_inc = 0
    great_dec = 0
    great_inc_m = 0
    great_dec_m = 0

    #Read each row of data after the header
    for row in csvreader:
        
        #to add to month list and pl list
        month_list.append(row[0])
        pl_list.append(int(row[1]))
        
        # to accumulate total pl
        tot_pl = tot_pl + int(row[1])
    
        # to only calculate the change for row 2 onwards
        if counter >= 1:
            pl_chng = int(row[1]) - int(pl_prev)
            tot_chng = int(pl_chng) + int(tot_chng)
            pl_chng_list.append(pl_chng)
            pl_chng_m_list.append(row[0])
            pl_prev = int(row[1])
            counter = counter +1
        else: 
            pl_chng = int(row[1]) - int(row[1])
            tot_chng = int(pl_chng) + int(tot_chng)
            pl_chng_list.append(pl_chng)
            pl_chng_m_list.append(row[0])
            pl_prev = int(row[1])
            counter = counter +1

#comb_pl_list = zip(pl_chng_m_list, pl_chng_list)

    for change in pl_chng_list:
        if change > 1 and change > great_inc:
            great_inc = change
            
        elif change <1 and change < great_dec:
            great_dec = change
        
print(great_dec)
print(great_inc)

#print(pl_chng_list)
#print(pl_prev) 
#print(tot_chng)         


#to determine total month
tot_months =(len(month_list))

#to determine the total average change
tot_avg_chng = round(tot_chng/ (tot_months-1),2)

#to print the analysis
print(f"Financial Analysis")
print("--------------------------")
print(f"Total Month: {tot_months}")
print(f"Total: $ {tot_pl}")
print(f"Average Change: $ {tot_avg_chng}")

#print(pl_list)
#print(month_list)
#print(tot_chng)
#print(tot_avg_chng)
