import sys
import cv2 as cv

def pix(path):
    x, y = int(sys.argv[2]), int(sys.argv[3])


    img = cv.imread(path)

    # shape of the image
    print(f'Размеры: {img.shape}')

    pixel = img[x: x + 1, y: y + 1]

    # showing the pixel

    width = int(img.shape[1])
    height = int(img.shape[0])
    dim = (width, height)

    resized = cv.resize(pixel, dim, interpolation=cv.INTER_AREA)


    cv.imshow('Pixel', resized)
    cv.waitKey(0)
    cv.destroyAllWindows