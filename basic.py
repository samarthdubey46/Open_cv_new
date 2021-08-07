import cv2 as cv

img = cv.imread('./Photos/park.jpg')
# GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Blur
blur = cv.GaussianBlur(img, (5, 5), 4)

# Canny Edges
edges = cv.Canny(blur, 100, 100)


cv.imshow('Image', edges)

cv.waitKey(0)
