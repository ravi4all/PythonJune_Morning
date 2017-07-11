class Car:

    car_speed = 0

    def speed(self,car_s):
        Car.car_speed = car_s
        print("Speed :",Car.car_speed)

    def display(self,id,name,color):
        print("Car :",id,name,color)
        # print("Speed : ",Car.car_speed)


audi = Car()
audi.display(1,"Audi","Red")
audi.speed(250)