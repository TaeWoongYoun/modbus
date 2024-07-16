import serial_port
instrument = serial_port.set_port()

def write_bit():
    while True:
        color = input("색상을 선택하세요. ( RED:0 / GREEN:1 ) : ")
        if color.isdigit() and int(color) in [0, 1]:
            color = int(color)
            instrument.write_bit(color, True)
            if color == 0:
                instrument.write_bit(1, False)
            else:
                instrument.write_bit(0, False)
            print('색상 설정 완료')
            break
        else:
            print("유효한 색상을 입력하세요. ( RED:0 / GREEN:1 )")
