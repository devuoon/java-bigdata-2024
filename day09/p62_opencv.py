# file : p61_opencvTemp.py
# desc : OpenCV 계속

import cv2

image = cv2.imread('./day09/coby.jpg', cv2.IMREAD_UNCHANGED)
dst = cv2.blur(image, (5, 5), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
canny = cv2.Canny(image, 100, 255)

height, width, channel = image.shape

cv2.imshow('Coby the cat', image)
cv2.imshow('Blur', dst)
cv2.imshow('Sobel', sobel)
cv2.imshow('Laplacian', laplacian)
cv2.imshow('Canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()