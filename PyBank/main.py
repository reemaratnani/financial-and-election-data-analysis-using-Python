import csv
with open('budget_data.csv','r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csvfile) #To skip the header row
    # Prepared the list of Monthly-Profit/Loss column in csvfile and found Total Revenue and total month count
    Monthly_rev = [int(r[1]) for r in csv_reader]
    Month_count = len(Monthly_rev)
    Total = sum(Monthly_rev)
    #Iteration of Profit/Loss list through zip function to get the difference of each month revenue from the previous month.
    Rev_change = [(x[1]-x[0])for x in zip(Monthly_rev[:-1],Monthly_rev[1:])]
    Average_change = sum(Rev_change)/len(Rev_change)
    MaxRev_change = max(Rev_change)
    MinRev_change = min(Rev_change)
    #Reset the cursor position, skip header row then skip first row of Date, date column to pair with Rev-change and found max and min rev-change date
    csvfile.seek(0)
    next(csvfile)
    next(csvfile)
    Date = [str(r[0]) for r in csv_reader]
    MaxRev_change_Date = Date[Rev_change.index(max(Rev_change))]
    MinRev_change_Date = Date[Rev_change.index(min(Rev_change))]
    
    # To print the analysis report
    print("Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {Month_count}")
    print(f"Total:  ${Total}")
    print(f"Average Change: ${round(Average_change, 2)}")
    print(f"Greatest Increase in Profits: {MaxRev_change_Date} (${MaxRev_change})")
    print(f"Greatest Decrease in Profits: {MinRev_change_Date} (${MinRev_change})")