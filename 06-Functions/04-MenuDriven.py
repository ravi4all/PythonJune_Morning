def add(num_1,num_2):
    return num_1 + num_2

def sub(num_1,num_2):
    return num_1 - num_2

def div(num_1,num_2):
    return num_1 / num_2

def mul(num_1,num_2):
    return num_1 * num_2

def mainFunction():

    while True:

        print("""
1. Add
2. Sub
3. Div
4. Mul
""")

        user_choice = input("Enter your choice : ")

        num_1 = int(input("Enter first number : "))
        num_2 = int(input("Enter second number : "))

        # if user_choice == "1":
        #     print(add(num_1,num_2))
        # elif user_choice == "2":
        #     print(sub(num_1,num_2))
        # elif user_choice == "3":
        #     print(div(num_1,num_2))
        # else:
        #     print(mul(num_1,num_2))

        to_calc = {
            "1" : add,
            "2" : sub,
            "3" : div,
            "4" : mul
        }

        print(to_calc.get(user_choice)(num_1,num_2))


mainFunction()