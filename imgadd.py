import cv2 as cv
import numpy as np


def show_img(winname, img):
    cv.imshow(winname, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

img = cv.imread('data/Lena.jpg')

height, width, channels = img.shape

mask_50 = np.ones((img.shape), dtype=np.uint8) * 50
mask_100 = np.ones((img.shape), dtype=np.uint8) * 100
mask_150 = np.ones((img.shape), dtype=np.uint8) * 150

# 相加
add_img_50 = img + mask_50
add_img_100 = img + mask_100
add_img_150 = img + mask_150

# add_img_50 = cv.add(img, mask_50)
# add_img_100 = cv.add(img, mask_100)
# add_img_150 = cv.add(img, mask_150)

concat_imgs_50 = np.concatenate((img, mask_50, add_img_50), axis=1)
concat_imgs_100 = np.concatenate((img, mask_100, add_img_100), axis=1)
concat_imgs_150 = np.concatenate((img, mask_150, add_img_100), axis=1)

concat_imgs = np.concatenate((concat_imgs_50, concat_imgs_100, concat_imgs_150), axis=0)

# show_img('concat_imgs', concat_imgs)
# show_img('concat_imgs_150', concat_imgs_150)

img1 = cv.imread('data/dogs.jpg')[0:img.shape[0], 0:img.shape[1]]
show_img('img1', img1)

add_img = cv.add(img, img1)
# add_img = img + img1
show_img('add_img', add_img)