import cv2 as cv
import numpy as np


def show_img(title=None, img=None):
    cv.imshow(title, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

img = cv.imread('data/Lena.jpg', cv.IMREAD_COLOR)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 图像二值化
_, img_binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
# show_img('Lena', img_binary)

contours, hierarchy = cv.findContours(img_binary, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

# 绘制轮廓
draw_img = img.copy()
result = cv.drawContours(image=draw_img, contours=contours, contourIdx=-1, color=(0, 0, 255), thickness=2)
show_img('contours', result)