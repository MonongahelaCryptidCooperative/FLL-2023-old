from pybricks.parameters import Button, Color, Side, Stop
from pybricks.tools import wait, StopWatch
from mcc_universal_classes import *

## 1st Run Power plant
def power_plant(bot:Robot):
    """Uses blue attachment that starts on robot. Line up along wall
    Wall-hug by driving at a slight angle (attachment has a wheel). 
    mash into the power plant. 
    Flip up left arm to lift gate. Smash down right arm to release
    barrels. Catch the middle and right barrels and take back home. Takes ~ 5 seconds
    These are dumped into the toy factory during run 2. 
    Left barrel rolls over to the left start area"""
    drive_base = bot.drive_base
    attach_base = bot.attach_base
    drive_base.reset()
    attach_base.right_attach_motor.run_angle(500, 200, wait= False)
    attach_base.left_attach_motor.run_angle(500, -200, wait= False)
    drive_base.drive(500, -2)
    while (drive_base.distance() < 680):
        wait(1)
    drive_base.stop()
    wait(100)
    attach_base.left_attach_motor.run_time(100, 1200, wait=False)
    wait(200)
    attach_base.right_attach_motor.run_time(-1000, 1200, wait= False)
    wait(1000)
    drive_base.drive(-500, -2)
    while (drive_base.distance() > 0):
        wait(1)
    drive_base.stop()
    bot.hub_base.next_program()

RUN1_PROGRAM = RobotProgram(power_plant, "1", Color.BLUE)



"""Code to do 2nd Robot Run:
TV
Windmill
Rechargable Battery Pickup
Dump 2 barrels in the toy factory
Collect 2 looped water barrels
High Five
Collect Solar barrels
"""



def tv(bot:Robot):
    """ Drive forwards using an "S" turn to line up so the TV is pushed at the 
    center of the Robot's mass"""
    drive_base = bot.drive_base
    attach_base = bot.attach_base
    attach_base.right_attach_motor.run_angle(500, 220, wait= False)
    attach_base.left_attach_motor.run_angle(500, -300, wait= False)
    drive_base.drive(-100, 0)
    wait(400)
    drive_base.stop()
    wait(200)
    drive_base.reset()

    ## raise those attachements so they aren't in the way
    drive_base.curve(700, 13)
    drive_base.curve(700, -13)
    ## Do an S to make sure we hit the TV near the middle of the robot
    ## Drive forward squaring against the TV
    drive_base.reset()
    drive_base.drive(120, 0)
    while drive_base.distance() < 80:
        wait(3)
    wait(200)
    drive_base.stop()
    wait(50)
    drive_base.reset()

   
def windmill(bot:Robot):
    """dump 2 barrels into the toy factory. Then drive to the windmill"""
    drive_base = bot.drive_base  # makes it so we don't have to keep typing bot.drive_drivebase
    attach_base = bot.attach_base
    attach_base.left_attach_motor.dc(-35)
    attach_base.right_attach_motor.dc(25)
    drive_base.curve(-180, 45) # back up away from TV
    drive_base.straight(500) # Drive closer to windmill
    drive_base.turn(90)
    drive_base.straight(120, Stop.NONE)
    drive_base.drive(150, 0)
    wait(300)
    drive_base.stop()
    wait(100)
    drive_base.reset()
    #### Pump the windmill
    for i in range(0,2):
        drive_base.straight(-90)
        drive_base.straight(80, Stop.NONE)
        drive_base.drive(150, 0)
        wait(300)
        drive_base.stop()
        wait(100)
        drive_base.reset()

def get_battery(bot:Robot):
    drive_base = bot.drive_base
    attach_base = bot.attach_base
    drive_base.curve(-200, -40)
    drive_base.curve(-70, 40)
    drive_base.straight(-30, Stop.NONE)
    drive_base.set_robot_speed(10)
    drive_base.straight(-72)
    drive_base.set_default_speed()


def square_off_back_wall(bot:Robot):
    """ Square off the back wall"""
    drive_base = bot.drive_base
    drive_base.straight(190)
    drive_base.turn(140)
    drive_base.straight(-145, Stop.NONE)
    drive_base.drive(-100, 0)
    wait(400)
    drive_base.stop()
    wait(200)
    drive_base.reset()


