import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
   # img=cv2.imread('C:/Users/Lenovo/Desktop/color.jpeg')
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
 

    red_lower=np.array([136,87,111],np.uint8)
    red_upper=np.array([180,255,255],np.uint8)

    blue_lower=np.array([78,158,124],np.uint8)
    blue_upper=np.array([138,255,255],np.uint8)
	
    yellow_lower=np.array([22,60,200],np.uint8)
    yellow_upper=np.array([60,255,255],np.uint8)

    green_lower=np.array([40,100,100],np.uint8)
    green_upper=np.array([80,255,255],np.uint8)

    red=cv2.inRange(hsv, red_lower, red_upper)
    blue=cv2.inRange(hsv,blue_lower,blue_upper)
    yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
    green=cv2.inRange(hsv,green_lower,green_upper)
    	
    kernal = np.ones((5 ,5), "uint8")

    red=cv2.dilate(red, kernal)
    res=cv2.bitwise_and(img, img, mask = red)

    blue=cv2.dilate(blue,kernal)
    res1=cv2.bitwise_and(img, img, mask = blue)

    yellow=cv2.dilate(yellow,kernal)
    res2=cv2.bitwise_and(img, img, mask = yellow)  

    green=cv2.dilate(green,kernal)
    res3=cv2.bitwise_and(img, img, mask = green)    

    contours,hierarchy=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
		
            x,y,w,h= cv2.boundingRect(contour)	
            img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
            cv2.putText(img,"RED color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
			
	#Tracking the Blue Color
    contours,hierarchy=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
		
            x,y,w,h= cv2.boundingRect(contour)	
            img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
            cv2.putText(img,"blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
			
        
	#Tracking the yellow Color
    contours,hierarchy=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
		
            x,y,w,h= cv2.boundingRect(contour)	
            img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
            cv2.putText(img,"yellow color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))
			


    contours,hierarchy=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
		
            x,y,w,h= cv2.boundingRect(contour)	
            img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
            cv2.putText(img,"green color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
			
            
    cv2.imshow("Color Tracking",img)
    if cv2.waitKey(1)==13:
        break
cap.release(0)
cv2.waitKey(0)
cv2.destroyAllWindows()
    		