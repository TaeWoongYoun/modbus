import minimalmodbus

# 모드버스 장치 설정
instrument = minimalmodbus.Instrument('COM7', 1)  # COM 포트와 장치 주소 설정
instrument.serial.baudrate = 9600
instrument.serial.timeout = 3
instrument.serial.stopbits = 1
instrument.serial.bytesize = 8

for i in range(0,2):
    try:
        instrument.write_bit(1, True) #RED:0 / GREEN:1
        print('색상 설정 완료')
    except:
        continue