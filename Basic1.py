"""
Read Image, Read Video, Read Webcam Feed.
"""

import cv2

print('Package Imported')

# Show Images
# img = cv2.imread('Res/img1.jpg')
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# Show Video
# cap = cv2.VideoCapture('Res/vid1.mp4')
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# Show Webcam

# cap = cv2.VideoCapture(0)
# cap.set(3, 640)     # width
# cap.set(4, 480)     # height
# cap.set(10, 200)    # brightness
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# Show Image Size
img = cv2.imread('Res/img1.jpg')
print(img.shape)    # (720, 1280, 3) (Height, Width, Channels)
# cv2.imshow("Output", img)
# cv2.waitKey(0)