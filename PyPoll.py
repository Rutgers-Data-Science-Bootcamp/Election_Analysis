#The  data we need to retrieve.
from email import header
import os
import csv

# Set path for file
file_to_load = 'Resources/election_results.csv'
election_data = open(file_to_load, 'r')
print(election_data)

election_data.close()


with open(file_to_load) as election_data:
    print(election_data)


file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:

    print(election_data)

# Create a filename variable to a direct or indirect path to the file.

file_to_save = os.path.join("analysis", "election_analysis.txt")
outfile =open(file_to_save, "w")

outfile.write("Hello World")

outfile.close()

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:

    #txt_file.write("Hello World")
      #txt_file.write("Aparahoe, ")
      #txt_file.write("Denver, ")
      #txt_file.write("Jefferson, ")
      #txt_file.write("El Paso")

#Write three counties to the file
     #txt_file.write("Aparahoe, Denver, Jefferson")
      txt_file.write("Counties in the Election\n------------------------\nAparahoe\nDenver\nJefferson")

import csv
import os

#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1 Initialize a total vote counter.
total_votes = 0

# Candidate options
candidate_options = []

# Declare the empty dictionary
candidate_votes ={}
#open the election results and read the file.
with open(file_to_load) as election_data:

#read the file object with the reader function

   file_reader = csv.reader(election_data)

   #Read the header now
   headers =next(file_reader)
   #print(headers)

   #print each row in the CSV file.
   for row in file_reader:
       #print(row)
       #Add to the total vote count.
       total_votes += 1
       # Print the candidate name from each row
       candidate_name = row[2]

       #if the candidate does not match any existing candidate...
       if candidate_name not in candidate_options:
       #Add the cadidate name to the candidate list.
          candidate_options.append(candidate_name)
       #begin tracking that candidates's vote count.
          candidate_votes[candidate_name]= 0
       #Add a vote to that candidate's count.
       candidate_votes[candidate_name] += 1

print(candidate_votes)

#3. Print the total votes.
#print(total_votes)








#csvpath = os.path.join("..", "Resources", "election_results.csv")
# 1. The total number of votes cast
# 2. Complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

