'''
## Task

Write a program that generates a robot log file. 

Each time the program saves a snapshot of the robot, it should also record the following information and save it to log file:
- timestamp 
- position of the robot
- orientation of the robot
- the state information: "Collision with wall"/"Collision with obstacle" if the robot has collided with a wall or obstacle respectively, 
otherwise the state information should be blank (i.e. an empty string) 
'''

from robot_plotter import init_plot, snapshot, show_plot
from math import sin, cos, atan2, sqrt, pi
from random import random
from time import perf_counter
import csv

# Navigation mode: 'random_walk_mode' or 'goal_seek_mode'
mode = 'random_walk_mode' # 'goal_seek_mode' 

# Obstacle avoidance
avoid_obstacles = True

# Simulation start time
start_time = perf_counter() 

# Robot log file name
log_file_name = 'log_file.csv'

# Constants about the robot
robot_name = "Daneel"
robot_radius = 160
wheel_separation = 150
wheel_radius = 35

# Map information
map_x_min = 0
map_x_max = 5000
map_y_min  = 0
map_y_max = 5000
map_coords = ((map_x_min, map_x_max), 
              (map_y_min, map_y_max))

# Obstacles described using the format ((x, y), (width, height))
obstacles = [((100, 2250), (4000, 500)),
             ((3000, 3000), (800, 1500)),
             ((1500, 500), (600, 600))
            ]

# Goal position
goal = (1000, 4000)

# The number of timesteps to simulate 
num_steps = 50

# The timestep in seconds
delta_t = 1 

def compute_new_positioning(robot_x_position, robot_y_position, robot_heading, linear_speed_left, linear_speed_right, 
                            wheel_separation, delta_t):
    """
    Computes the new x,y position and heading (theta) of the robot

    Parameters
    ----------
    robot_x_position : previous x coordinate
    robot_y_position : previous y coordinate
    robot_heading : previous heading
    linear_speed_left : left wheel linear speed 
    linear_speed_right : right wheel linear speed
    wheeel_separation : distance between left and right wheel
    delta_t : period that the robot moves for in seconds

    Returns
    -------
    x, y, theta : The new position and heading
    """

    # Compute angular speed of the robot
    ang_speed_robot = (linear_speed_left - linear_speed_right) / wheel_separation

    # Multiply angular speed by time to get angular displacement
    angle_change = ang_speed_robot * delta_t

    # Compute average of left and right wheel speed
    ave_speed = 0.5 * (linear_speed_left + linear_speed_right)

    # Compute sinc
    if angle_change**2 < 0.1**2:
        # Taylor series for small values
        the_sinc = 1 - (0.25 * angle_change**2 / 6.0)

    else:
        the_sinc = sin(0.5 * angle_change) / (0.5 * angle_change)

    # Update position
    robot_x_position = robot_x_position + ave_speed * delta_t * the_sinc * sin(robot_heading + 0.5 * angle_change)
    robot_y_position = robot_y_position + ave_speed * delta_t * the_sinc * cos(robot_heading + 0.5 * angle_change)

    # Update heading
    robot_heading = robot_heading + angle_change

    return robot_x_position, robot_y_position, robot_heading

def random_walk():

    """
    Returns randomly generated linear wheel speed for left and right wheel
    """

    # Set the angular wheel speeds to be random numbers between 0 and 5
    ang_speed_left = 5 * random()
    ang_speed_right = 5 * random()

    # Convert angular speeds into linear speeds
    linear_speed_left = ang_speed_left * wheel_radius
    linear_speed_right = ang_speed_right * wheel_radius
    
    return linear_speed_left, linear_speed_right

def goal_seek(step, angle_change, distance_robot, 
              delta_t, wheel_separation, num_steps):
    
    """
    Moves robot to goal position in a straight line over 
    specified number of timesteps

    Parameters
    ----------
    step : Current step in simulation
    angle_change : Angle to move through to point robot heading towards goal
    distance_robot : Distance from robot original position to goal
    delta_t : Period that the robot moves for in seconds
    wheel_separation : Distance between left and right wheel
    num_steps : Total number of steps in simulation
    delta_t : Period that the robot moves for in seconds

    Returns
    -------
    linear_speed_left, linear_speed_right : The left and right wheel 
    speed for the current step in the simulation
    """
    # Turn to face heading
    if step == 0:

        # Compute wheel displacement from robot angular displacement
        linear_displacement_left =  angle_change * wheel_separation / 2
        linear_displacement_right = -linear_displacement_left

        # Compute wheel linear speed
        linear_speed_left = linear_displacement_left / delta_t
        linear_speed_right = linear_displacement_right / delta_t

    # Move in straight line to heading
    else:

        # Compute linear speed of robot
        ave_speed = distance_robot / (num_steps - 1)

        # Compute wheel linear speeds
        linear_speed_left = linear_speed_right = ave_speed

    return linear_speed_left, linear_speed_right

