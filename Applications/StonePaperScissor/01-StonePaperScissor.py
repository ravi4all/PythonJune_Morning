import random

cpu = ["Stone","Paper","Scissor"]
cpu_choice = random.choice(cpu)

counter = 0

while True:

    user_choice = input("Enter your choice : ")

    if user_choice == cpu_choice:
        print("Match Tie")

    elif user_choice == "stone" and cpu_choice == "Scissor":
        print("CPU : ",cpu_choice)
        counter += 1
        print("You Win")
        print("Counter : {}".format(counter))

    elif user_choice == "paper" and cpu_choice == "Stone":
        print("CPU : ",cpu_choice)
        counter += 1
        print("You Win")
        print("Counter : {}".format(counter))

    elif user_choice == "scissor" and cpu_choice == "Paper":
        print("CPU : ",cpu_choice)
        counter += 1
        print("You Win")
        print("Counter : {}".format(counter))

    elif user_choice == "stone" and cpu_choice == "Paper":
        print("CPU : ",cpu_choice)
        counter -= 1
        print("You Loss")
        print("Counter : {}".format(counter))

    elif user_choice == "paper" and cpu_choice == "Scissor":
        print("CPU : ",cpu_choice)
        counter -= 1
        print("You Loss")
        print("Counter : {}".format(counter))

    elif user_choice == "scissor" and cpu_choice == "Stone":
        print("CPU : ",cpu_choice)
        counter -= 1
        print("You Loss")
        print("Counter : {}".format(counter))

    else:
        print("Wrong Choice")

    cpu_choice = random.choice(cpu)