import minimalmodbus

# 시리얼 포트 설정
instrument = minimalmodbus.Instrument('COM7', 1)
instrument.serial.baudrate = 9600
instrument.serial.timeout = 1
instrument.serial.stopbits = 1
instrument.serial.bytesize = 8

# 모드버스에 입력되는 숫자
digital_segment_value = 7777

for i in range(0, 3):
    try:
        # 모드버스 RTU 프레임 전송 및 데이터 읽기 
        instrument.write_register(3, digital_segment_value)        
    except:
        continue