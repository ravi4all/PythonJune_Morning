import csv

path = "data.csv"

data = ["First Name, Last Name".split(","),
        "Sachin, Tendulkar".split(","),
        "MS, Dhoni".split(","),
        "John, Cena".split(","),
        "Virat,Kohli".split(",")]

# csv_file = open(path,'w')
with open(path,'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')

    for line in data:
        writer.writerow(line)