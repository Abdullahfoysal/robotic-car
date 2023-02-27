import cv2

cap = cv2.VideoCapture(0)

def getImg(display= False,size=[480,240],steering=0):
    _, img = cap.read()
    img = cv2.resize(img,(size[0],size[1]))
    #cv2.putText(img, str(steering), (0, 85), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    #if display:
    #    cv2.imshow('IMG',img)
    return img

if __name__ == '__main__':
    while True:
        img = getImg(True)
        cv2.waitKey(1)