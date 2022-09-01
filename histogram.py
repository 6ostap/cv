import cv2 as cv
import numpy as np

def histEqual(img):
    imgHist = cv.imread(r'C:\Users\ostap\PycharmProjects\CVtraining\Photos\lady.jpg', 0)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    equ = cv.equalizeHist(gray)
    res = np.hstack((imgHist, equ))

    cv.imshow('histogram equalization', res)
    cv.waitKey(0)
    cv.destroyAllWindows