from tensorflow.keras.models import load_model
import cv2
import numpy as np
from threading import Timer
# LED IMPORT ##

import time
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import subprocess
# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)
# Display Parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5
# Display Refresh
LOOPTIME = 1.0
# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)
# Clear display.
oled.fill(0)
oled.show()
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)
font = ImageFont.truetype('PixelOperator.ttf', 16)
font1 = ImageFont.truetype('PixelOperator.ttf', 16)
#              ##

sign = [  "Speed limit (20km/h)",  "Speed limit (30km/h)",  "Speed limit (50km/h)",  "Speed limit (60km/h)",  "Speed limit (70km/h)",  "Speed limit (80km/h)",  "End of speed limit (80km/h)",  "Speed limit (100km/h)",  "Speed limit (120km/h)",  "No passing",  "No passing for vechiles over 3.5 metric tons",  "Right-of-way at the next intersection",  "Priority road",  "Yield",  "Stop",  "No vechiles",  "Vechiles over 3.5 metric tons prohibited",  "No entry",  "General caution",  "Dangerous curve to the left",  "Dangerous curve to the right",  "Double curve",  "Bumpy road",  "Slippery road",  "Road narrows on the right",  "Road work",  "Traffic signals",  "Pedestrians",  "Children crossing",  "Bicycles crossing",  "Beware of ice/snow",  "Wild animals crossing",  "End of all speed and passing limits",  "Turn right ahead",  "Turn left ahead",  "Ahead only",  "Go straight or right",  "Go straight or left",  "Keep right",  "Keep left",  "Roundabout mandatory",  "End of no passing",  "End of no passing by vechiles over 3.5 metric tons"]

imags = []
labels = []
#######################################
steeringSen = 0.70  # Steering Sensitivity
maxThrottle = 0.22  # Forward Speed %
#motor = mM.Motor(12,8,10,33,35,37) # Pin Numbers
model = load_model('/home/pi/Desktop/robotic-car/predestraint/best_model')
######################################

cap = cv2.VideoCapture(0)

def preProcess(img):
    img = img[54:120, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img / 255
    return img

def getImg(display= True,size=[480,240]):
    _, img = cap.read()
    img = cv2.resize(img,(size[0],size[1]))
    if display:
        cv2.imshow('IMG',img)
    return img

def processing(img):
    data = []
    #img_path = '/home/pi/Desktop/robotic-car/predestraint/go_ahead.png'
    #curr_img = cv2.imread(img_path)
    image_fromarray = Image.fromarray(img, 'RGB')
    resize_image = image_fromarray.resize((30, 30))
    data.append(np.array(resize_image))
    X_test = np.array(data)
    X_test = X_test / 255
    preds = np.argmax(model.predict(X_test))
    return preds

def drawText(txt):
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
    # Pi Stats Display
    draw.text((0, 16), "Road Sign : " , font=font1, fill=255)
    draw.text((0, 32), str(txt), font=font, fill=255)
    # Display image
    oled.image(image)
    oled.show()
    time.sleep(LOOPTIME)
    
if __name__ == '__main__':
    while True:
        #img = wM.getImg(True, size=[240, 120])
        #img = getImg(True)
        _, img = cap.read()
        img = cv2.resize(img,(480,280))
        #cv2.imshow('IMG',img)
        #img_path = '/home/pi/Desktop/robotic-car/predestraint/go_ahead.png'
        #curr_img = cv2.imread(img_path)
        
        value =  processing(img)
        print(sign[value])
        drawText(sign[value])
        
        cv2.waitKey(1)
