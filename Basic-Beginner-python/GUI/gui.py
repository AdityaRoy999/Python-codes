from tkinter import *
#widgets - GUI elements: buttons, textboxes, labels, images
#windows - serves as a container to hold to contain these widgets 
window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Box")
#icon = PhotoImage(file='1.png')
#window.iconphoto(True, icon) #replaces the icon with your icon 
window.config(background="red")#you can also have a hex value instead of a color name 
window.mainloop() #places windows on computer screen and listen to events 
