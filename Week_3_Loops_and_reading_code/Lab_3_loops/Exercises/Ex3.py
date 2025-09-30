'''
## Exercise 3 - Robot Line Sensor

Lots of robots use light sensors to detect and follow marker lines on the floor.  Sometimes fancier sensors like magnetic detection of guide wires are used, but the principles are the same.  Consider a robot with three sensors, one on the centreline and one on either side.  A sensor returns `True` if it is over a line and `False` otherwise.  The useful combinations are:

| Left sensor | Middle sensor | Right sensor | Meaning |
| ---- | ---- | ---- | ---- |
| False | True | False | Centred on line: drive straight |
| True | True | False | Line is slightly to my left: turn left |
| False | True | True | Line is slightly to my right: turn right |
| True | False | False | Line is far to my left: slow and turn left |
| False | False | True | Line is far to my right: slow and turn right |

The image here (https://raw.githubusercontent.com/engmaths/SEMT10002_2025/refs/heads/main/media/week_2/robot_numbers.png) illustrates the set up.

> Implement the control logic for the robot.  _There are lots of ways of doing this._

> How many other possible readings are there?  And what might they mean?  Extend your code to handle everything.

'''

# replace with trial values
left_sensor = '???'
middle_sensor = '???'
right_sensor = '???'
