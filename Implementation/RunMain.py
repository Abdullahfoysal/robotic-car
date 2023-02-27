import cv2
import numpy as np
from tensorflow.keras.models import load_model

import WebcamModule as wM
import MotorModule as mM

#######################################
steeringSen = 0.70  # Steering Sensitivity
maxThrottle = 0.22  # Forward Speed %
motor = mM.Motor(12,8,10,33,35,37) # Pin Numbers
model = load_model('/home/pi/Desktop/robotic-car/Implementation/nvidiamodel.h5')
######################################

cap = cv2.VideoCapture(0)

def preProcess(img):
    img = img[54:120, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img / 255
    return img

def getImg(display= False,size=[480,240]):
    _, img = cap.read()
    img = cv2.resize(img,(size[0],size[1]))
    if display:
        cv2.imshow('IMG',img)
    return img

while True:
    img = wM.getImg(True, size=[240, 120])
    #img = getImg(True)
    
    
    img1 = np.asarray(img)
    img2 = preProcess(img1)
    img3 = np.array([img2])
    steering = float(model.predict(img3))
    cv2.putText(img, str(steering), (0, 85), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    cv2.imshow('IMG',img)
    #print(steering*steeringSen)
    #motor.move(maxThrottle,-steering*steeringSen)
    cv2.waitKey(1)
