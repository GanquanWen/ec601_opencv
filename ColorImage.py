#Copyright 2017 Ganquan Wen wengq@bu.edu

import cv2
import numpy as np
import sys

#Mat src
src = cv2.imread(sys.argv[1], 1)
cv2.namedWindow( "Original image", cv2.WINDOW_AUTOSIZE )
cv2.imshow( "Original image", src)

b, r, g = cv2.split(src)
cv2.imshow( "blue", b)
cv2.imwrite( "blue_"+sys.argv[1], b)
cv2.imshow( "red", r)
cv2.imwrite( "red_"+sys.argv[1], r)
cv2.imshow( "green", g)
cv2.imwrite( "green_"+sys.argv[1], g)
print("BRG:", src[20, 25])

ycrcb_image = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
y, cr, cb = cv2.split(ycrcb_image)
cv2.imshow( "y", y)
cv2.imwrite( "y_"+sys.argv[1], y)
cv2.imshow( "cr", r)
cv2.imwrite( "cr_"+sys.argv[1], cr)
cv2.imshow( "cb", g)
cv2.imwrite( "cb_"+sys.argv[1], cb)
print("YCrCb:", ycrcb_image[20, 25])

hsv_image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_image)
cv2.imshow( "h", h)
cv2.imwrite( "h_"+sys.argv[1], h)
cv2.imshow( "s", s)
cv2.imwrite( "s_"+sys.argv[1], s)
cv2.imshow( "v", v)
cv2.imwrite( "v_"+sys.argv[1], v)
print("HSV:", hsv_image[20, 25])
