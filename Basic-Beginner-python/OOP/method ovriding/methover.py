class Animal:
    def eat(self):   #here eat(self) is known as method signature
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):  #here it overides specifically for rabbit
        print("This rabbit is eating a carrot")




Rabbit = Rabbit()
Rabbit.eat()

Animal = Animal()
Animal.eat()