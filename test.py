from roboclaw import RoboClaw
import serial
import time

# if port.isOpen():
#     port.close()
#     port.open()
roboclaw1 = RoboClaw('/dev/ttyACM0', 0x80)

roboclaw1.drive_to_position(1, 0, 0, 0, 25, 1)
while True:
    print(roboclaw1.read_position(1))
    time.sleep(0.5)
