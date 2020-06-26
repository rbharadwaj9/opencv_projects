import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    ret, img = cap.read()
    white = cv2.imread('white.png')

##img = cv2.imread('opencv-corner-detection-sample.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##print(gray)
    gray = np.float32(gray)
##print(gray)
    corners = cv2.goodFeaturesToTrack(gray, 20000, 0.01, 10)
##print(corners)
    corners = np.int0(corners)
##print(corners)

    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(white, (x,y), 3, 255, -1)

    cv2.imshow('Corner', white)
    cv2.imshow('original', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
