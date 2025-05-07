import csv

""" with open('test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['user_id', 'user_id', 'comments_qty'])
    writer.writerow([2311, 'vika', '2136'])
    writer.writerow([2221, 'bogdan', '2434'])
    writer.writerow([2211, 'vfv', '2834'])
 """

with open('test.csv') as csv_file:
    reader = csv.reader(csv_file)
    print(reader)
    print(type(reader))
    for line in reader:
        print(line)