def drive_to_car(bot:Robot):
    """ First line square on the line in front of the car so that our X/Y 
    coordinates are effectively reset (wall squared just prior to this)
    The robot's location is now accurate""" 
    drive_base = bot.drive_base
    attach_base = bot.attach_base
    drive_base.curve(175, 90)
    bot.line_square_white(50)

def flip_car(bot:Robot):
    """ Cozy up to the car and flip it with the right attachment"""
    drive_base = bot.drive_base
    attach_base = bot.attach_base
    drive_base.straight(75)
    drive_base.turn(30)
    attach_base.right_attach_motor.run_time(-1000, 1200, wait=False)
    wait(300)
    drive_base.turn(20)
    attach_base.right_attach_motor.run_time(1000, 1200)
    attach_base.right_attach_motor.run_time(-1000, 1200)
    attach_base.right_attach_motor.dc(30)

    

def drive_water_barrels(bot:Robot):
    """ drive away from the car. Find the line. Follow line to looped barrels
    scoop up barrels and secure by lowering the left attachment.""" 
    drive_base = bot.drive_base
    attach_base = bot.attach_base
    drive_base.turn(-20)
    attach_base.right_attach_motor.run_time(1000, 1000, wait= False)
    wait(300)
    drive_base.turn(-47)
    bot.find_line(Side.RIGHT)
    bot.line_follow(Side.RIGHT, Side.LEFT, 100, 50)
    bot.line_follow(Side.RIGHT, Side.LEFT, 100, 62, False)
    drive_base.set_robot_speed(50)
    drive_base.curve(100, -90)
    attach_base.left_attach_motor.run_time(1000, 1000)
    attach_base.left_attach_motor.dc(35)
    wait(100)
    drive_base.set_default_speed()



def high_five_and_solar(bot:Robot):
    """ Backup to push the high-five hand and obtain a solar barrel with the
    passive rear gate. Next drive over and get the two remaining solar barrels 
    by also backing over them with the rear passive gate"""
    drive_base = bot.drive_base
    #### High Five
    drive_base.set_robot_speed(50)
    drive_base.straight(-100)
    drive_base.turn(-45)
    drive_base.straight(-90)
    drive_base.turn(45)
    drive_base.set_default_speed()
    drive_base.straight(-140, Stop.NONE)
    drive_base.drive(-100, 0)
    wait(400)
    drive_base.stop()
    wait(200)
    drive_base.reset()
    drive_base.straight(20)
    drive_base.curve(250, -45)
    drive_base.curve(-110, 45)
    drive_base.curve(-220, -30)
    drive_base.curve(-220, 30)
    drive_base.straight(-60)
    drive_base.turn(90)
    drive_base.straight(-105, Stop.NONE)
    drive_base.drive(-100, 0)
    wait(400)
    drive_base.stop()
    wait(200)
    drive_base.reset()


def drive_home(bot:Robot):
    """Drive over to the hydroelectric dam and flip the side level using
    the right attachment then drive to home."""
    drive_base = bot.drive_base
    attach_base = bot.attach_base
    left_attach = attach_base.left_attach_motor
    right_attach = attach_base.right_attach_motor
    drive_base.straight(100)
    drive_base.curve(100, 50)
    drive_base.straight(300, Stop.NONE)
    drive_base.curve(300, -10, Stop.NONE)
    drive_base.straight(450, Stop.COAST)
    left_attach.dc(-50)
    right_attach.dc(35)

def run2_func(bot:PrimeRobot):
    """ Combines all of the individual parts of run2 and calls the functions
    in the correct order uses the Red attachment"""
    tv(bot)
    windmill(bot)
    get_battery(bot)
    square_off_back_wall(bot)
    drive_to_car(bot)
    flip_car(bot)
    drive_water_barrels(bot)
    high_five_and_solar(bot)
    drive_home(bot)
    bot.hub_base.next_program()

RUN2_PROGRAM = RobotProgram(run2_func, "2", Color.RED)


""" Third Robot run
Drive forward use the right active attachement to obtain the 3rd looped barrel 
and energy barrel released by the hydroelectric dam"""


