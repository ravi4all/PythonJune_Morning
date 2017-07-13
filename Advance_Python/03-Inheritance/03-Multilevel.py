class Parent:

    def __init__(self):
        self.name = "Ram"
        self.age = 32

    def show_details(self):
        print(self.name, self.age)

class Child_1(Parent):

    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__()

    def show_details(self):
        print(self.name, self.age)


class Child_2(Child_1):

    def __init__(self):
        self.name = "Shyam"
        self.age = 30

    def show_details(self):
        print(self.name, self.age)