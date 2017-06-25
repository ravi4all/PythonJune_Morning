a = 10
b = 5

def add(a,b):
    print(a+b)

def sub(a=4,b=5,c="Hello"):
    print(a-b)
    print(c)

def div(a,b):
    print(a/b)

def mul(a,b):
    print(a*b)


def dynamic_args(*x):
    for i in x:
        print(i)

add(a = 2,b = 4)
sub(a,b)
div(a,b)
mul(a,b)

dynamic_args("Hello","This","is","Python")