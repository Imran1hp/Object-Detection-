import cv2 as cv
import numpy as np

def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv.cvtColor(c,cv.COLOR_BGR2HSV)
    lowerLimit = hsvC[0][0][0]-10,100,100
    upperLimit = hsvC[0][0][0]+10,255,255


    lowerLimit = np.array(lowerLimit,dtype=np.uint8)
    upperLimit = np.array(upperLimit,dtype=np.uint8)
    
    return lowerLimit,upperLimit