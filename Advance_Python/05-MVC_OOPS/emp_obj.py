import emp

avengers_list = []

def add_avengers(name,power,skills):

    avengerId = 0
    avengerObj = emp.Avenger(name,power,skills)
    avengerId +=1
    avengers_list.append(avengerObj)
    return avengers_list
