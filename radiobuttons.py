from tkinter import *
import cv2 as cv
import os
food = ['pizza', 'hamburger', 'hotdogs']

window = Tk()

filename = 'E:\THeDolaken\Python\Python-Symbol-res.png'

path = 'E:\THeDolaken\Python\Python-Symbol-res2.png'

if (os.path.exists(path)):
    print("Image is already created")
else:
    photo = cv.imread(filename)
    resized = cv.resize(photo,(100,100))
    cv.imwrite('Python-Symbol-res2.png',resized)

realphoto = PhotoImage(file ='Python-Symbol-res2.png')
foodImages = [realphoto,realphoto,realphoto]
x = IntVar()

def chosen():
    if (x.get() == 0):
        print("Eat Pizza")
    elif (x.get()  == 1):
        print('Eat hamburger')
    elif(x.get()  == 2):
        print('Eat hotdogs')
    else:
        print("huh?")


for item in range(len(food)):
    button = Radiobutton(window,
                        text = food[item],#addes text
                        variable=x, #groups radiobuttons together if they share same variable
                        value = item, #assigns radiobutton different value - chose option
                        padx = 25,
                        pady = 25,
                        font = ("Impact",30),
                        image = foodImages[item],#adds images t radiobuttons)
                        compound='left',# adds image and text lef side
                        width=300,
                        indicatoron=0, #eliminate circle idnicators = pushbuttons
                        command = chosen # Set command of radiobutton to fucntion
                        ) 
    
    button.pack()
    
window.mainloop()