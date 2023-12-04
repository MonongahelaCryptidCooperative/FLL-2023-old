from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Side, Axis
from pybricks.pupdevices import Motor, ColorSensor, Remote
from pybricks.tools import StopWatch, wait
from pybricks.robotics import DriveBase
from mcc_universal_classes import *

PrimeHub()
class MCCPrimeHub(PrimeHub):
    """Class that adds functionality to the prime hub to store and run our programs
     configured for a vertically oriented hub"""
    def __init__(
        self,
        top_side:Axis = Axis.Z,
        front_side:Axis = Axis.X, 
        broadcast_channel:int = 0, 
        observe_channels:Sequence[int] = [],
        list_of_robot_programs:list = list()
        ):
        super().__init__(top_side, front_side, broadcast_channel, observe_channels)
        self.programs_list:list = list_of_robot_programs
        self.selected_program = 0
        self.system.set_stop_button([Button.LEFT, Button.RIGHT])

    def update_hub(self):
        "updates the hubs display and button color based on current program"
        program:RobotProgram = self.programs_list[self.selected_program]
        self.display.char(program.label)
        self.light.on(program.color)

    def prior_program(self):
        "Selects the previous program"
        self.selected_program = (self.selected_program - 1) % len(self.programs_list)
        wait(200)
        self.update_hub()

    def next_program(self):
        "Selects the next program"
        self.selected_program = (self.selected_program + 1) % len(self.programs_list)
        wait(200)
        self.update_hub()

    ### Launch the active program
    def launch_program(self, bot:PrimeRobot):
        program:RobotProgram = self.programs_list[self.selected_program]
        program.function(bot)
    
    def wait_for_button_press(self):
        print("button pressed")
        self.light.blink(Color.YELLOW, [100, 100])
        while not Button.BLUETOOTH in self.buttons.pressed():
            wait(10)
        self.light.on(Color.YELLOW)

    ### Check buttons that are pressed
    def check_buttons(self, bot:PrimeRobot):
        b_list = self.buttons.pressed()
        timer = bot.timer
        if len(b_list) > 0:
            timer.reset()
        if Button.BLUETOOTH in b_list:
            self.launch_program(bot)
        elif Button.CENTER in b_list and Button.LEFT in b_list:
                self.prior_program()
                wait(200)
        elif Button.CENTER in b_list and Button.RIGHT in b_list:
                self.next_program()
                wait(200)

