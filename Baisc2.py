"""
Functions: Grayscale, Blur, Edge detection, Edge Thickening, Edge Thinning
"""


import cv2
import numpy as np

img = cv2.imread("Res/img1.jpg")
kernel = np.ones((5, 5), np.uint8)


# Gray Image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow("Output", img)
# cv2.imshow("OutputGray", imgGray)
# cv2.waitKey(0)

# Blur Image
imgBlur = cv2.GaussianBlur(imgGray, (15, 15), 0)
# cv2.imshow("OutputBlur", imgBlur)

# Edge Detection
imgCanny = cv2.Canny(img, 350, 100)
cv2.imshow("OutputCanny", imgCanny)

# Dialation - Make edges thicker
imgDialation = cv2.dilate(imgCanny, kernel, iterations=2)
cv2.imshow("OutputDialation", imgDialation)

# Erosion - Make edges thinner
imgEroded = cv2.erode(imgDialation, kernel, iterations=2)
cv2.imshow("OutputE Eroded", imgEroded)

cv2.waitKey(0)