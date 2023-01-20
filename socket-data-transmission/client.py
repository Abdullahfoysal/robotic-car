#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 16:01:44 2023

@author: foysalmac
"""

import socketio
import base64
from PIL import Image
from io import BytesIO

sio = socketio.Client()
cap = cv2.VideoCapture('vid.mp4')

def encodeImage():
    
    with open("image.jpg", "rb") as image_file:
        print("heelo")
        data = base64.b64encode(image_file.read())
    
    return data
 
def getImage():
    success, img = cap.read()
    return img

def send_image():
    
    frameCounter = 0
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0
            break
         
        img = getImage()
        img = base64.b64encode(img)
        sio.emit('messageFromClient',{'img': img})
        cv2.waitKey(1)
        
        


def send_sensor_reading():
    while True:
        sio.emit('messageFromClient',{'temp': 45})
        sio.sleep(5)

@sio.event
def connect():
    print('connection established')
    sio.start_background_task(send_image)

@sio.event
def messageFromServer(data):
    print('messageFromServer ', data)
   

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://192.168.31.168:5010')
sio.wait()