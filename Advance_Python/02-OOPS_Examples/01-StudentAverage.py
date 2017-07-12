class Student:

    def __init__(self,p,c,m):
        self.p = p
        self.c = c
        self.m = m
        self.average = 0
        self.grade = ""

    def marks(self):
        self.average = (self.p + self.c + self.m) // 3
        print("Average is",self.average)

    def grading_system(self):

        if self.average > 90:
            self.grade = 'A'
            print("Grade : {}".format(self.grade))
        elif self.average < 90 and self.average > 75:
            self.grade = 'B'
            print("Grade : {}".format(self.grade))
        elif self.average < 75 and self.average > 60:
            self.grade = 'C'
            print("Grade : {}".format(self.grade))
        else:
            print("Get Lost....")


phy = int(input("Enter marks of physics : "))
chem = int(input("Enter marks of chemistry : "))
maths = int(input("Enter marks of maths : "))


ram = Student(phy,chem,maths)
ram.marks()
ram.grading_system()