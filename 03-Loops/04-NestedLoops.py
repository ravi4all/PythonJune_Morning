# for i in range(1,31,3):
#     for j in range(10,20):
#         print("Inside J",j)
#     print("Inside I",i)

# for i in range(0,11):
#     for j in range(0,i):
#         print("*",end="")
#     print()

for i in reversed(range(0,11)):
    for j in range(0,i):
        print("*",end="")
    print()