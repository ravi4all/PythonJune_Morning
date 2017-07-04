# import calculator
from modules import calculator

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

addition = calculator.add(num_1,num_2)
subtraction = calculator.sub(num_1,num_2)
division = calculator.div(num_1,num_2)
multiply = calculator.mul(num_1,num_2)
# print("Addition : ",addition)
# print("Subtraction : ",subtraction)
# print("Division : ",division)
# print("Multiplication : ",multiply)

# print("Addition of {} and {} is: ".format(num_1,num_2),addition)
# print("Subtraction of {} and {} is : ".format(num_1,num_2),subtraction)
# print("Division of {} and {} is : ".format(num_1,num_2),division)
# print("Multiplication of {} and {} is : ".format(num_1,num_2),multiply)

print("Addition of %s and %s is: "%(num_1,num_2),addition)
print("Subtraction of %s and %s is : "%(num_1,num_2),subtraction)
print("Division of %s and %s is : "%(num_1,num_2),division)
print("Multiplication of %s and %s is : "%(num_1,num_2),multiply)