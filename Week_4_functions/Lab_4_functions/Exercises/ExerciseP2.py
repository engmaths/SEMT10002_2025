# robot simulation

'''
## Task

Write a program that simulates a robot driving the lawnmower search pattern from Week 3.  Your robot should stop when it gets within 100mm distance of the point (1200,-400), representing collision with an obstacle.

Use functions where appropriate to make your code managable and clear.

> A good function does one job, well.

You have all the pieces to do this already, stretching back to Week 1.  The task here is to assemble and test them.  A tidy structure with functions will make it easy to test and degug as you go.

Make your file a library called `ExerciseP2.py`, including a function called `main` that runs the simulation described.  Use the `if __name__` trick so that the simulation also runs if you invoke your file as a script.  _The template will help you with this._

> Use the script `test_P2.py` to test your library: running `test_p2.py` should run your simulation.
'''

# import the trigonometry
from math import cos, sin

# robot constants
robot_name = "Daneel"
robot_radius = 160 # mm
# put any other constants you need here

# utility functions...
def sinc(x):
    if x**2<0.01**2:
        the_sinc = 1-(x*x/6.0)
    else:
        the_sinc = sin(x)/x
    return the_sinc

# any more functions you need in here
def move_robot(ang_speed_left,ang_speed_right,delta_t):
    # convert angular speeds into linear speeds with linear_velocity = angular_velocity * radius
    linear_speed_left = ang_speed_left * robot_wheel_radius
    linear_speed_right = ang_speed_right * robot_wheel_radius
    # angular speed of the robot is given by the difference in speeds divided by wheel spacing
    ang_speed_robot = (linear_speed_left - linear_speed_right) / wheel_separation
    # multiply angular speed by time to get the amount the angle has changed.
    angle_change = ang_speed_robot * delta_t
    ave_speed = 0.5*(linear_speed_left + linear_speed_right)

# main simulation function
def main():
    # your code here
    '???' # <-- replace

# magic to run the main function if invoked as a script
if __name__=='__main__':
    main()
