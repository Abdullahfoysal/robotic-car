#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 16:13:51 2023

@author: foysalmac
"""

import eventlet
import socketio
import base64
from PIL import Image
from io import BytesIO

sio = socketio.Server()
app = socketio.WSGIApp(sio)
def decodeImage(data):
    im = Image.open(BytesIO(base64.b64decode(data)))
    im.save('image2.png', 'PNG')

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def messageFromClient(sid, data):
    print('messageFromClient ', "data['img']")
    decodeImage(data['img'])
    
    #sio.emit('messageFromServer',{'gottemp': 45})

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5555)), app)