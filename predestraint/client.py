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

cap = cv2.VideoCapture(0)


def getImg(display= True,size=[480,240]):
    _, img = cap.read()
    resize_frame = cv2.resize(img, dsize=(480, 240), interpolation=cv2.INTER_AREA)
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
    result, imgencode = cv2.imencode('.jpg', resize_frame, encode_param)
    data = np.array(imgencode)
    stringData = base64.b64encode(data)
    length = str(len(stringData))
    sio.emit('messageFromClient',{'img': stringData,'len': length})
    
   # img = cv2.resize(img,(size[0],size[1]))
    if display:
        cv2.imshow('IMG',img)
    return img

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
    sio.emit('messageFromClient',{'img': img})

def send_sensor_reading():
    while True:
        img = getImg(True)
        #send_image(img)
        #sio.sleep(5)
        cv2.waitKey(1)

@sio.event
def connect():
    print('connection established')
    sio.start_background_task(send_sensor_reading)

@sio.event
def messageFromServer(data):
    print('messageFromServer : prediction: ', data)
    
   

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5556')
sio.wait()

