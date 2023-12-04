# FLL
Code to use Pybricks for competitive robotics


Code is broken down into various files. To provide an example code from our 
team's entry in the 2023 FLL Masterpiece Challenge is included. 


Code is provided under the MIT license (just give us a shoutout if it is used/
shower us with buttons/team swag if we cross paths at any competitions). We will be doing FTC soon.

We would also love to hear from any teams that find this useful. Bonus points 
if you are very far away from West Virginia. 


Instructions to use (will create better tutorials later):
oad all of the .py files into pybricks
If you are using a spike prime hub go to the PrimeBotMain.py file. Compile and load this to the hub.
If you are using a technic hub go to the TechnicBotMain.py file and complile and load to the hub (we cannot afford multiple spike hubs so we make experimental robots using cheap 4-port technic hubs, they are actually quite capable and, if allowed, could have completed this year's robot game)


Code assumes left drive motor is A, right drive motor is B
Left attachment motor is C, Right attachment motor is D
Light sensors are on E and F ports (if applicable, not present on technic bots)
change the wheel size and axle spacing to whatever your bot uses (wheel size is printed on the wheels, have to measure wheel spacing or just count lego technic holes (holes are spaced 8 mm on center) 

You may also want to change the the speed settings. By default pyricks sets the maximal speed to about 40%
of the true maximal speed based on motor speed and wheel size. We thus override this for a higher top speed 
closer to 80% of the theoretical maximum. Also the acceleration paratmeters for pybricks are a bit aggressive.
They likely work fine if you have a lightweight robot but in our case these were reduced to about 1/2 of the default values.
Play with these values as needed. The code does print off to the console what pybricks would like these values to be before they are 
overwritten upon the creating of a MCCDriveBase class. 

Calibrate as follows:
1st: Adjust distance. Do this by running the program labeled "S"
1st buy a meter stick and place tape exactly 1 meter apart on the floor
next run the program "S"
If it drives too far you need to increase the wheel diameter
If it drives too short you need to reduce the wheel diameter

2nd: adjust wheel spacing
Run the program labeled "T"
This will cause the robot to turn 1080 degrees.
If it turns too far it you need to adjust the wheel spacing parameter to be smaller
If it turns not enough you need to make the wheel spacing parameter larger

3rd: light sensor
A pretty cool program is included that will tell you what values you need to use for black, white and threshold (line following for porportional control)
Robot will drive 1/2 meter constantly compairing values and report the maximal and mininmal reflectance values as well as recommended settings. Make sure the robot drives over at least one set of white and black lines. Run in both full light and dim conditions so you can make sure the values you choose will work no matter what. 




In order to switch programs on a spike hub you have to press both the center button and the left or right button at the same time
This was done as our team members would accidently bump the arrow buttons. Given that the code auto advances you shouldn't be using these buttons during a match anyways.

Launching program/runs is done via pressing the bluetooth button (our robot had a unique design that blocked the center button when attachments were in place). You may wish to change this in the code

To pair with a remote select/launch the program labeled "R". Then push the center button on the lego bluetooth remote. The Red LEFT/RIGHT buttons act as macros and, when held down, will cause the left/right up/down buttons on the opposite side to control the attachment motors.A cool feature of the remote is that if you push both the left and right buttons it will print off how far the robot has driven, turned, and how many degrees the attachment motors have moved. This is very useful for programming the robot.

We have included all of the code for our 2023-2024 Masterpiece runs in the zif_masterpiece_programs file. A video of our performance can be seen here;https://youtu.be/jPaWqd5SM1U?si=mEACfuPGs_pU4lnI

Hope this helps everyone up their robot game! Would love to be beaten by someone who found this code useful! We are also wokring on starter code for using hte new Pybrick's block interface. 
