# file : p63_opencv.py
# desc : OpenCV 영상처리

import cv2

samplePath = './day09/testVideo.mp4'
cap = cv2.VideoCapture(samplePath) # 0은 웹캠 또는 문자열로 동영상 경로

while True:
  ret, frame = cap.read()

  if not ret:
    cap = cv2.VideoCapture(samplePath)
    continue

  cv2.imshow('original', frame)

  key = cv2.waitKey(25) # q
  if key == 27: 
    break

cap.release()
cv2.destroyAllWindows


    