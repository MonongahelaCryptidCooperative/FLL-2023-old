"""
This file holds the code that is needed for the Prime Hub and WILL NOT WORK WITH 
THE TECHNIC HUB. When running a robot design, either this file or the mcc_technic 
file needs to be imported depending on which hub is used. 
"""
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Side, Stop
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import Remote
### Import MCC stuff need the universal classes and math
from mcc_universal_classes import *
from mcc_math import *



class MCCPrimeHub(PrimeHub):
    "Class that adds functionality to the prime hub and stores the loaded programs/allows for program selection"
    def __init__(
        self, 
        list_of_robot_programs:list = list(),
        button_map:HubButtonMap = HubButtonMap()
        ):
        super().__init__()
        self.programs_list:list = list_of_robot_programs
        self.selected_program = 0
        self.button_map:HubButtonMap = button_map
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
        self.update_hub()

    def next_program(self):
        "Selects the next program"
        self.selected_program = (self.selected_program + 1) % len(self.programs_list)
        wait(200)
        self.update_hub()

    ### Launch the active program
    def launch_program(self, bot:Robot):
        program:RobotProgram = self.programs_list[self.selected_program]
        program.function(bot)
    
    def wait_for_button_press(self):
        print("button pressed")
        self.light.blink(Color.YELLOW, [100, 100])
        while not Button.BLUETOOTH in self.buttons.pressed():
            wait(10)
        self.light.on(Color.YELLOW)

    ### Check buttons that are pressed
    def check_buttons(self, bot:Robot):
        bmap = self.button_map
        b_list = self.buttons.pressed()
        timer = bot.timer
        if len(b_list) > 0:
            timer.reset()
        if bmap.launch_button in b_list:
            self.launch_program(bot)
        elif bmap.prior_button in b_list and bmap.safety_button in b_list:
                self.prior_program()
                wait(200)
        elif bmap.next_button in b_list and bmap.safety_button in b_list:
                self.next_program()
                wait(200)


        

class PrimeRobot(object):
    """Class for the PrimeRobot. Contains code for line following and squaring 
    as such code requires both a LightBase and DriveBase which a PrimeBot 
    contains. Technic Hubs can't handle this code."""
    def __init__(
        self, 
        hub_base:MCCPrimeHub,
        drive_base:MCCDriveBase,
        light_base:MCCLightBase,
        attach_base:MCCAttachBase,
        rc_base:RobotRC,
        light_settings:MCCLightValues
        ):
        # define class variables
        self.hub_base:MCCPrimeHub = hub_base
        self.drive_base:MCCDriveBase = drive_base
        self.light_base:LightBase = light_base
        self.attach_base:AttachBase = attach_base
        self.rc_base:RobotRC = rc_base
        self.light_settings = light_settings
        self.timer:StopWatch = StopWatch()
        self.timeout:int = 10  ### timeout in minutes. Hub will shut off if no button presses on remote or bot
    

    def master_loop(self):
        """Just a big while loop that checks for button presses/runs everything.
         Now will timeout based on self.timeout settings and shut down. We did 
         this for energy savings in keeping with this years SuperPowered theme."""
        while self.timer.time() < (self.timeout * 1000 * 60):
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
        print("The theme is energy use/savings after all!")
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
   
    def reflectance_check(self, light:Side, operator, light_level):
        """Checks if the reflectance for the given light sensor is either lessthan 
        or greaterthan (depending which operator is given) a given light level 
        BLACK, WHITE, THRESHOLD"""
        return operator(self.light_base.reflectance(light), light_level)


    def line_square_white(self, speed:int = 50):
        "Square on a white line, can tell how fast to drive"
        pass

    def line_square_black(self, speed:int = 50):
        "Square on a black line, can tell how fast to drive"
        pass


    def line_square_threshold(self, operator):
        """line square on the threshold value. Needs an operator depending on 
        whether it is crossing the black or white line first"""
        pass



    def line_follow(self, sensor_side:Side, black_line_side:Side, speed:int = 50, min_dist:int = 60, stop_on_white:bool = True):
        """Follows a line. Need to tell it which sensor to use and which side 
        the black line will be on the sensor. Also takes the speed to travel and a 
        minimum distance. The minimum distance prevents the bot from 'tripping' on
        a white line."""
        pass

    ### Line finding fuctions (run prior to running line following)
    ### Find white line then stop on threshold (to prep for line following)
    ### Or fine white line, cross over black line,
    ### and find threshold on opposite side 
    def find_line(self, side:Side, speed:int = 100):
        pass
    
    def find_line_crossover(self, side:Side, speed:int = 100):
        pass