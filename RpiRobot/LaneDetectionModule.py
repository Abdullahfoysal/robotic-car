import cv2
import numpy as np
import utils


def getLaneCurve(img):
    imgCopy = img.copy()
    ##step 1
    imgThres = utils.thresholding(img)
    
    #step 2
    h, w, c = img.shape
    points = utils.valTrackBars()
    imgWarp = utils.warpImg(imgThres, points, w, h)
    imgWrapPoints  =utils.drawPoints(imgCopy, 
                                     points)
    cv2.imshow('Thres',imgThres)
    cv2.imshow('Wrap',imgWarp)
    cv2.imshow('Wrap points',imgWrapPoints)
        
    
    return None
    
    

if __name__ == '__main__':
    cap = cv2.VideoCapture('vid.mp4')
    initializeTrackbarVals =[102,80,20,214]
    utils.initializeTrackbars(initializeTrackbarVals)
  
    while (cap.isOpened()):
        ret, img = cap.read() 
        #cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
        #cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        
        if ret:
            img = cv2.resize(img,(480,240))
            getLaneCurve(img)
            cv2.imshow("Vid", img)
        else:
           print('no video')
           cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
           continue
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
       
    