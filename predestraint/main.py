import cv2
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

#import WebcamModule as wM
#import MotorModule as mM
imags = []
labels = []
#######################################
steeringSen = 0.70  # Steering Sensitivity
maxThrottle = 0.22  # Forward Speed %
#motor = mM.Motor(12,8,10,33,35,37) # Pin Numbers
model = load_model('/home/pi/Desktop/robotic-car/predestraint/best_model')
######################################

cap = cv2.VideoCapture('vid.mp4')

def preProcess(img):
    img = img[54:120, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img / 255
    return img

def getImg(display= True,size=[480,240]):
    #_, img = cap.read()
    img_path = '/home/sifat/Downloads/robotic-car-sifat_dev/predestraint/predestran.jpg'
    curr_img = cv2.imread(img_path)
    gray_img = cv2.resize(curr_img, (size[0],size[1]))
    gray_img = np.array(gray_img, dtype='float32')
    gray_img = gray_img / 255
    #img = cv2.resize(img,(size[0],size[1]))
    if display:
        cv2.imshow('IMG',curr_img)
        cv2.imshow('IMG_Gray', gray_img)
    #imags.append(curr_img)
    return curr_img
def processing():
    data = []
    img_path = '/home/pi/Desktop/robotic-car/predestraint/go_ahead.png'
    curr_img = cv2.imread(img_path)
    image_fromarray = Image.fromarray(curr_img, 'RGB')
    resize_image = image_fromarray.resize((30, 30))
    data.append(np.array(resize_image))
    X_test = np.array(data)
    X_test = X_test / 255
    preds = np.argmax(model.predict(X_test))
    print(preds)
while True:

    #img = wM.getImg(True, size=[240, 120])
    #img = getImg(True, size=[200, 200])
    processing()
    #  labels = pd.DataFrame(labels)
    #labels = np.array(labels, dtype='int32')
    #img = np.asarray(img)
    #img = preProcess(img)
    #img = np.array([img])
    #steering = float(model.predict(img))
    #print(steering*steeringSen)
    #motor.move(maxThrottle,-steering*steeringSen)
    cv2.waitKey(1)
