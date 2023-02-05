import cv2 as cv
import numpy as np


img = np.zeros((500, 500), dtype=np.uint8)
img[100:300, 100:300] = 255

# 非运算
not_img = cv.bitwise_not(img)
concat_not_img = np.concatenate((img, not_img), axis=1)
# cv.imshow('concat_not_img', concat_not_img)

# 与操作

img1 = np.zeros((500, 500), dtype=np.uint8)
img1[200 : 400, 200 : 400] = 255
# and_img = cv.bitwise_and(img, img1)
# concat_and_img = np.concatenate((img, img1, and_img), axis=1)
# cv.imshow('concat_and_img', concat_and_img)

# 或 or
# or_img = cv.bitwise_or(img, img1)
# concat_or_img = np.concatenate((img, img1, or_img), axis=1)
# cv.imshow('concat_and_img', concat_or_img)

# 异或 xor
xor_img = cv.bitwise_xor(img, img1)
concat_xor_img = np.concatenate((img, img1, xor_img), axis=1)
cv.imshow('concat_and_img', concat_xor_img)

cv.waitKey(0)
cv.destroyAllWindows()
