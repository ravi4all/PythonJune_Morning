import re

str_1 = "A quick brown fox jumps over the lazy dog"
str_2 = "Salary of Ram is 12000 and Salary of Shyam is 15000"

# pattern_1 = re.search(r'([A-Z])\w+',str_2)
pattern_1 = re.findall(r'([A-Z][a-z]+)',str_2)
patter_2 = re.findall(r'[\d]+',str_2)

print(pattern_1)
print(patter_2)