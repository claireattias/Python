# import necessary libraries 
import os
import csv

# import budget_data.csv file using your path
budget_data_csv = os.path.join("/Users/AttiasC16/Desktop/Data_Classwork/Assignments/python-challenge/PyBank/Resources/budget_data.csv")

# define variables
total_months = []
total_profit = []
profit_change = []
profit_change_date = []

# open and read file
with open(budget_data_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # skip header 
    header = next(csv_reader)

    # read through all rows in csv file 
    for row in csv_reader:
    # print(row) would show you all rows in the csv file

    # calcualte total number of months and total amount of profit/losses
        total_months.append(row[0]) # specifying only the first column
        total_profit.append(int(row[1])) # specifying the second column (int because numerical values)

    print(total_months) # prints all values in the first column
    print(len(total_months)) # calculates the number of months in the first column
    print(total_profit) # print the values in the second column
    print(sum(total_profit)) # calculates the total amount of profits/losseslosses 

# calculate the changes in profit/losses 
for x in range(len(total_profit)-1):
    profit_change.append(total_profit[x+1]-total_profit[x])

profit_change_length = len(profit_change) # calculate the length 
profit_change_sum = sum(profit_change) # calculate the total value 

# calculate the average change in profts/losses
profit_change_avg = profit_change_sum / profit_change_length
print(round(profit_change_avg, 2)) # print average and round to 2 decimal places 

# calculate the min and max monthly profit change (max is month with most change, min is month with least change)
min_profit_change = min(profit_change)
max_profit_change = max(profit_change)

# print min and max monthly profit change
    # print(min_profit_change)
    # print(max_profit_change)

# determine which month correlates with the min and max profit change 

min_profit_change_month = profit_change.index(min(profit_change)) +1
max_profit_change_month = profit_change.index(max(profit_change)) +1

# print the months that correlate with min and max profit change 
    # print(f"{total_months[min_profit_change_month]}") 
    # print(f"{total_months[max_profit_change_month]}") 

# print financial analysis 

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${(round(profit_change_avg, 2))}")
print(f"Greatest Increase in Profits: {total_months[max_profit_change_month]} (${(str(max_profit_change))})")
print(f"Greatest Decrease in Profits: {total_months[min_profit_change_month]} (${(str(min_profit_change))})")  

# export text file 

# output path where new file will go
text_file = os.path.join("/Users/AttiasC16/Desktop/Data_Classwork/Assignments/python-challenge/PyBank/analysis/analysis.txt")

with open(text_file,"w") as file:

    file.write("Financial Analysis")
    file.write("\n") # use "\n" to move to a new line 
    file.write("--------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: ${(round(profit_change_avg, 2))}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_profit_change_month]} (${(str(max_profit_change))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[min_profit_change_month]} (${(str(min_profit_change))})")  



