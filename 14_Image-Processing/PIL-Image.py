"""
https://pillow.readthedocs.io/en/stable/
"""
from PIL import Image, ImageOps, ImageFilter
import matplotlib.pyplot as plt

im = Image.open('dva1.jpg')
print(im.format, im.size, im.mode)

""" Show Image """
im = Image.open('dva1.jpg')
# im.show()       # Use system image viewer, high quality
plt.figure(1)
plt.imshow(im)  # Use matplotlib ugly figure axes, low quality

""" Image Crop """
im = Image.open('dva1.jpg')
rect = (700,200,1500,1000)
# crop(box = (left, upper, right, lower pixel coordinate))
img = im.crop(rect)
plt.figure(2)
plt.imshow(img)

""" Thumbnail """
im = Image.open('dva1.jpg')
size = 128,128
img = ImageOps.fit(im,size,Image.LANCZOS)
# Method can be PIL.Image.NEAREST, PIL.Image.BILINEAR, 
# PIL.Image.BICUBIC, or PIL.Image.LANCZOS.
plt.figure(3)
plt.imshow(img)

""" Resize and Paste """
im = Image.open('dva1.jpg')
rect = 700,200,1500,1000
img1 = im.crop(rect)
width, height = img1.size 
img2 = Image.open('dva2.jpg')
img2.paste(img1.resize((int(width),int(height))),(20,200))
# paste(img,(upper left corner))
plt.figure(4)
plt.imshow(img2)

""" Rotate and Flip """
im = Image.open('dva1.jpg')
plt.figure(5)
plt.imshow(im.rotate(45))
plt.figure(6)
plt.imshow(im.transpose(Image.FLIP_LEFT_RIGHT))

""" Pixel Processing """
im = Image.open('dva1.jpg')
for x in range(700,1500):
    for y in range(200,1000):
        im.putpixel((x,y),(255,155,55))
plt.figure(7)
plt.imshow(im)

""" Filter """
im = Image.open('dva1.jpg')
plt.figure(8)
plt.imshow(im.filter(ImageFilter.CONTOUR))
# Predefined ImageFilter: 
# BLUR
# CONTOUR
# DETAIL
# EDGE_ENHANCE
# EDGE_ENHANCE_MORE
# EMBOSS
# FIND_EDGES
# SHARPEN
# SMOOTH
# SMOOTH_MORE

plt.show()

