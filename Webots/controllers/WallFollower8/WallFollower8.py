from controller import Robot

robot = Robot()
# get the time step of the current world.
max_speed = 3.14
time_step = 32

motor1 = robot.getDevice("Ban1")
motor2 = robot.getDevice("Ban2")
motor3 = robot.getDevice("Ban3")
motor4 = robot.getDevice("Ban4")

motor1.setPosition(float('inf'))
motor2.setPosition(float('inf'))
motor3.setPosition(float('inf'))
motor4.setPosition(float('inf'))

motor1.setVelocity(0.0)
motor2.setVelocity(0.0)
motor3.setVelocity(0.0)
motor4.setVelocity(0.0)

left_sensor = robot.getDevice('SLEFT')
left_sensor.enable(time_step)

right_sensor = robot.getDevice('SRIGHT')
right_sensor.enable(time_step)

rightbot_sensor = robot.getDevice('RightBot')
rightbot_sensor.enable(time_step)

LeftBot_sensor = robot.getDevice('LeftBot')
LeftBot_sensor.enable(time_step)

midleft_sensor = robot.getDevice('SMIDL')
midleft_sensor.enable(time_step)

motor1_speed = max_speed /2
motor2_speed = max_speed /2
motor3_speed = max_speed /2
motor4_speed = max_speed /2

ki = 0.0002
kp = 0.015
kd = 0.0001
errL = 0
W_int = 0

while robot.step(time_step) != -1:
    
    left_sensor_value = left_sensor.getValue()
    LeftBot_sensor_value = LeftBot_sensor.getValue()
    midleft_sensor_value = midleft_sensor.getValue()
    right_sensor_value = right_sensor.getValue()
    rightbot_sensor_value = rightbot_sensor.getValue()
    
    left_wall = LeftBot_sensor_value < 300 and rightbot_sensor_value < 400 and left_sensor_value <= 300
    
    print("left: {} leftBot: {} right: {} midleft: {} rightbot: {}".format(left_sensor_value, LeftBot_sensor_value, right_sensor_value, midleft_sensor_value, rightbot_sensor_value))
    
    if (right_sensor_value >=  200) and (midleft_sensor_value > 600) and (left_sensor_value >= 350) and (LeftBot_sensor_value <=700) :
        motor2_speed = -max_speed / 2
        motor1_speed = max_speed * 3
        print ("Belok Kiri")
    else :
        err = left_wall - 100
        W_int = err - W_int
        W_der =  err - errL
    
        W_Corr = (kp * err) + (kd * W_der) + (ki * W_int)
        err = errL
        
        motor2_speed = (max_speed/2) - W_Corr
        motor3_speed = (max_speed/2) - W_Corr
        motor1_speed = (max_speed/2) + W_Corr
        Motor4_speed = (max_speed/2) + W_Corr
        print ("Drift Kanan")
    
    motor1.setVelocity(motor1_speed)
    motor2.setVelocity(motor2_speed)
    motor3.setVelocity(motor3_speed)
    motor4.setVelocity(motor4_speed)