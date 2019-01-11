import csv
with open('budget_data.csv','r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    Total_months = 0
    Total_rev = 0
    last_MonthRev = 0
    Maximum = -100
    Minimum = 1000
    rev_change_list=[]

    for r in csv_reader:
        # To get the total number of months
        Total_months += 1 
        Total_rev += int(r[1]) # To get the sum of total revenue
        rev_change = int(r[1]) - last_MonthRev #To get the difference of revenue from previous month
        rev_change_list.append(rev_change)#Append the revenue change in the list to calculate the required values after loop
        #To reset the last Month Revenue for the next row
        last_MonthRev = int(r[1])
        # If loop is set up to get the Date when maximum and minimum revenue changed happen
        if rev_change > Maximum:
            Maximum = rev_change
            MaxRev_change_date = r[0]
        if rev_change < Minimum:
            Minimum = rev_change
            MinRev_change_date = r[0]
    # To remove 1st item in revenue_change_list which was done by setting last_MonthRev zero for the first row Rev_change calculation
    rev_change_list.pop(0)
    MaxRev_Change = max(rev_change_list)
    MinRev_Change = min(rev_change_list)
    Average_Change = sum(rev_change_list)/len(rev_change_list)

     # To print the analysis report
    print("Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {Total_months}")
    print(f"Total:  ${Total_rev}")
    print(f"Average Change: ${round(Average_Change, 2)}")
    print(f"Greatest Increase in Profits: {MaxRev_change_date} (${MaxRev_Change})")
    print(f"Greatest Decrease in Profits: {MinRev_change_date} (${MinRev_Change})")   
    
    