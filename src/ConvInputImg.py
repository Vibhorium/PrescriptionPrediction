# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:21:17 2019

@author: vibho
"""
import os
import numpy as np
import cv2
from PIL import Image
def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)
    return img.point(contrast)
path=os.getcwd()
#os.setcwd('C:/Users/vibho/Desktop/BTP SEM 7/WordSegmentation/data')
#temp=Image.open(path+'\\2.png')
#temp = cv2.imread('../data/85.png')
 
#dimensions = temp.shape
 
#print(temp.shape[0],temp.shape[1])
dim=(1700,170)


#img.save('../data/84.png')
#cv2.imwrite('../data/84.png', img)
#img.show()
"""
def change_contrast_multi(img, steps):
    width, height = img.size
    canvas = Image.new('RGB', (width * len(steps), height))
    for n, level in enumerate(steps):
        img_filtered = change_contrast(img, level)
        canvas.paste(img_filtered, (width * n, 0))
    return canvas
"""
#Img=change_contrast_multi(Image.open('in3.jpg'), [-100, 0, 100, 200, 300])
#Img.show()
# read
img=change_contrast(Image.open('in3.jpg'), 100)
# increase contrast
pxmin = np.min(img)
pxmax = np.max(img)
imgContrast = (img - pxmin) / (pxmax - pxmin) * 255

# increase line width
kernel = np.ones((3, 3), np.uint8)
imgMorph = cv2.erode(imgContrast, kernel, iterations = 1)
imgMorph=cv2.resize(imgMorph,dim,interpolation = cv2.INTER_AREA)
# write
print(imgMorph.shape[0],imgMorph.shape[1])
cv2.imwrite('../data/88.png', imgMorph)
