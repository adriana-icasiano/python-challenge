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
    win_list = []
    name_list = []
    comb_win_list = []
    percent_list = []

    # Read each row of data after the header
    for row in csvreader:
        if row[2] == "Khan":
            khan_v = khan_v + 1
        if row[2] == "Correy":
            correy_v = correy_v +1
        if row[2] == "Li":
            li_v = li_v + 1
        if row[2] == "O'Tooley":
            otooley_v = otooley_v +1
        #to track vote count
        tot_v = tot_v + 1

# create list votes and name
win_list = [khan_v, correy_v, li_v, otooley_v]
name_list = ["Khan","Correy","Li","O'Tooley"]

#combined the votes and name list
comb_win_list = zip(name_list, win_list)

#looped through votes to determine winner
for row in comb_win_list:
    percent = round(row[1]/tot_v*100,3)
    percent_list.append(percent)    
    if int(row [1]) > win_v:
        win_name = row [0]
        win_v = row [1]

#dict = {"name":[name_list], "vote_count":[win_list], "percent":[percent_list]}

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
