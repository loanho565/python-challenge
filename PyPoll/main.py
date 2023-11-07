# Modules
import os
import csv
from pathlib import Path

total_vote = 0
candidate_list ={}


# Path to collect data from the Resources folder
PyPoll_csv = os.path.join('Resources', 'election_data.csv')
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Open the CSV
with open(PyPoll_csv, encoding ="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    print (csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Loop through all the row in the file
    for row in csvreader:
        # Calculate the total number of votes cast
        total_vote += 1

        # Count candidates
        if row[2] not in candidate_list:
            candidate_list[row[2]] = 1
        else:
            candidate_list[row[2]] += 1
    
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(total_vote))
print("----------------------------")


# Set variable for output file
output_file = os.path.join("Analysis","PyPoll_Summary.txt")

#  Open the output file
with open(output_file, "w", newline='') as file:
    writer = csv.writer(file)
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write("Total Votes: " + str(total_vote))
    file.write("\n")
    file.write("----------------------------\n")
    # Code from Tiffany Cheung to find a complete list of candidates, total number of votes won, and percentage of votes
    pecentage_vote = 0
    max_value = 0
    for name, count in candidate_list.items():
        if count > max_value:
            winner = name
            max_value = count
        print(f'{name}: {round(count/total_vote*100,3)}% ({count})')
        file.write(f'{name}: {round(count/total_vote*100,3)}% ({count})\n')
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")
    
    # Export a text file 
    
    file.write("----------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("----------------------------\n")
