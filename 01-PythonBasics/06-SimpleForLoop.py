'''
a = [1,2,3,4,5,56,67,8,8,45,34,675,8,679,67]

for i in a:
    print(i)
    print("------")
'''

# Pattern Program
#z = [1,2,3,4,5,6]

for x in range(0,6):
    for y in range(0,x):
        print("*", end="----")
    print()


for x in reversed(range(0,6)):
    for y in range(0,x):
        print("*", end="----")
    print()
