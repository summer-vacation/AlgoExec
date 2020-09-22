# -*- coding: utf-8 -*-
"""
File Name:    utils.py
Author :      jynnezhang
Date:         2020/5/12 3:41 下午
Description:

opencv的基础使用
"""

import cv2

img = cv2.imread(r"data/temp.png")
cv2.imshow("img", img)

# 灰度图
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grey", img_gray)

# cv2.THRESH_BINARY:     小于阈值的像素置为0，大于阈值的置为maxval
# cv2.THRESH_BINARY_INV： 小于阈值的像素置为maxval，大于阈值的置为0
# cv2.THRESH_TRUNC：      小于阈值的像素不变，大于阈值的置为thresh
# cv2.THRESH_TOZERO       小于阈值的像素置0，大于阈值的不变
# cv2.THRESH_TOZERO_INV   小于阈值的不变，大于阈值的像素置0
ret, img_threshold = cv2.threshold(img_gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY)        # 二值化
cv2.imshow("threshold", img_threshold)

# 通道分离，输出三个单通道图片
b, g, r = cv2.split(img)  # 将彩色图像分割成3个通道
cv2.imshow("blue", b)
cv2.imshow("green", g)
cv2.imshow("red", r)

# shape
# rows(height), cols(width), channels
print(img.shape)

key = cv2.waitKey(0)
if key == 27:     # 按esc键时，关闭所有窗口
    cv2.destroyAllWindows()
