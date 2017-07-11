class Player:

    def __init__(self):
        self.name = []
        self.scores = []

    def show(self,n,s):
        self.name.append(n)
        self.scores.append(s)
        print("Names : ",self.name)
        print("Scores : ",self.scores)

player_1 = Player()
player_1.show("Sachin",87)

print("Player_1 Name : ",player_1.name)

player_2 = Player()
player_2.show("Rahul",67)

print("Player_2 Name : ",player_2.name)