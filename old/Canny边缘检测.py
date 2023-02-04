#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :Canny边缘检测.py
@说明        :Canny边缘检测一共四步:
                    1. 通过高斯滤波去除噪音点
                    2. 使用Sobel算子计算梯度和方向
                    3. 使用非极大值抑制选择最合适的边缘线
                    4. 应用双阈值去除一些不算边缘的边缘点
@时间        :2022/11/17 15:43:13
@作者        :Reggie
@版本        :1.0
'''
# 使用高斯滤波器, 平滑图像, 去掉噪音
# 计算图像中每个像素点的梯度强度和方向
# 应用非极大值抑制, 以消除边缘检测带来的杂散相应
# 应用双阈值检测来确定真实和潜在的边缘
# 通过抑制孤立的弱边缘最终完成边缘检测

import cv2 as cv
import numpy as np
import math
import matplotlib.pyplot as ptl


def show_img(name=None, img=None):
    cv.imshow(name, img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def gauss(x, y, sigma=1):
    # sigma 是标准差
    # (1 / 2*pi) e^(-(x^2 + y^2) / 2)
    return ((1 / (2 * math.pi * sigma**2)) * math.exp(-(x**2 + y**2) / (2 * sigma**2)))


# 高斯滤波
def get_gauss_kernel():
    """
    构造一个高斯核
    高斯核构造: i_s, j_s 分别是两个辅助矩阵, 分别用于存放高斯计算的 X 和 Y
    """
    gauss_kernel = np.zeros((3, 3))
    i_s = np.array([-1, 0, 1] * 3).reshape(3, 3)
    j_s = np.array([1, 0, -1] * 3).reshape(3, 3).T
    # 计算高斯值
    for i in range(3):
        for j in range(3):
            gauss_kernel[i, j] = gauss(i_s[i, j], j_s[i, j], 1.5)
    # 归一化
    gauss_sum = gauss_kernel.sum()
    for i in range(3):
        for j in range(3):
            gauss_kernel[i, j] = gauss_kernel[i, j] / gauss_sum
    print(f'gauss_kernel = {gauss_kernel}')
    return gauss_kernel


def gauss_blur(src_img, kernel):
    """
    高斯滤波
    """
    dst_img = np.zeros(shape=src_img.shape, dtype=src_img.dtype)
    X, Y = src_img.shape
    ksize = kernel.shape[0]
    x_num_steps = X - ksize + 1
    y_num_steps = Y - ksize + 1
    for i in range(x_num_steps):
        for j in range(y_num_steps):
            dst_img[i+1, j+1] = (kernel * src_img[i:i + ksize, j:j + ksize]).sum()
    
    show_img(name='guassblur_diy', img=dst_img)
    return dst_img


def norm(data):
    if data < 0:
        data = np.abs(data)
    if data > 255:
        data = 255
    return data        


def my_sobel(src_img):
    X, Y = src_img.shape
    dst_img = np.zeros(shape=src_img.shape, dtype=src_img.dtype)
    grad_degrees = np.zeros_like(dst_img)

    for i in range(1, X - 1):
        for j in range(1, Y - 1):
            # 计算梯度值
            resultx = (int(src_img[i-1, j+1]) - int(src_img[i-1, j-1])) + 2 * (int(src_img[i, j+1]) - int(src_img[i, j-1])) + (int(src_img[i+1, j+1]) - int(src_img[i+1, j-1]))
            resulty = (int(src_img[i-1, j-1]) - int(src_img[i+1, j-1])) + 2 * (int(src_img[i-1, j]) - int(src_img[i+1, j])) + (int(src_img[i-1, j+1]) - int(src_img[i+1, j+1]))
            # resultx = norm(resultx)
            # resulty = norm(resulty)
            dst_img[i, j] = np.sqrt(resultx**2 + resulty**2)
            # 计算梯度方向
            grad_degrees[i, j] = np.arctan2(np.abs(resulty), np.abs(resultx)) * 180 / np.pi
    show_img('sobel_diy', dst_img)
    return dst_img, grad_degrees


if __name__ == '__main__':
    # 读取图片
    img = cv.imread('data/dogs.jpg', cv.IMREAD_GRAYSCALE) # 512 * 512
    # 获取高斯核
    gauss_kernel = get_gauss_kernel()
    # 高斯滤波
    gauss_img = gauss_blur(img, gauss_kernel)
    # Sobel算子计算梯度
    sobel_img, grad_degrees = my_sobel(gauss_img)
    # NMS
    # NMS(sobel_img, grad_degrees)

    # sobel = cv.Sobel(src=gauss_img, ddepth=cv.CV_64F, dx=1, dy=0, ksize=3)
    # sobelx = cv.convertScaleAbs(sobel)
    # sobel = cv.Sobel(src=gauss_img, ddepth=cv.CV_64F, dx=0, dy=1, ksize=3)
    # sobely = cv.convertScaleAbs(sobel)
    # sobelxy = cv.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    # show_img(name="opencv.sobel", img=sobelxy)