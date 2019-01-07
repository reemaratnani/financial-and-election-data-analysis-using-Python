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
    print(round(Average_change, 2))
    csvfile.seek(0)
    next(csvfile)
    next(csvfile)
    month_column = [r[0] for r in csv_reader]
    Month_Monthchange = dict(zip(month_column,Monthly_change))
    Greatest_increase = max(zip(Month_Monthchange.values(), Month_Monthchange.keys()))
    Greatest_decrease = min(zip(Month_Monthchange.values(), Month_Monthchange.keys()))
    print(Greatest_increase)
    print(Greatest_decrease)