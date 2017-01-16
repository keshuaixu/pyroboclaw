# pyRoboClaw

Unofficial library for talking to RoboClaw motor controllers sold by Pololu. We wrote our owm because the manufacturer supplied ridiculously shitty code.

*WARNING* The API is not stable yet. Some of the methods do other things than the name suggests because of our specific application.

# Example

You might have to read the RoboClaw manual and the source code to understand what the commands actually do.

```
from roboclaw import RoboClaw
import time

roboclaw1 = RoboClaw(port='/dev/ttyACM0', address=0x80)
# Read the roboclaw manual to understand the trajectory parameters
roboclaw1.drive_to_position_raw(motor=1, accel=0, speed=0, deccel=0, position=25, buffer=1)
while True:
    print(roboclaw1.read_position(1))
    time.sleep(0.5)
```

# Install

Tested on Python 3.5 and 3.6. It will probably not work on Python 2.

```
pip install roboclaw
```