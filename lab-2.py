#! /usr/bin/env python
from SimpleCV import Image,Camera

c = Camera ()
img=c.getImage()
img.save("Lab2.jpg")
img.show
imgGray=img.grayscale()
imgGray.save("grayLab2")
imgGray.show()
hist=imgGray.histogram()
plot(hist)
