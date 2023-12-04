from pybricks.parameters import Button, Color, Side, Stop
from pybricks.tools import wait, StopWatch
from mcc_universal_classes import *

#### Remote Control Programs

"""This is where the Code to use remote controls with Technic Hubs resides.
We never use this code during the Robot Game, but we do use it to test and
iterate attachment designs, mission solutions, and mission approaches."""

def default_remote_func(bot:PrimeRobot):
    drive_base:MCCDriveBase = bot.drive_base
    rc_base:MCCRCBase = bot.rc_base
    left = bot.left_attach
    right = bot.right_attach
    speed_settings:RobotSpeedSettings = rc_base.speed_settings
    ### Button List
    b_list = rc_base.remote.buttons.pressed()
    ### State variables
    straight = 0
    turn = 0
    left_attach = 0
    right_attach = 0
    ### Check buttons
    if Button.CENTER in b_list:
        rc_base.next_rc_control()
    elif Button.LEFT in b_list:
        if Button.RIGHT_PLUS in b_list:
            right_attach = speed_settings.right_attach
        elif Button.RIGHT_MINUS in b_list:
            right_attach = -speed_settings.right_attach
        elif Button.RIGHT in b_list:
            print("Robot has driven ", drive_base.distance(), " mm since last reset")
            print("Robot has turned ", drive_base.angle(), " degrees since last reset")
            print("Left attachment as moved ", left.angle(), " degrees since last reset")
            print("Right attachment as moved ", right.angle(), " degrees since last reset")
            print("Resetting the cumulative distance/angle")
            drive_base.reset()
            left.reset_angle(0)
            right.reset_angle(0)
            bot.hub_base.speaker.beep(500, 300)
        else:
            pass
    elif Button.RIGHT in b_list:
        if Button.LEFT_PLUS in b_list:
            left_attach = speed_settings.left_attach
        elif Button.LEFT_MINUS in b_list:
            left_attach = -speed_settings.left_attach
        else:
            pass
    else:
        if Button.LEFT_PLUS in b_list:
            straight = speed_settings.straight_speed
        elif Button.LEFT_MINUS in b_list:
            straight = -speed_settings.straight_speed
        else:
            pass
        if Button.RIGHT_MINUS in b_list:
            turn = -speed_settings.turn_speed
        elif Button.RIGHT_PLUS in b_list:
            turn = speed_settings.turn_speed
        else: 
            pass
    drive_base.drive(straight, turn)
    left.run(left_attach)
    right.run(right_attach)        

DEFAULT_RC_PROGRAM = RobotProgram(default_remote_func)


def dualmotor_remote_func(bot:PrimeRobot):
    drive_base:MCCDriveBase = bot.drive_base
    rc_base:MCCRCBase = bot.rc_base
    left = bot.left_attach
    right = bot.right_attach
    speed_settings:RobotSpeedSettings = rc_base.speed_settings
    ### Button List
    b_list = rc_base.remote.buttons.pressed()
    ### State variables
    straight = 0
    turn = 0
    left_attach = 0
    right_attach = 0
    ### Check buttons
    if Button.CENTER in b_list:
        rc_base.next_rc_control()
    elif Button.LEFT in b_list:
        left_attach = -speed_settings.left_attach
    elif Button.RIGHT in b_list:
        left_attach = speed_settings.left_attach
    else:
        if Button.LEFT_PLUS in b_list:
            straight = speed_settings.straight_speed
        elif Button.LEFT_MINUS in b_list:
            straight = -speed_settings.straight_speed
        else:
            pass
        if Button.RIGHT_MINUS in b_list:
            turn = -speed_settings.turn_speed
        elif Button.RIGHT_PLUS in b_list:
            turn = speed_settings.turn_speed
        else: 
            pass
    drive_base.drive(straight, turn)
    left.run(left_attach)
    right.run(-left_attach)
DUALMOTOR_RC_PROGRAM = RobotProgram(dualmotor_remote_func, light_color= Color.YELLOW)