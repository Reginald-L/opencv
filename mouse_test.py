import cv2 as cv

cv.namedWindow('mouse win', cv.WINDOW_NORMAL)

def callback(event, x, y, flags, userdata=None):
    if event == cv.EVENT_MOUSEMOVE:
        print('move')
    if event == cv.EVENT_LBUTTONDOWN:
        print('左键按下')
    if event == cv.EVENT_LBUTTONUP:
        print('左键释放')
    if event == cv.EVENT_RBUTTONDOWN:
        print('右键按下')
    if event == cv.EVENT_RBUTTONUP:
        print('右键释放')
    if event == cv.EVENT_MBUTTONDOWN:
        print('中键按下')
    if event == cv.EVENT_MBUTTONUP:
        print('中键释放')
    if event == cv.EVENT_LBUTTONDBLCLK:
        print('左键双击')
    if event == cv.EVENT_RBUTTONDBLCLK:
        print('右键双击')
    if event == cv.EVENT_MBUTTONDBLCLK:
        print('中键双击')

# 参数: winname, callback, userdata(默认为None)
cv.setMouseCallback('mouse win', callback)


cv.imshow('trackbar_win', 0)
key = cv.waitKey(0)
cv.destroyAllWindows()