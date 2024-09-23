import serial_port
instrument = serial_port.set_port()

def read_register():
    # 모드버스 RTU 프레임 전송 및 데이터 읽기
    response = instrument.read_registers(0, 3)
    print(f"거리: {response[0]}")
    print(f"습도: {response[1]}")
    print(f"온도: {response[2]}")
    return response[0], response[1], response[2]