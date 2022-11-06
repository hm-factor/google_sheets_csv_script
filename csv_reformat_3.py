import csv
import re

headers = ['Date', 'Day', 
        'Time-1', 'Time-2', 'Time-3', 'Time-4', 
        'Pred-1(Ft)', 'Pred-2(Ft)', 'Pred-3(Ft)', 'Pred-4(Ft)',
        'Pred-1(cm)', 'Pred-2(cm)', 'Pred-3(cm)', 'Pred-4(cm)',
        'High/Low-1', 'High/Low-2', 'High/Low-3', 'High/Low-4']
data = []

with open('./Data/sandy_hook.csv', 'r') as f:
    date = [""]
    day = [""]
    time = []
    pred_ft = []
    pred_cm = []
    high_low = []
    count = 0

    for row in f:
        row = re.split(', |,| |[|]', row)
        row[-1] = row[-1].strip("\r\n")
        
        if date[0] != row[0]:
            if count == 3:
                time.append('')
                pred_ft.append('')
                pred_cm.append('')
                high_low.append('')
            temp = date + day + time + pred_ft + pred_cm + high_low
            data.append(temp)
            date[0] = row[0]
            day[0] = row[1]
            time = []
            pred_ft = []
            pred_cm = []
            high_low = []
            count = 0
            
        time.append(row[2])
        pred_ft.append(row[3])
        pred_cm.append(row[4])
        high_low.append(row[5])
        count += 1

# creates a new file under this name composed of all the data above
# CHANGE NEW FILE NAME HERE
with open('./new_sandy_hook.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)
