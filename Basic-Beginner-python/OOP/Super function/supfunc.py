#super() = function used to give access to the methods of parent class.
#          Returns a temporary object of a parent class when used
class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

class square(rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width
        

class Cube(rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height
    def volume(self):
        return self.width*self.height*self.length


square = square(3,3)
cube = Cube(3,3,3)


print(square.area())
print(cube.volume())

