#!/usr/bin/env python
#import the necessary packages
from sklearn.cluster import KMeans
import time
import matplotlib.pyplot as plt
import argparse

import cv2

from SimpleCV import Image,Camera,Display,Image
cam=Camera ()
img=cam.getImage()
img.save("Lab2.jpg")
img.show
time.sleep(4)

imgGray=img.grayscale()
imgGray.save("grayLab2.jpg")
hist=imgGray.histogram(255)

plt.figure(1)
plt.plot(hist)
plt.savefig("histogray.png")


(red,green,blue)=img.splitChannels(False)


red_histogram=red.histogram(255)
plt.figure(2)
plt.plot(red_histogram)
plt.savefig("histogred.png")

green_histogram=green.histogram(255)
plt.figure(3)
plt.plot(green_histogram)
plt.savefig("histogreen.png")

blue_histogram=blue.histogram(255)
plt.figure(4)
plt.plot(blue_histogram)

plt.savefig("histoblue.png")


imgb=imgGray.binarize(100)
imgb.save("bingray.png")


imgf= imgGray - imgb
imgb.save("fondogray.png")
