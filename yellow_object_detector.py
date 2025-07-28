import cv2 as cv
from PIL import Image
from utlis import get_limits 



yellow = (0,255,255)
cap =cv.VideoCapture(0)
while True:

    ret,frame = cap.read()
    hsvImage = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lowerLimit,upperLimit =  get_limits(yellow)

    mask = cv.inRange(hsvImage,lowerLimit,upperLimit)
    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox:
       frame = cv.rectangle(frame,(bbox[0],bbox[1]),(bbox[2],bbox[3]),(0,255,0),5)


    cv.imshow('mask',frame)

    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()    