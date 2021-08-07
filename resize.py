import cv2 as cv
import numpy as np
img = cv.imread('./Photos/cat.jpg')
def resize(frame,scale=0.75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    return cv.resize(frame,(300,300),interpolation=cv.INTER_AREA)

#
# cpt = cv.VideoCapture(0)
# while True:
#     true,frame = cpt.read()
#     cv.imshow('v',resize(frame))
#     if cv.waitKey(20) and 0xFF == ord('d'):
#         break

print(img)

cv.imshow('Image',resize(img))
cv.waitKey(0)
# cpt.release()
# cv.destroyAllWindows()
