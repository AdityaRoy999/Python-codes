#str.format() = optional method that gives users
#more control when displaying output

name = "Bro"

print("Hello, my name is {}". format(name) )
print("Hello, my name is {:10}. Nice to meet you". format(name) )  #padding string spaces
print("Hello, my name is {:<10}. Nice to meet you". format(name) )
print("Hello, my name is {:>10}. Nice to meet you". format(name) )
print("Hello, my name is {:^10}. Nice to meet you". format(name) )

number = 1000

#print("The number pi is {:.3f}". format (number)) #display first three digits after the decimal if any 
print("The number is {:,}". format (number) )
print("The number is {:b}". format(number))
print("The number is {:o}". format (number) )
print("The number is {:X}". format (number))
print("The number is {:E}". format (number) )

animal = "cow"
item = "moon"

#print ("The "tanimal+" jumped over the "+item)
print("The {} jumped over the {}".format(animal, item) )
print("The {1} jumped over the {0}".format(animal, item) ) #positional argument changes on what number you have writen.

#f-string = new method introduced in Python 3.6 for string formatting with variables in a more readable way than str.format()    
