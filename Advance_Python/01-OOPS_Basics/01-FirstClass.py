class Car:
    """This is my first class with OOPS"""
    id = 0
    name = ""
    color = ""

audi = Car()
audi.id = 1
audi.name = "Audi"
audi.color = "Black"

bmw = Car()
bmw.id = 2
bmw.name = "BMW"
bmw.color = "Red"

#print(Car.__dict__)
print(Car.__doc__)

print("Name : {}, Color : {}".format(audi.name, audi.color))

print("Name : {}, Color : {}".format(bmw.name, bmw.color))