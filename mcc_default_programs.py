from pybricks.parameters import Button, Color, Side, Stop
from pybricks.tools import wait, StopWatch
from mcc_universal_classes import *


""" Default Programs for calibration of drivebase settings as well as light
sensors/line following."""

def turn_1080(bot:Robot):
    """Code to Calibrate Turns (Wheel Distance)
    If it doesn't turn enough increase axle distance in default_values_objects
    If it turns too far decrease axle distance in default_values_objects"""
    drive_base = bot.drive_base
    drive_base.turn(1080)
    drive_base.set_default_speed()
    
TURN_CALLIBRATION_PROGRAM = RobotProgram(turn_1080, "T", Color.RED)



def straight_1000mm(bot:Robot):
    """Code to Calibrate Movement Wheel Size. Drives 1 meter. If too short decrease
    wheel diameter. If too long increase wheel diameter"""
    drive_base = bot.drive_base
    drive_base.set_robot_speed(50)
    drive_base.straight(1000)
    drive_base.set_default_speed()

STRAIGHT_CALLIBRATION_PROGRAM = RobotProgram(straight_1000mm, "S", Color.BLUE)

def light_sample(bot:Robot):
    """ Drives around recording light values and reports the min/max for each 
    sensor and gives recommendations for settings of black and white"""
    light_base = bot.light_base
    drive_base = bot.drive_base
    min_left = 50
    max_left = 50
    min_right = 50
    max_right = 50
    drive_base.reset()
    while drive_base.distance() < 500:
        left_light = light_base.reflectance(Side.LEFT)
        right_light = light_base.reflectance(Side.RIGHT)
        min_left = min(left_light, min_left)
        max_left = max(left_light, max_left)
        min_right = min(right_light, min_right)
        max_right = max(right_light, max_right)
        drive_base.drive(50, 0)    
    print("Maximum: Left: ", max_left, " Right: ", max_right)
    print("Minimum: Left: ", min_left, " Right: ", min_right)
    print("Set White: ", (max_right + max_left)/2 - 10)
    print("Set Black: ", (min_left + min_right)/2 + 10)
    print("Threshold: ", (((max_right + max_left)/2 - 10) + ((min_left + min_right)/2 + 10))/2)
    drive_base.stop()
LIGHT_CALIBRATION_PROGRAM = RobotProgram(light_sample, "L", Color.WHITE)


def launch_rc(bot:Robot):
    bot.setup_RC()
RC_MODE_PROGRAM = RobotProgram(launch_rc, "R", Color.GREEN)
