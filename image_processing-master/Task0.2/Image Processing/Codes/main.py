import cv2
import numpy as np
import os

def partA():
    import csv
   
    img1=cv2.imread(r'C:\Users\Hardik Arora\Desktop\image_processing-master\Task0.2\Image Processing\Images\bird.jpg',1)    
    img2=cv2.imread(r'C:\Users\Hardik Arora\Desktop\image_processing-master\Task0.2\Image Processing\Images\cat.jpg',1)
    img3=cv2.imread(r'C:\Users\Hardik Arora\Desktop\image_processing-master\Task0.2\Image Processing\Images\flowers.jpg',1)
    img4=cv2.imread(r'C:\Users\Hardik Arora\Desktop\image_processing-master\Task0.2\Image Processing\Images\horse.jpg',1)
    name1="bird.jpg"
    name2="cat.jpg"
    name3="flowers.jpg"
    name4="horse.jpg"
    height1,width1,channel1=img1.shape
    height2,width2,channel2=img2.shape
    height3,width3,channel3=img3.shape
    height4,width4,channel4=img4.shape

    M=int(input("enter the value of M"))
    N=int(input("enter the value of N"))
    M=int(M/2)
    N=int(N/2)
    p11,p12,p13=img1[M,N]
    p21,p22,p23=img2[M,N]
    p31,p32,p33=img3[M,N]
    p41,p42,p43=img4[M,N]
    
    with open(r'C:\Users\Hardik Arora\Desktop\image_processing-master\Task0.2\Image Processing\Generated\stats.csv','w',newline='') as f:
        
        tw=csv.writer(f)
        tw.writerow([name1,height1,width1,channel1,p11,p12,p13])
        tw.writerow([name2,height2,width2,channel2,p21,p22,p23])
        tw.writerow([name3,height3,width3,channel3,p31,p32,p33])
        tw.writerow([name4,height4,width4,channel4,p41,p42,p43]) 
    pass

def partB():
    img2=cv2.imread(r'C:\Users\Hardik Arora\Desktop\image_processing-master\Task0.2\Image Processing\Images\cat.jpg',1)
    new=img2
    new[:,:,0]=0
    new[:,:,1]=0
    cv2.imwrite
    path = r'C:\Users\Hardik Arora\Desktop\image_processing-master\Task0.2\Image Processing\Generated'
    cv2.imwrite(os.path.join(path , 'cat_red.jpg'),new)

    pass

def partC():
    img3=cv2.imread(r'C:\Users\Hardik Arora\Desktop\image_processing-master\Task0.2\Image Processing\Images\flowers.jpg',1)
    new1 = cv2.cvtColor(img3, cv2.COLOR_BGR2BGRA)
    new1[:,:,3]=128
    path = r'C:\Users\Hardik Arora\Desktop\image_processing-master\Task0.2\Image Processing\Generated'
    cv2.imwrite(os.path.join(path , 'flower_alpha.png'),new1)
    pass

def partD():
    path = r'C:\Users\Hardik Arora\Desktop\image_processing-master\Task0.2\Image Processing\Generated'
    img4=cv2.imread(r'C:\Users\Hardik Arora\Desktop\image_processing-master\Task0.2\Image Processing\Images\horse.jpg',1)
    rows,columns,ch=img4.shape
    for i in range(rows):
        for j in range(columns):
            b,g,r=img4[i,j]
            I=0.3*r+0.9*g+0.11*b
            img4[i,j]=I
    
    cv2.imwrite(os.path.join(path , 'horse_gray.jpg'),img4)
    
    pass

partA()
partB()
partC()
partD()
