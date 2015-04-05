import numpy as np
import cv2
import os

######
# Read an image and dispaly it
# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html#display-image

# Load an color image in grayscale
img = cv2.imread('./resources/img/tutorial/lenna.png',0)

# Show the image in an application window
cv2.imshow('image', img)

# Await forever for a key stroke to continue execution
cv2.waitKey(0)

# What it says on the tin.
cv2.destroyAllWindows()