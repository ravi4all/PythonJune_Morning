class Avengers:

    def __init__(self,age,height):
        self.age = age
        self.height = height

    def eligible(self):
        if self.age < 35 or self.height > 6:
            print("Welcome to Avengers Team")
            Avenger.selected_avengers(self)
        else:
            print("Too Old....")


class Avenger(Avengers):

    avengers_list = []

    def __init__(self,name,age,powers,skills,height):
        self.name = name
        self.age = age
        self.powers = powers
        self.skills = skills
        self.height = height

        # Avengers.__init__(self.age,self.height)
        super().__init__(self.age,self.height)

    def print_avenger(self):
        print("Name : {}, Age : {}, Powers : {}, Skills : {}, Height : {}"
              .format(self.name,self.age,self.powers,self.skills,self.height))

    def selected_avengers(self):
        self.avengers_list.append([self.name,self.age,self.powers,self.skills,self.height])

        for av in self.avengers_list:
            print(av)


while True:

    name = input("Enter your Name : ")
    age = int(input("Enter your age : "))
    power = input("Enter your powers : ")
    skills = input("Enter your skills : ")
    height = int(input("Enter your height : "))

    obj = Avenger(name,age,power,skills,height)
    obj.print_avenger()
    obj.eligible()



# hulk = Avenger("Hulk",34,"Monster Strength","Hulk Smash",15)
# hulk.print_avenger()
# hulk.eligible()
#
# iron_man = Avenger("Iron Man",38,"Iron Suit","Intelligence,Fly,Speed",6)
# iron_man.print_avenger()
# iron_man.eligible()
#
# captain_america = Avenger("Captain America",120,"Shield","Fast,Powerful,MMA",6.2)
# captain_america.print_avenger()
# captain_america.eligible()