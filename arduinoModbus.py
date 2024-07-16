import minimalmodbus
import time

# 시리얼 포트 설정
instrument = minimalmodbus.Instrument('COM8', 1)
instrument.serial.baudrate = 9600
instrument.serial.timeout = 1
instrument.serial.stopbits = 1
instrument.serial.bytesize = 8
time.sleep(2)
while True:
    number = input("숫자 1(read), 2(write), 3(LED) 중 하나를 입력하세요: ")
    
    if number.isdigit():
        number = int(number)
        if number == 1:
            print("read모드를 선택하셨습니다.")
            # 모드버스 RTU 프레임 전송 및 데이터 읽기
            response = instrument.read_registers(0, 3)
            print(f"거리: {response[0]}")
            print(f"습도: {response[1]}")
            print(f"온도: {response[2]}")
            # break
        elif number == 2:
            print("write모드를 선택하셨습니다.")
            digital_segment_value = input("입력하고 싶은 네자리 숫자를 입력하세요 : ")
            if digital_segment_value.isdigit() and len(digital_segment_value) == 4:
                digital_segment_value = int(digital_segment_value)
                # 모드버스 RTU 프레임 전송 및 데이터 쓰기
                instrument.write_register(3, digital_segment_value)
                print(f"{digital_segment_value} 값을 쓰기 성공")
            else:
                print("유효한 네 자리 숫자를 입력하세요.")
            # break
        elif number == 3:
            print("LED모드를 선택하셨습니다.")
            color = input("색상을 선택하세요. ( RED:0 / GREEN:1 ) : ")
            if color.isdigit() and int(color) in [0, 1]:
                color = int(color)
                instrument.write_bit(color, True)
                print('색상 설정 완료')
            else:
                print("유효한 색상을 입력하세요. ( RED:0 / GREEN:1 )")
            # break
        else:
            print("숫자 1(read), 2(write), 3(LED) 중 하나를 입력하세요: ")
    else:
        print("유효한 숫자를 입력하세요.")
