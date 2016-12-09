# main.py
# 12/9/2016

from pylab import *

from PIL import Image

# open the image
im = Image.open('headshot.jpg').convert('L')

im = array(im)

imshow(im, cmap="gray")