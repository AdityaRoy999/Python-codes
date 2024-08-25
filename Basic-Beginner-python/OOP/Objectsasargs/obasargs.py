class Car:
    color = None

class Motocycle:
    color = None

def color_change(Caar,color):  # here car should be same in the next line 
    Caar.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()
bike_1 = Motocycle()

color_change(car_1,"red")
color_change(car_2,"yellow")
color_change(car_3,"silver")
color_change(bike_1,"black")


print(car_1.color())
print(car_2.color())
print(car_3.color())

