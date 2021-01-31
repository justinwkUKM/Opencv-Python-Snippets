"""
Stacking Images.
"""

import cv2
import numpy as np
from utils import stack_images

img = cv2.imread("Res/img1.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hor = np.hstack((img, img))
ver = np.vstack((img, img))

img_stack = stack_images(0.5, ([img, img, img], [img, img_gray, img]))

cv2.imshow("Image", img_stack)

cv2.waitKey(0)


