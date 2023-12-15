import os
import csv

#set path
csvpath = os.path.join("Resources", "election_data.csv")

#read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader) #skip the header line
    
    #intialize the varaibles
    voter_count=0
    candidates_dict = {}

    for row in csvreader: #go through each row of the csv file
        voter_count = voter_count + 1 #increment the vote count by 1, every row is one person/vote
        if row[2] in candidates_dict: #check to see if the candidate that voter voted for is already in the candidates dictionary
            #if the candidate is already in the dictionary, then increment the vote count 
            current_count = candidates_dict[row[2]] #set the current vote count to the current_count variable
            candidates_dict[row[2]] = current_count + 1 #increment the current_count by 1 and then set it back to the candidates[row[2]]
        else:
            #candidate is not included in the candidates dictionary yet
            candidates_dict[row[2]] = 1 #add the candidate to the dictionary and then set their vote count to 1, because at least one person voted for them to be in the list.

    #function to print the line separations
    def line_separation():
        text.write ("-------------------------\n")
        
#opening the analysis file and writing to it
with open ("analysis/pypoll_analysis.txt", 'w') as text:
    text.write("Election Results\n")
    line_separation()
    text.write(f"Total Votes: {voter_count}\n") #total vote counts
    line_separation() #calling function for the line separations
    #initializing the variables to figure out the max votes/winner
    max_votes = 0
    winner = ""
    #for every candiate in candidates dictionary
    for key in candidates_dict:
        percent_votes = round(((candidates_dict[key] / voter_count) * 100), 3) #calculate the percent votes and then round to 3 decimal points
        text.write(f"{key}: {percent_votes}% ({candidates_dict[key]})\n") #print the string for candidate/ percent votes/ and number of votes
        if max_votes < candidates_dict[key]: #figuring out the candidate with the most votes and then whoever has the max votes is the winner
            max_votes = candidates_dict[key]
            winner = key #key in this dictionary is the candidate's name
    line_separation() # call line separator
    text.write(f"Winner: {winner}\n") # print the winner
    line_separation()
text.close() # close the text file we write to 
csvfile.close() #close the csv file we read from 