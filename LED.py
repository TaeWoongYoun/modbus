import minimalmodbus

# 모드버스 장치 설정
instrument = minimalmodbus.Instrument('COM8', 1)  # COM 포트와 장치 주소 설정
instrument.serial.baudrate = 9600
instrument.serial.timeout = 3
instrument.serial.stopbits = 1
instrument.serial.bytesize = 8

# LED 제어 함수
def control_led(color):
    try:
        if color == 0:
            # 붉은색 LED 제어
            instrument.write_bit(0, True)  # 0번 레지스터에 True(1) 쓰기
            instrument.write_bit(1, False) # 1번 레지스터에 False(0) 쓰기
            print("붉은색 LED를 켰습니다.")
        elif color == 1:
            # 초록색 LED 제어
            instrument.write_bit(0, False)  # 0번 레지스터에 False(0) 쓰기
            instrument.write_bit(1, True)   # 1번 레지스터에 True(1) 쓰기
            print("초록색 LED를 켰습니다.")
        else:
            print("잘못된 선택입니다. 0 또는 1을 입력하세요.")
    except Exception as e:
        print(f"모드버스 통신 오류: {e}")

# 사용자 입력 받기
while True:
    try:
        choice = int(input("LED 색상을 선택하세요 (0: 붉은색, 1: 초록색): "))
        if choice == 0 or choice == 1:
            control_led(choice)
            break
        else:
            print("잘못된 입력입니다. 0 또는 1을 입력하세요.")
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력하세요.")
