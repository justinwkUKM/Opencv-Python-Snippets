"""
Read Image, Resize Image, Crop Image.
"""

import cv2

print('Package Imported')

# Show Image Size
img = cv2.imread('Res/img1.jpg')
print(img.shape)    # (720, 1280, 3) (Height, Width, Channels)

# Image Resize
imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)

# Image Crop
imgCrop = imgResize[0:100, 0:200]   # [Height, Width]

# cv2.imshow("Output", img)
cv2.imshow("OutputResize", imgCrop)

cv2.waitKey(0)