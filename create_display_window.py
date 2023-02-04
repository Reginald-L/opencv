import os
import cv2 as cv

'''
namedWindow(): 为窗口命名
    - winname: 窗口名
    - flags: 窗口属性
        - WINDOW_NORMAL: 允许自定义窗口大小
        - WINDOW_AUTOSIZE: 窗口大小默认和图片大小一致
imshow(): 显示窗口
    - winname: 窗口名
    - mat: 显示的图片数据

resizeWindow(窗口名, 宽, 高): 设置窗口大小, 默认为图片窗口
key = waitKey(0): 等待键盘或鼠标响应, 返回响应键, 即 key == 'q'
destoryAllWindows(): 摧毁所有的窗口, 释放窗口资源
'''

def create_window(winname,img, width=None, height=None):
    '''
    创建一个窗口
    winname: 窗口名
    width: 窗口宽
    height: 窗口高
    若width & height不为None, 那么就会对窗口进行resize
    '''
    cv.namedWindow(winname=winname, flags=cv.WINDOW_NORMAL)
    if width is not None or height is not None:
        cv.resizeWindow(winname, width, height)
    cv.imshow('My first window', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    winname = 'My first window'
    img = cv.imread('old_data/Lena.jpg')
    create_window(winname, img)