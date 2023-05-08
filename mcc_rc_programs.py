from pybricks.parameters import Button, Color, Side, Stop
from pybricks.tools import wait, StopWatch
from mcc_universal_classes import *

#### Remote Control Programs

"""This is where the Code to use remote controls with Technic Hubs resides.
We never use this code during the Robot Game, but we do use it to test and
iterate attachment designs, mission solutions, and mission approaches."""

def default_remote_func(bot:Robot):
    drive_base:MCCDriveBase = bot.drive_base
    rc_base:MCCRCBase = bot.rc_base
    attach_base:MCCAttachBase = bot.attach_base
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
            print("Robot has driven ", drive_base.distance(), " since last reset")
            print("Robot has turned ", drive_base.angle(), "since last reset")
            print("Resetting the cumulative distance/angle")
            drive_base.reset()
            wait(200)
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
    attach_base.left_attach_motor.run(left_attach)
    attach_base.right_attach_motor.run(right_attach)        
DEFAULT_RC_PROGRAM = RemoteProgram(default_remote_func)




