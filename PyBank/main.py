#import os module
import os

#import csv module
import csv
csvpath = os.path.join( 'Resources', 'budget_data.csv')


#read csv data
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Declare P_L listing
    PL_List = []
    # Read each row of data after the header
    for row in csvreader:
        PL_List.append(row)
        print(range(len(PL_List)))
        