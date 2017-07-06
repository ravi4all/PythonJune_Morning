def division():
    a = int(input("Enter a number: "))
    b = a/2
    try:
        assert(b > 0 ), "Try Again"
        print("Result is ",b)
    except AssertionError as er:
        print(er)

division()

