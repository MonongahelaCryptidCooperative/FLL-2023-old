from pybricks.parameters import Button, Color, Side, Stop
from pybricks.tools import wait, StopWatch
from pybricks.hubs import PrimeHub
from mcc_icons_music import *
from mcc_primebot_classes import *
from mcc_default_programs import launch_rc


def rollingcamera_func(bot:PrimeRobot):
    ### Quality of life stuff
    drive_base = bot.drive_base
    left_attach = bot.left_attach
    right_attach = bot.right_attach
    speaker = bot.hub_base.speaker
    display = bot.hub_base.display
    drive_base.set_default()
    display.icon(SMILE)
    ### Get attachements in position
    left_attach.run_angle(1000, 400, wait = False)
    right_attach.dc(30)
    ### Start run code now
    speaker.beep(500, 500) 
    drive_base.reset()
    drive_base.set_robot_accel(50)
    drive_base.drive(300, -4)
    while(drive_base.distance() < 280):
        pass
    drive_base.stop()
    drive_base.set_default()
    drive_base.reset()
    drive_base.use_gyro(True)
    display.icon(CONCENTRATE)
    left_attach.reset_angle(0)
    ### Slaps the orange lever
    left_attach.run_angle(1000, -500, Stop.NONE)
    wait(300)
    left_attach.run_angle(300, 100, Stop.NONE)
    left_attach.run_angle(1000, 200, Stop.NONE)
    left_attach.run_angle(1000, 350, wait= False)
    ### Rams camera
    drive_base.straight(10, Stop.NONE)
    wait(200)
    display.icon(WINK)
    right_attach.run_angle(1000, -30, Stop.NONE)
    wait(200)
    drive_base.set_robot_accel(200)
    display.icon(SMILE)
    ### Goes back home
    drive_base.straight(-200, Stop.NONE)
    drive_base.use_gyro(False)
    drive_base.straight(-300, Stop.COAST)
    right_attach.stop()
    left_attach.stop()
    drive_base.set_default()
    drive_base.use_gyro(False)
    bot.hub_base.next_program()
ROLLINGCAMERA = RobotProgram(rollingcamera_func, "1", Color.YELLOW)

def stage_func(bot:PrimeRobot):
    ### Quality of life stuff
    drive_base = bot.drive_base
    left_attach = bot.left_attach
    right_attach = bot.right_attach
    speaker = bot.hub_base.speaker
    display = bot.hub_base.display
    drive_base.set_default()
    display.icon(SMILE)
    ### Get attachments into position
    left_attach.dc(-30)
    right_attach.stop()
    ### Square off of the wall
    drive_base.set_robot_accel(50)
    drive_base.drive(-100, 0)
    bot.hub_base.speaker.beep(500, 400)
    drive_base.stop()
    wait(100)
    drive_base.use_gyro(True)
    wait(100)
    drive_base.set_default()
    drive_base.reset()
    drive_base.straight(655)
    display.icon(RIGHT_SMILE)
    drive_base.curve(155, 15)
    display.icon(CONCENTRATE)
    drive_base.turn(-40)
    drive_base.straight(-100)
    display.icon(LEFT_SMILE)
    drive_base.turn(-35)
    drive_base.straight(140)
    display.icon(WINK)
    drive_base.turn(55)
    drive_base.straight(20, Stop.NONE)
    wait(50)
    drive_base.stop()
    drive_base.reset()
    drive_base.set_robot_accel(160)
    display.icon(SMILE)
    drive_base.curve(-400, 20)
    drive_base.straight(-250, Stop.NONE)
    drive_base.use_gyro(False)
    drive_base.straight(-350, Stop.COAST)
    drive_base.set_default()
    bot.hub_base.next_program()
STAGE = RobotProgram(stage_func, "2", Color.MAGENTA)

def chicken_func(bot:PrimeRobot):
    ### Quality of life stuff
    drive_base = bot.drive_base
    left_attach = bot.left_attach
    right_attach = bot.right_attach
    speaker = bot.hub_base.speaker
    display = bot.hub_base.display
    drive_base.set_default()
    display.icon(SMILE)
    ### Get attachements positioned
    left_attach.dc(30)
    ### Square off back wall
    drive_base.set_robot_accel(50)
    drive_base.drive(-100, 0)
    speaker.beep(500, 400)
    drive_base.stop()
    wait(100)
    drive_base.use_gyro(True)
    wait(100)
    drive_base.reset()
    drive_base.set_default()
    ### Start run
    display.icon(LEFT_SMILE)
    drive_base.curve(435, -45)
    display.icon(SMILE)
    drive_base.straight(135)
    display.icon(CONCENTRATE)
    ### Get Izzy
    left_attach.run_angle(300, -200, Stop.NONE)
    left_attach.dc(-30)
    ### Spin Chicken
    right_attach.dc(-100)
    display.icon(CONCENTRATE)
    drive_base.set_default()
    drive_base.drive(600, 0)
    wait(2700)
    display.icon(WINK)
    right_attach.stop()
    drive_base.stop()
    drive_base.reset()
    drive_base.set_robot_accel(160)
    ### Open craft machine
    drive_base.curve(-600, -20, Stop.NONE)
    display.icon(SMILE)
    drive_base.curve(-300, 20, Stop.NONE)
    drive_base.straight(-100, Stop.NONE)
    drive_base.use_gyro(False)
    drive_base.straight(-300, Stop.COAST)
    drive_base.set_default()
    bot.hub_base.next_program()
