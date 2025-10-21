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
# import the plotter
from robot_plotter import init_plot,snapshot,show_plot

# constants about the robot
robot_name = "Daneel"
robot_radius = 160
wheel_separation = 150
robot_wheel_radius = 35

# function to calculate sinc
def sinc(x):
    if x**2<0.01**2:
        the_sinc = 1-(x*x/6.0)
    else:
        the_sinc = sin(x)/x
    return the_sinc

# function to calculate if distance between two points closer than threshold
def closer(x1,y1,x2,y2,d):
    flag = False
    if (x2-x1)**2 + (y2-y1)**2 < d**2:
        flag = True
    return flag

# function to move robot
def new_robot_pos(robot_x_position,robot_y_position,robot_heading,ang_speed_left,ang_speed_right,delta_t):
    # convert angular speeds into linear speeds with linear_velocity = angular_velocity * radius
    linear_speed_left = ang_speed_left * robot_wheel_radius
    linear_speed_right = ang_speed_right * robot_wheel_radius
    # angular speed of the robot is given by the difference in speeds divided by wheel spacing
    ang_speed_robot = (linear_speed_left - linear_speed_right) / wheel_separation
    # multiply angular speed by time to get the amount the angle has changed.
    angle_change = ang_speed_robot * delta_t
    # average forward speed
    ave_speed = 0.5*(linear_speed_left + linear_speed_right)
    # propagate state
    new_robot_x_position = robot_x_position + ave_speed*delta_t*sinc(0.5*angle_change)*sin(robot_heading + 0.5*angle_change)
    new_robot_y_position = robot_y_position + ave_speed*delta_t*sinc(0.5*angle_change)*cos(robot_heading + 0.5*angle_change)
    new_robot_heading = robot_heading + angle_change
    return new_robot_x_position, new_robot_y_position, new_robot_heading

# any more functions you need in here
def robot_pivot_on_wheel(robot_x_position,robot_y_position,robot_heading,clockwise):
    # pribot on one wheel
    if clockwise==True:
        ang_speed_left = 1
        ang_speed_right = 0
    else:
        ang_speed_left = 0
        ang_speed_right = 1
    delta_t = 13.464
    new_robot_x_position, new_robot_y_position, new_robot_heading = new_robot_pos(robot_x_position,robot_y_position,robot_heading,ang_speed_left,ang_speed_right,delta_t)
    return new_robot_x_position, new_robot_y_position, new_robot_heading

# any more functions you need in here
def robot_drive_forward(robot_x_position,robot_y_position,robot_heading,delta_t):
    # drive forward for delta_t seconds at default speed (37mm/s)
    new_robot_x_position, new_robot_y_position, new_robot_heading = new_robot_pos(robot_x_position,robot_y_position,robot_heading,1,1,delta_t)
    return new_robot_x_position, new_robot_y_position, new_robot_heading

# main simulation function
def main():
    # initial robot configuration
    robot_x_position = 0
    robot_y_position = 0
    robot_heading = 0
    init_plot(0,0,0)

    # flag for detecting obstacle
    obstacle_flag = False

    for ii in range(5):

        for jj in range(22):
            # cycle of 22 moves for each pair of "rungs": turn right, 10*steps forward, turn left, 10*steps forward
            if jj==0:
                # first step - turn right
                robot_x_position,robot_y_position,robot_heading = robot_pivot_on_wheel(robot_x_position,robot_y_position,robot_heading,True)
            elif jj==11:
                # step 11 - turn left
                robot_x_position,robot_y_position,robot_heading = robot_pivot_on_wheel(robot_x_position,robot_y_position,robot_heading,False)                
            else:
                # all other steps - drive forward
                robot_x_position,robot_y_position,robot_heading = robot_drive_forward(robot_x_position,robot_y_position,robot_heading,2)

            print(ii,jj,robot_x_position,robot_y_position,robot_heading)
            snapshot(robot_x_position,robot_y_position,robot_heading)

            if closer(robot_x_position,robot_y_position,1200,-400,100):
                # break here will only exit the inner "for jj" loop
                # to also stop the outer "for ii" loop, set a flag as a message
                obstacle_flag = True
                break

        if obstacle_flag==True:
            # exit this loop as well if reached the obstacle
            break

    show_plot()

# magic to run the main function if invoked as a script
if __name__=='__main__':
    main()
