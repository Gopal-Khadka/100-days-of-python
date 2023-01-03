class Animal():
    def __init__(self):
        self.eyes=2
    def breathe(self):
        print("Inhale and exhale")

class fish(Animal):
    def __init__(self):
        # super().__init__()
        self.hands=0

    def breathe(self):
        # this func inherits and modifies alittle
        super().breathe()
        print("I hate water")

    def move(self):
        print("moving in the water")

Fish=fish()
# Fish.move()
Fish.breathe()
# print(Fish.eyes)