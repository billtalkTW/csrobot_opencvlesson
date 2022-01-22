from controller import Robot
import math
import time
import cv2
import numpy as np

robot = Robot()
timeStep = 32

# init motor & encoder
leftMotor = robot.getDevice("wheel2 motor")    
rightMotor = robot.getDevice("wheel1 motor")
leftMotor.setPosition(float('inf'))            
rightMotor.setPosition(float('inf'))
leftEncoder = leftMotor.getPositionSensor()    
rightEncoder = rightMotor.getPositionSensor()
leftEncoder.enable(timeStep)                   
rightEncoder.enable(timeStep)

leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

# init distance sensors
distanceSensors = [] 
for i in range(5):
    distanceSensors.append(robot.getDevice("distance sensor" + str(i+1)))
    distanceSensors[i].enable(timeStep)

# init gps
gps = robot.getDevice("gps")
gps.enable(timeStep)
startX = gps.getValues()[0] 
startZ = gps.getValues()[2]

# init gyro
gyro = robot.getDevice("gyro")
gyro.enable(timeStep)
global rotation 
rotation = 0

# init colour sensor
hole = [b';;;\xff',b'---\xff',b'ooo\xff']
swamp = [b'\x82\xd2\xf0\xff',b'\x82\xd3\xee\xff',b'\x82\xd2\xee\xff',b'\x82\xd3\xee\xff',b'\x8f\xde\xf5\xff',b'\x8e\xde\xf5\xff']
checkpoint = [b'\xff\xff\xff\xff',b'\xfe\xfe\xfe\xff',b'\xfd\xfd\xfd\xff',b'\xfc\xfc\xfc\xff',b'\xfd\xfe\xfe\xff',b'\xfc\xfb\xfb\xff']
colour = robot.getCamera("colour_sensor")
colour.enable(timeStep)

# init cameras
rcamera = robot.getCamera("Rcamera")
rcamera.enable(timeStep)
lcamera = robot.getCamera("Lcamera")
lcamera.enable(timeStep)

# function for get distance values from No.1~No.5
def getDistance(sensorNum):
    return distanceSensors[sensorNum-1].getValue()

# function for get gyro value
def getGyro():
    diff_rotation = gyro.getValues()[1] * (timeStep / 1000)
    global rotation 
    rotation -= diff_rotation*90/math.pi
    return rotation

# function for get encoder values
def getEncoder(LorR):
    if(LorR == "left"):
        encoderValue = leftEncoder.getValue()
    elif(LorR == "right"):
        encoderValue = rightEncoder.getValue()
    return encoderValue

# function for get gps position
def getPosition(XorZ):
    if(XorZ == "x"):
        position = gps.getValues()[0]
    elif(XorZ == "z"):
        position = gps.getValues()[2]
    return position

# function for get colour value
def getColour():
    colourValue = colour.getImage()
    if colourValue in hole:
        return "hole"
    elif colourValue in swamp:
        return "swamp"
    elif colourValue in checkpoint:
        return "check point"
    else:
        return colourValue
    

def getCameraImg():
    img_r = rcamera.getImage()
    img_l = lcamera.getImage()
    r_img = np.array(np.frombuffer(img_r, np.uint8).reshape((rcamera.getHeight(), rcamera.getWidth(), 4)))
    r_img[:,:,2] = np.zeros([r_img.shape[0], r_img.shape[1]])  
    cv2.imwrite('image_r.jpg', r_img)
    l_img = np.array(np.frombuffer(img_l, np.uint8).reshape((lcamera.getHeight(), lcamera.getWidth(), 4)))
    l_img[:,:,2] = np.zeros([l_img.shape[0], l_img.shape[1]])
    cv2.imwrite('image_l.jpg', l_img)

def printSensorValues():
    print("----------distance sensor----------")
    for k in range(5):
        print("distance sensor" + str(k+1) + ": " + str(getDistance(k+1)))
    print("----------gyro sensor----------")
    print("gyro value: "+str(getGyro()))
    print("----------encoder----------")
    print("left encoder: "+str(getEncoder("left")))
    print("right encoder: "+str(getEncoder("right")))
    print("----------gps position----------")
    print("x-position: "+str(getPosition("x")))
    print("z-position: "+str(getPosition("z")))
    print("----------colour sensor----------")
    print(getColour())
    print("----------camera----------")
    getCameraImg()
    print("cameras take pictures done!!")

while robot.step(timeStep) != -1:
    printSensorValues()    
