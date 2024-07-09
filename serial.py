import minimalmodbus

# 시리얼 포트 설정
instrument = minimalmodbus.Instrument('COM7', 1)  # COM 포트와 장치 주소 설정
instrument.serial.baudrate = 9600
instrument.serial.timeout = 3
instrument.serial.stopbits = 1
instrument.serial.bytesize = 8