# file : p60_opencv.py
# desc : OpenCV 이미지 처리 계속

import cv2

image = cv2.imread('./day09/coby.jpg', cv2.IMREAD_UNCHANGED)
dst = cv2.filp(image, 0) # 0 : 위아래 반전, 1 : 좌우반전

height, width, channel = image.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
thrd = cv2.warpAffine(image, matrix, (width, height))

cv2.imshow('Coby the cat', image)
cv2.imshow('Flip', dst)
cv2.imshow('Rotaion', thrd)

cv2.waitKey(0)
cv2.destroyAllWindows()