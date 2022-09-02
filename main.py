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
(thresh, blackAndWhite) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)


cv.imshow('original', img)
cv.waitKey(0)

pix(path)

convertToBlackAndWhite(img, path)

histEqual(img, path)

sigm(img)

thresholding(img)

# Morphological Transformations

erosion(blackAndWhite)

dilation(blackAndWhite)

opening(blackAndWhite)

close(blackAndWhite)

grad(blackAndWhite)

tophat(blackAndWhite)

blackHat(blackAndWhite)