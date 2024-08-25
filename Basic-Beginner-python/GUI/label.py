from tkinter import *
#label = an area of the widget that holds text and/or an image within a window
window = Tk()
photo = PhotoImage(file='C:\\Users\\adiro\\Downloads\\Python\\Basic-Beginner-python\\GUI\\1.png')


label = Label(window,
              text="Hello World",
              font=('Arial',40,'bold'),
              fg='green',bg='black',   #fg stands for foreground(color of the text) 
              relief=RAISED,           #relief is the effect on the border of the text 
              bd=10,
              padx=10,
              pady=20,
              image=photo,
              compound='bottom')
window.geometry("540x540")
window.iconphoto(True,photo)
window.title("Hello World")
label.place(x=100,y=100), #it will print the text on the app based on the coordinates
window.mainloop()