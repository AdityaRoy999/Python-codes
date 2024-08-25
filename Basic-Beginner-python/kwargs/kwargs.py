#**kwargs  parameter that will pack all arguments into a dictionary
#useful so that a function can accept a varying amount of keyword argume

def hello(** kwargs) :  #here you can use any name instead of kwarsg only the thing is important is **
#print ("Hello " + kwargs['first!] + " " + kwargs[last'])
 print("Hello",end=" ")
 for key,value in kwargs.items():
  print(key,value,end=" ")

hello(title="Mr.", first="Bro",middle="Dude", last="Code")

