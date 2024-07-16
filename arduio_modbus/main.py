import Analog_read
import Analog_write
import BIT_LED

while True:
    number = input("숫자 1(read), 2(write), 3(LED) 중 하나를 입력하세요: ")
    
    if number.isdigit():
        number = int(number)
        if number == 1:
            print("read모드를 선택하셨습니다.")
            Analog_read.read_register()
        elif number == 2:
            print("write모드를 선택하셨습니다.")
            Analog_write.write_register()
        elif number == 3:
            print("LED모드를 선택하셨습니다.")
            BIT_LED.write_bit()
    else:
        print("숫자를 입력하세요.")
