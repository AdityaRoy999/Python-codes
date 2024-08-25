class Animal:
    alive = True 

    def eat(self):
        print("This animal is eating")
    
    def sleep(self):
        print("this animal is sleeping ")

class rabit(Animal):     #here child class is rabit and parent class is animal
    def run(self):
        print("This rabbit is running")
class fish(Animal):
    def swim(self):
        print("This Fish is swimming")
class hawk(Animal):
    def fly(self):
        print("This Hawk is flying")

rabbit = rabit()
Fish = fish()
Hawk = hawk()

Fish.swim()
Fish.sleep()
Hawk.fly()
