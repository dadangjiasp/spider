import csv
output_list = ['1', '2','3','4']
with open('test.csv', 'a+', encoding='utf-8', newline='') as csvfile:
    w = csv.writer(csvfile)
    w.writerow(output_list)