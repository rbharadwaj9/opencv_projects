import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #cv2.imshow('frame', frame)
    # hsv - hue sat value
    
    lower_red = np.array([0,120,30])
    upper_red = np.array([10,255,255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask = mask)

    kernel = np.ones((15,15), np.float32)/225
    #smoothed= cv2.filter2D(res, -1, kernel)

    #blur = cv2.GaussianBlur(res, (15,15),0)
    median = cv2.medianBlur(res, 15)
    #bilateral = cv2.bilateralFilter(res, 15,75, 75)

    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    #cv2.imshow('smoothed', smoothed)
    #cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    #cv2.imshow('bilateral', bilateral)
    


##    lower_blue = np.array([100,50,0])
##    upper_blue = np.array([255,255,255])
##    mask2 = cv2.inRange(hsv, lower_blue, upper_blue)
##    cv2.imshow('mask2', mask2)
##    res2 = cv2.bitwise_and(frame,frame, mask = mask2)
##    cv2.imshow('res2', res2)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
