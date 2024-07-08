import minimalmodbus
import serial

# 시리얼 포트 설정
instrument = minimalmodbus.Instrument('COM8', 1)  # 포트 이름, 슬레이브 주소
instrument.serial.baudrate = 9600
instrument.serial.timeout = 1
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.bytesize = 8
instrument.mode = minimalmodbus.MODE_RTU

try:
    response_count = 0
    max_responses = 1
    while response_count < max_responses:
        try:
            # 모드버스 RTU 프레임 전송 및 데이터 읽기
            response = instrument.read_registers(0, 3)  # 시작 주소, 읽을 레지스터 수

            if len(response) >= 3:  # 최소한 거리, 습도, 온도의 응답이 있는 경우
                humidity = response[0]
                temperature = response[1]
                distance = response[2]

                print(f"거리: {humidity}")
                print(f"습도: {temperature}")
                print(f"온도: {distance}")
                response_count += 1  # 응답 횟수 증가
            else:
                continue  # 응답이 불완전한 경우 다시 시도

        except:
            continue  # 예외 발생 시 다시 시도

finally:
    # 시리얼 포트 닫기
    instrument.serial.close()
