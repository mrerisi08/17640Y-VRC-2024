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

driveController = Controller()
mechController = Controller()

leftMotor = Motor(Ports.PORT11)
rightMotor = Motor(Ports.PORT14, True)

driveTrain = DriveTrain(leftMotor, rightMotor)

intakeMotor: Motor = Motor(Ports.PORT8)
intakeMotor.set_velocity(100, PERCENT)

brain.screen.print("Hello V5")


# motor1 = Motor(Ports.PORT1)
# motor1.spin(FORWARD)
# time.sleep(2)
# motor1.stop()

driveTrain.drive_for(FORWARD, 100)

brain.screen.print(driveController.axis1.position())

def leftjoychange():
    driveTrain.drive(FORWARD,driveController.axis3.position(),PERCENT)
def rightjoychange():
    driveTrain.drive(FORWARD, driveController.axis1.position(), PERCENT)



def intake_func(forward):
    if forward:
        intakeMotor.spin(FORWARD)
    else:
        intakeMotor.spin(REVERSE)


def stop_intake():
    intakeMotor.stop()


driveController.axis1.changed(rightjoychange)
driveController.axis3.changed(leftjoychange)

mechController.buttonL1.pressed(intake_func, True)
mechController.buttonL2.pressed(intake_func, False)

# when L1 or L2 is released, stop_intake()
mechController.buttonL1.released(stop_intake)
mechController.buttonL2.released(stop_intake)

pneu = DigitalOut(brain.three_wire_port.b)
def push_func():
    pneu.set(True)

def pull_func():
    pneu.set(False)

mechController.buttonR1.pressed(push_func)
mechController.buttonR2.pressed(pull_func)