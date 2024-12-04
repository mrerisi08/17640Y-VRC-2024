# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       ashleycai                                                    #
# 	Created:      12/3/2024, 3:18:29 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import time

# Brain should be defined by default
brain=Brain()

# controllers
driveController = Controller()
mechController = Controller()

# drivetrain
leftMotor = Motor(Ports.PORT11)
rightMotor = Motor(Ports.PORT14, True)
driveTrain = DriveTrain(leftMotor, rightMotor)

intakeMotor = Motor(Ports.PORT13)


brain.screen.print("Hello V5")


# motor1 = Motor(Ports.PORT1)
# motor1.spin(FORWARD)
# time.sleep(2)
# motor1.stop()

driveTrain.drive_for(FORWARD, 100)