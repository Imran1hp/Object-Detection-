import cv2 as cv 
import numpy as np 

img = cv.imread('Photos/omr2.png',)
cv.imshow('omr',img,)
img = cv.resize(img,(600,600))
img_contour=img.copy()
gray_omr = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray_omr',gray_omr)

omr_blur = cv.GaussianBlur(gray_omr,(5,5),1)
cv.imshow('omr_blur',omr_blur)


edage_of_omr = cv.Canny(omr_blur,10,50)
cv.imshow('edage_of_omr',edage_of_omr)

contours,hierarchy = cv.findContours(edage_of_omr,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img_contour,contours,-1,(0,255,0),2)

cv.imshow('countours',img_contour)










cv.waitKey()
