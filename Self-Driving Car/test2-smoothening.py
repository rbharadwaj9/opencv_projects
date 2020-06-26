import cv2
import numpy as np

feed = cv2.VideoCapture(0)

while True:
    ret, frame = feed.read()
    grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    required_roi = grayscaled #This changes into a cropped version according to the final robot.

    retval, threshold = cv2.threshold(required_roi, 100, 255, cv2.THRESH_BINARY_INV)
    gauss = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 201, 1)
    gauss_mask = cv2.bitwise_not(gauss)

##    kernel = np.ones((5,5), np.uint8)
##    #erosion = cv2.erode(threshold, kernel, iterations = 1)
##    #dilation = cv2.dilate(threshold, kernel, iterations = 1)
##
##    #opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
##    closing = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)
##    
##    #cv2.imshow('erosion', erosion)
##    #cv2.imshow('dilation', dilation)
##    #cv2.imshow('opening', opening)
##    cv2.imshow('closing', closing)

    kernel = np.ones((15,15), np.float32)/225
    #smoothed= cv2.filter2D(threshold, -1, kernel)

    #blur = cv2.GaussianBlur(threshold, (15,15),0)
    median = cv2.medianBlur(threshold, 45)
    #bilateral = cv2.bilateralFilter(threshold, 15,75, 75)

    #cv2.imshow('smoothed', smoothed)
    #cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    #cv2.imshow('bilateral', bilateral)
    
    cv2.imshow('gaussian', gauss_mask)
    cv2.imshow('original', grayscaled)
    cv2.imshow('ththresholdhold', threshold)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
feed.release()
