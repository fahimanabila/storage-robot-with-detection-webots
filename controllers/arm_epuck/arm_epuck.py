from controller import Robot, Motor, PositionSensor

# Time step in milliseconds
TIME_STEP = 64

# Initialize the robot
robot = Robot()

# Initialize e-puck motors
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Initialize arm motors and sensors
arm_motor_1 = robot.getDevice('arm_motor_1')
arm_motor_2 = robot.getDevice('arm_motor_2')
arm_motor_1.setPosition(float('inf'))
arm_motor_2.setPosition(float('inf'))
arm_motor_1.setVelocity(0.0)
arm_motor_2.setVelocity(0.0)

arm_sensor_1 = robot.getDevice('arm_sensor_1')
arm_sensor_2 = robot.getDevice('arm_sensor_2')
arm_sensor_1.enable(TIME_STEP)
arm_sensor_2.enable(TIME_STEP)

# Function to move the e-puck forward
def move_forward(speed):
    left_motor.setVelocity(speed)
    right_motor.setVelocity(speed)

# Function to control the arm
def control_arm(target_position_1, target_position_2):
    arm_motor_1.setPosition(target_position_1)
    arm_motor_2.setPosition(target_position_2)

# Main control loop
while robot.step(TIME_STEP) != -1:
    # Move the e-puck forward
    move_forward(2.0)
    
    # Control the arm - example positions (radians)
    control_arm(0.5, -0.5)
    
    # Optionally read the current positions of the arm joints
    arm_position_1 = arm_sensor_1.getValue()
    arm_position_2 = arm_sensor_2.getValue()
    print(f"Arm positions: Joint 1 = {arm_position_1}, Joint 2 = {arm_position_2}")
