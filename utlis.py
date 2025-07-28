import cv2 as cv
import numpy as np

def rectContour(contours):
    rectCon =[]
    for i in contours:
     area = cv.contourArea(i)
    
     if area>50:
        peri = cv.arcLength(i,True)
        approx = cv.approxPolyDP(i,0.02*peri,True)
        if len(approx)==4:
            rectCon.append(i)
    
    rectCon = sorted(rectCon,key=cv.contourArea,reverse=True) 

    return rectCon


def getconnerPoints(cont):
   peri = cv.arcLength(cont,True)
   approx = cv.approxPolyDP(cont,0.02*peri,True)
   return approx


def reorder(my_point):
   my_point = my_point.reshape((4,2))
   add = my_point.sum(1)