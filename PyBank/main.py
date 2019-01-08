import csv
with open('budget_data.csv','r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    headerline = next(csvfile)
    # for row in csv_reader:
    new_list = [int(r[1]) for r in csv_reader]
    Month_count = len(new_list)
    # print(Month_count)
    Total = sum(new_list)
    # print(Total)
    Monthly_change = [(x[1]-x[0])for x in zip(new_list[:-1],new_list[1:])]
    Average_change = sum(Monthly_change)/len(Monthly_change)
    # print(round(Average_change, 2))
    csvfile.seek(0)
    next(csvfile)
    next(csvfile)
    month_column = [r[0] for r in csv_reader]
    Month_Monthchange = dict(zip(month_column,Monthly_change))
    key, value = max(Month_Monthchange.items(), key=lambda x:x[1])
    key1, value1 = min(Month_Monthchange.items(), key=lambda x:x[1])
    # print(key, value)
    # print(key1, value1)
    print(f"Total Months: {Month_count}")
    print(f"Total:  ${Total}")
    print(f"Average Change: ${round(Average_change, 2)}")
    print(f"Greatest Increase in Profits: {key} (${value})")
    print(f"Greatest Decrease in Profits: {key1} (${value1})")