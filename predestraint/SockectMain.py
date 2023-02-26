from tensorflow.keras.models import load_model
import cv2
import numpy as np
from PIL import Image
#socket start 
import eventlet
import socketio
import base64
from PIL import Image
from io import BytesIO

sio = socketio.Server()
app = socketio.WSGIApp(sio)

def processing(image):
    data = []
   # img_path = '/Users/foysalmac/Desktop/robotic-car/predestraint/processImage.png'
    #curr_img = cv2.imread(img_path)
    image_fromarray = Image.fromarray(image, 'RGB')
    resize_image = image_fromarray.resize((30, 30))
    data.append(np.array(resize_image))
    X_test = np.array(data)
    X_test = X_test / 255
    preds = np.argmax(model.predict(X_test))
   # print(preds)
    return preds

def decodeImage(data):
    im = Image.open(BytesIO(base64.b64decode(data)))
    im.save('processImage.png', 'PNG')
    return processing()


    
    

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def messageFromClient(sid, data):
    print('messageFromClient ', "data['img']")
   # value = decode64StringImage(data['img'])
    #print("prdicted: ",value)
    print(data['img'],data['len'])
    #sio.emit('messageFromServer',{'gottemp': str(value)})
    data = np.frombuffer(base64.b64decode(data['img']), np.uint8)
    decimg = cv2.imdecode(data, 1)
    result = processing(decimg)
    print(result)
    sio.emit('messageFromServer',{'gottemp': sign[result]})
    cv2.imshow("image", decimg)
    cv2.waitKey(1)
    

@sio.event
def disconnect(sid):
    print('disconnect ', sid)
    
#socket End


sign = [  "Speed limit (20km/h)",  "Speed limit (30km/h)",  "Speed limit (50km/h)",  "Speed limit (60km/h)",  "Speed limit (70km/h)",  "Speed limit (80km/h)",  "End of speed limit (80km/h)",  "Speed limit (100km/h)",  "Speed limit (120km/h)",  "No passing",  "No passing for vechiles over 3.5 metric tons",  "Right-of-way at the next intersection",  "Priority road",  "Yield",  "Stop",  "No vechiles",  "Vechiles over 3.5 metric tons prohibited",  "No entry",  "General caution",  "Dangerous curve to the left",  "Dangerous curve to the right",  "Double curve",  "Bumpy road",  "Slippery road",  "Road narrows on the right",  "Road work",  "Traffic signals",  "Pedestrians",  "Children crossing",  "Bicycles crossing",  "Beware of ice/snow",  "Wild animals crossing",  "End of all speed and passing limits",  "Turn right ahead",  "Turn left ahead",  "Ahead only",  "Go straight or right",  "Go straight or left",  "Keep right",  "Keep left",  "Roundabout mandatory",  "End of no passing",  "End of no passing by vechiles over 3.5 metric tons"]



model = load_model('/Users/foysalmac/Desktop/robotic-car/predestraint/best_model')
######################################






if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('192.168.31.168', 5557)), app)
  # while True:
        #img = wM.getImg(True, size=[240, 120])
        #img = getImg(True)
      
      
        
      #  cv2.waitKey(1)
