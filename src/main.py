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



# listeners
def driveLeftJoystickChanged():
    driveTrain.drive(FORWARD, driveController.axis3.position(), PERCENT)
    # # with open("data.txt", "a") as f:
    #     # f.write(str(driveController.axis3.position()) + "\n")
    # brain.screen.clear_screen()
    # brain.screen.print(driveController.axis3.position())
    # brain.screen.next_row()
    # brain.screen.print("ASDJHKL")
driveController.axis3.changed(driveLeftJoystickChanged)
# while True:
#     driveLeftJoystickChanged()
#     time.sleep(0.15)

brain.screen.print("Hello V5")


# motor1 = Motor(Ports.PORT1)
# motor1.spin(FORWARD)
# time.sleep(2)
# motor1.stop()

driveTrain.drive_for(FORWARD, 100)