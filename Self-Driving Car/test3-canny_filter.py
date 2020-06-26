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

    kernel = np.ones((15,15), np.float32)/225
    median = cv2.medianBlur(threshold, 35)

    edges = cv2.Canny(median, 100, 100)

    #cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('gaussian', gauss_mask)
    cv2.imshow('original', grayscaled)
    cv2.imshow('threshold', threshold)
    cv2.imshow('edges', edges)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
feed.release()

