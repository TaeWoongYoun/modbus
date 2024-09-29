import cv2  # OpenCV 라이브러리
import numpy as np

# 이미지 불러오기
img = cv2.imread('cat.png', cv2.IMREAD_COLOR)

# 이미지를 그레이스케일로 변환 (에지 검출을 위해 필요)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# GaussianBlur 적용해서 노이즈 제거 (에지 검출을 좀 더 정확하게 하기 위해)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Canny 에지 검출기 적용
edges = cv2.Canny(blur, 100, 200)

# 원본 이미지와 에지 검출된 결과를 화면에 보여줌
cv2.imshow('Original Image', img)
cv2.imshow('Edge Detected Image', edges)

# 키 입력을 기다렸다가 창을 닫음
cv2.waitKey(0)
cv2.destroyAllWindows()
