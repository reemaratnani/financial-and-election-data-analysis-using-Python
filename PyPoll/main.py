import csv
with open('election_data.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter =",")
    Vote_count = {}                # Initialize dictionary to add candidate name as key and the total vote counts of each candidate as values
    for row in csv_reader:
        i = row['Candidate']        
        if i in Vote_count:      # To sum the total votes of candidate and vote count set up to go up by 1 for candidate's name when it appears in row
            Vote_count[i] += 1  
        else:
            Vote_count[i] = 1    #Initialize vote count = 1 for 1st vote as name appear 1st time in row for each candidates(key)

Total_votes = sum(Vote_count.values())  # To get the total number of votes cast
print("Election Results")
print("------------------------")
print(f"Total Votes: {Total_votes}")
print("------------------------")
for key, value in Vote_count.items():   # Loop through dictionary to calculate percentage of vote each candidate won
    percentage = value*100.0/Total_votes
    print(f"{key}: {percentage:.3f}% ({value})")

winner = max(Vote_count, key = Vote_count.get) # Max function is used to find the Winner's name who achieved highest number of votes   
print("------------------------")
print(f"Winner: {winner}")                     # Set to get the key(winner's name) with the maximum value
print("------------------------")

with open('Election_Results.txt','w') as f:
    f.write("Election Results")
    f.write("\n")
    f.write("------------------------")
    f.write(f"Total Votes: {Total_votes}")
    f.write("\n")
    f.write("------------------------")
    f.write("\n")
    f.write(f"{key}: {percentage:.3f}% ({value})")
    f.write("\n")
    f.write("------------------------")
    f.write("\n")
    f.write(f"Winner: {winner}")
    f.write("\n")
    f.write("------------------------")