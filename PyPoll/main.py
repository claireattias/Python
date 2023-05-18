# import libraries
import os
import csv

# import election_data.csv file with path
election_data_csv = os.path.join("/Users/AttiasC16/Desktop/Data_Classwork/Assignments/python-challenge/PyPoll/Resources/election_data.csv")

# define variable 
votes = []
candidates = []

# open and read csv file
with open(election_data_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

# skip header
    header = next(csv_reader)

    # assign variables to columns in csv
    for row in csv_reader:
        votes.append(int(row[0]))
        candidates.append(row[2])
    
    # count the total number of votes
    total_votes = (len(votes))
    print(total_votes)

    # find unique candidates
    unique_candidates = list(set(candidates))
    print(unique_candidates)

    # set to zero because couter 
    stockham_votes = 0
    degette_votes = 0
    doane_votes = 0

    # count number of votes for each candidate
    for candidate_name in candidates:
        if candidate_name == "Charles Casper Stockham":
            stockham_votes += 1
        elif candidate_name == "Diana DeGette":
            degette_votes += 1
        else:
            doane_votes += 1
        
    print(stockham_votes)
    print(degette_votes)
    print(doane_votes)

    # calculate the percentage of votes each candidate won
    stockham_percent = round(((stockham_votes / total_votes) * 100), 3)
    degette_percent = round(((degette_votes / total_votes) * 100), 3)
    doane_percent = round(((doane_votes / total_votes) * 100), 3)

    print(stockham_percent)
    print(degette_percent)
    print(doane_percent)
 
    # determine winner of the election based on popular vote
     # max is showing the max value out of the three 
    winner = max(stockham_votes, degette_votes, doane_votes)
    
    if winner == stockham_votes:
        winner_name = "Charles Casper Stockham"
    elif winner == degette_votes:
        winner_name = "Diana DeGette"
    else:
        winner_name = "Raymon Anthony Doane"

    print(winner_name)

# print analysis 
print("Election Results")
print("----------------------------")
print(f'Total Votes: {total_votes}')
print("-----------------------------")
print(f'Charles Casper Stockham: {stockham_percent}% ({stockham_votes})')
print(f'Diane Degette: {degette_percent}% ({degette_votes})')
print(f'Raymon Anythony Doane: {doane_percent}% ({doane_votes})')
print("-----------------------------")
print(f'Winner: {winner_name}')

# export text file 

# output path where new file will go
text_file = os.path.join("/Users/AttiasC16/Desktop/Data_Classwork/Assignments/python-challenge/PyPoll/analysis/analysis.txt")

with open(text_file,"w") as file:

    file.write("Election Results")
    file.write("\n") # use "\n" to move to a new line 
    file.write("--------------------------")
    file.write("\n")
    file.write(f'Total Votes: {total_votes}')
    file.write("\n")
    file.write("--------------------------")
    file.write("\n")
    file.write(f'Charles Casper Stockham: {stockham_percent}% ({stockham_votes})')
    file.write("\n")
    file.write(f'Diane Degette: {degette_percent}% ({degette_votes})')
    file.write("\n")
    file.write(f'Raymon Anythony Doane: {doane_percent}% ({doane_votes})')
    file.write("\n")
    file.write("--------------------------")
    file.write("\n")
    file.write(f'Winner: {winner_name}')


