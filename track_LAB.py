import cv2
import numpy as np
def empty(v):
    pass
img=cv2.imread("2.jpg")
img=cv2.resize(img,(0,0),fx=0.1,fy=0.1)
lab=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)


cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar",640,320)

cv2.createTrackbar("L Min",'TrackBar',0,100,empty)
cv2.createTrackbar("L Max",'TrackBar',100,100,empty)
cv2.createTrackbar("A Min",'TrackBar',0,255,empty)
cv2.createTrackbar("A Max",'TrackBar',255,255,empty)
cv2.createTrackbar("B Min",'TrackBar',0,255,empty)
cv2.createTrackbar("B Max",'TrackBar',255,255,empty)
while True:
    l_min=cv2.getTrackbarPos('L Min','TrackBar')
    l_max=cv2.getTrackbarPos('L Max','TrackBar')
    a_min=cv2.getTrackbarPos('A Min','TrackBar')
    a_max=cv2.getTrackbarPos('A Max','TrackBar')
    b_min=cv2.getTrackbarPos('B Min','TrackBar')
    b_max=cv2.getTrackbarPos('B Max','TrackBar')
    print(l_min,l_max,a_min,a_max,b_min,b_max)

    lower=np.array([l_min,a_min,b_min])
    upper=np.array([l_max,a_max,b_max])
    mask=cv2.inRange(lab,lower,upper)
    result=cv2.bitwise_and(img,img,mask=mask)
    cv2.waitKey(1)
    cv2.imshow("img",img)
    cv2.imshow("lab",lab)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    

cv2.waitKey(0)