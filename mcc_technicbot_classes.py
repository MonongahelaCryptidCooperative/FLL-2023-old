from pybricks.hubs import TechnicHub
from pybricks.parameters import Button, Color, Direction, Side, Axis
from pybricks.pupdevices import Motor, Remote
from pybricks.tools import StopWatch, wait
from pybricks.robotics import DriveBase
from mcc_universal_classes import *

class MCCTechnicHub(TechnicHub):
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
        self.system.set_stop_button([])

    def update_hub(self):
        "updates the hubs display and button color based on current program"
        program:RobotProgram = self.programs_list[self.selected_program]
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
        while not Button.CENTER in self.buttons.pressed():
            wait(10)
        self.light.on(Color.YELLOW)

    ### Check buttons that are pressed
    def check_buttons(self, bot:PrimeRobot):
        b_list = self.button.pressed()
        timer = bot.timer
        if len(b_list) > 0:
            timer.reset()
        if Button.CENTER in b_list:
            self.launch_program(bot)

class TechnicRobot(object):
    """Class for the PrimeRobot. Contains code for line following and squaring 
    as such code"""
    def __init__(
        self, 
        hub_base:MCCPrimeHub,
        drive_base:MCCDriveBase,
        left_attach:Motor,
        right_attach:Motor,
        rc_base:RobotRC
        ):
        # define class variables
        self.hub_base:MCCPrimeHub = hub_base
        self.drive_base:MCCDriveBase = drive_base
        self.right_attach:Motor = right_attach
        self.left_attach:Motor = left_attach
        self.rc_base:RobotRC = rc_base
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
