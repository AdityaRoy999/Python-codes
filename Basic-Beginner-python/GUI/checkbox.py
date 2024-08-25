from tkinter import *

def display():
    if(x.get()==1):
        print("You agree")
    else:
        print("You dont agree ")
windows = Tk()

x = IntVar()
checkbutton1 = Checkbutton(windows, 
                           text = "i agree to something",
                           variable=x,onvalue=1,
                           offvalue=0,
                           command = display,
                           font=('Arial',20),
                           fg = 'Green',
                           activeforeground ='Green',
                           background='Black',
                           activebackground='Black',
                           padx=25,
                           pady=10)
checkbutton1.pack()
windows.mainloop()