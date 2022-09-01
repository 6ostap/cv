import cv2 as cv
import re

def convertToBlackAndWhite(img, path):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    (thresh, blackAndWhite) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

    cv.imshow('Black and white', blackAndWhite)

    cv.waitKey(0)
    cv.destroyAllWindows





    # saving
    newPath = path

    clear = re.compile(r'\\\w+.\w+$')
    newPath = clear.sub(r'\\blackAndWhite.jpg', newPath)
    cv.imwrite(newPath, blackAndWhite)

