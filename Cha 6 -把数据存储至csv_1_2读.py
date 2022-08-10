import csv
with open('test.txt', 'r',encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)
        print(row[0])