CHICKEN = RobotProgram(chicken_func, "3", Color.RED)



def light_show_func(bot:PrimeRobot):
    ### Quality of life stuff
    drive_base = bot.drive_base
    left_attach = bot.left_attach
    right_attach = bot.right_attach
    speaker = bot.hub_base.speaker
    display = bot.hub_base.display
    drive_base.set_default()
    display.icon(SMILE)
    ### Get attachments in position
    left_attach.dc(-30)
    ### Square off of back wall
    drive_base.set_robot_accel(50)
    drive_base.drive(-100, 0)
    speaker.beep(500, 500)
    drive_base.stop()
    wait(100)
    drive_base.use_gyro(True)
    wait(100)
    drive_base.reset()
    drive_base.set_default()
    ### Start run
    drive_base.set_robot_accel(60)
    drive_base.straight(310)
    display.icon(LEFT_SMILE)
    drive_base.curve(400, -90)
    display.icon(RIGHT_SMILE)
    drive_base.curve(425, 45)
    display.icon(WINK)
    ### Drop off art
    drive_base.straight(-110)
    drive_base.turn(-45)
    drive_base.straight(195)
    drive_base.turn(-90)
    ### Spin tower
    right_attach.dc(-100)
    drive_base.set_robot_accel(30)
    drive_base.drive(100, 0)
    wait(3400)
    display.icon(WINK)
    drive_base.stop()
    wait(100)
    drive_base.reset()
    drive_base.straight(-260)
    right_attach.stop()
    drive_base.straight(80)
    drive_base.set_default()
    display.icon(SMILE)
    drive_base.turn(-120)
    display.icon(CONCENTRATE)
    drive_base.straight(110)
    drive_base.turn(-35)
    drive_base.straight(40)
    drive_base.turn(50)
    drive_base.straight(70)    
    drive_base.straight(-70)
    drive_base.turn(-30)
    drive_base.straight(-400)
    drive_base.turn(-35)
    drive_base.straight(-330)
    drive_base.turn(55)
    left_attach.stop()
    drive_base.use_gyro(False)
    drive_base.straight(-700, Stop.COAST)
    bot.hub_base.next_program()
LIGHT_SHOW = RobotProgram(light_show_func, "4",  Color.RED)


def scene_change_func(bot:PrimeRobot):
    ### Quality of life stuff
    drive_base = bot.drive_base
    left_attach = bot.left_attach
    right_attach = bot.right_attach
    speaker = bot.hub_base.speaker
    display = bot.hub_base.display
    drive_base.set_default()
    display.icon(SMILE)
    ### Get attachments into correct positions
    right_attach.dc(-30)
    left_attach.dc(-30)
    ### Square off of back wall
    drive_base.set_robot_accel(50)
    drive_base.drive(-100, 0)
    speaker.beep(500, 400)
    drive_base.stop()
    wait(100)
    drive_base.use_gyro(True)
    wait(100)
    drive_base.reset()
    drive_base.set_default()
    display.icon(RIGHT_SMILE)
    drive_base.curve(175, 90)
    display.icon(LEFT_SMILE)
    drive_base.turn(-90)
    display.icon(SMILE)
    drive_base.straight(535)
    display.icon(LEFT_SMILE)
    drive_base.turn(-45)
    display.icon(CONCENTRATE)
    drive_base.drive(100, 0)
    wait(600)
    ### Pick up Sam
    right_attach.run_angle(300, 250, Stop.NONE)
    drive_base.stop()
    display.icon(WINK)
    bot.line_square_black(-40)
    right_attach.dc(30)
    display.icon(RIGHT_SMILE)
    drive_base.turn(115)
    display.icon(SMILE)
    drive_base.straight(110)
    display.icon(CONCENTRATE)
    left_attach.run_angle(300, 480, Stop.NONE)
    ### Drops off Izzy
    wait(300)
    left_attach.run_angle(1000, -25)
    display.icon(RIGHT_SMILE)
    drive_base.turn(20)
    display.icon(WINK)
    left_attach.run_angle(1000, -400)
    left_attach.dc(-30)
    display.icon(SMILE)
    drive_base.straight(410)
    display.icon(LEFT_SMILE)
    drive_base.turn(-90)
    display.icon(CONCENTRATE)
    drive_base.straight(-25)
    left_attach.run_angle(1000, 300, Stop.NONE)
    ### Slams down arm
    wait(300)
    display.icon(WINK)
    left_attach.run_angle(1000, -300)
    left_attach.dc(-30)
    display.icon(LEFT_SMILE)
    drive_base.curve(-200, -20)
    display.icon(SMILE)
    drive_base.set_robot_accel(200)
    drive_base.straight(-350)
    display.icon(RIGHT_SMILE)
    drive_base.turn(50)
    display.icon(SMILE)
    drive_base.straight(-200, Stop.NONE)
    drive_base.use_gyro(False)
    drive_base.straight(-500, Stop.COAST)
    drive_base.set_default()
    bot.hub_base.next_program()
