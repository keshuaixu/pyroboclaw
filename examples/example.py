from roboclaw import RoboClaw
import time

roboclaw1 = RoboClaw('/dev/ttyACM0', 0x80)
roboclaw1.drive_to_position_raw(motor=1, accel=0, speed=0, deccel=0, position=25, buffer=1)
while True:
    print(roboclaw1.read_position(1))
    time.sleep(0.5)
