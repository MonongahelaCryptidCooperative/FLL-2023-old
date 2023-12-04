from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch



pi = 3.1415926535897


class MCCRCBase(object):
    """ A class/object to hold the stuff needed for RC control. Takes two 
    arguments. One is a list of RC programs. The other is a RobotSpeedSettings 
    object that defines the speed setting we want to use while under RC control"""
    # init method
    def __init__(
        self, 
        list_of_rc_controls:list,
        speed_settings:RobotSpeedSettings
        ):
        self.remote:Remote = None
        self.list_of_rc_controls:list = list_of_rc_controls
        self.active_control:int = 0
        self.speed_settings:RobotSpeedSettings = speed_settings
    
    def next_rc_control(self):
        """ Selects the next RC control scheme/program in the list.
        Generally this function gets called when the center button is pushed"""
        self.active_control = (self.active_control + 1) % len(self.list_of_rc_controls)
        wait(200)

    def update_remote(self):
        """ Function to set the remote's light color to the color specified
        in the active RemoteProgram object"""
        active_control:RobotProgram = self.list_of_rc_controls[self.active_control]
        self.remote.light.on(active_control.color)

    def check_buttons(self, bot:PrimeRobot):
        """ Code that checks which remote buttons are pressed. Has to be given
        the object of Class Robot that holds the remote object so that the 
        time out timer can be reset so bot does not shut down"""
        remote = self.remote
        active_control:RemoteProgram = self.list_of_rc_controls[self.active_control]
        if remote:
            active_control.function(bot)
            self.update_remote()
            b_list = remote.buttons.pressed()
            if len(b_list) > 0:
                bot.timer.reset()
        else:
            pass


class MCCDriveBase(DriveBase):
    """ Inherits from the built-in DriveBase class from Pybrick's Robotics
    module. Holds the motors and adds methods to do stuff like set the default
    speed or have the robot drive at a percentage of its default speed.
    """
    def __init__(
        self,
        wheel_size:int,
        wheel_spacing:int,
        right_drive_motor:Motor,
        left_drive_motor:Motor,
        default_speed_settings:RobotSpeedSettings
    ):
        super().__init__(left_drive_motor, right_drive_motor, wheel_size, wheel_spacing)
        self.right_drive_motor:Motor = right_drive_motor
        self.left_drive_motor:Motor = left_drive_motor
        self.wheel_size:int = wheel_size
        self.default_speed_settings:RobotSpeedSettings = default_speed_settings
        print(self.settings())
        self.set_default()

    ### convert speed in mm/s to wheel rotations (degrees/sec)
    def convert_speed_to_rotations(self, speed):
        """ Converts speed in mm/s to degrees/s. Used for the single motor
        control methods that are mainly used for line squaring"""
        return speed/(pi * self.wheel_size)*360

 
    def set_default(self):
        """ Set default speed based on settings provided in a RobotSpeedSettings
        object"""
        self.settings(
            self.default_speed_settings.straight_speed,
            self.default_speed_settings.straight_accel, 
            self.default_speed_settings.turn_speed,
            self.default_speed_settings.turn_accel)
        
    def set_robot_speed(self, percentage):
        """Slow down or speed up the robot by a percentage.
        Useful when pushing objects, or wanting finer control of movements """
        x = percentage / 100
        self.settings(
            self.default_speed_settings.straight_speed*x,
            self.default_speed_settings.straight_accel*x, 
            self.default_speed_settings.turn_speed*x,
            self.default_speed_settings.turn_accel*x)

    def set_robot_accel(self, percentage):
        """Slow down or speed up the robots acceleration by a percentage.
        Useful when pushing objects, or wanting finer control of movements """
        x = percentage / 100
        self.settings(
            self.default_speed_settings.straight_speed,
            self.default_speed_settings.straight_accel*x, 
            self.default_speed_settings.turn_speed,
            self.default_speed_settings.turn_accel*x)
    
    def get_motor(self, side:Side):
        """ very simple function that returns the motor you asked for. Can
        take Side.LEFT or Side.RIGHT as arguements to return left or right 
        motor"""
        if side == Side.LEFT:
            return self.left_drive_motor
        elif side == Side.RIGHT:
            return self.right_drive_motor
        else:
            return None

    def run_single_motor(self, side:Side, speed:int = 100):
        """ Method to run a single motor at a given speed (mm/s)
        Used in line squaring"""
        x = self.convert_speed_to_rotations(speed)
        self.get_motor(side).run(x)

    def hold_single_motor(self, side:Side):
        """ Method to hold a single motor. Used in line squaring"""
        self.get_motor(side).hold()

### Data holding Classes

class MCCLightValues(object):
    """ Class to hold the various values needed to line follow. Holds 
    values for black, white, threshold as well as line following coefficients"""
    def __init__(
        self, 
        black:int = 19,
        white:int = 70,
        porportional_coefficient:float = 1.5
        ):
        self.BLACK = black
        self.WHITE = white
        self.THRESHOLD = (black + white)/2
        self.porportional_coef = porportional_coefficient

class RobotSpeedSettings(object):
    """ Class for robot speed settings. Used for drive_base as well as RC control"""
    def __init__(
        self,
        straight_speed:int = 450,   # Straight speed
        straight_accel:int = 510,   # Straight acceleration
        turn_speed:int = 250,       # Turn Speed
        turn_accel:int = 320,       # Turn acceleration
        left_attach:int = 500, 
        right_attach:int = 500,
    ):
        self.straight_speed:int = straight_speed
        self.straight_accel:int = straight_accel
        self.turn_speed:int = turn_speed
        self.turn_accel:int = turn_accel
        self.left_attach:int = left_attach
        self.right_attach:int = right_attach


class RobotProgram(object):
    """ A class that holds our RobotPrograms. RobotPrograms have a method
    that is called when a program is launched. Also has as single character that,
    if the robot has a display, will be displayed as well as a color attribute
    that will change the color of the light on the hub. This is used to match the
    color of attachments to the color of the program and provides an additional
    cue to ensure the correct attachements are placed on the robot"""
    def __init__(
        self,
        func:callable,
        character:chr = "X",
        light_color:Color = Color.BLUE,
        button_press:Button = Button.LEFT):

        self.label:chr = character
        self.color:Color = light_color 
        self.function:callable = func
        self.button_press = button_press
