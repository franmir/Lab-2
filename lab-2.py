#! /usr/bin/env python
from SimpleCV import Image,Camera

cam = Camera ()
img=cam.getImage()
img.save("FrKa.jpg")
