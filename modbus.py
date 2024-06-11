from pymodbus.client import ModbusSerialClient as ModbusClient
# 모드버스 클라이언트 설정
client = ModbusClient(
    method='rtu',
    port='COM3',  # 사용할 COM 포트
    baudrate=9600,
    stopbits=1,
    bytesize=8,
    parity='N',
    timeout=1
)

# 클라이언트 연결
connection = client.connect()

if connection:
    try:
        # 레지스터 읽기 (주소 1번부터 3개의 레지스터)
        result = client.read_holding_registers(address=1, count=3, unit=1)
        
        if not result.isError():
            # 결과 출력
            humidity = result.registers[0]
            temperature = result.registers[1]
            distance = result.registers[2]
            
            print(f"습도: {humidity}")
            print(f"온도: {temperature}")
            print(f"거리: {distance}")
        else:
            print("Error reading registers")

    except Exception as e:
        print(f"Exception: {e}")

    finally:
        # 클라이언트 연결 해제
        client.close()
else:
    print("Unable to connect to the Modbus server")
