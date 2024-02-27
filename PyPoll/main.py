import csv
import os


#open csv 
election_csv = os.path.join( "Resources", "election_data.csv")

#reading csv file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    votes= list(csvreader)
    total_votes= len(votes)-1
print("Election Results")
print("-------------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------------")

candidates = {}
for row in votes[1:]:
    if row[2] not in candidates:
        candidates[row[2]] = 1
    else:
        candidates[row[2]] += 1

for candidate, vote_count in candidates.items():
    percentage = (vote_count / total_votes) * 100
    print(f'{candidate}: {percentage:.3f}% ({vote_count})')

winner = max(candidates, key=candidates.get)
print("-------------------------------")
print(f'Winner: {winner}')




analysis = ['Election Results',
'-------------------------------',
'Total Votes: 369711',
'-------------------------------',
'Charles Casper Stockham: 23.049% (85213)',
'Diana DeGette: 73.812% (272892)',
'Raymon Anthony Doane: 3.139% (11606)',
'-------------------------------',
'Winner: Diana DeGette']


#output files
output_file = os.path.join("election_data_final.csv")

#open output file
with open(output_file, 'w', newline='') as textfile:
    writer = csv.writer(textfile)
    for item in analysis:
        writer.writerow([item])

