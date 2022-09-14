import serial
import time

arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)
value = 0


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


while not (value == b'55'):
    num = input("Enter a number until you receive '55' (three tries for security): ")  # Taking input from user
    value = write_read(num)
    print(value)  # printing the value
    time.sleep(0.1)
print("You have established connection")
