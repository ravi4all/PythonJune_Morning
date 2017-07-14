import re

str_1 = "A quick brown fox jumps over the lazy dog"
str_2 = "Salary of Ram is 12000 and Salary of Shyam is 15000"


if re.search('([A-Z])',str_2):
    print("Match Found...")
else:
    print("Not Found")


if re.search(r'[\d]',str_1):
    print("Match Found")
else:
    print("Not Found")