"""
This file holds the code that is needed for the Technic Hub and will not work with
the prime hub. Either this file or the mcc_prime file needs to be imported
depending on which hub is used. This allows for the reuse of code
"""

from pybricks.hubs import TechnicHub
from pybricks.parameters import Button, Color, Side
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import Remote


from mcc_universal_classes import *


class MCCTechnicHub(TechnicHub):
    """A class to expand upon the TechnicHub class. Makes it so the center
    button no longer automatically shuts down the bot. Has a method to query 
    button presses"""
    def __init__(
        self, 
        ):
        super().__init__()
        self.system.set_stop_button(None)

    ### Check buttons that are pressed
    def check_buttons(self, bot:Robot):
        b_list = self.button.pressed()
        timer = bot.timer
        rc_base = bot.rc_base
        if rc_base.remote == None:
            self.light.blink(Color.YELLOW, [50, 50])
            if Button.CENTER in b_list:
                bot.setup_RC()
                timer.reset()
        elif len(b_list) > 0:
            bot.shutdown()

    def wait_for_button_press(self):
        self.light.blink(Color.RED, [100, 100])
        while not Button.CENTER in self.button.pressed():
            wait(10)
        self.light.on(Color.GREEN)
    
    def next_program(self):
        pass
        




class TechnicRobot(Robot):
    """Class for a TechicBot. Technic Hubs have only 4 ports and no display
    but can still do a heck of a lot. We use them for prototyping as they can 
    run the same code as the Prime Hubs but, due to only 4 ports, lack light 
    sensors. We call them "Blind Bots." Inherits from the default Robot class. 
    The Class overrides functions.
    """
    def __init__(
        self, 
        hub_base:MCCPrimeHub,
        drive_base:MCCDriveBase,
        attach_base:MCCAttachBase,
        rc_base:RCBase
        ):
        # define class variables
        self.hub_base:MCCTechnicHub = hub_base
        self.drive_base:MCCDriveBase = drive_base
        self.attach_base:MCCAttachBase = attach_base
        self.rc_base:MCCRCBase = rc_base
        self.timer:StopWatch = StopWatch()
        self.timeout:int = 10  ### timeout in minutes. Hub will shut off if no button presses on remote or bot
    
    ### Loop that runs everything, call to start at bottom of code
    def master_loop(self):
        hub_base:MCCTechnicHub = self.hub_base
        rc_base:MCCRCBase = self.rc_base
        hub_base.light.blink(Color.YELLOW, [100, 100])
        while self.timer.time() < (self.timeout * 1000 * 60):
            hub_base.check_buttons(self)
            if rc_base.remote != None:
                rc_base.check_buttons(self)
            else:
                pass
            wait(10)
        self.shutdown()

    def setup_RC(self):
        hub_base = self.hub_base
        rc_base = self.rc_base
        hub_base.light.blink(Color.GREEN, [200, 200])
        rc_base.remote = Remote()
        hub_base.light.on(Color.GREEN)
        wait(200)
        rc_base.update_remote()

    def shutdown(self):
        hub_base = self.hub_base
        print("Robot is shutting down to save battery!")
        print("The 2022 Superpowered theme is energy use/savings after all!")
        hub_base.system.shutdown()
    
    def run_program(self, program:RobotProgram):
        self.hub_base.wait_for_button_press()
        program.function(self)
   