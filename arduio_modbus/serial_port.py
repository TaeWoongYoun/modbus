import minimalmodbus
import time

# 시리얼 포트 설정
def set_port(a):
    instrument = minimalmodbus.Instrument(a, 1)
    instrument.serial.baudrate = 9600
    instrument.serial.timeout = 1
    instrument.serial.stopbits = 1
    instrument.serial.bytesize = 8
    time.sleep(2)
    return instrument