SCENE_CHANGE = RobotProgram(scene_change_func, "5", Color.BLUE)


def cinema_func(bot:PrimeRobot):
    ### Quality of life stuff
    drive_base = bot.drive_base
    left_attach = bot.left_attach
    right_attach = bot.right_attach
    speaker = bot.hub_base.speaker
    display = bot.hub_base.display
    drive_base.set_default()
    display.icon(SMILE)
    ### Get attachments positioned
    right_attach.dc(30)
    left_attach.dc(-30)
    ### Square off of backwall
    drive_base.set_robot_accel(50)
    drive_base.drive(100, 0)
    speaker.beep(500, 400)
    drive_base.stop()
    wait(100)
    drive_base.use_gyro(True)
    wait(100)
    drive_base.reset()
    ### Start Run
    display.icon(CONCENTRATE)
    drive_base.set_robot_accel(40)
    drive_base.curve(-150, 40)
    drive_base.curve(-150, -40)
    drive_base.set_robot_accel(150)
    drive_base.straight(-500, Stop.NONE, wait= False)
    wait(1500)
    drive_base.turn(30, wait = False)
    wait(400)
    drive_base.stop()
    drive_base.reset()
    display.icon(WINK)
    drive_base.set_robot_accel(200)
    drive_base.straight(100, Stop.NONE)
    drive_base.use_gyro(False)
    drive_base.straight(125, Stop.COAST)
    drive_base.set_default()
    bot.hub_base.next_program()
CINEMA = RobotProgram(cinema_func, "6", Color.WHITE)


def mixingboard_func(bot:PrimeRobot):
    ### Quality of life stuff
    drive_base = bot.drive_base
    left_attach = bot.left_attach
    right_attach = bot.right_attach
    speaker = bot.hub_base.speaker
    display = bot.hub_base.display
    drive_base.set_default()
    ### Make sure the attachments are in the right position
    left_attach.dc(-30)
    right_attach.dc(30)
    ### Square against the backwall
    display.icon(SMILE)
    drive_base.set_robot_accel(50)
    drive_base.drive(100, 0)
    speaker.beep(500, 400)
    drive_base.stop()
    wait(100)
    drive_base.use_gyro(True)
    drive_base.reset()
    wait(100)
    drive_base.set_robot_accel(70)
    ### Now for the actual program
    drive_base.straight(-60)
    display.icon(LEFT_SMILE)
    drive_base.turn(40)
    display.icon(CONCENTRATE)
    drive_base.straight(-440, Stop.COAST)
    drive_base.drive(-100, 0)
    display.icon(SMILE)
    wait(300)
    display.icon(WINK)
    wait(200)
    drive_base.stop()
    drive_base.reset()
    display.icon(LEFT_SMILE)
    drive_base.curve(160, -90)
    display.icon(SMILE)
    left_attach.run_angle(1000, 465)
    drive_base.set_robot_speed(30)
    drive_base.straight(70)
    display.icon(CONCENTRATE)
    left_attach.dc(30)
    wait(300)
    display.icon(WINK)
    drive_base.straight(-210)
    drive_base.set_robot_speed(60)
    left_attach.run_angle(1000, -200, Stop.NONE)
    left_attach.dc(-40)
    drive_base.set_default()
    display.icon(LEFT_SMILE)
    drive_base.turn(-50)
    display.icon(SMILE)
    drive_base.straight(365)
    display.icon(RIGHT_SMILE)
    drive_base.turn(35)
    display.icon(SMILE)
    drive_base.straight(225)
    brightness = list(range(0, 100, 4)) + list(range(100, 0, -4))
    # Example code from Pybricks
    # Create an animation of the heart icon with changing brightness.
    display.animate([REBEL * i / 100 for i in brightness], 30)
    # The animation repeats in the background. Here we just wait.
    star_wars_func(bot)
    left_attach.stop()
    right_attach.stop()
    drive_base.use_gyro(False)
    display.icon(WINK)
    wait(300)
MIXINGBOARD = RobotProgram(mixingboard_func, "7", Color.YELLOW)


