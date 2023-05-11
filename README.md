# FLL
Code to use Pybricks for competitive robotics


Code is broken down into various files. To provide an example code from our 
team's entry in the 2022 FLL Superpowered Challenge is included. 


Code is provided under the MIT license (just give us a shoutout if it is used/
shower us with buttons/team swag if we cross paths at any competitions).

We would also love to hear from any teams that find this useful. Bonus points 
if you are very far away from West Virginia. 


Instructions to use (will create better tutorials later):
Code assumes left drive motor is A, right drive motor is B
Left attachment motor is C, Right attachment motor is D
and light sensors are on E and F ports (if applicable, not present on technic bots)
Load all of the .py files into pybricks

In the mcc_default_values_objects change the wheel size and axle spacing to whatever your bot uses (wheel size is printed on the wheels, have to measure wheel spacing or just count lego technic holes (holes are spaced 8 mm on center) 

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
Robot will drive 1/2 meter constantly compairing values and report the maximal and mininmal reflectance values as well as recommended settings. Make sure the robot drives over at least one set of 
white and black lines. Run in both full light and dim conditions so you can make sure the values you choose will work no matter what. 


If you are using a spike prime hub go to the PrimeBotMain.py file. Compile and load this to the hub.
If you are using a technic hub go to the TechnicBotMain.py file and complile and load to the hub



In order to switch programs on a spike hub you have to press both the center button and the left or right button at the same time
This was done as our team members would accidently bump the arrow buttons. The Class HubButtonMap is where you can assign which button to do what if you want to switch this. 

Launching program/runs is done via pressing the bluetooth button (our robot had a unique design that blocked the center button when attachments were in place). You may wish to change this in the HubButtonMap class used to contruct your robot. 

To pair with a remote select/launch the program labeled "R". Then push the center button on the lego bluetooth remote. The Red LEFT/RIGHT buttons act as macros and, when held down, will cause
the left/right up/down buttons on the opposite side to control the attachment motors. The remote code is written so you can give it a list of RemotePrograms objects each of which is essentially a different button mapping. An alternative way to handle the remove it actually to create 2 different RemotePrograms, one of which maps the Red LEFT/RIGHT BUttons to the left attachment motor and the another that maps to the right attachement motor. Thus the center button can be used to switch between controlling the two attachments (rather than using the default macro approach). This is particuarly useful if you want to do lego battlebots as then you can still drive (somewhat, difficult to press multiple buttons) while opperating a grabber/flipper/etc. We have also used experimental code to do motion controls (Pybricks has experimental broadcast code) using a technic hubs gyro and then use the remote purely for attachments/other uses. Such is not included. 



We have included all of the code for our 2023 superpowered runs in the ets_superpowered_programs (we used to be called exploding toaster supernova) as demo code and these are loaded as the first 5 programs by default. 400 points is coded (got 375 in real life).
Would advise watching a run with the code open to get some ideas of how you might accomplish things in future years (though we are no where near as advanced in our mechanical engineering as some of the top world's teams). https://www.youtube.com/watch?v=I4g1R-PBdCY&t=16746s. Our Run starts at 4:36:00. Did not code moving the truck with the barrels in it due to time crunch, probably could have figured something out if we moved onto the post-season. Removed code for line following/line squaring so missions will not run correctly (it just passess) as the culture seems to be teams need to create such themselves. Will eventally create a website with some video demos as well as 3D models of our bot and attachments in case anyone wants to copy things. 

Hope this helps everyone up their robot game! Would love to be beaten by someone who found this code useful! We are also actively working on a block interface that will basically allow programming a pybricks bot with blocks. Stay Tuned!
