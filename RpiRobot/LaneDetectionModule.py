import cv2
import numpy as np
import utlis

def getLaneCurve(img):
    imgCopy = img.copy()
    ## step 1
    imgThres = utlis.thresholding(img)
    cv2.imshow('Thres',imgThres)
    
    ## step 2
    h,w,c = img.shape
    points = utlis.valTrackbars()
    
    imgWarp = utlis.warpImg(imgThres,points,w,h)
    cv2.imshow('Warp',imgWarp)
    
    imgWarpPoints = utlis.drawPoints(imgCopy,points)
    cv2.imshow('Warp Points',imgWarpPoints)
    return None

if __name__ == '__main__':
    cap = cv2.VideoCapture('vid.mp4')
    intialTracbarVals = [142,83,79,240]
    utlis.initializeTrackbars(intialTracbarVals)
    frameCounter = 0
    while True:
        frameCounter +=1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) ==frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES,0)
            frameCounter=0
            
        _, img = cap.read() # GET THE IMAGE
        img = cv2.resize(img,(640,480)) # RESIZE
        getLaneCurve(img)
        cv2.imshow("Vid",img)
        cv2.waitKey(1)

