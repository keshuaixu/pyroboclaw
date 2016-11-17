from roboclaw import RoboClaw
import serial
import time

# if port.isOpen():
#     port.close()
#     port.open()
addr = 0x80
roboclaw1 = RoboClaw('/dev/ttyACM0')

while True:
    print(roboclaw1.read_voltages(addr))
    roboclaw1.set_speed(addr, 1, 2000)
    time.sleep(0.5)
    print(roboclaw1.read_currents(addr))
