import serial
import serial.tools.list_ports

# COM 포트 검색
def find_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if 'COM3' in port.device:
            return port.device
    return None

try:
    # COM 포트 찾기
    port = find_port()
    if port:
        # 시리얼 포트 열기
        ser = serial.Serial(port, 9600, timeout=1)
        
        # 시리얼 포트가 열렸는지 확인
        if ser.is_open:
            print(f"Serial port {ser.name} opened successfully")
            
            # 시리얼 포트에서 데이터 읽기
            while True:
                line = ser.readline().decode().strip()
                if line:
                    print("Received:", line)
        else:
            print(f"Failed to open serial port {port}")

    else:
        print("COM3 포트를 찾을 수 없습니다.")

except Exception as e:
    print(f"Exception: {e}")

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial port closed")
