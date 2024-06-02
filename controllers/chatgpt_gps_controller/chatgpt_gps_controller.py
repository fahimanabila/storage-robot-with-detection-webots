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

# Function to turn the robot left
def turn_right(speed):
    left_motor.setVelocity(speed)
    right_motor.setVelocity(-speed)

# Function to make the robot stop
def stop_robot ():
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

# Variable to keep track of whether the robot has turned
has_turned = False
has_turned2 = True
has_turned3 = True
has_turned4 = True
has_turned5 = True
has_turned6 = True

has_spinned = False
has_spinned2 = False
has_spinned3 = True
has_spinned4 = True
has_spinned5 = True
has_spinned6 = True
has_spinned7 = True

# Main control loop
while robot.step(TIME_STEP) != -1:
    # Get the current GPS coordinates
    position = gps.getValues()
    x, y, z = position
    print(position)

# PHASE 1
    # Check if the robot has reached the specific x-coordinate and hasn't turned yet
    if x >= 0.654548 and not has_turned:
        turn_left(2.0)
        # Let the robot turn for a short duration
        robot.step(1100)  # Adjust the duration as needed
        has_turned = True
    else:
        move_forward(2.0)
    
    # Check if the robot has reached the specific x-coordinate and hasn't turned yet
    if x <= 0.290518 and not has_spinned:
        turn_left(2.0)
        # Let the robot turn for a short duration
        robot.step(2200)  # Adjust the duration as needed
        has_spinned = True
    else:
        move_forward(2.0)
        
    #1.0585652244672425, 0.5564122272809321, 0.04853386451399671]
    if x >= 1.058565 and not has_spinned2:
        turn_left(2.0)
        # Let the robot turn for a short duration
        robot.step(2200)  # Adjust the duration as needed
        has_spinned2 = True
        has_turned2 = False 
    else:
        move_forward(2.0)
        
    if x <= 0.686364 and not has_turned2:
        turn_right(2.0)
        # Let the robot turn for a short duration
        robot.step(1000)  # Adjust the duration as needed
        has_turned2 = True
        has_turned3 = False
    else:
        move_forward(2.0)     

# PHASE 2    
    
    if x <= 0.641213 and not has_turned3:
        turn_left(2.0)
        # Let the robot turn for a short duration
        robot.step(1000)  # Adjust the duration as needed
        has_turned3 = True
        has_spinned3 = False
    else:
        move_forward(2.0)  
        
    
    if x <= 0.244206 and not has_spinned3:
        turn_left(2.0)
        # Let the robot turn for a short duration
        robot.step(2200)  # Adjust the duration as needed
        has_spinned3 = True
        has_spinned4 = False
    else:
        move_forward(2.0)
    
    
    if x >= 1.079676 and not has_spinned4:
        turn_left(2.0)
        # Let the robot turn for a short duration
        robot.step(2200)  # Adjust the duration as needed
        has_spinned4 = True
        has_turned4 = False
    else:
        move_forward(2.0)
        
    if x <= 0.656104 and not has_turned4:
        turn_right(2.0)
        # Let the robot turn for a short duration
        robot.step(1000) # Adjust the duration as needed
        has_turned4 = True
        has_turned5 = False
    else:
        move_forward(2.0)

# PHASE 3

    if x <= 0.639906 and not has_turned5:
        turn_left(2.0)
        # Let the robot turn for a short duration
        robot.step(1000)  # Adjust the duration as needed
        has_turned5 = True
        has_spinned5 = False
    else:
        move_forward(2.0)
    
    if x <= 0.190546 and not has_spinned5:
        turn_left(2.0)
        # Let the robot turn for a short duration
        robot.step(2250)  # Adjust the duration as needed
        has_spinned5 = True
        has_spinned6 = False
    else:
        move_forward(2.0)  
    
    if x >= 1.120987 and not has_spinned6:
        turn_left(2.0)
        # Let the robot turn for a short duration
        robot.step(2200)  # Adjust the duration as needed
        has_spinned6 = True
        has_turned6 = False
    else:
        move_forward(2.0) 
       
    if x <= 0.656104 and not has_turned6:
        turn_left(2.0)
        # Let the robot turn for a short duration
        robot.step(1100) # Adjust the duration as needed
        has_turned6 = True
        has_spinned7 = False
    else:
        move_forward(2.0) 
        