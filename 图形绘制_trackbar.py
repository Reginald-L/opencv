import cv2 as cv
import numpy as np


# 创建窗口
cv.namedWindow('My blackboard', cv.WINDOW_AUTOSIZE)
board = np.zeros((1000, 1000, 3), dtype=np.uint8)

# 添加画笔 Trackbar
# 目标是设置画笔的颜色
cv.createTrackbar('pen_R', 'My blackboard', 255, 255, lambda x:None)
cv.createTrackbar('pen_G', 'My blackboard', 255, 255, lambda x:None)
cv.createTrackbar('pen_B', 'My blackboard', 255, 255, lambda x:None)


# pen_color = (255, 255, 255)

# 创建鼠标事件
def callback(event, x, y, flag, userdata=None):
    print(event)
    if event == cv.EVENT_LBUTTONUP:
        print(f'左键释放图形绘制结束')
    if flag == cv.EVENT_FLAG_LBUTTON and event == cv.EVENT_MOUSEMOVE:
        print(f'鼠标从点 ({x}, {y}) 开始移动')
        cv.circle(board, (x, y), 1, pen_color, 1)

cv.setMouseCallback('My blackboard', callback)

while True:
    # 获取画笔
    pen_r = cv.getTrackbarPos('pen_R', 'My blackboard')
    pen_g = cv.getTrackbarPos('pen_G', 'My blackboard')
    pen_b = cv.getTrackbarPos('pen_B', 'My blackboard')

    pen_color = (pen_b, pen_g, pen_r)

    cv.imshow('My blackboard', board)

    key = cv.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cv.destroyAllWindows()

