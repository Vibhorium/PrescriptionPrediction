{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from __future__ import division\n",
    "from __future__ import print_function\n",
    "\n",
    "import sys\n",
    "import argparse\n",
    "import cv2\n",
    "import editdistance\n",
    "from DataLoader import DataLoader, Batch\n",
    "from Model import Model, DecoderType\n",
    "from SamplePreprocessor import preprocess\n",
    "import os\n",
    "import numpy as np\n",
    "from PIL import Image\n",
    "from WordSegmentation import wordSegmentation, prepareImg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Removing noise, improving contrast\n",
    "def change_contrast(img, level):\n",
    "    factor = (259 * (level + 255)) / (255 * (259 - level))\n",
    "\n",
    "    def contrast(c):\n",
    "        return 128 + factor * (c - 128)\n",
    "\n",
    "    return img.point(contrast)\n",
    "\n",
    "\n",
    "def convInputImg2(img):\n",
    "    # cv2.imshow(\"img\",img)\n",
    "\n",
    "    # -----Converting image to LAB Color model-----------------------------------\n",
    "    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)\n",
    "    # cv2.imshow(\"lab\",lab)\n",
    "\n",
    "    # -----Splitting the LAB image to different channels-------------------------\n",
    "    l, a, b = cv2.split(lab)\n",
    "    # cv2.imshow('l_channel', l)\n",
    "    # cv2.imshow('a_channel', a)\n",
    "    # cv2.imshow('b_channel', b)\n",
    "\n",
    "    # -----Applying CLAHE to L-channel-------------------------------------------\n",
    "    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))\n",
    "    cl = clahe.apply(l)\n",
    "    # cv2.imshow('CLAHE output', cl)\n",
    "\n",
    "    # -----Merge the CLAHE enhanced L-channel with the a and b channel-----------\n",
    "    limg = cv2.merge((cl, a, b))\n",
    "    # cv2.imshow('limg', limg)\n",
    "\n",
    "    # -----Converting image from LAB Color model to RGB model--------------------\n",
    "    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)\n",
    "    # cv2.imshow('final', final)\n",
    "    return final\n",
    "\n",
    "\n",
    "def convInputImg(img):\n",
    "    # img = cv2.imread('in.png', cv2.IMREAD_GRAYSCALE)\n",
    "\n",
    "    # increase contrast\n",
    "    pxmin = np.min(img)\n",
    "    pxmax = np.max(img)\n",
    "    imgContrast = (img - pxmin) / (pxmax - pxmin) * 255\n",
    "\n",
    "    # increase line width\n",
    "    kernel = np.ones((3, 3), np.uint8)\n",
    "    imgMorph = cv2.erode(imgContrast, kernel, iterations=1)\n",
    "\n",
    "    # write\n",
    "    # cv2.imwrite('out.png', imgMorph)\n",
    "    return imgMorph"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
