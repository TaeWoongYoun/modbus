import minimalmodbus
import time

# 시리얼 포트 설정
instrument = minimalmodbus.Instrument('COM3', 1)
instrument.serial.baudrate = 9600
instrument.serial.timeout = 1
instrument.serial.stopbits = 1
instrument.serial.bytesize = 8

time.sleep(3)

response = instrument.read_registers(0, 3)
print(f"거리: {response[0]}")
print(f"습도: {response[1]}")
print(f"온도: {response[2]}")