import cv2 as cv
from PIL import Image
from util import limits
blue=[255,0,0]

url='http://192.168.1.11:8080/video'
cap = cv.VideoCapture(0)
while True:
    ret,frame=cap.read()
    
    hsvimage=cv.cvtColor(frame,cv.COLOR_BGR2HSV) 
    lowerlimit,upperlimit=limits(color=blue)
    mask=cv.inRange(hsvimage,lowerlimit,upperlimit )
    mask_=Image.fromarray(mask)
    bbox=mask_.getbbox()
    if bbox is not None:
        x1,y1,x2,y2=bbox
        frame=cv.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
    cv.imshow('frame',frame)
    if cv.waitKey(1)==ord('q'):
        break
cap.release()
cv.destroyAllWindows()

