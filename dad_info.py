import csv

headers = ['Date', 'Day', 'Time-1', 'Time-2',
           'Time-3', 'Time-4', 'Pred(Ft)-1', 
           'Pred(Ft)-2', 'Pred(Ft)-3', 'Pred(Ft)-4']

data = []

with open('./albany_test.csv') as f:
  file_reader = csv.reader(f, delimiter=' ', quotechar='|')

  data_row_date = ['']
  data_row_times = []
  data_row_fts = []

  for row in file_reader:
    curr_date = data_row_date[0]
    if len(row)==1:
      new_row = row[0].split(",")
      if new_row[0] != curr_date:
        if data_row_date[0] != '':
          if len(data_row_times) == 3:
            data_row_times.append('')
            data_row_fts.append('')
          data_row_date += data_row_times + data_row_fts
          data.append(data_row_date)

        data_row_date = []
        data_row_times = []
        data_row_fts = []

        data_row_date.append(new_row[0])
        data_row_date.append(new_row[1])
        data_row_times.append(new_row[2])
        data_row_fts.append(new_row[3])
      else:
        data_row_times.append(new_row[2])
        data_row_fts.append(new_row[3])

with open('./script_test.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerow(headers)
  writer.writerows(data)