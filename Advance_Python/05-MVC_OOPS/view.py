import controller

def user_operatiopns():

    while True:
        name = input("Enter your name : ")
        power = input("Enter your powers : ")
        skills = input("Enter your skills : ")

        avengersData = controller.get_avengers(name,power,skills)

        printAvengers(avengersData)

def printAvengers(data):

    for i in data:
        print(i)

user_operatiopns()

