#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 16:01:44 2023

@author: foysalmac
"""
import cv2
import numpy as np
import socketio
import base64
from PIL import Image
from io import BytesIO

# LED #

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

#     #

def drawText(txt):
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
    # Pi Stats Display
    draw.text((0, 16), "Road Sign : " , font=font1, fill=255)
    draw.text((0, 32), str(txt), font=font, fill=255)
    # Display image
    oled.image(image)
    oled.show()
    time.sleep(LOOPTIME)

cap = cv2.VideoCapture(0)


def getImg(display= True,size=[480,240]):
    _, img = cap.read()
    resize_frame = cv2.resize(img, dsize=(480, 240), interpolation=cv2.INTER_AREA)
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
    result, imgencode = cv2.imencode('.jpg', resize_frame, encode_param)
    data = np.array(imgencode)
    stringData = base64.b64encode(data)
    length = str(len(stringData))
    
    
   # img = cv2.resize(img,(size[0],size[1]))
    #if display:
    #cv2.imshow('IMG',img)
    return stringData,length

sio = socketio.Client()


def encodeImageFromLocal():
    with open("go_ahead.png", "rb") as image_file:
        print("heelo")
        data = base64.b64encode(image_file.read())
    
    return data

def encodedImage(img):
    data = base64.b64encode(img)
    return data

def send_image(img):
    
    img = encodedImage(img)
    #img =encodeImageFromLocal()
    sio.emit('messageFromClient',{'img': img})

def send_sensor_reading():
    while True:
        stringData,length=getImg(True)
        #send_image(img)
        sio.emit('messageFromClient',{'img': stringData,'len': length})
        #sio.sleep(1)
        cv2.waitKey(1)

@sio.event
def connect():
    print('connection established')
    sio.start_background_task(send_sensor_reading)

@sio.event
def messageFromServer(data):
    print('messageFromServer : prediction: ', data)
    drawText(data["gottemp"])
    
   

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://192.168.31.89:5557')
sio.wait()

