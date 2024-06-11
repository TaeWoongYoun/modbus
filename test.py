# import minimalmodbus

# instrument = minimalmodbus.Instrument('COM4', 1)
# temperature = instrument.read_register(1, 1)
# print(temperature)

import minimalmodbus
import serial

if __name__ == '__main__':
    try:
        # COM 포트와 슬레이브 주소 설정
        instrument = minimalmodbus.Instrument('COM5', 1)
        instrument.serial.baudrate = 9600  # Baud rate 설정
        instrument.serial.bytesize = 8     # 데이터 비트 설정
        instrument.serial.parity = serial.PARITY_NONE  # 패리티 설정
        instrument.serial.stopbits = 1     # 스톱 비트 설정
        instrument.serial.timeout = 1      # 타임아웃 설정 (초 단위)
        
        # 버퍼 지우기 설정
        instrument.clear_buffers_before_each_transaction = True
        
        # 통신 테스트
        print("Opening serial port...")
        if instrument.serial.is_open:
            print("Serial port opened successfully.")
        else:
            print("Failed to open serial port.")
        
        # 레지스터 읽기 (예: 주소 0의 입력 레지스터 읽기)
        try:
            print("Attempting to read register...")
            value = instrument.read_register(0, 0, functioncode=4)
            print(f'Read value: {value}')
        except IOError as e:
            print('Failed to read from instrument')
            print(f'Error details: {e}')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        # 시리얼 포트 닫기
        instrument.serial.close()