class PrimeRobot(object):
    """Class for the PrimeRobot. Contains code for line following and squaring 
    as such code"""
    def __init__(
        self, 
        hub_base:MCCPrimeHub,
        drive_base:MCCDriveBase,
        left_attach:Motor,
        right_attach:Motor,
        rc_base:RobotRC,
        left_light:ColorSensor,
        right_light:ColorSensor,
        light_settings:MCCLightValues
        ):
        # define class variables
        self.hub_base:MCCPrimeHub = hub_base
        self.drive_base:MCCDriveBase = drive_base
        self.right_attach:Motor = right_attach
        self.left_attach:Motor = left_attach
        self.rc_base:RobotRC = rc_base
        self.left_light:ColorSensor = left_light
        self.right_light:ColorSensor = right_light
        self.light_settings = light_settings
        self.timer:StopWatch = StopWatch()
        self.timeout:int = 30  ### timeout in minutes.
        ### Hub will shut off if no button presses on remote or bot
    
    def master_loop(self):
        """Just a big while loop that checks for button presses/runs everything.
         Now will timeout based on self.timeout settings and shut down."""
        while self.timer.time() < (self.timeout * 60 * 1000):
            hub_base:MCCPrimeHub = self.hub_base
            rc_base:RCBase = self.rc_base
            hub_base.update_hub()
            hub_base.check_buttons(self)
            rc_base.check_buttons(self)
            wait(10)
        self.shutdown()

    def shutdown(self):
        "A function to shutdown the hub. Plays some music/prints to the console"
        hub_base = self.hub_base
        print("Robot is shutting down to save battery!")
        hub_base.speaker.play_notes(["C4/4", "C3/4", "C2/4"])
        hub_base.system.shutdown()

    def setup_RC(self):
        """Initializes the Remote. Will crash if remote not found in 60 seconds.
        This code is never active during the Robot Game."""
        hub_base = self.hub_base
        rc_base = self.rc_base
        hub_base.light.blink(Color.GREEN, [200, 200])
        rc_base.remote = Remote()
        hub_base.light.on(Color.GREEN)
        wait(200)
        rc_base.update_remote()

    def line_square_white(self, speed:int = 50):
        "Square on a white line, can tell how fast to drive"
        drive_base:MCCDriveBase = self.drive_base
        left_light:ColorSensor = self.left_light
        right_light:ColorSensor = self.right_light
        leftline = True
        rightline = True
        white = self.light_settings.WHITE
        drive_base.run_single_motor(Side.LEFT, speed)
        drive_base.run_single_motor(Side.RIGHT, speed)
        while(leftline or rightline):
            if(left_light.reflection() > white):
                drive_base.hold_single_motor(Side.LEFT)
                leftline = False
            if(right_light.reflection() > white):
                drive_base.hold_single_motor(Side.RIGHT)
                rightline = False
            wait(10)

    def line_square_black(self, speed:int = 50):
        "Square on a black line, can tell how fast to drive"
        drive_base:MCCDriveBase = self.drive_base
        left_light:ColorSensor = self.left_light
        right_light:ColorSensor = self.right_light
        leftline = True
        rightline = True
        black = self.light_settings.BLACK
        drive_base.run_single_motor(Side.LEFT, speed)
        drive_base.run_single_motor(Side.RIGHT, speed)
        while(leftline or rightline):
            if(left_light.reflection() < black):
                drive_base.hold_single_motor(Side.LEFT)
                leftline = False
            if(right_light.reflection() < black):
                drive_base.hold_single_motor(Side.RIGHT)
                rightline = False
            wait(10)

    def line_follow(self, sensor_side:Side, black_line_side:Side, speed:int = 50, min_dist:int = 60):
        """Follows a line. Need to tell it which sensor to use and which side 
        the black line will be on the sensor. Also takes the speed to travel and a 
        minimum distance. The minimum distance prevents the bot from 'tripping' on
        a white line."""
        drive_base:MCCDriveBase = self.drive_base
        left_light:ColorSensor = self.left_light
        right_light:ColorSensor = self.right_light
        go = True
        threshold = self.light_settings.THRESHOLD
        black = self.light_settings.BLACK
        coefficient = self.light_settings.porportional_coef
        drive_base.reset()
        while go == True:
            dist = (drive_base.distance() > min_dist)
            if(sensor_side == Side.LEFT and black_line_side == Side.LEFT):
                turning = (threshold - left_light.reflection()) *  coefficient
                if (dist and (right_light.reflection() < black)):
                    go = False
            elif(sensor_side == Side.LEFT and black_line_side == Side.RIGHT):
                turning = (left_light.reflection() - threshold) *  coefficient
                if (dist and (right_light.reflection() < black)):
                    go = False
            elif(sensor_side == Side.RIGHT and black_line_side == Side.LEFT):
                turning = (threshold - right_light.reflection()  ) *  coefficient
                if (dist and (left_light.reflection() < black)):
                    go = False
            elif(sensor_side == Side.RIGHT and black_line_side == Side.RIGHT):
                turning = (right_light.reflection() - threshold) *  coefficient
                if (dist and (left_light.reflection() < black)):
                    go = False
            drive_base.drive(speed, turning)
        drive_base.stop()    

    ### Line finding fuctions (run prior to running line following)
    ### Find white line then stop on threshold (to prep for line following)
    ### Or fine white line, cross over black line,
    ### and find threshold on opposite side 
    def find_line_crossover(self, side:Side, speed:int = 100):
        drive_base:MCCDriveBase = self.drive_base
        black = self.light_settings.BLACK 
        white = self.light_settings.WHITE
        if side == Side.LEFT:
            light:ColorSensor = self.left_light
        else: 
            light:ColorSensor = self.right_light
        drive_base.drive(speed, 0)
        while(light.reflection() > black):
            wait(10)
        while(light.reflection() < white):
            wait(10)
        drive_base.stop()

    def find_line(self, side:Side, speed:int = 100):
        drive_base:MCCDriveBase = self.drive_base
        black = self.light_settings.BLACK 
        if side == Side.LEFT:
            light:ColorSensor = self.left_light
        else: 
            light:ColorSensor = self.right_light
        drive_base.drive(speed, 0)
        while(light.reflection() > black):
            wait(10)
        drive_base.stop()