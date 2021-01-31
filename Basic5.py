"""
Crop and Warp.
"""

import cv2
import numpy as np

img = cv2.imread("Res/img1.jpg")

width, height = 250, 350
pts1 = np.float32([[529, 468], [650, 390], [780, 430], [756, 509]])
pts2 = np.float32([[width, 0], [0, 0], [width, height], [0, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow("Image", imgOutput)

cv2.waitKey(0)


