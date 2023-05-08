"""
This is the file where the various robot parts are loaded and combined to make 
a Prime Hub Robot (load/compile this file to create a Prime Hub Bot)
Every is encapsulated and compartmentalized makes it less intimidating for our 
team members who are still learning python as it makes the file
much smaller and easier to navigate. This also means that it is easy for each team
member to write programs/functions and add them to the libary later and not worry
about breaking anything. 
"""

### Required pybricks modules will not need to be changed
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch

### MC^2 modules needed, should not need to be changed
from mcc_math import *
from mcc_universal_classes import *
from mcc_prime import PrimeRobot, MCCPrimeHub
from mcc_default_values_objects import *

### Choose which programs to load from the modules. MAY NEED TO LOAD DIFFERENT PROGRAMS/CHANGE THIS CODE
from mcc_default_programs import RC_MODE_PROGRAM, TURN_CALLIBRATION_PROGRAM, STRAIGHT_CALLIBRATION_PROGRAM, LIGHT_CALIBRATION_PROGRAM
from ets_superpowered_programs import RUN1_PROGRAM, RUN2_PROGRAM, RUN3_PROGRAM, RUN4_PROGRAM, RUN5_PROGRAM, LINE_FOLLOW_DEMO

""" 
Can use the area below to work on a program. Once program is finalized it will be
placed in an apporpriate file and can be imported. This keeps the workspace
clean and makes autocompletion work better.
"""


def demo_func(bot:Robot):
    drive_base = bot.drive_base
    attach_base = bot.attach_base
    drive_base.straight(300)
    drive_base.turn(90)
    drive_base.straight(300)
    drive_base.turn(90)
    drive_base.straight(300)
    drive_base.turn(90)
    drive_base.straight(150)
    drive_base.turn(360)
    attach_base.right_attach_motor.run_angle(100, -50)
    attach_base.right_attach_motor.run_angle(100,50)


demo_run = RobotProgram(demo_func, "A", Color.YELLOW)



"""
Make A Bot. Definte the classes that are unique to the Prime Hub
use the defaults from other files for rthe universal parts
This bot is called Toasty, our Technic Hub bots are called Crostini. Will need
to change the program list but otherwise this code doesn't need to be changed
"""
### Choose which programs you want displayed/loaded to the bot. WILL NEED TO CHANGE AS NEEDED
PROGRAM_LIST = [RUN1_PROGRAM, RUN2_PROGRAM, RUN3_PROGRAM, RUN4_PROGRAM, RUN5_PROGRAM, RC_MODE_PROGRAM, LIGHT_CALIBRATION_PROGRAM, TURN_CALLIBRATION_PROGRAM, STRAIGHT_CALLIBRATION_PROGRAM, LINE_FOLLOW_DEMO]


ROBOT_DRIVE = MCCDriveBase(
    WHEEL_SIZE, 
    WHEEL_SPACING, 
    Motor(Port.B),
    Motor(Port.A, Direction.COUNTERCLOCKWISE),
    DEFAULT_DRIVEBASE_SETTINGS)

### No need to touch code below this line
ROBOT_LIGHT = MCCLightBase(ColorSensor(Port.E), ColorSensor(Port.F))
PRIME_HUB = MCCPrimeHub(PROGRAM_LIST, ROBOT_BUTTON_MAP)
PrimeBot = PrimeRobot(PRIME_HUB, ROBOT_DRIVE, ROBOT_LIGHT, ROBOT_ATTACHMENTS, ROBOT_RC, LIGHT_DEFAULT)

""" 
Run the master loop. This checks for button pushes, loads the right programs
and will shut down the bot if no inputs for 10 minutes to save energy
"""

PrimeBot.master_loop()
