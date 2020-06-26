import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('ball.jpg')
cv2.imshow('original', img2)

#print (img2.shape)
rows,cols,channels = img2.shape

roi = img1[0:rows, 0:cols]
#cv2.imshow('roi', roi)
raw_add = cv2.add(roi, img2)
#cv2.imshow('raw_add', raw_add)

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', img2gray)

ret, mask = cv2.threshold(img2gray, 20,255, cv2.THRESH_BINARY_INV)
cv2.imshow('masked', mask)

mask_inv = cv2.bitwise_not(mask)
cv2.imshow('masked_inv', mask_inv)

img1_bg = cv2.bitwise_and(roi,roi, mask = mask_inv)
cv2.imshow('img1_bg', img1_bg)

img2_fg = cv2.bitwise_and(img2,img2, mask = mask)
cv2.imshow('img2_fg', img2_fg)

dst = cv2.add(img1_bg,img2_fg)
cv2.imshow('dst',dst)

img1[0:rows,0:cols] = dst
cv2.imshow('final', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
