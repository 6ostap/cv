import cv2 as cv
import numpy as np

def histEqual(img, path):
    imgHist = cv.imread(path, 0)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    equ = cv.equalizeHist(gray)
    res = np.hstack((imgHist, equ))

    cv.imshow('histogram equalization', res)
    cv.waitKey(0)
    cv.destroyAllWindows