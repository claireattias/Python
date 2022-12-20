# import libraries
import os
import csv

# import election_data.csv file with path
election_data_csv = os.path.join("/Users/AttiasC16/Desktop/python-challenge/PyPoll/Resources/election_data.csv")

# define variables 
total_votes = 0

# open and read csv file
with open(election_data_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

# skip header
    header = next(csv_reader)

   # Iterate through rows 
    for row in csv_reader:

        # counts number of rows 


        # get list of candidates
        

       
