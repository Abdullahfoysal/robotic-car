import cv2
import numpy as np
import utlis

def getLaneCurve(img):
    imgThres = utlis.thresholding(img)
    cv2.imshow('Thres',imgThres)
if __name__ == '__main__':
    cap = cv2.VideoCapture('vid.mp4')
    while True:
        _, img = cap.read() # GET THE IMAGE
        img = cv2.resize(img,(640,480)) # RESIZE
        getLaneCurve(img)
        cv2.imshow("Vid",img)
        cv2.waitKey(1)