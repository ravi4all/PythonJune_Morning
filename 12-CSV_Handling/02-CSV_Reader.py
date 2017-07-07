import csv

path = "data.csv"

with open(path,'r') as csv_file:
    reader = csv.reader(csv_file)

    for data in reader:
        print(data[0],data[1])