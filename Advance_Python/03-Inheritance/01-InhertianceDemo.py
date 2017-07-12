class Parent:

    def add(self):
        x = 10
        y = 20
        z = x+y
        print(z)

    def parent_disp(self):
        print("This is parent...")

    def show(self):
        print("This method is inside Parent")

class Child(Parent):

    def sub(self):
        x = 12
        y = 10
        z = x - y
        print(z)

    def child_disp(self):
        print("This is child...")

    def show(self):
        print("This method is inside Child")

obj_1 = Child()
# obj_1.sub()
# obj_1.add()
obj_1.parent_disp()
obj_1.child_disp()

obj_1.show()