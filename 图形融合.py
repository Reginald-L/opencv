import cv2 as cv
import numpy as np


img1 = cv.imread('data/Lena.jpg')
img2 = cv.imread('data/dogs.jpg')[500 : 500 + img1.shape[0], 500 : 500 + img1.shape[1]]

out = cv.addWeighted(img1, 0.7, img2, 0.5, 0)

def show_img(winname, img):
    cv.imshow(winname, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

show_img('图像融合', out)