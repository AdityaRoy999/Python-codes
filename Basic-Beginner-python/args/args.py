#parameter that will pack all arguments into a tuple(you don't have to define each argument indiviually)
#useful* so that a function can accept a varying amount of arguments

def add(*stuff):
 sum = 0
 stuff = list(stuff)
 stuff[0] = 0
 for i in stuff:
  sum += i      # or sum = sum + i 
 return sum
 
print(add(1,2,3,4,5,6))