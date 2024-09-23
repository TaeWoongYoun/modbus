import minimalmodbus

# 시리얼 포트 설정
def set_port():
    instrument = minimalmodbus.Instrument('COM3', 1)
    instrument.serial.baudrate = 9600
    instrument.serial.timeout = 1
    instrument.serial.stopbits = 1
    instrument.serial.bytesize = 8
    return instrument