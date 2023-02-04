import cv2
#读取图片
img = cv2.imread('data/cell.jpg')
#灰度化处理
GrayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#通过阈值抑制，来去除背景部分
ret,thresh = cv2.threshold(GrayImage,50,255,cv2.THRESH_BINARY)
#查找物体的轮廓
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#画出检测得到的轮廓
cv2.drawContours(img,contours,-1,(0,0,255),2)
#可视化
cv2.imshow("Image", img)
cv2.imshow("GrayImage_thresh", thresh)
cv2.waitKey()
cv2.destroyAllWindows()
