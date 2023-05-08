"""
This is the file where the various robot parts are loaded and combined to make 
a Technic Hub Robot. It also is where code/programs can be tried that are later added to our modules. 
Having things ecapsulated and compartmentalized makes it less intimidating for our 
team members who are still learning python as it makes the file
much smaller and easier to navigate. This also means that it is easy for each team
member to write programs/functions and add them to the libary later and not worry
about breaking anything. 
"""

from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch
from mcc_math import *
from mcc_universal_classes import *
from mcc_technic import MCCTechnicHub, TechnicRobot
from mcc_default_programs import RC_MODE_PROGRAM
from mcc_default_values_objects import *




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



##### Make a Technic Bot, defite parts exclusive to the technic hub
#### Rest come from the default values and objects file
TECHNIC_HUB = MCCTechnicHub()


ROBOT_DRIVE = MCCDriveBase(
    WHEEL_SIZE, 
    WHEEL_SPACING, 
    Motor(Port.B),
    Motor(Port.A, Direction.COUNTERCLOCKWISE),
    DEFAULT_DRIVEBASE_SETTINGS)

TechnicBot = TechnicRobot(TECHNIC_HUB, ROBOT_DRIVE, ROBOT_ATTACHMENTS, ROBOT_RC)



### Run the master loop to get into RC Mode or have the bot wait for a button press and run a single program.
### example of how you can use a remote.
TechnicBot.run_program(RC_MODE_PROGRAM)
TechnicBot.master_loop()
