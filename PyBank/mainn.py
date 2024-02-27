import csv
import os

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #use next to skip first row
    next(csvreader)
    # list to store data
    total_months = []
    total_prof = []
    prof_change = 0
    monthly_change = []

    for row in csvreader:
        # add months
        total_months.append(row[0])
         # add profit/loss
        total_prof.append(int(row[1]))

        
print("Financial Analysis")
print("----------------------------")
print("Total Months:", len(total_months))
print("Total: $", sum(total_prof))


for row in range(1,len(total_prof)):
    monthly_change.append(total_prof[row]-total_prof[row-1])
    
    # determine average change for profit & loss
    avg_change = sum(monthly_change)/len(monthly_change)
    rounded = round(avg_change,2)
    # greatest increase & decrease
    greatest_increase = max(monthly_change)
    greatest_decrease = min(monthly_change)
    #determine the day of greatest change
    dayOf_GreatInc = total_months[monthly_change.index(greatest_increase)+1]
    dayOf_GreatDec = total_months[monthly_change.index(greatest_decrease)+1]
    
# print avg change, greatest increase, and decrease
print("Average Change:", rounded)
print("Greatest Increase in Profits:", (dayOf_GreatInc),"($",greatest_increase,")")
print("Greatest Decrease in Profits:", (dayOf_GreatDec),"($",greatest_decrease,")")


analysis = ['Financial Analysis', 
'----------------------------',
'Total Months: 86',
'Total: $ 22564198',
'Average Change: -8311.11',
'Greatest Increase in Profits: Aug-16 ($ 1862002 )',
'Greatest Decrease in Profits: Feb-14 ($ -1825558 )']
#output files
output_file = os.path.join("budget_data_final.csv")

#open output file
with open(output_file, 'w', newline='') as textfile:
    writer = csv.writer(textfile)
    for item in analysis:
        writer.writerow([item])
