
"""
This is the file where the various robot parts are loaded and combined to make 
a Technic Hub Robot (load/compile this file to create a Technic Hub Bot)
"""
### Required pybricks modules will not need to be changed
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.tools import wait, StopWatch

### MC^2 modules needed, should not need to be changed
from mcc_technicbot_classes import *
from mcc_universal_classes import *

### Choose which programs to load from the modules. 
### MAY NEED TO LOAD DIFFERENT PROGRAMS/CHANGE THIS CODE
from mcc_default_programs import RC_MODE_PROGRAM
from mcc_rc_programs import *


""" 
Can use the area below to work on a robot run/program. Once program is
 finalized it will beplaced in an apporpriate file and can be imported.
 This keeps the workspaceclean and makes autocompletion work better.
"""


"""
 Choose which programs you want displayed/loaded to the bot.
  WILL NEED TO CHANGE AS NEEDED
 """
PROGRAM_LIST = [RC_MODE_PROGRAM]

RC_LIST = [DUALMOTOR_RC_PROGRAM]


### Constants (Can change as needed)
LIGHT_DEFAULT = MCCLightValues(25, 89, porportional_coefficient= 1.5)
WHEEL_SIZE = 86.6
WHEEL_SPACING = 128

DEFAULT_DRIVEBASE_SETTINGS = RobotSpeedSettings(
    500, ## Speed in mm/s
    350, ## acceleration in mm/s2
    500, ## turn rate
    300) ## turn acceleration         

RC_SPEED_SETTINGS = RobotSpeedSettings(
    300,
    200,
    150,
    200,
    500,
    500)

### Definte parts of the robot/create an instance of PrimeBot
ROBOT_RC = MCCRCBase(RC_LIST, RC_SPEED_SETTINGS)

ROBOT_DRIVE = MCCDriveBase(
    WHEEL_SIZE, 
    WHEEL_SPACING, 
    Motor(Port.B),
    Motor(Port.A, Direction.COUNTERCLOCKWISE),
    DEFAULT_DRIVEBASE_SETTINGS)


TECHNIC_HUB = MCCTechnicHub(Axis.Y, Axis.Z, list_of_robot_programs= PROGRAM_LIST)
TECHNIC_ROBOT = TechnicRobot(TECHNIC_HUB, ROBOT_DRIVE, Motor(Port.C), Motor(Port.D),
 ROBOT_RC)

""" 
Run the master loop. This checks for button pushes, loads the right programs
and will shut down the bot if no inputs for 10 minutes to save energy
"""
TECHNIC_ROBOT.master_loop()