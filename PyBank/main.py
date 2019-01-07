import csv
with open('budget_data.csv','r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    headerline = next(csvfile)
    # for row in csv_reader:
    new_list = [int(r[1]) for r in csv_reader]
    Month_count = len(new_list)
    print(Month_count)
    Total = sum(new_list)
    print(Total)
    Monthly_change = [(x[1]-x[0])for x in zip(new_list[:-1],new_list[1:])]
    Average_change = sum(Monthly_change)/len(Monthly_change)
    print(Average_change)
    print(max(Monthly_change))
    print(min(Monthly_change))