import Analog_read
import Analog_write
import BIT_LED
import time
import pymysql

time.sleep(2)

# MySQL 연결
conn = pymysql.connect(host='localhost', user='root', password='1234', db='modbus', charset='utf8')
cursor = conn.cursor()

while True:
    number = input("숫자 1(read), 2(write), 3(LED) 중 하나를 입력하세요: ")

    if number.isdigit():
        number = int(number)
        
        if number == 1:
            print("read모드를 선택하셨습니다.")
            read_value = Analog_read.read_register()
            sql = "INSERT INTO program (Analog_read, Analog_write, BIT_LED) VALUES (%s, %s, %s)"
            cursor.execute(sql, (read_value, None, None))

        elif number == 2:
            print("write모드를 선택하셨습니다.")
            write_value = Analog_write.write_register()
            sql = "INSERT INTO program (Analog_read, Analog_write, BIT_LED) VALUES (%s, %s, %s)"
            cursor.execute(sql, (None, write_value, None))

        elif number == 3:
            print("LED모드를 선택하셨습니다.")
            led_value = BIT_LED.write_bit()
            sql = "INSERT INTO program (Analog_read, Analog_write, BIT_LED) VALUES (%s, %s, %s)"
            cursor.execute(sql, (None, None, led_value))

        # 변경 사항 커밋
        conn.commit()

    else:
        print("숫자를 입력하세요.")

# 연결 종료
conn.close()
