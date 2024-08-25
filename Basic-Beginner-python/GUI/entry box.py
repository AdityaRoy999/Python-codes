from tkinter import *
from turtle import bgcolor

from numpy import blackman, size



#entry widget = textbox that accepts single line of input 
def submit():
    username = entry.get()
    print(username)
def delete1():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1,END)
window = Tk()
entry = Entry(window,
              font=("ariel",50),
              bg = "black",
              fg="white",
              show="*")
entry.insert(0,'Hello ')
entry.place(x=10,y=40)
entry.pack(side=TOP)
sumit_1 = Button(window,
                 text="Submit",
                 relief=RAISED,
                 bg="green",
                 activebackground="green",
                 command=submit)
sumit_1.pack(side=RIGHT)
delete_1 = Button(window,
                  text="delete",
                  relief=RAISED,
                  bg="red",
                  activebackground="red",
                  command=delete1,
                  )
delete_1.pack(side=RIGHT)
backspace_1 = Button(window,
                     text="backspace",
                     relief=RAISED,
                     bg="red",
                     activebackground="red",
                     command=backspace,
                     )
backspace_1.pack(side=RIGHT)

window.config(background="black")
window.mainloop()