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


pix(path)

convertToBlackAndWhite(img, path)

histEqual(img)

sigm(img)

thresholding(img)

# Morphological Transformations

erosion(img)

dilation(img)

opening(img)

close(img)

grad(img)

tophat(img)

blackHat(img)