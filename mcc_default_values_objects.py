from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side
from mcc_universal_classes import *
from mcc_rc_programs import DEFAULT_RC_PROGRAM

"""This file has the default settings for various objects in our code.These
settings can be and are changed throughout the code, but in the absence of stated
values, these are the values the robot will use for the various objects."""

### Default Values (Can change as needed)


LIGHT_DEFAULT = MCCLightValues(20, 70, porportional_coefficient=1.8)

WHEEL_SIZE = 62.99
WHEEL_SPACING = 170


DEFAULT_DRIVEBASE_SETTINGS = RobotSpeedSettings(
    400, ## Speed in mm/s
    450, ## acceleration in mm/s2
    180, ## turn rate
    350) ## turn acceleration         

RC_SPEED_SETTINGS = RobotSpeedSettings(
    300,
    300,
    100,
    200,
    500,
    500)


ROBOT_BUTTON_MAP = HubButtonMap(Button.BLUETOOTH, Button.RIGHT, Button.LEFT, Button.CENTER)



ROBOT_RC = MCCRCBase([DEFAULT_RC_PROGRAM], RC_SPEED_SETTINGS)

ROBOT_ATTACHMENTS = MCCAttachBase(
    Motor(Port.C, gears=[[12, 20], [12, 20]]), ## Left Attachment Motor
    Motor(Port.D, gears=[[12, 20], [12, 20]])) ## Right Attachment Motor