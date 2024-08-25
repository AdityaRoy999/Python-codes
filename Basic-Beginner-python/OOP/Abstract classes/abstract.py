#prevents a user from creating a object of that class
# * compels a user to overiide abstract methods in a child class

# abstract class = a class which contains one or more abstract methods 
#abstact methods = a method that has a declaration but does not have an implementation.
#here we will prevent the vehicle to be created as a object because basically it doesn't contain anything 
from abc import ABC,abstractmethod
class Vehicle:
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("You drive tha car")
    def stop(self):
        print("This car has stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("This car has stopped")
#motorcycle = Motorcycle()
#car = Car()

#car.stop()
#motorcycle.stop()

#car.go()
#motorcycle.go()

#Vehicle = Vehicle()  #here the vehicle object will give error
# and also if you print pass in any of the car or motocycle instead of go func which is present 
#inside it will basically consider the default of vehicle which contains the abstract class for the particular function hence gives error
#NOTE - this absract method is for the func inside the Vehicle class not the class itself.