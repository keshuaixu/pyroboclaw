from roboclaw import RoboClaw
import serial
import time

port = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=0.1, interCharTimeout=0.01)
if port.isOpen():
    port.close()
    port.open()
addr = 0x80
roboclaw1 = RoboClaw(port)

while True:
    print(roboclaw1.read_voltages(addr))
    roboclaw1.set_speed(addr, 1, 200)
    time.sleep(0.5)
