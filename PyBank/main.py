# Modules
import os
import csv
from pathlib import Path

total_months =[]
total_profit = []
change_in_profit = []

# Path to collect data from the Resources folder
PyBank_csv = os.path.join('Resources', 'budget_data.csv')
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Open the CSV
with open(PyBank_csv, encoding ="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    print (csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Loop through all the row in the file
    for row in csvreader:
       # Add total months and total profit to the corresponding list
       total_months.append(row[0]) 
       total_profit.append(int(row[1]))
    for i in range(len(total_profit)-1):
        change = total_profit[i+1] - total_profit[i]
        change_in_profit.append(change)
    average_change = round((sum(change_in_profit) / len(change_in_profit)),2)
    Greatest_increase_in_profit_amount = max(change_in_profit)
    Greatest_decrease_in_profit_amount = min(change_in_profit)
    Greatest_increase_in_profit_date = total_months[change_in_profit.index(Greatest_increase_in_profit_amount) + 1]
    Greatest_decrease_in_profit_date = total_months[change_in_profit.index(Greatest_decrease_in_profit_amount) + 1]

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(len(total_months)))
print("Total: " + "$" + str(sum(total_profit)))
print("Average Change: " + "$" + str(average_change))
print(f"Greatest Increase in Profits: {Greatest_increase_in_profit_date} (${Greatest_increase_in_profit_amount})")
print(f"Greatest Decrease in Profits: {Greatest_decrease_in_profit_date} (${Greatest_decrease_in_profit_amount})")

# Set variable for output file
output_file = os.path.join("Analysis","PyBank_Summary.txt")

#  Open the output file
with open(output_file, "w", newline='') as file:
    writer = csv.writer(file)

    # Export a text file 
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write("Total Months: " + str(len(total_months)))
    file.write("\n")
    file.write("Total: " + "$" + str(sum(total_profit)))
    file.write("\n")
    file.write("Average Change: " + "$" + str(average_change))
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {Greatest_increase_in_profit_date} (${Greatest_increase_in_profit_amount})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {Greatest_decrease_in_profit_date} (${Greatest_decrease_in_profit_amount})")