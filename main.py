import sys

import cv2 as cv

from pixel import pix
from blackAndWhite import convertToBlackAndWhite
from histogram import histEqual
from sigmenation import sigm
from thresh import thresholding
from morphological import erosion, dilation, opening, close, grad, tophat, blackHat

path = sys.argv[1]
img = cv.imread(path)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('original', img)
cv.waitKey(0)

pix(path)

convertToBlackAndWhite(img, path)

histEqual(img, path)

sigm(img)

thresholding(img)

# Morphological Transformations

erosion(gray)

dilation(gray)

opening(gray)

close(gray)

grad(gray)

tophat(gray)

blackHat(gray)