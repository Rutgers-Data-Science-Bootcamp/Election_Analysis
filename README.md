# Election-Analysis
Using Python scripts to analysis Colorado election outcome for three candidates from three counties.  

## Project Overview:
A Colorado Board of Election employee has gave me the following tasks to complete the election audit of a recent local congressional election.
1. Calculate the total number of votes cast.
2. Voter turnout for each county and their percentages out of the total count.
3. Find the county has the highest turnout.
4. Get a complete list of candidates who received votes.
5. Calculate the total number of votes each candidate received.
6. Calculate the percentage of votes each candidate won.
7. Determine the winner of the election based on popular vote. 

## Resources: 
- Data Source: election_results.csv
- Software: Python 3.7.10, Visual Studio Code, 

## Election-Audit Results:
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- There were three counties and their turnouts and percentages are:
    - Jefferson: 10.51% (38,855)
    - Denver: 82.78% (306,055)
    - Arapahoe: 6.71% (24,801)
- The county which had the largest number of votes was Denver 
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- the Candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 of votes.
    - Raymon Anthony Doane 3.1% of the vote and 11,606 of votes.
- The winner of the election was:
    - Candidate Diana DeGette, who received 73.8% of the vote and 272,892 number of votes. 

## Election-Audit Summary:
Using this Python script to analysis same type of Election resultsis would be quite straight forward. It will be very useful to analysis same type of data again and again with just one click to run the analysis with some modifications based on the datasets provided. The example for the modifications would be, e.g. 1) based on the election_result_csv file location, this code should be modified: file_to_load = os.path.join("..","Resources", "election_results.csv"); 2) if the election_result_csv file has more that 3 columns so that column for the candidate name and column for the county are different than this , the indexes of the row should be corrected: candidate_name = row[2] and county_name =row[1]; 

