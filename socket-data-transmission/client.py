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


def encodeImage():
    
    with open("image.jpg", "rb") as image_file:
        print("heelo")
        data = base64.b64encode(image_file.read())
    
    return data

def send_image():
    img = encodeImage()
    sio.emit('messageFromClient',{'img': img})

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

sio.connect('http://192.168.31.255:5555')
sio.wait()