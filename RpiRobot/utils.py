import cv2
import numpy as np
  
def thresholding(img):
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerWhite = np.array([80,0,0])
    upperWhite =np.array([255,160,255])
    maskWhite = cv2.inRange(imgHsv,lowerWhite,upperWhite)
    
    return maskWhite


def warpImg(img,points,w,h):
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgWarp = cv2.warpPerspective(img,matrix,(w,h))
    return imgWarp

def nothing():
    pass

def initializeTrackbars(initializeTrackbarsVals,wT=480,hT =240):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Width Top","Trackbars",initializeTrackbarsVals[0],wT//2,nothing)
    cv2.createTrackbar("Height Top","Trackbars",initializeTrackbarsVals[1],hT,nothing)
    cv2.createTrackbar("Width Bottom","Trackbars",initializeTrackbarsVals[2],wT//2,nothing)
    cv2.createTrackbar("Height Bottom","Trackbars",initializeTrackbarsVals[3],hT,nothing) 

def valTrackBars(wT=480,hT=240):
    
    widthTop = cv2.getTrackbarPos("Width Top", "Trackbars")
    heightTop = cv2.getTrackbarPos("Height Top", "Trackbars")
    widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
    heightBottom = cv2.getTrackbarPos("Height Bottom", "Trackbars")
    points = np.float32([(widthTop, heightTop), (wT-widthTop, heightTop),
                      (widthBottom , heightBottom ), (wT-widthBottom, heightBottom)])
    return points

def drawPoints(img,points):
    for x in range(4):
        cv2.circle(img,(int(points[x][0]),int(points[x][1])),15,(0,0,255),cv2.FILLED)
    return img






