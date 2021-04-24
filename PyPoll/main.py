#import os module
import os

#import csv reading module
import csv

csvpath = os.path.join('Resources',"election_data.csv")

#Improved reading using csv module
with open(csvpath) as csvfile:

     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #declare variable to track votes and list
    tot_v = 0
    khan_v = 0
    correy_v = 0
    li_v = 0
    otooley_v = 0
    win_v = 0
    win_name = 0
      
    # Read each row of data after the header
    for row in csvreader:
        if row[2] == "Khan":
            khan_v = khan_v +1
        if khan_v > win_v:
            win_v = khan_v
            win_name = row [2]
        if row[2] == "Correy":
            correy_v = correy_v +1
        if correy_v > win_v:
            win_v = khan_v
            win_name = row [2]
        if row[2] == "Li":
            li_v = li_v + 1
        if li_v > win_v:
            win_v = li_v
            win_name = row [2]
        if row[2] == "O'Tooley":
            otooley_v = otooley_v +1
        if otooley_v > win_v:
            win_v = otooley_v
            win_name = row [2]
        
        #to track vote count
        tot_v = tot_v + 1
       
# Calculate percentages      
li_percent = round((li_v/ tot_v*100),3)
otooley_percent = round((otooley_v/tot_v*100),3)
khan_percent = round((khan_v/tot_v*100),3)
correy_percent = round((correy_v/tot_v*100),3)

#to print output to text file
output_file = os.path.join("Analysis", "pl_analysis.txt")

with open(output_file,"w") as text_file:
    text_file.write("```text \n")
    text_file.write("Election Results \n")
    text_file.write("---------------------- \n")
    text_file.write("Total Votes: "+ str(tot_v)+"\n")
    text_file.write("---------------------- \n")
    text_file.write("Khan: "+str(khan_percent)+ "% ("+str(khan_v)+")\n")
    text_file.write("Correy: "+str(correy_percent)+ "% ("+str(correy_v)+")\n")
    text_file.write("Li: "+str(li_percent)+ "% ("+str(li_v)+")\n")
    text_file.write("O'Tooley: "+str(otooley_percent)+ "% ("+str(otooley_v)+")\n")
    text_file.write("---------------------- \n")
    text_file.write("Winner: "+str(win_name)+ "\n")
    text_file.write("---------------------- \n")
    text_file.write("```\n")

#print to terminal
print(f"```text")
print(f"Election Results")
print(f"------------------------")
print(f"Total Votes: {tot_v}")
print(f"------------------------")
print(f"Khan: {khan_percent}% ({khan_v})")
print(f"Correy: {correy_percent}% ({correy_v})")
print(f"Li: {li_percent}% ({li_v})")
print(f"O'Tooley: {otooley_percent}% ({otooley_v})")
print(f"------------------------")
print(f"Winner: {win_name}")
print(f"------------------------")
print(f"```")