def detect_obstacles(robot_x_position, 
                      robot_y_position, 
                      obstacles):
    
    """
    Detects if the robot has collided with a wall or obstacle

    Parameters
    ----------
    robot_x_position : x coordinate
    robot_y_position : y coordinate
    obstacles : list of positions and dimensions of obstacles 

    Returns
    -------
    obstacle_detected : True if obstacle detected, else False
    obstacle_type : 'obstacle' or 'wall'
    """

    # Initailise variables
    obstacle_detected = False
    obstacle_type = None

    # Detect obstacles    
    for ii in obstacles:
        obstacle_x = ii[0][0]
        obstacle_y = ii[0][1]
        obstacle_width = ii[1][0]
        obstacle_height = ii[1][1]

        if (obstacle_x < robot_x_position < obstacle_x + obstacle_width and 
            obstacle_y < robot_y_position < obstacle_y + obstacle_height):

            obstacle_detected = True
            obstacle_type = 'obstacle'

    # Detect edges of map
    if (robot_x_position > map_x_max or
        robot_x_position < map_x_min or
        robot_y_position > map_y_max or
        robot_y_position < map_y_min):

        obstacle_detected = True
        obstacle_type = 'wall'

    return obstacle_detected, obstacle_type

def avoid_obstacle_maneuver(wheel_separation):
        
    """
    Returns wheel speed for left and right wheel to turn 180 degrees 
    on the spot in one timestep (1 second)
    """
    linear_displacement_left =  pi * wheel_separation / 2
    linear_displacement_right = -linear_displacement_left

    linear_speed_left = linear_displacement_left / delta_t
    linear_speed_right = linear_displacement_right / delta_t 

    return linear_speed_left, linear_speed_right

def update_log_file(position, heading, obstacle_type):

    # Generate time stamp
    time_now = perf_counter()
    time_stamp = round((time_now - start_time), 3)

    # Generate state information
    if obstacle_type==None:
        state = ''
    else:
        state = 'Collision with ' + obstacle_type

    # Generate position information 
    for ii in range(len(position)):
        position[ii] = round(position[ii], 3)

    # Generate heading information 
    heading = round(heading, 3)

    # Generate row to write to log file
    row = [time_stamp, position, heading, state]
    
    # Open the CSV file in append mode
    with open(log_file_name, 'a', newline='') as file:
        writer = csv.writer(file)

        # Append a single row
        writer.writerow(row)  


def main():

    # Initial robot configuration
    robot_x_position = 500
    robot_y_position = 500
    robot_heading = 0

    # Initialise visualisation
    init_plot(robot_x_position, 
              robot_y_position, 
              robot_heading)
    
    # Initialise log file with column headings
    with open(log_file_name, 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Time (s)','Position [x,y]',
                         'Orientation (rads)','State information']) 

    # Compute angle to turn robot to face goal
    angle_change = atan2(goal[0] - robot_x_position, 
                         goal[1] - robot_y_position) - robot_heading
    
    print('Angle to turn is', angle_change, 'radians')

    # Compute distance to goal 
    distance_robot = sqrt((goal[0] - robot_x_position)**2 + 
                          (goal[1] - robot_y_position)**2)
    
    print('Distance to travel is', distance_robot)

    for step in range(num_steps):

        if mode == 'goal_seek_mode':
            linear_speed_left, linear_speed_right = goal_seek(step, 
                                                              angle_change, 
                                                              distance_robot,
                                                              delta_t, 
                                                              wheel_separation, 
                                                              num_steps)
            
        elif mode == 'random_walk_mode':
            linear_speed_left, linear_speed_right = random_walk()

        # Compute new position and orientation
        robot_x_position_new, robot_y_position_new, robot_heading_new = compute_new_positioning(robot_x_position, 
                                                                                                robot_y_position, 
                                                                                                robot_heading, 
                                                                                                linear_speed_left, 
                                                                                                linear_speed_right, 
                                                                                                wheel_separation, 
                                                                                                delta_t)                   

        # OBSTACLE AVOIDANCE 
        if avoid_obstacles:
            obstacle_detected, obstacle_type = detect_obstacles(robot_x_position_new, 
                                                                robot_y_position_new, 
                                                                obstacles)

            if obstacle_detected:

                # Turn 180 degrees on the spot if collision with obstacle is detected 
                linear_speed_left, linear_speed_right = avoid_obstacle_maneuver(wheel_separation)

                # Compute new position and orientation
                robot_x_position_new, robot_y_position_new, robot_heading_new = compute_new_positioning(robot_x_position, 
                                                                                                        robot_y_position, 
                                                                                                        robot_heading, 
                                                                                                        linear_speed_left, 
                                                                                                        linear_speed_right, 
                                                                                                        wheel_separation, 
                                                                                                        delta_t)
        else:
            obstacle_type = None

        # Update robot state
        robot_x_position = robot_x_position_new
        robot_y_position = robot_y_position_new
        robot_heading = robot_heading_new

        # Plot robot at current state
        snapshot(robot_x_position, robot_y_position, robot_heading)
        
        # Update log file
        update_log_file([robot_x_position, robot_y_position], 
                        robot_heading, 
                        obstacle_type)

        # Display current frame 
        show_plot(map_coords, goal=goal, obstacles=obstacles, pause=0.1)

    # Display final frame 
    show_plot(map_coords, goal=goal, obstacles=obstacles)

if __name__ == '__main__':
    main()