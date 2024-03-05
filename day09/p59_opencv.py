# file : p59_opencv.py
# desc : OpenCV 활용

# OpenCV 실시간 이미지 프로세싱 라이브러리
'''
>> pip install opencv-python
'''

import cv2

# print(cv2.__version__) # OpenCV 설치 확인용

image = cv2.imread('./day09/coby.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 원본 이미지를 흑백으로 변경



height, width, channel = image.shape
print(width, height, channel)

sizeSmall = cv2.resize(image, (width//2, height//2))

img_cropped = image[:, :(width//2)]

cv2.imshow('Coby the Cat, color', image)
cv2.imshow('Reduced Coby', sizeSmall)
cv2.imshow('Coby the Cat, gray', gray)
cv2.imshow('Half Coby', img_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()