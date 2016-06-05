#!/usr/bin/env python
#import the necessary packages
from sklearn.cluster import KMeans
import time
import matplotlib.pyplot as plt
import numpy as np

import cv2

from SimpleCV import Image,Camera,Display,Image


img=Image("lunarr2.jpg")#importamos la imagen a la cual deseamos determinarle los bordes

#imagen en escala de grises
imgGray=img.grayscale()
imgGray.save("grayLab2.png")
hist=imgGray.histogram(255)

plt.figure(1)
plt.plot(hist)
plt.savefig("histogray.png")


#imagen en escala RGB
(red,green,blue)=img.splitChannels(False)

#Histograma imagen RGB
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

#se guardan la imagen RGB
red.save("imagen_r.png")
green.save("imagen_g.png")
blue.save("imagen_b.png")

imgb=imgGray.binarize(50)
imgb.save("bingray.png")

#estimación del gradiente"

bingrad=imgb.morphGradient().save("bingradiennre.png")# determinamos el gradiente de la imagen binarizada, lo que nos da los bordes.
graygrad=imgGray.morphGradient().save("Graygradiennre.png")
REDgrad=red.morphGradient().save("redgradiente.png")
GREENgrad=green.morphGradient().save("greengradiente.png")
BLUEgrad=blue.morphGradient().save("blegradiente.png")
