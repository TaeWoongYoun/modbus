import minimalmodbus
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox

# 시리얼 포트 설정
instrument = minimalmodbus.Instrument('COM6', 1)
instrument.serial.baudrate = 9600
instrument.serial.timeout = 1
instrument.serial.stopbits = 1
instrument.serial.bytesize = 8

# Tkinter 애플리케이션 생성
root = Tk()
root.title("Modbus Data Display")

# 값 표시를 위한 라벨 생성
distance_label = Label(root, text="거리:")
distance_label.grid(row=0, column=0, padx=10, pady=5)
distance_value = Label(root, text="")
distance_value.grid(row=0, column=1, padx=10, pady=5)

humidity_label = Label(root, text="습도:")
humidity_label.grid(row=1, column=0, padx=10, pady=5)
humidity_value = Label(root, text="")
humidity_value.grid(row=1, column=1, padx=10, pady=5)

temperature_label = Label(root, text="온도:")
temperature_label.grid(row=2, column=0, padx=10, pady=5)
temperature_value = Label(root, text="")
temperature_value.grid(row=2, column=1, padx=10, pady=5)

def read_data():
    for i in range(3):
        try:
            # 모드버스 RTU 프레임 전송 및 데이터 읽기
            response = instrument.read_registers(0, 3)
            distance_value.config(text=str(response[0]))
            humidity_value.config(text=str(response[1]))
            temperature_value.config(text=str(response[2]))
            break
        except Exception as e:
            print(f"읽기 시도 {i+1}에서 오류 발생: {e}")
    else:
        messagebox.showerror("오류", "세 번의 시도 후에도 읽기 실패")

def write_data():
    digital_segment_value = simpledialog.askstring("입력", "입력하고 싶은 네자리 숫자를 입력하세요:")
    if digital_segment_value.isdigit() and len(digital_segment_value) == 4:
        digital_segment_value = int(digital_segment_value)
        for i in range(3):
            try:
                instrument.write_register(3, digital_segment_value)
                messagebox.showinfo("성공", f"{digital_segment_value} 값을 쓰기 성공")
                break
            except Exception as e:
                print(f"쓰기 시도 {i+1}에서 오류 발생: {e}")
        else:
            messagebox.showerror("오류", "세 번의 시도 후에도 쓰기 실패")
    else:
        messagebox.showerror("오류", "유효한 네 자리 숫자를 입력하세요.")

def control_led():
    color = simpledialog.askstring("입력", "색상을 선택하세요. (RED:0 / GREEN:1):")
    if color.isdigit() and int(color) in [0, 1]:
        color = int(color)
        for i in range(2):
            try:
                instrument.write_bit(color, True)
                messagebox.showinfo("성공", "색상 설정 완료")
                break
            except Exception as e:
                print(f"LED 제어 시도 {i+1}에서 오류 발생: {e}")
        else:
            messagebox.showerror("오류", "두 번의 시도 후에도 LED 제어 실패")
    else:
        messagebox.showerror("오류", "유효한 색상을 입력하세요. (RED:0 / GREEN:1)")

# 버튼 생성
read_button = Button(root, text="Read Data", command=read_data)
read_button.grid(row=3, column=0, padx=10, pady=10)

write_button = Button(root, text="Write Data", command=write_data)
write_button.grid(row=3, column=1, padx=10, pady=10)

led_button = Button(root, text="Control LED", command=control_led)
led_button.grid(row=3, column=2, padx=10, pady=10)

# Tkinter 애플리케이션 실행
root.mainloop()

# 시리얼 포트 닫기
instrument.serial.close()
