from tkinter import *
import serial

# 시리얼 포트 설정
ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    timeout=1
)

# Tkinter 애플리케이션 생성
root = Tk()
root.title("Modbus Data Display")

# 값 표시를 위한 라벨 생성
humidity_label = Label(root, text="거리:")
humidity_label.grid(row=0, column=0, padx=10, pady=5)
humidity_value = Label(root, text="")
humidity_value.grid(row=0, column=1, padx=10, pady=5)

temperature_label = Label(root, text="습도:")
temperature_label.grid(row=1, column=0, padx=10, pady=5)
temperature_value = Label(root, text="")
temperature_value.grid(row=1, column=1, padx=10, pady=5)

distance_label = Label(root, text="온도:")
distance_label.grid(row=2, column=0, padx=10, pady=5)
distance_value = Label(root, text="")
distance_value.grid(row=2, column=1, padx=10, pady=5)

# 시리얼 통신으로 데이터 읽고 값 업데이트
def update_values():
    try:
        if ser.is_open:
            ser.write(b'\x01\x03\x00\x00\x00\x03\x05\xCB')  # 모드버스 RTU 프레임
            response = ser.read(255)
            if response:
                if len(response) >= 9:  # 최소한 거리, 습도, 온도의 응답이 있는 경우
                    expected_length = response[2] + 5
                    if len(response) >= expected_length:
                        # 데이터 해석
                        humidity = response[3] * 256 + response[4]
                        temperature = response[5] * 256 + response[6]
                        distance = response[7] * 256 + response[8]

                        # 라벨에 값 업데이트
                        humidity_value.config(text=str(humidity))
                        temperature_value.config(text=str(temperature))
                        distance_value.config(text=str(distance))

    except Exception as e:
        print(f"Exception: {e}")

    root.after(1000, update_values)  # 1초마다 값 업데이트

# 초기 값 업데이트
update_values()

# Tkinter 애플리케이션 실행
root.mainloop()

# 시리얼 포트 닫기
ser.close()
