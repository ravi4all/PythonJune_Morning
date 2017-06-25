def calculator(ch,num_1,num_2):
    value = 'num_1' + ch + 'num_2'
    return eval(value)

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

        to_calc = {
            "1" : "+",
            "2" : "-",
            "3" : "/",
            "4" : "*"
        }

        print("Result is",calculator(to_calc[user_choice],num_1,num_2))

mainFunction()