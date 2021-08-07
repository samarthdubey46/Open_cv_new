import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.rectangle(blank,(0,0),(255,255),(25,123,14))
cv.circle(blank, (250, 250), 50, (124, 90, 123), thickness=-1)
cv.imshow('blank', blank)

cv.waitKey(0)
