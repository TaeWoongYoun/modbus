import minimalmodbus
import time

port = input("사용할 시리얼 포트를 입력하세요 (예: COM1): ")

instrument = minimalmodbus.Instrument(port, 1)
instrument.serial.baudrate = 9600
instrument.serial.timeout = 1
instrument.serial.stopbits = 1
instrument.serial.bytesize = 8

time.sleep(3)

try:
    response = instrument.read_registers(0, 3)
    print(f"거리: {response[0]}")
    print(f"습도: {response[1]}")
    print(f"온도: {response[2]}")
except Exception as e:
    print(f"시리얼 포트 에러")
