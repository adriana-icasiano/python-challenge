#import os module
import os

#import csv module
import csv
csvpath = os.path.join( 'Resources', 'budget_data.csv')


#read csv data
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Declare P_L listing
    month_list = []
    pl_list = []
    # Read each row of data after the header
    for row in csvreader:
        month_list.append(row[0])
        pl_list.append(row[1])

    #to output a clean file
clean_file = zip(month_list, pl_list)
        #total_month = range(len(month_list))
    #print(total_month)
    #print(month_list)
    
    output_file = os.path.join("web_final_AI_1.csv")

with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Title", "Price", "Subscriber Count", "Number of Reviews", "Percent", "Course Length"])

    writer.writerows(cleaned_file)  