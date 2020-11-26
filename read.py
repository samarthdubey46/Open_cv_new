import cv2 as cv
# s = cv.imread('')
capture = cv.VideoCapture('./Videos/dog.mp4')
while True:
    isTrue,frame = capture.read()
    cv.imshow('v',frame)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break
# cv.waitKey(0)
capture.release()
cv.destroyAllWindows()
