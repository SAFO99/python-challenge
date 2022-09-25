import os
import csv
import statistics

data_path='./Resources/budget_data.csv'
Total_months=0
Net_total=0
Average_Change=0
Greatest_increase=0
Greatest_decrease=0
Greatest_increase_date=""
Greatest_decrease_date=""
Change=[]
Month_to_month_Change=[]

with open(data_path, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        Total_months += 1
       
        Current_net =int(row[1])
        previous_Net = 0
        Net_total += Current_net
        if len(Change) >0:
            previous_Net =Change[-1]
        if  Current_net - previous_Net > Greatest_increase:
            Greatest_increase_date = (row[0])
            Greatest_increase = Current_net - previous_Net
        elif Current_net - previous_Net < Greatest_decrease:
            Greatest_decrease_date = (row[0])
            Greatest_decrease = Current_net - previous_Net
        Change.append(Current_net)

# track monthly Changes
for i in range(len(Change)-1):
    monthlyChange = (Change[i+1] - Change[i])
    Month_to_month_Change.append(monthlyChange)   

Average_Change = statistics.mean(Month_to_month_Change)

print("Financial Analysis")
print("___________________________________")

print("Total Months: " + str(Total_months))
print("Total: $" + str(Net_total))
print("Average Change is: $" + str(round(Average_Change, 2)))
print("Greatest Increase in Profits: " + str(Greatest_increase_date) + "  ($" + str(Greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(Greatest_decrease_date) + "  ($" + str(Greatest_decrease) + ")")

# now write this to an output file
f = open("./Analysis/financial_analysis.txt", "w")
f.write("Financial Analysis\n")
f.write("___________________________________\n")

f.write("Total Months: " + str(Total_months)+"\n")
f.write("Total: $" + str(Net_total)+"\n")
f.write("Average Change is: $" + str(round(Average_Change, 2))+"\n")
f.write("Greatest Increase in Profits: " + str(Greatest_increase_date) + "  ($" + str(Greatest_increase) + ")\n")
f.write("Greatest Decrease in Profits: " + str(Greatest_decrease_date) + "  ($" + str(Greatest_decrease) + ")")

