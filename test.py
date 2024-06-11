# import minimalmodbus

# instrument = minimalmodbus.Instrument('COM4', 1)
# temperature = instrument.read_register(1, 1)
# print(temperature)

import minimalmodbus
import serial

def print_instrument_settings(instrument):
    print(f"Port: {instrument.serial.port}")
    print(f"Baudrate: {instrument.serial.baudrate}")
    print(f"Bytesize: {instrument.serial.bytesize}")
    print(f"Parity: {instrument.serial.parity}")
    print(f"Stopbits: {instrument.serial.stopbits}")
    print(f"Timeout: {instrument.serial.timeout}")

if __name__ == '__main__':
    try:
        instrument = minimalmodbus.Instrument('COM5', 1)
        instrument.serial.baudrate = 9600
        instrument.serial.bytesize = 8
        instrument.serial.parity = serial.PARITY_NONE
        instrument.serial.stopbits = 1
        instrument.serial.timeout = 1
        instrument.clear_buffers_before_each_transaction = True

        print("Instrument settings:")
        print_instrument_settings(instrument)

        # 시도 1: functioncode=4
        try:
            print("Attempting to read register with functioncode=4...")
            value = instrument.read_register(0, 0, functioncode=4)
            print(f'Read value (functioncode=4): {value}')
        except IOError as e:
            print('Failed to read from instrument with functioncode=4')
            print(f'Error details: {e}')

        # 시도 2: functioncode=3
        try:
            print("Attempting to read register with functioncode=3...")
            value = instrument.read_register(0, 0, functioncode=3)
            print(f'Read value (functioncode=3): {value}')
        except IOError as e:
            print('Failed to read from instrument with functioncode=3')
            print(f'Error details: {e}')

    except Exception as e:
        print(f'Error: {e}')
    finally:
        instrument.serial.close()
