import cv2 as cv

video = cv.VideoCapture('old_data/test.mp4')
# 判断视频是否被正确加载
if video.isOpened():
    open, frame = video.read()
else:
    open = False
# 循环读取视频帧数
while True:
    ret, frame = video.read() # ret的目的是告诉我们是否读取成功， True / False
    if frame is None:
        break
    if ret == True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('result', gray)
        if cv.waitKey(10) & 0xFF == 27: # 0xFF == ord('q') 
            break
video.release()
cv.destroyAllWindows()