import cv2 as cv 
import numpy as np 
from utlis import rectContour,getconnerPoints

img = cv.imread('Photos/omr2.png',)
cv.imshow('omr',img,)
img = cv.resize(img,(600,600))
img_contour=img.copy()
img_biggest_contour = img.copy()
gray_omr = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray_omr',gray_omr)

omr_blur = cv.GaussianBlur(gray_omr,(5,5),1)
cv.imshow('omr_blur',omr_blur)


edage_of_omr = cv.Canny(omr_blur,10,50)
cv.imshow('edage_of_omr',edage_of_omr)

contours,hierarchy = cv.findContours(edage_of_omr,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img_contour,contours,-1,(0,255,0),2)

cv.imshow('countours',img_contour)

rectCon = rectContour(contours)
biggestContour  = getconnerPoints(rectCon[0])
gradePoint = getconnerPoints(rectCon[1])


if biggestContour.size !=0 and gradePoint.size !=0:
    cv.drawContours(img_biggest_contour,biggestContour,-1,(0,255,0),20)
    cv.drawContours(img_biggest_contour,gradePoint,-1,(255,0,0),20)

cv.imshow('biggestContour',img_biggest_contour)
cv.imshow('gradePoint',img_biggest_contour)






cv.waitKey()
