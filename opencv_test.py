import cv2  # OpenCV 가져오기
import numpy as np  # NumPy 가져오기
import matplotlib.pyplot as plt  # Matplotlib 가져오기

# 이미지 파일 경로 설정
image_path = 'cat.png'  # cat.png 파일이 현재 작업 디렉토리에 있어야 합니다.

# 이미지 읽기
img = cv2.imread(image_path)

# 이미지가 정상적으로 불러와졌는지 확인
if img is None:
    print("이미지를 불러올 수 없습니다. 파일 경로를 확인하세요.")
else:
    # 이미지를 그레이스케일로 변환
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Canny 에지 검출
    canny_image = cv2.Canny(gray_image, 10, 100, apertureSize=3, L2gradient=True)

    # Hough 변환으로 직선 검출
    lines = cv2.HoughLinesP(canny_image, 1, np.pi/180, 160, minLineLength=50, maxLineGap=5)

    # Hough 변환 이미지 생성 (BGR로 변환)
    hough_image = cv2.cvtColor(canny_image, cv2.COLOR_GRAY2BGR)

    # 검출된 선을 이미지에 그리기
    if lines is not None:
        for i in range(lines.shape[0]):
            pt1 = (lines[i][0][0], lines[i][0][1])  # 시작점 좌표
            pt2 = (lines[i][0][2], lines[i][0][3])  # 끝점 좌표
            cv2.line(hough_image, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

    # 결과 이미지 표시
    plt.figure(figsize=(8, 5))
    plt.imshow(cv2.cvtColor(hough_image, cv2.COLOR_BGR2RGB))  # OpenCV는 BGR로 읽으므로 RGB로 변환
    plt.title('Hough Transform Image')
    plt.axis('off')  # 축 숨기기
    plt.show()
