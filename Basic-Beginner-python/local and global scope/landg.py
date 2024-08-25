# scope = The region that a variable is recognized
#A variable is only available from inside the region it is created.
#A global and locally scoped versions of a variable can be created

  # global scope (available inside & outside functions) #function ke bahar and andar use kr sakte hai 
name = 'bro'
def display_name():
 name = "Code" # local scope (available only inside this function) #local scope variable jo 
 print(name)              #function ke andar define kiya hai (bas function ke andar hi use kiya ja sakta hai)print(name)

display_name ()
print(name)