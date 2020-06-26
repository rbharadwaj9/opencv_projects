import cv2
import numpy as np
import io
import picamera

#Create a memory stream so photos doesn't need to be saved in a file
stream = io.BytesIO()

#Get the picture (low resolution, so it should be quite fast)
#Here you can also specify other parameters (e.g.:rotate the image)
with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.capture(stream, format='jpeg')

#Convert the picture into a numpy array
buff = np.fromstring(stream.getvalue(), dtype=np.uint8)

#Now creates an OpenCV image
image = cv2.imdecode(buff, 1)

#IMREAD_COLOR - 1
#IMREAD_UNCHANGED = -1
#IMREAD_GRAYSCALE = 0


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('gray.jpg', gray)
