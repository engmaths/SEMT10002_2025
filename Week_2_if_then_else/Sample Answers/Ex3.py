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
left_sensor = True
middle_sensor = False
right_sensor = False

if middle_sensor:
    # X1X
    if left_sensor:
        # 11X
        if right_sensor:
            # 111
            print('all three on line - sideways')
        else:
            #110
            print('turn left')
    elif right_sensor:
        # 011
        print('turn right')
    else:
        # 010
        print('go straight')
else:
    #X0X
    if left_sensor:
        # 10X
        if right_sensor:
            # 101
            print('gap in the middle - fault')
        else:
            #100
            print('slow and turn left')
    elif right_sensor:
        # 001
        print('slow and turn right')
    else:
        # 000
        print('no line at all - lost')
