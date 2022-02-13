from tkinter import *

from numpy import size

window = Tk()

def display():
    if(x.get()=="YES"):
        print("You agree !")
    else:
        print("You dont agree: :(")

pyth_photo = PhotoImage(file = 'Python-Symbol-res.png')

x = StringVar()

check_button = Checkbutton(window, 
                            text = "I Agree to something",
                            variable = x,
                            onvalue="YES",
                            offvalue="NO",
                            command = display,
                            font = ("Comic Sans", 40),
                            fg = '#00FF00',
                            bg = 'black',
                            activebackground='black',
                            activeforeground='#00FF00',
                            padx=25,
                            pady = 20,
                            image = pyth_photo,
                            compound='left',
                            width = 500,
                            height=500)

check_button.pack()
window.mainloop()