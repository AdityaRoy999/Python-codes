from tkinter import *
#buttons = you click , it actions 
count = 0
def click():
    print("GOOD MORNING MAA ❤️")
    

window = Tk()
photo = PhotoImage(file='C:\\Users\\adiro\\Downloads\\g.png')
button =Button(window,
               text="Click me:",
               command=click,
               relief=RAISED,
               bd=10,
               fg='white',
               font=("Comic sans",30),
               bg="black",
               activebackground="black",
               activeforeground="white",
               compound='bottom',
               image=photo)
window.config(bg="black")
button.pack()
window.mainloop()