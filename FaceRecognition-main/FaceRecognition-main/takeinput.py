import cv2
import os
import keyboard

import random
import numpy as np
from matplotlib import pyplot as plt
INPUT_PATH = os.path.join('data', 'image')
name=input("Nhap ten: ");
import time
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Không thể mở camera")
    exit()
while cap.isOpened(): 
    ret, frame = cap.read()
    # Cut down frame to 250x250px
    frame = frame[120:120+250,200:200+250, :]
    if not ret:
        print("Không thể nhận dữ liệu từ camera")
        break      
    count =0
    
    if cv2.waitKey(1) & 0XFF == ord('s'):
        for i in range(1000):         
            print("đang chụp tấm ảnh thứ"+str(count))
            count+=1;
            time.sleep(0.3)#0.1 giây +1 bức
            if count >0 and count <10:
                ret, frame = cap.read()
                frame = frame[120:120+250,200:200+250, :]
                cv2.imshow('Image Collection', frame)
                imgname = os.path.join(INPUT_PATH, str(name)+'_00H0'+str(count)+'.jpg')
                cv2.imwrite(imgname, frame)
            if count >9 and count <100:
                ret, frame = cap.read()
                frame = frame[120:120+250,200:200+250, :]
                cv2.imshow('Image Collection', frame)
                imgname = os.path.join(INPUT_PATH, str(name)+'_00'+str(count)+'.jpg')
                cv2.imwrite(imgname, frame)
            if count >99 and count <1001:
                ret, frame = cap.read()
                frame = frame[120:120+250,200:200+250, :]
                cv2.imshow('Image Collection', frame)
                imgname = os.path.join(INPUT_PATH, str(name)+'_0'+str(count)+'.jpg')
                cv2.imwrite(imgname, frame)
    cv2.imshow('Image Collection', frame)
    if cv2.waitKey(1) & 0XFF == ord('b'):
        break
# Release the webcam
cap.release()
# Close the image show frame
cv2.destroyAllWindows()