# OCN n61 basic temperature sensor

# main.py files are automatically launched when the microcontroller is given power
# This code uses the sample_sound() function created in field_deployment.py
# This code requires that hmain.py is already loaded on your ESP8266

#----------------------------------------------------------------------------

# SET PARAMETERS
# Do you want the instrument to go to sleep and sample? Yes = 1, No = 0
sleep = 1
# What is the sampling interval? Number of seconds between each sample
samp_int = 60

#----------------------------------------------------------------------------

from time import sleep_ms
from machine import Pin

# First, turn on the blue LED so we know the instrument has woken up
p2=Pin(2,Pin.OUT)   # Assign the blue LED
p2.value(0)         # Turn blue LED on (LED goes on when pin 2 is pulled low - 0V)

# sleep for 2 seconds before starting sampling
sleep_ms(2000)      

p16 = Pin(16, Pin.IN)  # Set Pin 16 as an input


# If Pin 16 is pulled high (as in not connected to Pin 2), start sampling cycle!
if p16.value()==1:
    from hmain import sample_sound # import sample_sound function from hmain code

    # Use sample_temp function with parameters set above
    sample_sound(sleep_flag=sleep, sample_interval_sec=samp_int)


