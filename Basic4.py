"""
Read Image, Resize Image, Crop Image.
"""

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

# coloring the matrix/img
# img[:400, 200:400] = 255, 0, 0

# Line
cv2.line(img, (225, 225), (255, 512), (0, 255, 0), 3)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 3)

# Rectangle
cv2.rectangle(img, (255, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 3)
cv2.rectangle(img, (255, 0), (img.shape[1], 255), (0, 0, 255), cv2.FILLED)

# Circle
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)

# Text
cv2.putText(img, "OpenCV", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0.200, 200), 5)

cv2.imshow("OutputResize", img)
cv2.waitKey(0)