def hydro_electric_func(bot:Robot):
    drive_base = bot.drive_base
    attach_base = bot.attach_base
    left_attach = attach_base.left_attach_motor
    right_attach = attach_base.right_attach_motor
    left_attach.run_angle(1000, -300, wait= False)
    right_attach.run_angle(1000, 200, wait= False)
    drive_base.drive(-100, 0)
    bot.hub_base.speaker.beep(duration=400)
    drive_base.stop()
    wait(200)
    drive_base.reset()
    drive_base.set_robot_speed(50)
    drive_base.curve(335, 50)
    right_attach.run_angle(1000, -200, wait= False)
    drive_base.straight(85)
    right_attach.run(1000)
    drive_base.straight(-15)
    left_attach.run_angle(1000, 150)
    left_attach.dc(40)
    right_attach.dc(40)
    drive_base.set_robot_speed(10)
    drive_base.straight(-30, Stop.NONE)
    drive_base.set_default_speed()
    drive_base.straight(-580, Stop.COAST)
    left_attach.run_angle(1000, -300)
    left_attach.dc(-40)
    bot.hub_base.next_program()

RUN3_PROGRAM = RobotProgram(hydro_electric_func, "3", Color.RED)



def energy_storage(bot:Robot):
    """dump barrels and obtain sled from energy storage""" 
    drive_base = bot.drive_base
    attach_base = bot.attach_base
    left_attachment = bot.attach_base.left_attach_motor
    right_attachment = bot.attach_base.right_attach_motor
    left_attachment.run_angle(400, -300, wait= False)
    right_attachment.run_angle(400, 200, wait= False)
    drive_base.drive(-100, 0)
    bot.hub_base.speaker.beep(duration=400)
    drive_base.stop()
    wait(200)
    drive_base.curve(480, 39)
    drive_base.curve(480, -39)
    bot.find_line(Side.RIGHT)
    drive_base.straight(20)
    left_attachment.run(70)
    wait(2500)
    drive_base.curve(-500, -36, Stop.NONE)
    drive_base.straight(-600, Stop.COAST)
    left_attachment.dc(-45)
    right_attachment.dc(45)
    bot.hub_base.next_program()

RUN4_PROGRAM = RobotProgram(energy_storage, "4", Color.RED)



"""5th Robot run 
Switch attachments. On the 6th run we drive forward and place the looped barrels
Next we drop off a box containing the projet model and 3 energy barrels in the 
power to x area. Finally we drive around the toy factory to dump 3 barrels in 
the rechargable battery area then drive to the parking spot for the oil truck."""


def last_run(bot:Robot):
    drive_base = bot.drive_base
    attach_base = bot.attach_base
    left_attach = attach_base.left_attach_motor
    right_attach = attach_base.right_attach_motor
    left_attach.run_angle(200, -180, wait = False)
    right_attach.run_angle(200, 180, wait = False)
    drive_base.drive(-100, 0)
    bot.hub_base.speaker.beep(duration=400)
    drive_base.stop()
    wait(200)
    drive_base.reset()
    drive_base.set_robot_speed(70)
    drive_base.reset()
    drive_base.curve(1100, 16)
    drive_base.curve(1100, -16)
    drive_base.set_default_speed()
    for i in range(3):
        drive_base.straight(40)
        drive_base.straight(-40)
    drive_base.turn(65)
    drive_base.straight(420)
    drive_base.turn(40)
    bot.find_line(Side.LEFT)
    bot.line_follow(Side.LEFT, Side.RIGHT, 100, 10)
    drive_base.curve(-160, 45)
    drive_base.straight(-55, Stop.NONE)
    drive_base.drive(-200, 0)
    wait(300)
    right_attach.run_angle(1000, -200, wait = False)
    drive_base.stop()
    left_attach.run_angle(50, 300, wait = False)
    wait(1700)
    drive_base.reset()
    left_attach.run_angle(50, -300, wait = False)
    right_attach.run_angle(1000, 200, wait = False)
    drive_base.straight(65)
    drive_base.curve(160, 45)
    bot.line_follow(Side.LEFT, Side.RIGHT, 100, 250, False)
    drive_base.straight(75)
    drive_base.curve(100, 50)
    drive_base.straight(-200)

    

RUN5_PROGRAM = RobotProgram(last_run, "5", Color.YELLOW)




def line_follow_demo(bot:Robot):
    bot.find_line(Side.RIGHT)
    bot.line_follow(Side.RIGHT, Side.RIGHT, 150)

LINE_FOLLOW_DEMO = RobotProgram(line_follow_demo, "D", Color.MAGENTA)
