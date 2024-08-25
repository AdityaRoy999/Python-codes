#there are two parts attributes = is/has ex. name,age,height.
#methods = actions ex. eat ,sleep etc..
#to create attributes you need to create class(blueprint).
#here all the thing written inside the class car after def __init__ is called attributes.
#and the def drive and def stop and def __init__  is called methods or actions.

class Car:
 def __init__(self,make,model,year,color):   # in other languages it is called constructor 
    self.make = make 
    self.model = model
    self.year = year
    self.color = color 

 def drive(self):
        print("this "+self.model+" is driving ")
    
 def stop(self):
        print("This "+self.model+" is stopped")



