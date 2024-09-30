import minimalmodbus

# 시리얼 포트 설정
instrument = minimalmodbus.Instrument('COM7', 1)
instrument.serial.baudrate = 9600
instrument.serial.timeout = 1
instrument.serial.stopbits = 1
instrument.serial.bytesize = 8

for i in range(0, 3):
    try:
        # 모드버스 RTU 프레임 전송 및 데이터 읽기
        response = instrument.read_registers(0, 3)
        print(f"거리: {response[0]}")
        print(f"습도: {response[1]}")
        print(f"온도: {response[2]}")
    except:
        continue  # 예외 발생 시 다시 시도