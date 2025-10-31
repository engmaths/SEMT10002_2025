'''
================
Exercise 5
================

We are going to update the robot program so that the robot has, not just one, but *multiple* obstacles to avoid. 

The library robot_plotter.py has been updated...

The function `show_plot(map_coords, goal=None, obstacle=None, pause=0)` had an optional argument `obstacle`, with format:
((obstacle_x, obstacle_y), (obstacle_width, obstacle_height))

Rather than plotting a single obstacle, the function can now plot any number of obstacles. 
To achieve this, the optional argument, `obstacle`, has been replaced by an optional argument `obstacles` which 
instead has the format of a list. Examples:


1 obstacle

[((obstacle_1_x, obstacle_1_y), (obstacle_1_width, obstacle_1_height))]


2 obstacles

[((obstacle_1_x, obstacle_1_y), (obstacle_1_width, obstacle_1_height)),
 ((obstacle_2_x, obstacle_2_y), (obstacle_2_width, obstacle_2_height))]


3 obstacles

[((obstacle_1_x, obstacle_1_y), (obstacle_1_width, obstacle_1_height)),
 ((obstacle_2_x, obstacle_2_y), (obstacle_2_width, obstacle_2_height)),
 ((obstacle_3_x, obstacle_3_y), (obstacle_3_width, obstacle_3_height))]


1. Copy your code from Consolidation Exercise 1, Task 2: Collision Avoidance. 

2. Update your programme so that any number of obstacles can be generated, and the robot detects and avoids all obstcles
'''

from robot_plotter import init_plot, snapshot, show_plot
from math import sin, cos, atan2, sqrt, pi
from random import random

# constants about the robot
robot_name = "Daneel"
robot_radius = 160
wheel_separation = 150
robot_wheel_radius = 35

# Map information
map_x_min = 0
map_x_max = 5000
map_y_min  = 0
map_y_max = 5000
map_coords = ((map_x_min, map_x_max), (map_y_min, map_y_max))

# # An obstacle with bottom left corner at at x = 100, y = 2250, width of 500 and height of 800
# obstacle_x = 100
# obstacle_y = 2250
# obstacle_width = 4000
# obstacle_height = 500
# obstacle = ((obstacle_x, obstacle_y), (obstacle_width, obstacle_height))

# Obstacles described using the format ((x, y), (width, height))
obstacles = [((100, 2250), (4000, 500)),
             ((3000, 3000), (800, 1500)),
             ((1500, 500), (600, 600))
            ]

goal = (1000, 4000)

# This is the number of timesteps we simulate - change as is necessary.
num_steps = 50

# This is the default timestep - so by default we'll simulate 100 timesteps of 1 second= 100 seconds of movement. 
delta_t = 1 

def compute_new_positioning(x, y, theta, v_left, v_right, 
                            wheel_separation, delta_t):

    # angular speed of the robot is given by the difference in speeds divided by wheel spacing
    ang_speed_robot = (v_left - v_right) / wheel_separation

    # multiply angular speed by time to get the amount the angle has changed.
    angle_change = ang_speed_robot * delta_t
    ave_speed = 0.5*(v_left + v_right)

    # sinc
    if angle_change**2<0.01**2:
        the_sinc = 1-(0.25*angle_change*angle_change/6.0)
    else:
        the_sinc = sin(0.5*angle_change)/(0.5*angle_change)

    # Update position
    x = x + ave_speed*delta_t*the_sinc*sin(theta + 0.5*angle_change)
    y = y + ave_speed*delta_t*the_sinc*cos(theta + 0.5*angle_change)
    theta = theta + angle_change

    return x, y, theta

def random_walk():
    # Set the wheel speeds to be random numbers between 0 and 5
    ang_speed_left = 5 * random()
    ang_speed_right = 5 * random()

    # convert angular speeds into linear speeds with linear_velocity = angular_velocity * radius
    linear_speed_left = ang_speed_left * robot_wheel_radius
    linear_speed_right = ang_speed_right * robot_wheel_radius
    
    return linear_speed_left, linear_speed_right

def goal_seek(iteration, phi_robot, distance_robot, 
              delta_t, wheel_seperation, num_steps):
     # Turn to face heading
    if iteration == 0:

        # Compute wheel displacement from roobt angular displacement
        linear_displacement_left =  phi_robot * wheel_separation / 2
        linear_displacement_right = -linear_displacement_left

        # Compute wheel linear speed
        linear_speed_left = linear_displacement_left / delta_t
        linear_speed_right = linear_displacement_right / delta_t

    # Move in straight line to heading
    else:

        # Compute linear speed of robot
        v = distance_robot / (num_steps - 1)

        # Compute wheel linear speeds
        linear_speed_left = linear_speed_right = v 

    return linear_speed_left, linear_speed_right

def main():

    # initial robot configuration
    robot_x_position = 500
    robot_y_position = 500
    robot_heading = 0

    # Initialise visualisation
    init_plot(robot_x_position, 
              robot_y_position, 
              robot_heading)

    # Compute angle to turn to face goal
    phi_robot = atan2(goal[0]-robot_x_position, 
                    goal[1]-robot_y_position) - robot_heading
    print('angle to turn, phi, is', phi_robot)

    # Compute distance to goal 
    distance_robot = sqrt((goal[0]-robot_x_position)**2 + 
                          (goal[1]-robot_y_position)**2)
    print('distance to travel is', distance_robot)

    for ii in range(num_steps):

        # Random walk with obstacle avoiadance (comment out obstacle avoisance if not needed)
        linear_speed_left, linear_speed_right = random_walk()

        # Compute new position and orientation
        x, y, theta = compute_new_positioning(robot_x_position, robot_y_position, 
                                              robot_heading, linear_speed_left, 
                                              linear_speed_right, wheel_separation, 
                                              delta_t)

        # --------------------------------------------------------------
        # OBSTACLE AVOIDANCE 
        obstacle_detected = False

        # Detect any obstacles 
        for ii in obstacles:
            obstacle_x = ii[0][0]
            obstacle_y = ii[0][1]
            obstacle_width = ii[1][0]
            obstacle_height = ii[1][1]

            if (obstacle_x < x < obstacle_x + obstacle_width and 
                obstacle_y < y < obstacle_y + obstacle_height):

                obstacle_detected = True

        # Detect edges of map
        if (x > map_x_max or
            x < map_x_min or
            y > map_y_max or
            y < map_y_min):

            obstacle_detected = True

        if obstacle_detected:

            # Turn 180 degrees on the spot if collision with obstacle is detected 
            linear_displacement_left =  pi * wheel_separation / 2
            linear_displacement_right = -linear_displacement_left

            linear_speed_left = linear_displacement_left / delta_t
            linear_speed_right = linear_displacement_right / delta_t

            x, y, theta = compute_new_positioning(robot_x_position, robot_y_position, 
                                                  robot_heading,linear_speed_left, 
                                                  linear_speed_right, wheel_separation, 
                                                  delta_t)

        # Update robot state
        robot_x_position = x
        robot_y_position = y
        robot_heading = theta

        # Plot robot at current state
        snapshot(robot_x_position, 
                robot_y_position, 
                robot_heading)

        # Display current frame 
        show_plot(map_coords, goal=goal, 
                  obstacles=obstacles, pause=0.1)

    # Display final frame 
    show_plot(map_coords, goal=goal, 
              obstacles=obstacles)

if __name__ == '__main__':
    main()