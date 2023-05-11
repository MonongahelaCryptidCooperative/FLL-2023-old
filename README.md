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

In the mcc_default_values_objects change the wheel size and axle spacing to whatever your bot uses. 

If you are using a spike prime hub go to the PrimeBotMain.py file. Compile and load this to the hub.
If you are using a technic hub go to the TechnicBotMain.py file and complile and load to the hub



In order to switch programs on a spike hub you have to press both the center button and the left or right button at the same time
This was done as our team members would accidently bump the arrow buttons

Launching program/runs is done via pressing the bluetooth button (our robot had a unique design that blocked the center button when attachments were in place). You may wish to change this. 

To pair with a remote select/launch the program labeled "R". Then push the center button on the lego bluetooth remote. The Red LEFT/RIGHT buttons act as macros and, when held down, will cause
the left/right up/down buttons on the opposite side to control the attachment motors. 


We have included all of the code for our 2022 superpowered runs in the ets_superpowered_programs (we used to be called exploding toaster supernova) as demo code. 400 points is coded (got 375 in real life).
Would advise watching a run with teh code open to get some ideas of how you might accomplish things in future years (though we are no where near as advanced in our mechanical engineering as some of the top world's teams). https://www.youtube.com/watch?v=I4g1R-PBdCY&t=16746s. Our Run starts at 4:36:00. Did not code moving the truck with the barrels in it. Removed code for line following/line squaring so missions will not run correctly. 

Hope this helps everyone up their robot game! Would love to be beaten by someone who found this code useful! We are also actively working on a block interface that will basically allow programming a pybricks bot with blocks. Stay Tuned!
