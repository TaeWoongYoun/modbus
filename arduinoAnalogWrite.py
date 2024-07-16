import minimalmodbus
import time

# 시리얼 포트 설정
instrument = minimalmodbus.Instrument('COM8', 1)
instrument.serial.baudrate = 9600
instrument.serial.timeout = 1
instrument.serial.stopbits = 1
instrument.serial.bytesize = 8
time.sleep(2)

# 모드버스에 입력되는 숫자
digital_segment_value = 7777
# 모드버스 RTU 프레임 전송 및 데이터 읽기 
instrument.write_register(3, digital_segment_value)