import cv2 
  
cap = cv2.VideoCapture(0)
while(1):
    _, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    cv2.imshow("gray", gray)  
    ret, binary = cv2.threshold(gray,80,255,cv2.THRESH_BINARY)  
    cv2.imshow("binary", binary)  
    contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
    cv2.drawContours(img,contours,-1,(20,128,255),2)  
    cv2.imshow("img", img)  
    key=cv2.waitKey(1)
    if key == ord('q'):
    	break
