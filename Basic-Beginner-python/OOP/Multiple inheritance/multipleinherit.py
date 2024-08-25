#multiple inheritance = when a child class is serived from more than one parent class 

class Prey:

    def flee(self):
        print("This animal flees")

class predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass
class hawk(predator):
    pass

class Fish(Prey,predator):
    pass


rabbit = Rabbit()
Hawk = hawk()
Fish = Fish()

Fish.flee()
Fish.hunt()

    