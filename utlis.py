import cv2 as cv
import numpy as np

def rectContour(contours):
    rectContour =[]
    for i in contours:
     area = cv.contourArea(i)
    
     if area>50:
        peri = cv.arcLength(i,True)
        approx = cv.approxPolyDP(i,0.02*peri,True)
        if len(approx)==4:
            rectContour.append(i)
    