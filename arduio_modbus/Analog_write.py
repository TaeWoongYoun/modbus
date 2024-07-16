import serial_port
instrument = serial_port.set_port()

def write_register():
    while True:
        digital_segment_value = input("입력하고 싶은 네자리 숫자를 입력하세요: ")
        if digital_segment_value.isdigit() and len(digital_segment_value) == 4:
            digital_segment_value = int(digital_segment_value)
            # 모드버스 RTU 프레임 전송 및 데이터 쓰기
            instrument.write_register(3, digital_segment_value)
            print(f"{digital_segment_value} 값을 쓰기 성공")
            break  # 유효한 입력 후 루프 종료
        else:
            print("유효한 네 자리 숫자를 입력하세요.")