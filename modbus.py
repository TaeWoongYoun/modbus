import time
import serial

# 시리얼 포트 설정
ser = serial.Serial(
    port='COM3',  # 사용할 COM 포트
    baudrate=9600,
    timeout=1
)
try:
    if ser.is_open:
        response_count = 0
        max_responses = 1  # 최대 응답 횟수
        while response_count < max_responses:
            # 시리얼 포트에서 데이터 읽기
            ser.write(b'\x01\x03\x00\x00\x00\x03\x05\xCB')  # 모드버스 RTU 프레임
            response = ser.read(255)  # 최대한 많은 응답을 읽음 (255바이트)
            if response:
                # 응답 길이 확인
                if len(response) >= 9:  # 최소한 거리, 습도, 온도의 응답이 있는 경우
                    data_length = response[2]
                    expected_length = data_length + 5  # 데이터 길이 + 주소(1) + 기능코드(1) + 데이터길이(1) + CRC(2)
                    if len(response) >= expected_length:
                        # 데이터 해석
                        humidity = response[3] * 256 + response[4]
                        temperature = response[5] * 256 + response[6]
                        distance = response[7] * 256 + response[8]
                        
                        print(f"거리: {distance}")
                        print(f"습도: {humidity}")
                        print(f"온도: {temperature}")
                        response_count += 1  # 응답 횟수 증가

finally:
    # 시리얼 포트 닫기
    ser.close()
