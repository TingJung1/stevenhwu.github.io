import cv2
import numpy as np
def empty(v):
    pass
img=cv2.imread("trex.png")
img=cv2.resize(img,(0,0),fx=1,fy=1)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar",640,320)

cv2.createTrackbar("B Min",'TrackBar',0,255,empty)
cv2.createTrackbar("B Max",'TrackBar',255,255,empty)
cv2.createTrackbar("G Min",'TrackBar',0,255,empty)
cv2.createTrackbar("G Max",'TrackBar',255,255,empty)
cv2.createTrackbar("R Min",'TrackBar',0,255,empty)
cv2.createTrackbar("R Max",'TrackBar',255,255,empty)
while True:
    b_min=cv2.getTrackbarPos('B Min','TrackBar')
    b_max=cv2.getTrackbarPos('B Max','TrackBar')
    g_min=cv2.getTrackbarPos('G Min','TrackBar')
    g_max=cv2.getTrackbarPos('G Max','TrackBar')
    r_min=cv2.getTrackbarPos('R Min','TrackBar')
    r_max=cv2.getTrackbarPos('R Max','TrackBar')
    print(b_min,b_max,g_min,g_max,r_min,r_max)

    lower=np.array([b_min,g_min,r_min])
    upper=np.array([b_max,g_max,r_max])
    mask=cv2.inRange(img,lower,upper)
    result=cv2.bitwise_and(img,img,mask=mask)
    cv2.waitKey(1)
    cv2.imshow("img",img)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    

cv2.waitKey(0)