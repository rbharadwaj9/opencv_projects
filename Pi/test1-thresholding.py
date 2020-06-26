# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
 
# allow the camera to warmup
time.sleep(0.1)

feed = cv2.VideoCapture(camera)

while True:
	ret, frame = feed.read()
	grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	required_roi = grayscaled #This changes into a cropped version according to the final robot.
	
	retval, threshold = cv2.threshold(required_roi, 100, 255, cv2.THRESH_BINARY_INV)
	gauss = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 201, 1)
	gauss_mask = cv2.bitwise_not(gauss)
	
	cv2.imshow('gaussian', gauss_mask)
	cv2.imshow('original', grayscaled)
	cv2.imshow('threshold', threshold)
	
	if cv2.waitKey(5) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
feed.release()
