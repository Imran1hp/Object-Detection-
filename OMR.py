import cv2 as cv 
import numpy as np 

img = cv.imread('Photos/omr1.jpg')
cv.imshow('omr',img)

gray_omr = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray_omr',gray_omr)

omr_blur = cv.GaussianBlur(gray_omr,(5,5),1)
cv.imshow('omr_blur',omr_blur)


edage_of_omr = cv.Canny(omr_blur,100,200)
cv.imshow('edage_of_omr',edage_of_omr)












cv.waitKey()
