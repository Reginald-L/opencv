import cv2 as cv
import numpy as np


def show_img(winname, img):
    cv.imshow(winname, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

# loading lena
img = cv.imread('data/Lena.jpg')
# mask
mask = np.zeros(img.shape, dtype=np.uint8)
mask[100 : 400, 100 : 400] = 255
# bitwise_and
out = cv.bitwise_and(img, mask)

concat_img = np.concatenate((img, mask, out), axis=1)
show_img('concat_img', concat_img)
