import cv2 as cv
import numpy as np

# 创建窗口
cv.namedWindow('trackbar_win', flags=cv.WINDOW_NORMAL)
# 创建trackbar
cv.createTrackbar('R', 'trackbar_win', 0, 255, lambda x: None)
cv.createTrackbar('G', 'trackbar_win', 0, 255, lambda x: None)
cv.createTrackbar('B', 'trackbar_win', 0, 255, lambda x: None)

img = np.zeros((500, 600, 3), dtype=np.uint8)

while True:
    # 获取trackBar的值
    r = cv.getTrackbarPos('R', 'trackbar_win')
    g = cv.getTrackbarPos('G', 'trackbar_win')
    b = cv.getTrackbarPos('B', 'trackbar_win')

    # 修改背景
    img[:] = [b, g, r]

    # 显示窗口
    cv.imshow('trackbar_win', img)
    key = cv.waitKey(10)
    if key & 0xFF == ord('q'):
        break
    
cv.destroyAllWindows()