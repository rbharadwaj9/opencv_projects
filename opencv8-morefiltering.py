import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame', frame)
    # hsv - hue sat value
    lower_blue = np.array([100,50,0])
    upper_blue = np.array([180,180,180])

    lower_red = np.array([0,150,50])
    upper_red = np.array([20,180,150])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    cv2.imshow('mask', mask)
    cv2.imshow('mask2', mask2)

    res = cv2.bitwise_and(frame,frame, mask = mask)
    cv2.imshow('res', res)

    res2 = cv2.bitwise_and(frame,frame, mask = mask2)
    cv2.imshow('res2', res2)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
