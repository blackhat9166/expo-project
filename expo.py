import cv2
import time
import math
import datetime
import keyboard


    

h = 1
w = 1
n = 1
cap = cv2.VideoCapture(0)
i_time = 0
p_time = 0

while True:
    ret, frame = cap.read()

    font = cv2.FONT_HERSHEY_COMPLEX

    i_time = time.time()
    fps = int(1/(i_time-p_time))
    p_time = i_time
    fps = "fps = " + str(fps) + "  zoom ="+str(n)


    img = cv2.line(frame, (0,240), (640,240), (0,0,0),thickness=1, lineType=8)
    img = cv2.line(frame, (320, 0), (320, 480), (0, 0, 0), thickness=1, lineType=8)
    img = cv2.line(frame, (320, 240+n*h), (640, 240+n*h), (255, 0, 0), thickness=1, lineType=8)
    img = cv2.line(frame, (320+n*w, 240), (320+n*w, 480), (255, 0, 0), thickness=1, lineType=8)
    img = cv2.putText(img, fps, (5, 50), font, 1, (100, 255, 0), 1, cv2.LINE_AA)
    img = cv2.resize(img,(1200,800))
    
    if keyboard.is_pressed("z"):
     n += 2
    elif keyboard.is_pressed("o"):
     n -= 1
    cv2.imshow("video", img)
    

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

