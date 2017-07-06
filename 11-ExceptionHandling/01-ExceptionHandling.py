try:
    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))
    result = num_1 +num_2
    print("Result is",result)
except ValueError as v:
    print("You have entered something wrong....")
    print("Error is",v)