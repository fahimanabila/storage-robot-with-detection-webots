from controller import Robot, Motor, GPS

# Time step in milliseconds
TIME_STEP = 64

# Initialize the robot and devices
robot = Robot()
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
gps = robot.getDevice('gps')

# Enable GPS
gps.enable(TIME_STEP)

# Set the initial motor speeds
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Function to move the robot forward
def move_forward(speed):
    left_motor.setVelocity(speed)
    right_motor.setVelocity(speed)

# Function to turn the robot left
def turn_left(speed):
    left_motor.setVelocity(-speed)
    right_motor.setVelocity(speed)

# Function to move the robot backward
def move_backward(speed):
    left_motor.setVelocity(-speed)
    right_motor.setVelocity(-speed)

# Specific coordinates to trigger actions
target_x_coordinate_left = 0.654548
target_y_coordinate_back = 0.522142445597
#0.5221424455977874
# Variable to keep track of the initial position
initial_position = None

# Variable to keep track of whether the robot has turned left
has_turned_left = False

# Main control loop
while robot.step(TIME_STEP) != -1:
    # Get the current GPS coordinates
    position = gps.getValues()
    x, y, z = position
    
    print(x,y)

    # Store the initial position
    if initial_position is None:
        initial_position = position

    # Check if the robot has reached the specific x-coordinate to turn left
    if x >= target_x_coordinate_left and not has_turned_left:
        turn_left(2.0)
        robot.step(1000)  # Adjust the duration as needed for a 90-degree turn
        has_turned_left = True
        move_forward(2.0)
    # Check if the robot has reached the specific x-coordinate to move backward
    elif y >= target_y_coordinate_back and has_turned_left:
        move_backward(2.0)
        # Continue moving backward until reaching the initial position
        while robot.step(TIME_STEP) != -1:
            position = gps.getValues()
            x, y, z = position
            initial_x, initial_y, initial_z = initial_position
            # Stop moving backward when the initial position is reached
            if abs(x - initial_x) < 0.05 and abs(z - initial_z) < 0.05:
                left_motor.setVelocity(0.0)
                right_motor.setVelocity(0.0)
                break
    else:
        move_forward(2.0)
