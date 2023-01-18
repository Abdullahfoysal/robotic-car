import cv2
import utlis 
cap = cv2.VideoCapture('vid.mp4')
 
def getImg(display= True,size=[480,240]):
    success, img = cap.read()
    img = cv2.resize(img,(480,240))
    return img
 
if __name__ == '__main__':
    intialTrackBarVals = [155, 80, 46, 240 ]
    utlis.initializeTrackbars(intialTrackBarVals)
    frameCounter = 0
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0
        img = getImg(True)
        #cv2.waitKey(1)