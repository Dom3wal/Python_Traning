from tkinter import *

from cv2 import threshold

windows = Tk()

hotImage = PhotoImage(file="Python-Symbol-res2.png")
hotLabel = Label(image = hotImage)
hotLabel.pack()



def submit():
    print("The temperature is " + str(scale.get()) + " degrees C")

scale = Scale(windows,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL, #orientation of sscale
              font =("Ariel",20),
              tickinterval=20,
              showvalue=1, # hide current value when 0
              troughcolor='#69EAFF',# scale color
              fg = '#FF1C00', #font color text
              bg= '#000000')
scale.pack()
# scale.set(50) # sets default possiton
scale.set(((scale['from']-scale['to'])/2)+scale['to']) #always set scale to the midde even when we change from option to different range
button = Button(windows,
                text='submit',
                command=submit,
                )


coldImage = PhotoImage(file="Python-Symbol-res2.png")
coldLabel = Label(image = coldImage)
coldLabel.pack()

button.pack()
windows.mainloop()