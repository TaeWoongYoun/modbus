import minimalmodbus
import time
import pymysql

port = input("포트를 입력하세요 (예: COM1): ")

instrument = minimalmodbus.Instrument(port, 1)
instrument.serial.baudrate = 9600
instrument.serial.timeout = 1
instrument.serial.stopbits = 1
instrument.serial.bytesize = 8
time.sleep(3)

while True:
    data = instrument.read_registers(0, 3)
    print(f"거리: {data[0]} / 습도: {data[1]} / 온도: {data[2]}")
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='Analog_read', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO program (Distance, Humidity, Temperature) VALUES ('"+str(data[0])+"', '"+str(data[1])+"', '"+str(data[2])+"')"
    cursor.execute(sql)
    conn.commit()
    conn.close()
    time.sleep(10) 