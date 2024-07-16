import serial_port
instrument = serial_port.set_port()

def write_bit():
    color = input("색상을 선택하세요. ( RED:0 / GREEN:1 ) : ")
    if color.isdigit() and int(color) in [0, 1]:
        color = int(color)
        instrument.write_bit(color, True)
        print('색상 설정 완료')
    else:
        print("유효한 색상을 입력하세요. ( RED:0 / GREEN:1 )")