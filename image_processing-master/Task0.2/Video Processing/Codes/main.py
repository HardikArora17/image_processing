import cv2
import numpy as np
import os

def partA():
    cap = cv2.VideoCapture(r'C:\Users\Hardik Arora\Desktop\Task0.2\Video Processing\Videos\RoseBloom.mp4')
    cap.set(cv2.CAP_PROP_POS_MSEC,6000)      
    ret,image=cap.read()
    path = r'C:\Users\Hardik Arora\Desktop\Task0.2\Video Processing\Generated'
    cv2.imwrite(os.path.join(path , 'frame_as_6.jpg'),image)
    cap.release()


def partB():
    cap = cv2.VideoCapture(r'C:\Users\Hardik Arora\Desktop\Task0.2\Video Processing\Videos\RoseBloom.mp4')
    cap.set(cv2.CAP_PROP_POS_MSEC,6000)      
    ret,image=cap.read()
    img=image
    img[:,:,0]=0
    img[:,:,1]=0
    path = r'C:\Users\Hardik Arora\Desktop\Task0.2\Video Processing\Generated'
    cv2.imwrite(os.path.join(path , 'frame_as_6_red.jpg'),img)


partA()
partB()
