class Car:
 
 wheels = 4 #class variable
 def __init__(self,make,model,year,color):   # in other languages it is called constructor 
    self.make = make    #these are called instance variables 
    self.model = model
    self.year = year
    self.color = color

 def drive(self):
        print("this "+self.model+" is driving ")
    
 def stop(self):
        print("This "+self.model+" is stopped")

