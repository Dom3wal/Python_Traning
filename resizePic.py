from tkinter import PhotoImage
import cv2 as cv

photo = cv.imread('E:\THeDolaken\Python\Python-Symbol.png')

resized = cv.resize(photo,(400,400),interpolation=cv.INTER_CUBIC)

cv.imshow("Resized",resized)

cv.imwrite('Python-Symbol-res.png',resized)

cv.waitKey()