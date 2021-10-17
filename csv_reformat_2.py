import csv

headers = ['Date', 'Slack-Time-1', 'Slack-Time-2',
           'Slack-Time-3', 'Slack-Time-4', 'Slack-Time-5', 'Max-Time-1', 'Max-Time-2',
           'Max-Time-3', 'Max-Time-4', 'Max-Time-5', 'Knots-1', 'Knots-2',
           'Knots-3', 'Knots-4', 'Knots-5']

data = []

# you need to hardcode the name of the file in here (unless you are ok with them
# all being named the same thing)
with open('./test_hell.csv', 'r') as f:
  file_reader = csv.reader(f, delimiter=' ')

  date_value = [""]
  slack_times = []
  max_times = []
  knots = []

  for row in file_reader:
    row = [x for x in row if x != '']
    print(row)
    # store current date
    curr_date = date_value[0]
    print(curr_date != row[0], curr_date, row[0])

    if curr_date != row[0]:
      if curr_date != '':
        if len(slack_times) > len(max_times):
          max_times.append("")
          knots.append("")
        date_value += slack_times + max_times + knots
        print(date_value)
        data.append(date_value)
        date_value = [curr_date]
        slack_times = []
        max_times = []
        knots = []

      if row[2] != 'slack':
        slack_times.append("")
        max_times.append(row[1])
        max_type = row[2][0].upper()
        knots.append(row[3] + max_type)
      else:
        slack_times.append(row[1])
    else:
      if row[2] != 'slack':
        max_times.append(row[1])
        max_type = row[2][0].upper()
        knots.append(row[3] + max_type)
      else:
        slack_times.append(row[1])

  date_value += slack_times + max_times + knots
  data.append(date_value)

# creates a new file under this name composed of all the data above
with open('./new_test.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerow(headers)
  writer.writerows(data)
