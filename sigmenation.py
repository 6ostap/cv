import cv2 as cv

def sigm(img):
    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    hsv_img = cv.cvtColor(rgb_img, cv.COLOR_RGB2HSV)
    cv.imshow('hsb', hsv_img)

    light_orange = (1, 190, 200)
    dark_orange = (18, 255, 255)

    mask = cv.inRange(hsv_img, light_orange, dark_orange)

    result = cv.bitwise_and(img, img, mask=mask)
    cv.imshow('result', result)




    cv.waitKey(0)
    cv.destroyAllWindows()