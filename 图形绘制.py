import cv2 as cv
import numpy as np


# 创建窗口
cv.namedWindow('My blackboard', cv.WINDOW_AUTOSIZE)
board = np.zeros((1000, 1000, 3), dtype=np.uint8)

# 创建鼠标事件
def callback(event, x, y, flag, userdata=None):
    if event == cv.EVENT_LBUTTONUP:
        print(f'左键释放图形绘制结束')
    if flag == cv.EVENT_FLAG_LBUTTON and event == cv.EVENT_MOUSEMOVE:
        print(f'鼠标从点 ({x}, {y}) 开始移动')
        cv.circle(board, (x, y), 1, (255, 255, 255), 1)

cv.setMouseCallback('My blackboard', callback)

while True:
    cv.imshow('My blackboard', board)

    key = cv.waitKey(10)
    if key & 0xFF == ord('q'):
        break

cv.destroyAllWindows()

