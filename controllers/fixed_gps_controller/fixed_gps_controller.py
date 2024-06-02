# Initiation
from controller import Robot, Motor, GPS, DistanceSensor

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

# Initialize the distance sensors
distance_sensors = []
sensor_names = [
    'ps0', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7'
]

for sensor_name in sensor_names:
    sensor = robot.getDevice(sensor_name)
    sensor.enable(TIME_STEP)
    distance_sensors.append(sensor)

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

# Function to check if the robot has hit a wall
def has_hit_wall(threshold=100):
    for sensor in distance_sensors:
        if sensor.getValue() > threshold:
            return True
    return False
    
# Variable to keep track of whether the robot has turned and spinned
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
    # print(position)
    
    if has_hit_wall():
        if x >= 0.653411 and not has_turned:
        
            has_turned = True
            turn_left(2.0)
            robot.step(1100)
            move_forward(2.0)
            print("Robot terhalang di antara Gudang A & B")
            
        elif x <= 0.432527 and not has_spinned:
        
            has_spinned = True
            turn_left(2.0)
            robot.step(2200)
            move_forward(2.0)
            print("Peringatan : Gudang A penuh!")
            
        elif x >= 0.895677 and not has_spinned2:
        
            has_spinned2 = True
            has_turned2 = False
            turn_left(2.0)
            robot.step(2200)
            move_forward(2.0)
            print("Peringatan : Gudang B penuh!")
             
        elif x <= 0.686364 and not has_turned2:
        
            has_turned2 = True
            has_turned3 = False
            stop_robot()
            print("kondisi empat")
            
        elif x <= 0.649165 and not has_turned3:
        
            has_turned3 = True
            has_spinned3 = False
            stop_robot()
            print("Robot terhalang di antara Gudang C & D")
            
        elif x <= 0.427919 and not has_spinned3:
        
            has_spinned3 = True
            has_spinned4 = False
            turn_left(2.0)
            robot.step(2250)
            move_forward(2.0)
            print("Peringatan : Gudang C penuh!")
            
        elif x >= 0.902517 and not has_spinned4:
        
            has_spinned4 = True
            has_turned4 = False
            turn_left(2.0)
            robot.step(2200)
            move_forward(2.0)
            print("Peringatan : Gudang D penuh!")
            
        elif x <= 0.656104 and not has_turned4:
        
            has_turned4 = True
            has_turned5 = False
            print("kondisi delapan")
            
        elif x <= 0.639906 and not has_turned5:
        
            has_turned5 = True
            has_spinned5 = False
            stop_robot()
            print("Robot terhalang di antara Gudang E & F")
            
        elif x <= 0.446102 and not has_spinned5:
        
            has_spinned5 = True
            has_spinned6 = False
            turn_left(2.0)
            robot.step(2250)
            move_forward(2.0)
            print("Peringatan : Gudang E penuh!")
            
        elif x >= 0.909499 and not has_spinned6:
        
            has_spinned6 = True
            has_turned6 = False
            turn_left(2.0)
            robot.step(2200)
            move_forward(2.0)
            print("Peringatan : Gudang F penuh!")
            
        elif x <= 0.656104 and not has_turned6:
        
            has_turned6 = True
            has_spinned7 = False
            stop_robot()
            print("Robot terhalang kembali ke posisi awal")
            
        else:
            move_forward(2.0)

        # print("The robot has hit a wall.")
    else:
        move_forward(2.0)

# PHASE 1 Gudang A & B
    
    if x >= 0.654548 and not has_turned: #1
        turn_left(2.0)
        robot.step(1100)
        has_turned = True
    else:
        move_forward(2.0)
    
    if x <= 0.290518 and not has_spinned:
        turn_left(2.0)
        robot.step(2200)
        has_spinned = True
    else:
        move_forward(2.0)
        
    if x >= 1.058565 and not has_spinned2:
        turn_left(2.0)
        robot.step(2200)
        has_spinned2 = True
        has_turned2 = False 
    else:
        move_forward(2.0)
        
    if x <= 0.686364 and not has_turned2:
        turn_right(2.0)
        robot.step(1000)
        has_turned2 = True
        has_turned3 = False
    else:
        move_forward(2.0)     

# PHASE 2 Gudang C & D    
    
    if x <= 0.645309 and not has_turned3:
        turn_left(2.0)
        robot.step(1000)
        has_turned3 = True
        has_spinned3 = False
    else:
        move_forward(2.0)  
        
    
    if x <= 0.244206 and not has_spinned3:
        turn_left(2.0)
        robot.step(2250)
        has_spinned3 = True
        has_spinned4 = False
    else:
        move_forward(2.0)
    
    
    if x >= 1.079676 and not has_spinned4:
        turn_left(2.0)
        robot.step(2200)
        has_spinned4 = True
        has_turned4 = False
    else:
        move_forward(2.0)
        
    if x <= 0.689696 and not has_turned4:
        turn_right(2.0)
        robot.step(1000)
        has_turned4 = True
        has_turned5 = False
    else:
        move_forward(2.0)

# PHASE 3 Gudang E & F

    if x <= 0.631000 and not has_turned5:
        turn_left(2.0)
        robot.step(1000)
        has_turned5 = True
        has_spinned5 = False
    else:
        move_forward(2.0)
    
    if x <= 0.289962 and not has_spinned5:
        turn_left(2.0)
        robot.step(2250)
        has_spinned5 = True
        has_spinned6 = False
    else:
        move_forward(2.0)  
    
    if x >= 1.120987 and not has_spinned6:
        turn_left(2.0)
        robot.step(2200)
        has_spinned6 = True
        has_turned6 = False
    else:
        move_forward(2.0) 
       
    if x <= 0.656104 and not has_turned6:
        turn_left(2.0)
        robot.step(1050)
        has_turned6 = True
        has_spinned7 = False
    else:
        move_forward(2.0)