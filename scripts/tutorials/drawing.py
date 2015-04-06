import cv2
import numpy as np

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Drawe a diaglonal blue line with thickness of 5px
cv2.line(img, (0, 0), (511, 511), (255,0,0), 5)
cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)
#-1 thickness of a circle to fill it in
cv2.circle(img,(447,63), 63, (0,0,255), -1)

# Show the image in an application window
cv2.imshow('foo', img)

# Await forever for a key stroke to continue execution
cv2.waitKey(0)

# What it says on the tin.
cv2.destroyAllWindows()

