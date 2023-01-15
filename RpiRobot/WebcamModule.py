import cv2
 
cap = cv2.VideoCapture(0)
 
def getImg(display= True,size=[480,240]):
    success, img = cap.read()
    img = cv2.resize(img,(480,240))
    if success:
        cv2.imshow('IMG',img)
    return img
 
if __name__ == '__main__':
    while True:
        img = getImg(True)
        cv2.waitKey(1)