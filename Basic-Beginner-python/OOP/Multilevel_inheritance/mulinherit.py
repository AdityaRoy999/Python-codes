#multilevel inheritance = when a derived(child) class inherits another derived(child) class
#here organism is the grandparent, animal is the parent and dog is the child of animal 




class organism:
    alive = True

class Animal(organism):
    def eat(self):
        print("This animal is eating")

class dog(Animal):
    def bark(self):
        print("This dog is barking")



Dog = dog()



dog.bark(self=dog)
dog.eat(self=dog)



