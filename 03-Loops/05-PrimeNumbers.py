while True:
    num = int(input("Enter the number : "))

    if num > 2:
        for i in range(2,num):
            if num % i == 0:
                print("Not a prime number")
                break
        else:
            print(num,"is a Prime number")