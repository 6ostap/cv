import cv2 as cv
import numpy as np

# Morphological Transformations


# erosion
def erosion(img):
    kernel = np.ones((5,5),np.uint8)
    erosion = cv.erode(img,kernel,iterations=1)
    cv.imshow('erosion', erosion)
    cv.waitKey(0)
    cv.destroyAllWindows()

# dilation
def dilation(img):
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv.dilate(img,kernel,iterations = 1)
    cv.imshow('dilation', dilation)
    cv.waitKey(0)
    cv.destroyAllWindows()

# opening
def opening(img):
    kernel = np.ones((5, 5), np.uint8)
    opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
    cv.imshow('opening', opening)
    cv.waitKey(0)
    cv.destroyAllWindows()

# closing
def close(img):
    kernel = np.ones((5, 5), np.uint8)
    closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
    cv.imshow('closing', closing)
    cv.waitKey(0)
    cv.destroyAllWindows()

# gradient
def grad(img):
    kernel = np.ones((5, 5), np.uint8)
    gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
    cv.imshow('gradient',gradient)
    cv.waitKey(0)
    cv.destroyAllWindows()

# tophat
def tophat(img):
    kernel = np.ones((5, 5), np.uint8)
    tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
    cv.imshow('tophat', tophat)
    cv.waitKey(0)
    cv.destroyAllWindows()

# Black Hat
def blackHat(img):
    kernel = np.ones((5, 5), np.uint8)
    blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
    cv.imshow('blackhat', blackhat)
    cv.waitKey(0)
    cv.destroyAllWindows()

