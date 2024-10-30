# 📋 파이썬-아두이노 프로젝트

회사에서 진행하는 파이썬 아두이노 제어 프로젝트로, 온도, 습도, 거리 데이터를 받고 LED를 제어하며 아두이노에 숫자를 적을 수 있는 프로그램 입니다.

## 📂 프로젝트 구조

- `arduino_modbus/`
  - `Analog_read.py` : 거리, 습도, 온도를 읽어오는 기능을 하는 함수
  - `Analog_write.py` : 아두이노에 4자리 숫자를 적는 기능을 하는 함수
  - `BIT_LED.py` : LED 제어 기능을 하는 함수
  - `main.py` : 모든 함수를 사용해서 만든 메인 프로그램
  - `serial_port.py` : 시리얼 포트 함수
  - `test.py` : `main.py`를 만들기 전 테스트 프로그램
- `modbus_read/`
  - `read.py` : 거리, 습도, 온도를 읽고 MariaDB에 데이터를 저장
- `venv/` : (여기에 가상환경 관련 파일이 위치합니다)
- `arduino.py` : `arduino_modbus` 프로그램을 만들기 전 함수를 사용하지 않은 프로그램. 이 프로그램을 리팩토링하여 `arduino_modbus`가 탄생함
- `arduinoUI.py` : `arduino.py`에 UI를 추가
- `LED.py` : 간단한 LED 제어 프로그램
- `main-LED.py` : 코드를 수정하지 않고 LED를 사용자가 제어하는 프로그램
- `mysql.py` : SQL 사용 테스트 프로그램
- `write.py` : 아두이노에 4자리 숫자를 입력하는 프로그램

## 🖼️ 아두이노 이미지
<p align="center">
  <img src="images/modbus.jpg" alt="image" width="600">
</p>

## 🛠️ 사용된 기술 스택

- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
- ![Arduino](https://img.shields.io/badge/Arduino-00979D?style=flat-square&logo=arduino&logoColor=white)
- ![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=flat-square&logo=mariadb&logoColor=white)
- ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)

## 📦 사용한 주요 라이브러리

- ![minimalmodbus](https://img.shields.io/badge/minimalmodbus-FFD700?style=flat-square&logoColor=black)
- ![time](https://img.shields.io/badge/time-FF6F00?style=flat-square&logoColor=white)
- ![pymysql](https://img.shields.io/badge/pymysql-002D72?style=flat-square&logoColor=white)
- ![threading](https://img.shields.io/badge/threading-FFD700?style=flat-square&logoColor=black)