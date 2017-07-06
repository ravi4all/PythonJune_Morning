try:
    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))
    result = num_1 +num_2
    print("Result is",result)
    file = open("file_name.txt",'r')
    file.read()
except (FileNotFoundError,ValueError) as er:
    print(er)

finally:
    print("I will always execute")

print("Let me execute....")