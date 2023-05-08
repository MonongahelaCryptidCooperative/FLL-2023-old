"""
File to hold math functions that we need. Has no dependencies
"""

"""
Need to ability to pass the <,> operators as a callable object. This code is used
for the comparisons for the get_reflectance() function that is encapsulated in the 
PrimeRobot class. Also used as an arguement for the square_on_threshold function also
encapsulated within the PrimeRobot class
"""
def lessthan(a, b):
    "Same as a < b."
    return a < b


def greaterthan(a, b):
    "Same as a > b."
    return a > b


### Value of Pi
pi = 3.1415926

